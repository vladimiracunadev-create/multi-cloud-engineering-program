FROM python:3.12.11-slim@sha256:27f90d79cc85e9b7b2560063ef44fa0e9eaae7a7c3f5a9f74563065c5477cc24
WORKDIR /app
COPY app.py .
USER 65532:65532
EXPOSE 8080
HEALTHCHECK CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health/ready')"]
CMD ["python", "app.py"]
