FROM python:3.10.2-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "DashBot" ]


# docker run --name my_bot -d --rm --] mybot

