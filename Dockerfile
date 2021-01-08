FROM python:3.6-stretch

COPY ./api /api/api
COPY requirements.txt /requirements.txt

# install build utilities
RUN apt-get update && \
	apt-get install -y gcc make apt-utils apt-transport-https ca-certificates build-essential

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/api
WORKDIR /api

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["api.main:app", "--host", "0.0.0.0"]