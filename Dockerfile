# Use Python 3.12 slim image as the base
ARG PYTHON_VERSION=3.12.3
FROM python:${PYTHON_VERSION}-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency file and install dependencies
COPY requirements.txt requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install --no-cache-dir -r requirements.txt

# Create a non-privileged user and switch to it
ARG UID=10001
RUN adduser --disabled-password --gecos "" --home "/nonexistent" --shell "/sbin/nologin" --no-create-home --uid "${UID}" appuser

# Copy the entire project into the container
COPY . .

# Create database folder, set permissions so appuser can write
RUN mkdir -p /app/data && chown -R appuser:appuser /app/data && chmod 777 /app/data
RUN touch /app/data/db.sqlite3 && chmod 777 /app/data/db.sqlite3

# Expose the port that Django will use
EXPOSE 9000

# Switch to non-root user
USER appuser

# Run the application on 0.0.0.0:9000 so it’s accessible externally
CMD ["sh", "-c", "python manage.py migrate && python create_superuser.py && python manage.py runserver 0.0.0.0:9000"]
