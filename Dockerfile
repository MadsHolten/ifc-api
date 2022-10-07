FROM continuumio/miniconda3

WORKDIR /app

# Make RUN commands use `bash --login`:
SHELL ["/bin/bash", "--login", "-c"]

# Create the environment:
COPY environment-api.yml .
# RUN conda env update -f environment-api.yml
RUN conda env create -f environment-api.yml -n myenv

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

# Test env
RUN echo "Make sure ifcopenshell is installed:"
RUN python -c "import ifcopenshell"

COPY apis/ /app/apis
WORKDIR /app/apis

# The code to run when container is started:
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "myenv", "python", "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]