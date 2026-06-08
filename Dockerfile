# # Setting base image
# FROM python:3.11-slim

# # Setting working directory
# WORKDIR /app

# # Install Flask before copying everything else to save time
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# # Copy everything into the container
# COPY . .

# # Port the app will run on
# EXPOSE 5000

# # Creating a non root user - principle of least privilege
# RUN adduser --disabled-password --gecos "" appuser && chown -R appuser /app

# # Non root user running the app
# USER appuser

# # Command to run the app
# CMD ["python", "app.py"]


# Stage 1 - Builder
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 2 - Final
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
RUN adduser --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
EXPOSE 5000
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "app.py"]