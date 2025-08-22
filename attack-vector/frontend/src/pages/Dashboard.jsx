import React, {useEffect, useState} from 'react'
import { api } from '../lib/auth'

export default function Dashboard(){
  const [me,setMe]=useState(null)
  const [mine,setMine]=useState([])
  useEffect(()=>{
    api('/users/me').then(setMe).catch(console.error)
    api('/submissions/mine').then(setMine).catch(console.error)
  },[])
  return <div className="grid">
    <div className="card">
      <h2>Welcome {me?.email}</h2>
      <p>Solved challenges: {mine.filter(x=>x.correct).length}</p>
    </div>
    <div className="card">
      <h3>Your submissions</h3>
      <ul>
        {mine.map(s=>(<li key={s.id}>#{s.challenge_id} — {s.correct ? '✅ correct' : '❌ incorrect'}</li>))}
      </ul>
    </div>
  </div>
}
