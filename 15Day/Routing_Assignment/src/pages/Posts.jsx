import { useState, useEffect } from "react";

function Posts() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    async function fetchPosts() {
      const response = await fetch("https://jsonplaceholder.typicode.com/posts");
      const data = await response.json();
      setPosts(data);
    }
    fetchPosts();
  }, [])    

  return (
    <div className="container p-3">
      <h1 className="mb-3">POSTS</h1>
      {
        posts.map(post => (
          <div key={post.id}>
            <h2>{post.id}. {post.title}</h2>
            <p>{post.body}</p>
          </div>
        ))
      }
    </div>
  )
}

export default Posts;