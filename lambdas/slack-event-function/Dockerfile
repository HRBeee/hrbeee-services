FROM public.ecr.aws/lambda/python:3.10

WORKDIR /var/task

COPY slack-event-function/handler.py .
COPY slack-event-function/requirements.txt .

RUN /var/lang/bin/python3.10 -m pip install -r requirements.txt

CMD ["handler.lambda_handler"]