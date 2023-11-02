# Interoperability Simulator for Data Spaces

The Master Project of Aldi Doanta Kurnia - Master Computer Science student at the University of Twente.

The thesis is available on the [UT's Theses repository](https://essay.utwente.nl/97460/) and [ResearchGate](https://doi.org/10.13140/RG.2.2.27278.95042).

## Demo
<figure class="video_container">
  <video controls="true" allowfullscreen="true">
    <source src="artifacts/2023-09-04-isim-demo.mp4" type="video/mp4">
  </video>
</figure>

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

## Thesis Artifacts
The `artifacts/` directory contains the Master Project artifacts besides the source code, such as:
1. Archimate architecture diagrams
2. BPMN diagrams
3. CSV files that represent the interoperability scenarios
4. PowerPoint presentation files
