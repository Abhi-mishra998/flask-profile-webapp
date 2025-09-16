Flask Profile WebApp

A **single-container Flask web application** displaying my basic personal details.  
This project demonstrates **Docker usage** and **containerized deployment on AWS EC2**.

---

## 🚀 How to Run

1. **Clone the repository:**
```bash
git clone https://github.com/<your-username>/flask-profile-webapp.git
cd flask-profile-webapp
Build and run using Docker Compose:

bash
Copy code
docker compose up --build -d
Access the web app:

cpp
Copy code
http://<EC2-public-IP>/
✅ Useful Docker Commands
Command	Description
docker ps	List running containers
docker ps -a	List all containers (running + stopped)
docker stop <container_name>	Stop a container
docker rm <container_name>	Remove a container
docker logs <container_name>	View logs of a container
docker network ls	List Docker networks
docker volume ls	List Docker volumes
docker system prune -f	Remove unused Docker resources
