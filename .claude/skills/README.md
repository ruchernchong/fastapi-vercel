# Claude Code Skills

This directory contains custom skills for Claude Code to help with FastAPI development and deployment tasks.

## Available Skills

### `dev-server`
Starts the local FastAPI development server with hot reload enabled. Use this when you want to test your API locally.

**Usage**: Tell Claude to use the `dev-server` skill or type `/dev-server` in Claude Code.

### `deploy`
Deploys the FastAPI application to Vercel (preview or production). Handles git status checks and provides deployment URLs.

**Usage**: Tell Claude to use the `deploy` skill or type `/deploy` in Claude Code.

### `format-code`
Formats Python code using Black code formatter following the project's code style.

**Usage**: Tell Claude to use the `format-code` skill or type `/format-code` in Claude Code.

### `add-endpoint`
Guides you through adding a new FastAPI endpoint with proper conventions including:
- Pydantic models for validation
- Cache control headers for GET endpoints
- Proper type hints and documentation
- Code formatting

**Usage**: Tell Claude to use the `add-endpoint` skill or type `/add-endpoint` in Claude Code.

### `test-api`
Tests FastAPI endpoints locally using curl, including checking cache headers and request/response validation.

**Usage**: Tell Claude to use the `test-api` skill or type `/test-api` in Claude Code.

## How Skills Work

Skills are specialized prompts that guide Claude Code through specific development tasks. Each skill is defined in a markdown file and provides step-by-step instructions for completing common development workflows.

When you invoke a skill, Claude Code will follow the instructions in the skill file to help you complete the task efficiently and according to project conventions.
