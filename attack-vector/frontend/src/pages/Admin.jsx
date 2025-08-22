import React, {useEffect, useState} from 'react'
import { api } from '../lib/auth'

export default function Admin(){
  const [cats,setCats]=useState([])
  const [ch,setCh]=useState({title:'',description:'',difficulty:'easy',points:100,flag:'',category_id:'',storyline:'',sequence:''})
  const [msg,setMsg]=useState('')
  const load=()=>api('/admin/categories').then(setCats).catch(e=>setMsg(e.message))
  useEffect(load,[])

  const addCat=async()=>{
    try{ 
      await api('/admin/categories',{method:'POST',body:JSON.stringify({id:0,name:prompt('Category name'),description:prompt('Description')||''})})
      load()
    }catch(e){ setMsg(e.message) }
  }
  const addChallenge=async(e)=>{
    e.preventDefault()
    try{
      const body = {...ch, points:parseInt(ch.points||'0'), category_id:parseInt(ch.category_id||'0'), sequence: ch.sequence? parseInt(ch.sequence): null}
      await api('/admin/challenges',{method:'POST',body:JSON.stringify(body)})
      setMsg('Challenge added')
    }catch(e){ setMsg(e.message) }
  }

  return <div className="grid">
    <div className="card">
      <h2>Admin — Manage</h2>
      <button className="btn" onClick={addCat}>+ Add Category</button>
      <div style={{marginTop:'1rem'}}>
        <h3>New Challenge</h3>
        <form onSubmit={addChallenge} className="grid">
          <input className="input" placeholder="Title" value={ch.title} onChange={e=>setCh({...ch,title:e.target.value})}/>
          <textarea className="input" placeholder="Description" value={ch.description} onChange={e=>setCh({...ch,description:e.target.value})}/>
          <div style={{display:'flex', gap:'.5rem'}}>
            <select className="input" value={ch.difficulty} onChange={e=>setCh({...ch,difficulty:e.target.value})}>
              <option>easy</option><option>medium</option><option>hard</option>
            </select>
            <input className="input" type="number" placeholder="Points" value={ch.points} onChange={e=>setCh({...ch,points:e.target.value})}/>
          </div>
          <div style={{display:'flex', gap:'.5rem'}}>
            <select className="input" value={ch.category_id} onChange={e=>setCh({...ch,category_id:e.target.value})}>
              <option value="">Select category</option>
              {cats.map(c=>(<option key={c.id} value={c.id}>{c.name}</option>))}
            </select>
            <input className="input" placeholder="Flag (e.g., AV{...})" value={ch.flag} onChange={e=>setCh({...ch,flag:e.target.value})}/>
          </div>
          <div style={{display:'flex', gap:'.5rem'}}>
            <input className="input" placeholder="Storyline (optional)" value={ch.storyline} onChange={e=>setCh({...ch,storyline:e.target.value})}/>
            <input className="input" type="number" placeholder="Sequence (optional)" value={ch.sequence} onChange={e=>setCh({...ch,sequence:e.target.value})}/>
          </div>
          <button className="btn">Add Challenge</button>
          {msg && <div className="badge">{msg}</div>}
        </form>
      </div>
    </div>
    <div className="card">
      <h3>Tips</h3>
      <ul>
        <li>OSINT storylines: set the same <code>storyline</code> and ascending <code>sequence</code>.</li>
        <li>Flags are hashed server-side, never stored in plain text.</li>
        <li>Users cannot resubmit a flag after a correct solve.</li>
      </ul>
    </div>
  </div>
}
