export function saveTokens({access_token, refresh_token}){
  sessionStorage.setItem('access', access_token)
  sessionStorage.setItem('refresh', refresh_token)
}
export function getAccessToken(){ return sessionStorage.getItem('access') }
export async function api(path, opts={}){
  const headers = {'Content-Type':'application/json', ...(opts.headers||{})}
  const token = getAccessToken()
  if(token) headers['Authorization'] = 'Bearer ' + token
  const r = await fetch('/api'+path, {...opts, headers})
  if(!r.ok){
    const t = await r.json().catch(()=>({detail:r.statusText}))
    throw new Error(t.detail || 'Request failed')
  }
  return r.json()
}
