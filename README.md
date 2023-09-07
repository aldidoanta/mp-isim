# mp-isim

The Master Project of Aldi Doanta Kurnia - Master Computer Science student at the University of Twente.

## Installation
### Requirements/Preparations
1. Python 3
2. Java 17
3. Docker Engine
4. Make sure the current directory is at project root (`mp-isim`).
5. Create environment variable files using the following steps:  
  a. Create `.env` in `/vocabulary_hub` directory using [`/vocabulary_hub/.env.template`](vocabulary_hub/.env.template).   
  b. Create `.env` in `/matchers/coma` directory using [`/matchers/coma/.env.template`](matchers/coma/.env.template).   
  c. Create `.env` in `/matchers/cupid` directory using [`/matchers/cupid/.env.template`](matchers/cupid/.env.template).   
  d. Create `.env` in `/matchers/similarity_flooding` directory using [`/matchers/similarity_flooding/.env.template`](matchers/similarity_flooding/.env.template).   

### Installation using Docker
1. Download all the latest images from Docker Hub.
```bash
docker compose pull
```
2. Run all the containers.
```bash
docker compose up -d
```
3. To stop and remove all the containers:
```bash
docker compose down
```
