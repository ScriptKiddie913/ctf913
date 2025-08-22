import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Login from './pages/Login'
import Signup from './pages/Signup'
import Dashboard from './pages/Dashboard'
import Admin from './pages/Admin'
import Challenges from './pages/Challenges'
import Scoreboard from './pages/Scoreboard'
import { getAccessToken } from './lib/auth'

function AppShell({children}){
  return (
    <div className="container">
      <div className="nav card">
        <div style={{display:'flex',gap:'1rem',alignItems:'center'}}>
          <strong style={{fontSize:'1.2rem'}}>⚡ Attack Vector</strong>
          <a href="/challenges">Challenges</a>
          <a href="/scoreboard">Scoreboard</a>
          <a href="/admin">Admin</a>
        </div>
        <div>
          {getAccessToken() ? <a href="/dashboard">Dashboard</a> : <a href="/login">Login</a>}
        </div>
      </div>
      {children}
    </div>
  )
}

function PrivateRoute({children}){
  return getAccessToken() ? children : <Navigate to="/login" replace />
}

createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <AppShell>
      <Routes>
        <Route path="/" element={<Navigate to="/challenges" replace />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/dashboard" element={<PrivateRoute><Dashboard /></PrivateRoute>} />
        <Route path="/admin" element={<Admin />} />
        <Route path="/challenges" element={<Challenges />} />
        <Route path="/scoreboard" element={<Scoreboard />} />
      </Routes>
    </AppShell>
  </BrowserRouter>
)
