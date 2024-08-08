FROM python:3.7

# Create a virtual environment
RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

# Set the working directory
WORKDIR /app

# Copy the application code
ADD . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port
ENV PORT 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
