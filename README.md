# Concurrency-Server-Architecture-Lab
A Backend Systems project focused on building and analyzing high‑concurrency programs using threads, processes, async I/O, locks, race conditions, and applied AI inference pipelines.

## 🎯 Goal
Build a multi-phase backend system demonstrating:

- Thread, Process and I/O multiplexing(event loop) servers.
- Thread pools  
- Async event loops  
- Race conditions  
- Lock-based synchronization  
- Nginx → Gunicorn → Uvicorn → FastAPI production stack  
- GPU inference queueing using semaphores  

## 📌 Overview
I will build, develop, test, and analyze different server architectures across seven phases:

1. **Raw threaded, async, and process-based servers**  
2. **FastAPI sync server (thread pool)**  
3. **FastAPI async server (event loop)**  
4. **Race condition simulation**  
5. **Lock-based synchronization**  
6. **Nginx → Gunicorn → Uvicorn → FastAPI architecture**  
7. **GPU inference queue simulation**

Each phase includes:

- Code  
- Documentation  
- Load tests  
- Performance results  

This project teaches **real backend intuition** by letting me *experience* it firsthand.

## 🗂️ Directory Structure

```text
backend-concurrency-lab/
├── phase-1-simple-server/
│   ├── thread-server.py
│   ├── async-server.py
│   ├── process-server.py
│   ├── README.md
│   └── load-tests/
├── phase-2-fastapi-sync/
│   ├── app.py
│   ├── README.md
│   └── load-tests/
├── phase-3-fastapi-async/
│   ├── app.py
│   ├── README.md
│   └── load-tests/
├── phase-4-race-condition/
│   ├── app.py
│   └── README.md
├── phase-5-locks/
│   ├── app.py
│   └── README.md
├── phase-6-nginx-architecture/
│   ├── nginx.conf
│   ├── docker-compose.yml
│   └── README.md
├── phase-7-gpu-queue/
│   ├── app.py
│   ├── gpu_sim.py
│   └── README.md
└── docs/
    ├── architecture-diagrams/
    ├── performance-results/
    └── lessons-learned.md
```

## Project Goals

By completing this lab, I will:

- [ ] Experience thread explosion and context switching  
- [ ] Observe race conditions corrupt shared state  
- [ ] Fix concurrency bugs using locks and semaphores  
- [ ] Learn how async/await scales to 10k+ connections  
- [ ] Deploy a real production-style server stack  
- [ ] Simulate AI inference or GPU queueing mechanisms  
- [ ] Analyze real performance metrics  


## Load Testing & Performance Metrics

Each phase includes load tests measuring:

- [ ] Throughput (RPS)  
- [ ] Average latency  
- [ ] p95 / p99 latency  
- [ ] CPU usage  
- [ ] Memory usage  
- [ ] Number of threads  
- [ ] Event loop lag  
- [ ] Lock contention  

Results are stored in: ``` docs/performance-results/ ```

## 📬 Extensions & Future Work

You can extend this project with additional backend systems topics:

- Distributed locks  
- Redis caching  
- Kafka consumers  
- GPU batching  
- Microservices  
- Kubernetes deployment  

Just open an issue or continue the conversation.
