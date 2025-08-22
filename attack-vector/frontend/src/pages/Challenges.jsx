import React, {useEffect, useState} from 'react'
import { api } from '../lib/auth'

export default function Challenges(){
  const [items,setItems]=useState([])
  const [msg,setMsg]=useState('')
  const [flag,setFlag]=useState({})
  const load=()=>api('/challenges/').then(setItems).catch(e=>setMsg(e.message))
  useEffect(load,[])
  const submit=async(id)=>{
    try{
      await api('/submissions/',{method:'POST',body:JSON.stringify({challenge_id:id, flag:flag[id]||''})})
      setMsg('Flag correct!'); load()
    }catch(e){ setMsg(e.message) }
  }
  return <div className="grid">
    {msg && <div className="card">{msg}</div>}
    <div className="grid grid-2">
      {items.map(c=>(
        <div className="card" key={c.id}>
          <h3>{c.title} <span className="badge">{c.difficulty}</span> <span className="badge">{c.points} pts</span></h3>
          {c.storyline && <div className="badge">Story: {c.storyline} #{c.sequence||'?'}</div>}
          <p>{c.description}</p>
          <div style={{display:'flex',gap:'.5rem'}}>
            <input className="input" placeholder="AV{...}" value={flag[c.id]||''} onChange={e=>setFlag({...flag,[c.id]:e.target.value})}/>
            <button className="btn" onClick={()=>submit(c.id)}>Submit</button>
          </div>
        </div>
      ))}
    </div>
  </div>
}
