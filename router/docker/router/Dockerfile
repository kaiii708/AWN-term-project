FROM python:3.9

WORKDIR /src

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

COPY ./router.py config.py  /src

EXPOSE 8101 8201

CMD [ "python3", "-u", "router.py" ]