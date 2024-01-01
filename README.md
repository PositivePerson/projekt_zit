## Used WebRTC

There are three servers:
- JavaScript Node.JS Express
- Python AIOHTTP
- Python FastAPI

## Python installation
Run `docker compose -f docker-compose-fastapi.yaml up --build -d` to use FastAPI

## JavaScript installation

Run `docker compose -f docker-compose-nodejs.yaml up --build -d` to start video app, it would be available at [http://localhost:3000](http://localhost:3000)

## Local start

To run the app without docker:
 
`npm i && npm run dev`

## Links

- [Official site of WebRTC](https://webrtc.github.io/)
- [AIOHTTP Socket.IO](https://python-socketio.readthedocs.io/en/latest/server.html#aiohttp)
- [FastAPI Socket.IO](https://github.com/pyropy/fastapi-socketio)