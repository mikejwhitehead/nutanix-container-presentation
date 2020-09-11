# Demo Admin App Backend

This app provides the backend for a simple contact list application. It's purpose is to demonstrate how apps are containerized and how that container runs.

## Pre-requisites

* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Docker](https://docs.docker.com/get-docker/)
* [DockerHub Account](https://hub.docker.com/signup)

---
## In this tutorial

We'll get our python flask backend running in a container on our local machine. To get there, we'll cover:
* Building a container image using this [Dockerfile](Dockerfile)
* Storing the container hub in the Docker Hub registry.
* Running a [mongodb container](https://hub.docker.com/_/mongo) to provide the database for our application
* Running our demo-admin-backend example container
* Stopping our containers

---

## Build our container image
This walkthrough will be more copy/pasteable and therefore easier to step through if we set a couple environment variables for our docker creds first.
```
export DOCKER_HUB_USERNAME=<your_docker_hub_username>
export DOCKER_HUB_PASSWORD=<your_docker_hub_password>
```

Next you'll clone the repo and then change the current directory to where our `Dockerfile` is stored.
```
git clone https://github.com/mikejwhitehead/nutanix-container-presentation.git
cd nutanix-container-presentation/demo-admin-backend
```
Now that we are in the directory with our `Dockerfile`, simply run
```
docker build -t $DOCKER_HUB_USERNAME/demo-admin-backend:v0.1.0 .
```

To expain the above `docker-build` command
* **-t** set's the image tag
* **.** (period) at the end of the line sets the build context and is the path where docker look for the `Dockerfile`

## Store our image in a container registry
With our image created, we'll next want to push it to our container registry (Docker Hub). We need to login first:
```
echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USERNAME --password-stdin
```

Now push the container image
```
docker push $DOCKER_HUB_USERNAME/demo-admin-backend:v0.1.0
```

## Start a mongodb container
In order for our backend to run, we need a database for it. Here we will run a [mongodb container image](https://hub.docker.com/_/mongo) that's already available on Docker Hub. Before we start the container though, it'd be best to create a network so our containers can communicate with each other
```
docker network create demo-admin-app-network
```

Now we can start up the mongodb container, setting it's network to the one we just created
```
docker run -d \
    --name demo-admin-app-db \
    --network demo-admin-app-network \
    mongo
```
To detail this command further
* **-d** runs the container detached from the current shell (in the background)
  > **Note:** If you don't want to run the container detached, you would instead use the **-it** flag.
* **--name** gives our container a desired name
* **--network** connects our container to a specific docker network
* **mongo** is the container image that will run

Our mongodb container should now be running. You can confirm that it is by running the `docker ps` command. If it is running, the output should look something like
```
CONTAINER ID  IMAGE  COMMAND          CREATED        STATUS         PORTS                      NAMES
62496edd51db  mongo  "docker-entr…"   3 seconds ago  Up 3 seconds   0.0.0.0:27017->27017/tcp   demo-admin-app-db
```

## Start our container
In much the same fashion for how we started the mongodb container, lets get our application backend container up. This time we will run the container in interactive mode (with the **-it** flag)
```
docker run -it --name demo-admin-backend \
    --publish 5000:5000 --network demo-admin-app-network \
    $DOCKER_HUB_USERNAME/demo-admin-backend:v0.1.0
```
You may have noticed the **--publish** flag in the above command. This publishes the specified container port to the host.

In your terminal, you should see the demo-admin-backend running. Looking something like
```
Waiting for database...
database started
[2020-09-11 06:19:17 +0000] [7] [INFO] Starting gunicorn 20.0.4
[2020-09-11 06:19:17 +0000] [7] [INFO] Listening at: http://0.0.0.0:5000 (7)
[2020-09-11 06:19:17 +0000] [7] [INFO] Using worker: gthread
[2020-09-11 06:19:17 +0000] [9] [INFO] Booting worker with pid: 9
[2020-09-11 06:19:17 +0000] [10] [INFO] Booting worker with pid: 10
```
You should also be able to access the apps api documentation at http://localhost:5000/api-docs

---

## Wrapping Up
To stop all running containers use the command
```
docker container stop $(docker container ls -aq)
```
The `docker container ls -aq` in the above command generates a list of all containers.

Once all containers are stopped, remove them using the docker container rm command, followed by the containers ID list.
```
docker container rm $(docker container ls -aq)
```
---

## What's Next
- [Add the frontend and run the multi-container application with docker-compose](../docker-compose.md)

