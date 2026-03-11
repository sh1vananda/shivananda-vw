export default function TaskList({tasks, refresh, toggleTask, deleteTask}) {
    return (
        <div>
            {tasks.map(t => (
                <div key={t.id}>
                    <span> {t.title} ({t.priority})</span>
                    <button onClick={async () => {
                        await toggleTask(t.id)
                        refresh()
                    }}>
                        {t.completed ? "undo" : "complete"}
                    </button>
                    <button onClick={async () => {
                        await deleteTask(t.id)
                        refresh()
                    }}>
                        Delete
                    </button>
                </div>
            ))}
        </div>
    )
}