FROM python:3.10-alpine

#
WORKDIR /code

#
COPY requirements.txt /code/requirements.txt

#
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt
#
COPY ./app /code/app

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80","--reload"]