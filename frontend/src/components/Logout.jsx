import React from "react";
import { Link, useNavigate } from "react-router-dom";

function Logout(props) {

    const navigate = useNavigate();

    function logoutUser() {
        localStorage.removeItem('token');
        navigate('/login');
    }

    return (
        <button onClick={logoutUser}>Log out</button>
    )
}

export default Logout;