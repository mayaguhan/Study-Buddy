FROM python:3-slim
WORKDIR /usr/src/app
COPY http_amqp.reqs.txt ./
RUN pip install --no-cache-dir -r http_amqp.reqs.txt
COPY ./liaise_detail.py ./invokes.py ./amqp_setup.py ./
CMD [ "python", "./liaise_detail.py" ]