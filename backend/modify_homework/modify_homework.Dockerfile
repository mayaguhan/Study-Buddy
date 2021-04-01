FROM python:3-slim
WORKDIR /usr/src/app
COPY http_amqp.reqs.txt ./
RUN pip install --no-cache-dir -r http_amqp.reqs.txt
COPY ./modify_homework.py ./invokes.py ./amqp_setup.py ./
CMD [ "python", "./modify_homework.py" ]