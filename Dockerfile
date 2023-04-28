FROM python:3.9

RUN pip install keras tensorflow numpy tensorflowjs

ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
ENV OUTPUT_DIR=/Users/marcoshenrich/desktop/neural_search/model

WORKDIR /
COPY . /

CMD ["python", "spellcheck_test.py"]