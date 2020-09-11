# Docker Compose
Make's running multi-container applications on a single host a whole lot easier.

## Pre-requisites
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)
---

## In this tutorial

Previously we reviewed the steps for using docker to build an image, push it to a registry and run it. Expanding on our application, we're going to add a frontend and run our multi-container application with docker-compose

---

## Docker Compose Syntax
Before launching our application, it might be helpful to first review a bit of docker compose syntax. It's different from the Dockerfile syntax, it's a `.yaml` file, typically named `docker-compose.yaml`. Check out the [**docker compose reference guide**](https://docs.docker.com/compose/compose-file/) and our applications [**docker-compose.yaml**](docker-compose.yaml) to get an understanding of the file structure.

## Up
Make sure that your shell is set to the root of this repository, which is where the `docker-compose.yaml` file is located.

Now simply run
```
docker-compose up --build -d
```

You should see our containers building, followed by something like
```
Successfully tagged nutanix-container-presentation_demo-admin-app-frontend:latest
Creating demo-admin-app-db ... done
Creating demo-admin-app-backend ... done
Creating demo-admin-app-frontend ... done
```

## View the frontend
The front end is a simple admin panel UI built with React. You should be able to view the different app components at
- http://localhost/#/contacts
- http://localhost:5000/api/contacts
- http://localhost:5000/api-docs

## Check the logs
If you want to see what is being logged by our containers (stderr/stdout)
```
docker-compose logs -f
```

---

## Wrapping Up
To stop our containers, run
```
docker-compose down
```

---
## What's Next
- [Deploy the containerized application to Kubernetes](kubernetes/README.md)





