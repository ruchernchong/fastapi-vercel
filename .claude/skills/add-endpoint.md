# add-endpoint

Add a new endpoint to the FastAPI application following project conventions.

## Instructions

1. Ask the user for the following information:
   - HTTP method (GET, POST, PUT, DELETE, etc.)
   - Endpoint path (e.g., `/users/{user_id}`)
   - What the endpoint should do
   - If it needs request/response models

2. Read the current `api/index.py` file to understand the existing structure

3. Create the endpoint following these conventions:
   - Use Pydantic models for request/response validation if needed
   - For GET endpoints, add cache control headers using the `add_cache_control()` dependency pattern
   - Place the new endpoint in a logical location within the file
   - Add proper type hints and docstrings
   - Follow the existing code style

4. After adding the endpoint:
   - Format the code using Black: `uv run black api/`
   - Suggest testing the endpoint locally
   - Show the user how to access the new endpoint in the interactive docs at http://localhost:8000/docs
