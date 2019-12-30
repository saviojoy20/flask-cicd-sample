FROM  alpine:3.8

RUN  mkdir /var/app

WORKDIR /var/app

COPY ./app/app.py  .
COPY ./requirement.txt .

RUN apk add --no-cache python3
RUN pip3 install -r requirement.txt


CMD ["python3" , "app.py"]
