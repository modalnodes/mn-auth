FROM python:2.7.13


WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8090

CMD [ "python", "manage.py", "migrate" ]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8090" ]

