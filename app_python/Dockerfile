FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt main.py ./

RUN pip install --no-cache-dir -r requirements.txt

RUN groupadd -r nonroot_group \
    && useradd -r -m -g nonroot_group nonroot \
    && mkdir -p /app/data \
    && chown -R nonroot:nonroot_group /app/data \
    && chmod -R 775 /app/data

USER nonroot

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
