# Attack Vector — CTF Platform (CTFd-like)

Secure full-stack platform for hosting cybersecurity challenges.

## Features
- Admin portal (seeded with the requested credentials; change for production)
- Categories, challenges, OSINT storylines with sequence
- Secure JWT auth, bcrypt password hashing
- Scoreboard (points per correct solve)
- Prevents resubmission after solve
- Defenses: security headers, parameterized ORM (no raw SQL), CORS restricted, flags stored as SHA-256 hashes
- Dockerized: PostgreSQL, FastAPI backend, React frontend, Nginx proxy

## Quickstart
```bash
docker compose up --build
# visit http://localhost:8080
# backend: http://localhost:8080/api/health
```

## Admin
- Email: sagnik.saha.raptor@gmail.com
- Password: Hotmeha21@21@##
(Seeded via backend/app/seed.py; change in .env for production)

## Notes
- The frontend is a minimal but modern UI. Replace Vite dev server with a production build + nginx static in production.
- CSRF: Auth uses Bearer tokens (access in memory), reducing CSRF risk.
- Flags never stored in plaintext; only hashes.
- Database migrations via Alembic.
