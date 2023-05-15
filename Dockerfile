FROM python:3.10.9

SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update

RUN useradd -rms /bin/bash django && chmod 777 /opt /run

WORKDIR /app

RUN chown -R django:django /app && chmod 755 /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["gunicorn","-b","0.0.0.0:8001","soaqaz.wsgi:application"]