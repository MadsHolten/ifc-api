# IFC-APIs
This image should enable you to easily start building IFC to LBD parsers.

This final image is on Dockerhub and can be installed from there.

## Use
Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Run command `docker-compose up` from this folder
- Visit `http://localhost:5000/docs` in your browser
- Unfold `POST /api/hello-ifc/` and click `Try it out`
- Upload an IFC and execute the method

## Extend
The `apis` folder contains all the code. `main.py` specifies endpoints that call methods in the `methods`-folder and the `helpers`-folder contains generic helper functions that can be used anywhere.

The included `hello-ifc` endpoint simply demonstrates the use of the API. How to load an IFC-file and how to build and return some simple JSON-LD representation of the content.

If you need Python packages that are not included already, add them to `environment.yml` and run `docker-compose build`