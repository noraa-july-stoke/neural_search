FROM python:3.9

RUN pip install keras tensorflow numpy tensorflowjs

ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

COPY . /spellcheck_test
WORKDIR /spellcheck_test

CMD ["python", "spellcheck_test.py"]