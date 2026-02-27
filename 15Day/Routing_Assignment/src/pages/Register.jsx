import { Link, useNavigate } from "react-router-dom";

function Register() {
  const navigate = useNavigate();

  async function register(formData) {
    const username = formData.get("username");
    const password = formData.get("password");

    localStorage.setItem(
      "user",
      JSON.stringify({ username, password })
    );

    alert("Registered successfully!");
    navigate("/login");
  }

  return (
    <div className="container mt-5" style={{ maxWidth: "400px" }}>
      <h2 className="mb-4 text-center">Register</h2>

      <form action={register}>
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

        <button type="submit" className="btn btn-success w-100">Register</button>
      </form>

      <p className="mt-3 text-center">Existing user? <Link to="/login">Login</Link></p>
    </div>
  );
}

export default Register;