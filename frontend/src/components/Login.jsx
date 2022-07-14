import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Login(props) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState(''); 
    const history = useNavigate ();

    function handleSubmit(e) {
        e.preventDefault();

        loginUser().then(data => {
            props.setToken(data.access_token);
            localStorage.setItem('token', JSON.stringify(data.access_token));
            history('/');
        })
    }

    async function loginUser() {
        const searchParams = new URLSearchParams();
        searchParams.append ('username', username);
        searchParams.append ('password', password);

        const response = await fetch('/token', {
            method: 'POST',
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: searchParams.toString(),
        });
        const data = await response.json();

        return data;

    }

    function registerUser() {
        history('/register');
    }

    return (
        <div>
        <form onSubmit={handleSubmit}>
            <p>
                Username: <input type="text" onChange={e => setUsername(e.target.value)}/>
            </p>
            <p>
                Password: <input type="password" onChange={e => setPassword(e.target.value)}/>
            </p>
            <p>
                <button>Login</button>
            </p>
        </form>

        <button onClick={registerUser}>Register</button>
        </div>
    )
}

export default Login;