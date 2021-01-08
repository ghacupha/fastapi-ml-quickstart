# fastAPI ML quickstart

This is a quickstart app for serving a model on API with fastapi

## Environment

For purposes of creation of docker images configure the following variables in the GITHUB repo

 - DOCKERHUB_USERNAME
 - DOCKERHUB_TOKEN
 - DOCKERHUB_ORG
 - DOCKERHUB_REPO
 - DOCKERHUB_VER

## Project setup
1. Create the virtual environment.
```
virtualenv /path/to/venv --python=/path/to/python3
```
You can find out the path to your `python3` interpreter with the command `which python3`.

2. Activate the environment and install dependencies.
```
source /path/to/venv/bin/activate
pip install -r requirements.txt
```

3. Launch the service
```
uvicorn api.main:app
```

## Posting requests locally
When the service is running, try
```
127.0.0.1/docs
```
or 
```
curl
```

## Deployment with Docker
1. Build the Docker image
```
docker build --file Dockerfile --tag fastapi-ml-quickstart .
```

2. Running the Docker image
```
docker run -p 8000:8000 fastapi-ml-quickstart
```

3. Entering into the Docker image
```
docker run -it --entrypoint /bin/bash fastapi-ml-quickstart
```

## docker-compose
1. Launching the service
```
docker-compose up
```
This command looks for the `docker-compose.yaml` configuration file. If you want to use another configuration file,
it can be specified with the `-f` switch. For example  

2. Testing
```
docker-compose -f docker-compose.test.yaml up --abort-on-container-exit --exit-code-from fastapi-ml-quickstart
```


### Acknowledgments

The bulk of the source code in this illustration was created by [Tivadar Danka](https://github.com/cosmic-cortex/fastAPI-ML-quickstart)