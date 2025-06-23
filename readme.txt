Zero-Downtime Blue/Green Deployment (Docker + Nginx)

This project runs two versions of a web app (blue and green) at the same time using Docker. Nginx routes live traffic to one of them. You can update the inactive one, test it, and switch traffic to it without restarting anything. This is a local version of what you'd see in real blue/green CI/CD setups.

Tech:
- Python (Flask) for a basic API with version info
- Docker to containerize each version
- Docker Compose to manage both app versions + Nginx
- Nginx as a reverse proxy that handles switching between versions

Folder structure:
ZERODOWNTIMEWEBSITE/
├── blue/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── green/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── nginx/
│   └── default.conf
└── docker-compose.yml

How to run:
git clone <your-repo-url>
cd ZERODOWNTIMEWEBSITE
docker compose up --build -d

Access:
http://localhost          → active version via Nginx
http://localhost:8081     → blue version directly
http://localhost:8082     → green version directly
http://localhost/health   → health check via Nginx

How to switch versions:
1. Edit nginx/default.conf
   Change:
     proxy_pass http://web-blue:80;
   To:
     proxy_pass http://web-green:80;
2. Reload nginx:
   docker exec nginx-router nginx -s reload

Useful commands:
docker compose ps                      # list running containers
docker compose logs                    # logs for all containers
docker compose logs nginx              # logs for Nginx only
docker compose logs web-blue           # logs for blue
docker compose logs web-green          # logs for green
docker compose down                    # stop and remove everything
docker compose build web-blue          # rebuild blue version
docker compose build web-green         # rebuild green version
docker compose restart nginx           # restart Nginx after config change
docker exec -it nginx-router sh        # shell into Nginx container
docker exec -it web-blue sh            # shell into blue container
docker exec -it web-green sh           # shell into green container

What this project shows:
- Running multiple versions of a service
- Local blue/green deploy strategy
- Zero-downtime promotion of new code
- Reverse proxy routing with Nginx
- Container management with Docker Compose
- DevOps practice that mirrors real deployment pipelines
