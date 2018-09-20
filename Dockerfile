FROM bvlc/caffe:cpu
ADD ./app /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]