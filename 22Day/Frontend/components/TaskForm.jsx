import { useState } from "react"

export default function TaskFrom({refresh, createTask}) {
    const [title, setTitle] = useState("")
    const [priority, setPriority] = useState("low")

    const submit = async (e) => {
        e.preventDefault()
        await createTask({title, priority})
        setTitle("")
        refresh()
    }
    
    return (
        <form onSubmit={submit}>
            <input placeholder="title" value={title} onChange={e => setTitle(e.target.value)} required/>
            <select value={priority} onChange={e => setPriority(e.target.value)}>
                <option>low</option>
                <option>medium</option>
                <option>high</option>
            </select>
            <button>Add Task</button>
        </form>
    )
}