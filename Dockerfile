FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /REST_Library
COPY requirements.txt requirements.txt
# Install dependencies
RUN pip install -r requirements.txt
#RUN pip install .

# Copy project
COPY . /REST_Library/