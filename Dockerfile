# Use a slim Python 3.12 image as the base
FROM python:3.12

# Set a working directory for the container
WORKDIR /code

# Copy requirements file (if using)
COPY requirements.txt .
# Install dependencies (if using)
RUN pip install -r requirements.txt

# Define volume to mount source code
VOLUME ["/code"]

# Default command to run bash shell
CMD ["bash"]
