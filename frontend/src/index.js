import React, { useState }from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes , Route, Navigate } from 'react-router-dom';
import Board from './components/Board';
import Register from './components/Register';

function App() {
  const [token, setToken] = useState();

  return (
      <BrowserRouter>
        <Routes >
          <Route path="/register" element={<Register setToken={setToken}/>}/>
          {/* <Route path="/" element={token? <Board token={token}/> : <Navigate to="/register" replace/>}/> */}
          <Route path="/" element={<Board token={token}/>}/>
          <Route path="*" element={<Navigate to="/" replace />}/>
        </Routes>
      </BrowserRouter>
  )
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <App />
);

