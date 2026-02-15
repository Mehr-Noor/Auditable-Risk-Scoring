FROM python:3.11-slim

# جلوگیری از buffer شدن لاگ‌ها
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# مسیر کاری
WORKDIR /app

# نصب وابستگی‌ها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# کپی کل پروژه
COPY . .

# پورت API
EXPOSE 8000

# اجرای FastAPI
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
