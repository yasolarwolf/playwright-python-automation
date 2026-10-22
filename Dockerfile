FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy
WORKDIR /app
COPY requerements.txt .
RUN pip install --no cache-dir -r requerements.txt
COPY . .
CMD ["pytest"]