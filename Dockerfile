FROM tensorflow/tensorflow:2.7.2

WORKDIR /srv
ADD . .
RUN pip3 install --requirement requirements.txt

# Run server
CMD ["gunicorn", "app:app", "--bind", ":5000", "--workers", "1"]
