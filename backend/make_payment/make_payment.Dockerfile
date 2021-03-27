FROM python:3-slim
WORKDIR /usr/src/app
COPY http_amqp.reqs.txt ./
RUN pip install --no-cache-dir -r http_amqp.reqs.txt
COPY ./make_payment.py ./invokes.py ./amqp_setup.py ./
CMD [ "python", "./make_payment.py" ]