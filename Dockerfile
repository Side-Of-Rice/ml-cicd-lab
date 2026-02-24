FROM python:3.11
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

EXPOSE 5000
CMD ["python", "-u", "run_all.py"]