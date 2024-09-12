FROM public.ecr.aws/lambda/python:3.10

WORKDIR /var/task

COPY handler.py .
COPY requirements.txt .

RUN /var/lang/bin/python3.10 -m pip install -r requirements.txt

CMD ["handler.lambda_handler"]