# 🎓 Distributed College Management System

# Overview
The Distributed College Management System (DCMS) is a comprehensive solution designed to streamline and enhance the

management of college operations. It provides a centralized platform for administrators, faculty, and students to manage academic and administrative tasks efficiently.
# Features
- Student Information Management
- Course and Curriculum Management
- Attendance Tracking
- Grade and Exam Management
- Faculty Management
- Timetable Scheduling
- Library Management

# Environment Setup
To set up the development environment for DCMS, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/KEVIN-117/edu-distributed-manager.git
    cd edu-distributed-manager
    ```
2. Install the required dependencies:
    ```bash
   pip install -r requirements.txt
   ```
3. Configure the database settings in the `.env` file.
    ```dotenv
   # Environment variables for CMSD application
    PROJECT_NAME="edu_distributed_manager"
    PORT=8000
    # Application settings
    POSTGRES_DB=cmsd_db
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=VLSymZgffbnWWxEvJQgnXBgEPXWvJGSh
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    # REDIS
    REDIS_HOST=localhost
    REDIS_PORT=6379
    REDIS_DB=0
    REDIS_URL=redis://localhost:6379/0
    ```
4. Apply database migrations:
    ```bash
     python manege.py makemigrations
     python manage.py migrate
   ```
5. Run the development server:
    ```bash
   python run_app.py # Run celery worker and beat in background
   python manage.py runserver 
   ```

## References
- [Django Documentation](https://docs.djangoproject.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [Redis Documentation](https://redis.io/documentation)
- [Study Case](./docs/DOCS.md)