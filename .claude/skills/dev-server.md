# dev-server

Start the local FastAPI development server with hot reload.

## Instructions

1. Start the development server using uvicorn with hot reload enabled
2. Use the command: `uv run uvicorn api.index:app --reload`
3. Inform the user that the server is running at http://localhost:8000
4. Remind them that interactive API documentation is available at http://localhost:8000/docs
5. The server will automatically reload when code changes are detected
