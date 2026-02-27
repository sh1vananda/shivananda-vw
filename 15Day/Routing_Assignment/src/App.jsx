import { Routes, Route, Link, Navigate} from 'react-router-dom'
import { useState } from 'react'

import ProtectedRoute from './ProtectedRoute.jsx'

import Login from './pages/Login.jsx'
import Register from './pages/Register.jsx'

import Home from './pages/Home.jsx'
import Posts from './pages/Posts.jsx'
import Users from './pages/Users.jsx'
import Albums from './pages/Albums.jsx'

function App() {
  const [isAuth, setIsAuth] = useState(
    sessionStorage.getItem("isAuth") === "true"
  )

  return (
    <>
      <header>
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark px-4">
          <div className="container-fluid">

            <div className="navbar-nav">
              <Link className="nav-link text-light" to="/home">Home</Link>
              <Link className="nav-link text-light" to="/users">Users</Link>
              <Link className="nav-link text-light" to="/posts">Posts</Link>
              <Link className="nav-link text-light" to="/albums">Albums</Link>
            </div>

            <div className="ms-auto">

              {isAuth ? (
                <Link
                  className="btn btn-outline-light"
                  to="/home"
                  onClick={() => {
                    sessionStorage.removeItem("isAuth")
                    setIsAuth(false)
                  }}
                >
                  Logout
                </Link>
              ) : (
                <Link className="btn btn-outline-light" to="/login">
                  Login
                </Link>
              )}

            </div>

          </div>
        </nav>
      </header>

      <Routes>
        <Route path="/login" element={<Login setIsAuth={setIsAuth} />} />
        <Route path="/register" element={<Register />} />
        <Route path="/" element={<Navigate to="/home" replace />} />
        <Route path="/home" element={<Home />} />
        <Route path="/users" element={<ProtectedRoute><Users /></ProtectedRoute>} />
        <Route path="/posts" element={<ProtectedRoute><Posts /></ProtectedRoute>} />
        <Route path="/albums" element={<ProtectedRoute><Albums /></ProtectedRoute>} />
        
        <Route path="*" element={<h1>404 - Not Found</h1>} />
      </Routes>
    </>
  )
}

export default App;