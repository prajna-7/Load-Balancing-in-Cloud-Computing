FROM python:3-slim
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org Flask
RUN pip install psutil
ENV NAME Kurt Tutschku
CMD ["python", "app.py"]
