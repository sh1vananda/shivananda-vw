import { Link, useNavigate } from "react-router-dom";

function Login({ setIsAuth }) {
  const navigate = useNavigate();

  async function login(formData) {
    const username = formData.get("username");
    const password = formData.get("password");

    const storedUser = JSON.parse(localStorage.getItem("user"));

    if (
      storedUser &&
      storedUser.username === username &&
      storedUser.password === password
    ) {
      sessionStorage.setItem("isAuth", "true");
      setIsAuth(true);
      navigate("/home");
    } else {
      alert("Invalid credentials");
    }
  }

  return (
    <div className="container mt-5" style={{ maxWidth: "400px" }}>
      <h2 className="mb-4 text-center">Login</h2>
      <form action={login}>
        <div className="mb-3">

          <label className="form-label">Username</label>
          <input
            name="username"
            type="text"
            className="form-control"
            required
          />
        </div>

        <div className="mb-3">
          <label className="form-label">Password</label>
          <input
            name="password"
            type="password"
            className="form-control"
            required
          />
        </div>

        <button type="submit" className="btn btn-primary w-100">Login</button>
      </form>

      <p className="mt-3 text-center">New? <Link to="/register">Register</Link></p>
    </div>
  );
}

export default Login;