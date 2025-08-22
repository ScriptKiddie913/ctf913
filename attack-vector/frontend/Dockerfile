FROM node:20-slim

WORKDIR /app
COPY frontend/package.json /app/package.json
COPY frontend/vite.config.js /app/vite.config.js
RUN npm install
COPY frontend /app
EXPOSE 3000
CMD ["npm","run","dev"]
