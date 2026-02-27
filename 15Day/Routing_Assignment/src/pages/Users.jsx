import { useState, useEffect } from "react";

function Users() {
    const [users, setUsers] = useState([]);

    useEffect(()=> {
        async function getusers() {
            const response = await fetch("https://jsonplaceholder.typicode.com/users");
            const data = await response.json();
            setUsers(data);
        }
        getusers();
    }, [])

    return (
        <div className="container p-3">
            <h1 className="mb-3">USERS</h1>
            <ol className="list-group  w-50">          
                {
                    users.map(user => (
                        <li className="list-group-item" key={user.id}>{user.name} - {user.email}</li>
                    ))
                }
            </ol>  
        </div>
    )
    
}

export default Users;