# IFC-APIs
This image should enable you to easily start building IFC to LBD parsers.

This final image is on Dockerhub and can be installed from there.

## Use
Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Run command `docker-compose up` from this folder
- Visit http://localhost:5000/docs in your browser
- Unfold `POST /api/hello-ifc/` and click `Try it out`
- Upload an IFC and execute the method

## Run prebuilt image
If you just wish to use this image for your own implementation, simply get the built image from dockerhub and use the following `docker-compose.yml`:
```yml
version: '2.4'
services:

  ifc_apis:
    container_name: ifc_apis
    image: mhra/ifc-api:latest
    ports:
        - "5000:5000"
    networks:
        - "ifc_apis"
    volumes:
      - ./apis:/app/apis/

networks:
  ifc_apis:
```

All work is done in the apis folder, and you can start from the example in this repo and build from there. The important part is that you map your local folder to `/app/apis` in the container and that the folder contains a `main.py` file.

## Extend
The `apis` folder contains all the code. `main.py` specifies endpoints that call methods in the `methods`-folder and the `helpers`-folder contains generic helper functions that can be used anywhere.

The included `hello-ifc` endpoint simply demonstrates the use of the API. How to load an IFC-file and how to build and return some simple JSON-LD representation of the content.

If you need Python packages that are not included already, add them to `environment.yml` and run `docker-compose build`
