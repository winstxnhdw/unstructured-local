# unstructured-local

A locally hosted FastAPI server with HTTP/2 support for [unstructured](https://github.com/Unstructured-IO/unstructured).

## Setup

Populate the `.env` file with the following.

```bash
echo SERVER_URL=http://localhost >> .env
echo SERVER_CONTAINER_NAME=server >> .env
echo SERVER_PORT=5555 >> .env
```

Run the following command to start the server.

```bash
docker compose up
```
