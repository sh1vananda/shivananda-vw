import { useEffect, useState } from "react"
import TaskForm from "../components/TaskForm"
import TaskList from "../components/TaskList"

const API = "http://localhost:5000"

const getTasks = async (query="") => {
    const res = await fetch(`${API}/tasks${query}`)
    return res.json()
}

const createTask = async (task) => {
    await fetch(`${API}/tasks`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(task)
    })
}

const toggleTask = async (id) => {
    await fetch(`${API}/tasks/${id}/toggle`, {
        method: "PUT"
    })
}

const deleteTask = async (id) => {
    await fetch(`${API}/tasks/${id}`, {
        method: "DELETE"
    })
}

export default function TasksPage() {
    const [tasks, setTasks] = useState([])
    const load = async(query="") => {
        const data = await getTasks(query)
        setTasks(data)
    }
    useEffect(()=>{
        load()
    }, [])

    return (
        <div>
            <TaskForm refresh={load} createTask={createTask} />
            <TaskList
                tasks={tasks}
                refresh={load}
                toggleTask={toggleTask}
                deleteTask={deleteTask}
            />
        </div>
    )
}

