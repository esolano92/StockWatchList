# Use the official AWS Lambda Python 3.8 base image
FROM public.ecr.aws/lambda/python:3.8

# Copy your function code to the container
COPY app/app.py ${LAMBDA_TASK_ROOT}

# Copy your requirements file to the container
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Copy templates to the container
COPY templates ${LAMBDA_TASK_ROOT}/templates

# Install any additional system packages, if required
RUN yum install -y gcc g++ make

# Install Python dependencies in the container
RUN pip3 install --no-cache-dir -r requirements.txt -t ${LAMBDA_TASK_ROOT}

# Command to run your Lambda function handler
CMD ["app.handler"]
