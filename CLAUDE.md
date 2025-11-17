# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a FastAPI application configured for deployment on Vercel using zero-config deployment. The project uses Python 3.12 and leverages Vercel's serverless function architecture with the Singapore region (sin1) for optimal performance.

## Architecture

### Vercel Zero-Config Structure
- **Entry point**: `api/index.py` - Contains the FastAPI application instance (`app`)
- **Deployment**: Uses Vercel's automatic Python detection - no explicit `vercel.json` build configuration needed
- **Region**: Configured for Singapore region (`sin1`) in `.vercel.json`
- **Runtime**: Uvicorn is included as a dependency for local development and Vercel's Python runtime

### Application Structure
The FastAPI app follows a single-file structure:
- Main application: `api/index.py` contains all routes and the FastAPI app instance
- The app uses Pydantic models for request/response validation
- Cache control headers are implemented via dependency injection pattern using `add_cache_control()`

### Caching Strategy
GET endpoints use aggressive cache control headers:
- Root endpoint (`/`): 1 year cache (`max_age=31536000`)
- Item retrieval (`/items/{item_id}`): 1 year cache
- Implemented through FastAPI's dependency injection system in `api/index.py:9-17`
- PUT endpoints intentionally do not use caching

## Development Commands

### Package Management
This project uses `uv` for Python package management (not pip or poetry):
```bash
# Install dependencies
uv sync

# Add a new dependency
uv add <package-name>

# Add a dev dependency
uv add --dev <package-name>
```

### Code Formatting
```bash
# Format code with Black
uv run black api/
```

### Local Development
```bash
# Run locally with uvicorn
uv run uvicorn api.index:app --reload

# The app will be available at http://localhost:8000
# Interactive API docs at http://localhost:8000/docs
```

### Testing on Vercel
```bash
# Install Vercel CLI if not already installed
npm i -g vercel

# Deploy to preview
vercel

# Deploy to production
vercel --prod
```

## Python Version Management
- Python version is pinned to 3.12 in `.python-version`
- This is critical for Vercel compatibility - do not upgrade to 3.13+ yet
- `pyproject.toml` specifies `requires-python = ">=3.12"`

## Important Deployment Notes
- The application follows Vercel's zero-config deployment pattern
- The `api/` directory structure is automatically recognized by Vercel as serverless functions
- The FastAPI app instance must be named `app` in `api/index.py` for Vercel to detect it
- Vercel automatically handles the ASGI server configuration
