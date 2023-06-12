FROM python:3.9

WORKDIR /src

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

COPY ./server.py config.py  /src

EXPOSE 8001

CMD [ "python3", "-u", "server.py" ]