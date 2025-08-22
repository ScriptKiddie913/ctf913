import React, {useState} from 'react'
import { api, saveTokens } from '../lib/auth'

export default function Login(){
  const [email,setEmail]=useState('')
  const [password,setPassword]=useState('')
  const [msg,setMsg]=useState('')
  const submit=async(e)=>{
    e.preventDefault()
    try{
      const data = await api('/auth/login',{method:'POST',body:JSON.stringify({email,password})})
      saveTokens(data); location.href='/dashboard'
    }catch(e){ setMsg(e.message) }
  }
  return <div className="grid">
    <div className="card">
      <h2>Login</h2>
      <form onSubmit={submit} className="grid">
        <input className="input" value={email} onChange={e=>setEmail(e.target.value)} placeholder="Email" />
        <input className="input" type="password" value={password} onChange={e=>setPassword(e.target.value)} placeholder="Password" />
        <button className="btn">Login</button>
        {msg && <div className="badge">{msg}</div>}
      </form>
      <p>or <a href="/signup">Sign up</a></p>
    </div>
    <div className="card">
      <h3>Admin test creds</h3>
      <code>Email: sagnik.saha.raptor@gmail.com</code><br/>
      <code>Password: Hotmeha21@21@##</code>
    </div>
  </div>
}
