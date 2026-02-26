import { useState } from 'react'
import './App.css'
import Header from './components/Header'
import Footer from './components/Footer'

function App() {
  // const [count, setCount] = useState(0)
  const [users, setUsers] = useState([])

  async function getUsers() {
    const response = await fetch('https://jsonplaceholder.typicode.com/users')
    const data = await response.json()
    setUsers(data)
  }

  return (
    <>
      <Header />

      <main className="main">

        {/* <h1>{count}</h1>
        <div className="buttons">
          <button
            onClick={() => {
              if (count > 0) {
                setCount(count - 1)
              } else {
                console.log("cannot decrement below 0")
              }
            }}
          >-</button>
          <button onClick={() => setCount(count + 1)}>+</button>
          <button onClick={() => setCount(0)}>Reset</button>
        </div> */}

        <button onClick={getUsers}>Load Data</button>

        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Username</th>
              <th>Email</th>
              <th>City</th>
              <th>Company</th>
            </tr>
          </thead>

          <tbody>
            {users.map(user => (
              <tr key={user.id}>
                <td>{user.id}</td>
                <td>{user.name}</td>
                <td>{user.username}</td>
                <td>{user.email}</td>
                <td>{user.address.city}</td>
                <td>{user.company.name}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </main>

      <Footer />
    </>
  )
}

export default App