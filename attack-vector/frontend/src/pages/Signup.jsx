import React, {useState} from 'react'
import { api, saveTokens } from '../lib/auth'

export default function Signup(){
  const [email,setEmail]=useState('')
  const [password,setPassword]=useState('')
  const [msg,setMsg]=useState('')
  const submit=async(e)=>{
    e.preventDefault()
    try{
      const data = await api('/auth/signup',{method:'POST',body:JSON.stringify({email,password})})
      saveTokens(data); location.href='/dashboard'
    }catch(e){ setMsg(e.message) }
  }
  return <div className="card">
    <h2>Sign up</h2>
    <form onSubmit={submit} className="grid">
      <input className="input" value={email} onChange={e=>setEmail(e.target.value)} placeholder="Email" />
      <input className="input" type="password" value={password} onChange={e=>setPassword(e.target.value)} placeholder="Password" />
      <button className="btn">Create account</button>
      {msg && <div className="badge">{msg}</div>}
    </form>
  </div>
}
