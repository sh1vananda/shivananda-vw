function Home() {
  const isAuth = sessionStorage.getItem("isAuth") === "true";
  const storedUser = JSON.parse(localStorage.getItem("user"));

  return (
    <div className="container p-3">
      {isAuth ? (
        <h1>Hello, {storedUser.username}</h1>
      ) : (
        <h1>Hello, Guest</h1>
      )}
    </div>
  );
}

export default Home;