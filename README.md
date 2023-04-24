# unstructured-local

A locally hosted server with HTTP/2 support for [unstructured](https://github.com/Unstructured-IO/unstructured) with FastAPI.

## Setup

Populate the `.env` file with the following.

```bash
echo BACKEND_URL=http://localhost >> .env
echo BACKEND_CONTAINER_NAME=backend >> .env
echo BACKEND_PORT=5000 >> .env
```

Run the following command to start the server.

```bash
docker compose up --build
```
