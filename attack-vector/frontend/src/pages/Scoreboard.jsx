import React, {useEffect, useState} from 'react'
import { api } from '../lib/auth'

export default function Scoreboard(){
  const [rows,setRows]=useState([])
  useEffect(()=>{ api('/scoreboard/').then(setRows).catch(console.error) },[])
  return <div className="card">
    <h2>Scoreboard</h2>
    <table style={{width:'100%'}}>
      <thead><tr><th align="left">Rank</th><th align="left">User</th><th align="right">Score</th></tr></thead>
      <tbody>
        {rows.map((r,i)=>(<tr key={r.user_id}><td>{i+1}</td><td>{r.email}</td><td align="right">{r.score}</td></tr>))}
      </tbody>
    </table>
  </div>
}
