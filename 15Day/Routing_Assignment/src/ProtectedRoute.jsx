import  {Navigate} from "react-router";

function ProtectedRoute({children}) {
    const isAuth = sessionStorage.getItem("isAuth") === "true";

    if(!isAuth) {
        return <Navigate to="/login" replace/>
    }
    return children;
}

export default ProtectedRoute;