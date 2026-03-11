import { Routes, Route, Link } from "react-router-dom";
import TasksPage from "../pages/TasksPage";

export default function App() {
  return (
    <div>
      <h1>Task Manager</h1>
      <nav>
        <Link to="/">Tasks</Link>
      </nav>
      <Routes>
        <Route path="/" element={<TasksPage />} />
      </Routes>
    </div>
  )
}