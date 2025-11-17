# test-api

Test the FastAPI endpoints locally using curl or httpie.

## Instructions

1. Ask the user which endpoint they want to test

2. Check if the development server is running:
   - Try to connect to http://localhost:8000
   - If not running, offer to start it first

3. For GET requests:
   - Use curl with verbose headers to check cache control: `curl -v http://localhost:8000/endpoint`
   - Show the response and relevant headers

4. For POST/PUT requests:
   - Ask the user for the request body
   - Use curl with JSON content type: `curl -X POST http://localhost:8000/endpoint -H "Content-Type: application/json" -d '{"key": "value"}'`

5. Display the response clearly and check if it matches expectations

6. Remind the user they can also test interactively at http://localhost:8000/docs
