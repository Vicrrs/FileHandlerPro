# Use a Python slim-buster image as a parent image
FROM python:3.12-slim

# Environment variables to ensure Python runs in unbuffered mode
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /code

# Copy only the files necessary for installing dependencies
COPY pyproject.toml poetry.lock /code/

# Install dependencies using Poetry in a way that ensures no virtual environment is created
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

# Copy the rest of your application code
COPY . /code/

# Specify the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8100"]
