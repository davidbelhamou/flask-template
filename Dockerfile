FROM python:3.9

EXPOSE 5000
WORKDIR /app
COPY pip.conf /etc/pip.conf
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r req.txt

ENTRYPOINT ["python", "myApp.py"]
# ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5004", "webApp.:app]
