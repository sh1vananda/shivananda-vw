import { useState, useEffect } from "react";

function Albums() {
    const [albums, setAlbums] = useState([]);

    useEffect(() => {
        async function getAlbums() {
            const response = await fetch("https://jsonplaceholder.typicode.com/albums");
            const data = await response.json();
            setAlbums(data);
        }
        getAlbums();
    }, [])

    return (
        <div className="container p-3">
            <h1 className="mb-3">ALBUMS</h1>
            
            <table className="table table-striped w-50">
                <thead>
                    <tr>
                        <th style={{border: "1px solid black", padding: "8px"}}>ID</th>
                        <th style={{border: "1px solid black", padding: "8px"}}>Album Title</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        albums.map(album =>(
                            <tr key = {album.id}>
                                <td style={{ border: "1px solid black", padding: "8px" }}>{album.id}</td>
                                <td style={{ border: "1px solid black", padding: "8px" }}>{album.title}</td>
                            </tr>
                        ))
                    }
                </tbody>
            </table>
        </div>
    )
}

export default Albums;