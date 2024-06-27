# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt or environment.yml
# If using requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# If using conda environment file
# COPY conf/environment.yml /app/conf/environment.yml
# RUN apt-get update && apt-get install -y wget && \
#     wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
#     bash miniconda.sh -b -p /opt/conda && \
#     rm miniconda.sh && \
#     /opt/conda/bin/conda env create -f /app/conf/environment.yml && \
#     /opt/conda/bin/conda clean -afy

# Make sure the environment is active
ENV PATH /opt/conda/envs/$(head -n 1 /app/conf/environment.yml | cut -d' ' -f2)/bin:$PATH

# Expose any ports the app is running on
# For example, if your app runs on port 8000
# EXPOSE 8000

# Define environment variable for Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "src/main.py"]