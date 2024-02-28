FROM python:3.12.2-slim-bookworm

WORKDIR /usr/src/app

COPY . .
RUN pip install -r requirements.txt

RUN chmod +x build.sh
RUN ./build.sh
EXPOSE 12345
EXPOSE 5000
EXPOSE 12344

CMD ["./start.sh"]
