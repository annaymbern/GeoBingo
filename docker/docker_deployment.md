To make GeoBingo easy to run on any machine, we containerised the application using Docker. The Dockerfile (located in the docker/ directory) builds a lightweight image based on python:3.10-slim. It sets /geobingo as the working directory, copies requirements.txt into the image, installs all Python dependencies with pip, and then copies the rest of the project files. The container is configured to start the game by default using:

CMD ["python", "my_package/main.py"]


The container is orchestrated through docker-compose.yml, which defines a single service called geobingo. This service builds the image from the Dockerfile (docker/Dockerfile), runs it with stdin_open: true and tty: true so the user can interact with the terminal, and sets the working directory to /geobingo. A bind mount is used to provide the capitals dataset to the container (../data/capitals.csv:/geobingo/data/capitals.csv:ro), and a named volume (geobingo_state) is attached at /geobingo/state to persist any game state or logs independently of the container lifecycle. The service is configured with restart: unless, stopped to keep it available during development.

To build and run the final deployment, the user only needs Docker and Docker Compose. From the docker/ folder of the repository, running:

docker compose up --build


builds the image and starts the geobingo container. The game then runs directly inside the container’s interactive terminal, using the mounted CSV file and preserving state through the volume, which provides a reproducible and consistent runtime environment across different systems.
