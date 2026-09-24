#1. Grab a clean computer image that already has Python installed 
FROM python:3.13-slim

#2. Install uv inside the container 
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

#3. Set the working directory
WORKDIR /app

#4. Copy ONLY the dependency files first (for fast Docker caching)
COPY pyproject.toml uv.lock ./

#5. Install all dependencies system-wide inside the container
RUN uv pip install --system -r pyproject.toml

#6. Copy the rest of your FastAPI source code 
COPY . .

# Expose port 8000 so the app can be accessed from outside the container
EXPOSE 8000

#7. Start Uvicorn 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]