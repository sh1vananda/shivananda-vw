import { useEffect, useMemo, useState } from 'react'

function App() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  const [showForm, setShowForm] = useState(true);

  const [data, setData] = useState({
    firstName: "",
    lastName: "",
    email: "",
  });

  useEffect(() => {
    async function getPosts() {
      const response = await fetch("https://jsonplaceholder.typicode.com/posts")
      const data = await response.json()
      setPosts(data);
      setLoading(false);
    }
    getPosts();
  },[]);

  const groupedPosts = useMemo(() => {
    return posts.reduce((acc, post) => {
      if (!acc[post.userId]) {
        acc[post.userId] = [];
      }
      acc[post.userId].push(post);
      return acc;
    }, {});
  }, [posts]);

  console.log(groupedPosts)

  const submitAction = (formData) => {
    setData({
      firstName: formData.get("firstName"),
      lastName: formData.get("lastName"),
      email: formData.get("email"),
    })
    setShowForm(false);
  }

  return (
    <div className='d-flex flex-column gap-3 container p-3'>
      <h1>Hello, {data.firstName ? `${data.firstName} ${data.lastName}` : "Guest"}</h1>

      {showForm && (
        <form action={submitAction}>
          <div className='d-flex gap-3'>
            <input name="firstName" type="text" placeholder='First Name'/>
            <input name="lastName" type="text" placeholder='Last Name'/>
            <input name="email" type="email" placeholder='Email'/>
            <button type="submit">Submit</button>
          </div>
        </form>
      )}

      {!showForm && (
        <div className='d-flex flex-column gap-3'>
        <h2>Posts</h2>
        {loading ? <p>Loading...</p> : Object.entries(groupedPosts).map(([userId, userPosts]) => (
          <div key={userId} className="container-fluid bg-light rounded-3 p-3">
            <h3>User {userId}</h3>
            <table className="table table-striped">
              <thead>
                <tr>
                  <th>PID</th>
                  <th>Title</th>
                  <th>Body</th>
                </tr>
              </thead>
              <tbody>
                {userPosts.map(post => (
                  <tr key={post.id}>
                    <td>{post.id}</td>
                    <td>{post.title}</td>
                    <td>{post.body}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ))}
      </div>
      )}
    </div>
  )
}

export default App
