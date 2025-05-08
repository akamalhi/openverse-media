# ---- Base image with Python 3.11 on Alpine ----
  FROM python:3.11-alpine

  
  # ---- Set working directory ----
  WORKDIR /app
  
  # ---- Install pip dependencies ----
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  
  # ---- Copy rest of the application ----
  COPY . .
  
  # ---- Optional: collect static files ----
  # RUN python manage.py collectstatic --noinput
  
  # ---- Set environment variables ----
  ENV PYTHONDONTWRITEBYTECODE=1
  ENV PYTHONUNBUFFERED=1
  
  # ---- Expose port and run the app ----
  EXPOSE 8000
  CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
  