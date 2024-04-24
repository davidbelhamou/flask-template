FROM python:3.8.5
LABEL authors="davidb"

EXPOSE 8000
WORKDIR /app

COPY pip.conf /etc/pip.conf
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .


ENTRYPOINT ["gunicorn", "-b", "0.0.0.0", "webApp.feedbackRunner:app"]