#!/usr/bin/env python3
import argparse
import subprocess
import os

def create_react_docker_container(container_name, public_port):
    # Check if Docker is installed
    try:
        subprocess.check_output(['docker', '--version'])
    except OSError as e:
        print("Docker is not installed on this system.")
        return

    # Create a new Docker container
    try:
        subprocess.run(['docker', 'run', '-d', '--name', container_name, '-p', f"{public_port}:3000", 'node:12.18.3-alpine', 'npx', 'create-react-app', container_name])
        print(f"Successfully created React Docker container with name: {container_name}")
    except Exception as e:
        print(f"Failed to create React Docker container with name: {container_name}. Error: {e}")

    # Create a Dockerfile
    with open(f"{container_name}.Dockerfile", "w") as f:
        f.write(f"FROM node:12.18.3-alpine\n")
        f.write(f"WORKDIR /app\n")
        f.write(f"COPY . /app\n")
        f.write(f"RUN npm install\n")
        f.write(f"EXPOSE 3000\n")
        f.write(f"CMD [\"npm\", \"start\"]\n")
    print(f"Successfully created Dockerfile for project: {container_name}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--public-port", type=int, help="Public port for the React app")
    parser.add_argument("-n", "--project-name", help="Name of the React project")
    args = parser.parse_args()

    container_name = args.project_name
    public_port = args.public_port

    create_react_docker_container(container_name, public_port)
