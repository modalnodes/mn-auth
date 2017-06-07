FROM python:2.7.13


WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

LABEL mn=backend,frontend
LABEL mn.type=api,admin
LABEL mn.api.definiton=djoser.api
LABEL mn.api.flavour=drf
LABEL mn.technology=django

EXPOSE 8090

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8090" ]

