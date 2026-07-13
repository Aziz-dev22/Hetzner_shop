"""
Hetzner Shop
Docker Setup
"""

from __future__ import annotations


from pathlib import Path



ROOT_DIR = Path.cwd()



DOCKERFILE = ROOT_DIR / "Dockerfile"


COMPOSE_FILE = ROOT_DIR / "docker-compose.yml"



def create_dockerfile():


    content = """
FROM python:3.12-slim


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


CMD ["python", "-m", "app.main"]
"""


    DOCKERFILE.write_text(

        content.strip(),

        encoding="utf-8",

    )



def create_compose_file():


    content = """
services:

  app:

    build: .

    container_name: hetzner-shop

    restart: always


    env_file:

      - .env


    ports:

      - "8000:8000"



  postgres:

    image: postgres:16


    container_name: hetzner-shop-db


    restart: always


    environment:

      POSTGRES_DB: hetznershop

      POSTGRES_USER: hetzner

      POSTGRES_PASSWORD: change_me


    volumes:

      - postgres_data:/var/lib/postgresql/data



volumes:

  postgres_data:
"""


    COMPOSE_FILE.write_text(

        content.strip(),

        encoding="utf-8",

    )



def setup_docker():


    print(
        "Creating Docker configuration..."
    )


    create_dockerfile()


    create_compose_file()


    print(
        "Docker setup completed"
    )



if __name__ == "__main__":

    setup_docker()
