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

# Set permissions for db.sqlite3 to ensure write access
RUN chmod 777 /app/db.sqlite3

# Expose the port that Django will use
EXPOSE 9000

# Switch to non-root user
USER appuser

# Command to run on container startup:
CMD ["sh", "-c", "python manage.py migrate && python create_superuser.py && python manage.py runserver 0.0.0.0:9000"]
