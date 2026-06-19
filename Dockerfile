FROM python:3.12-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       openmpi-bin \
       libopenmpi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY examples ./examples

CMD ["mpirun", "--allow-run-as-root", "-np", "4", "python", "examples/01_hello.py"]
