# 📘 Database Configuration and Setup Guide

This document provides a comprehensive guide to configuring and setting up the database for your application.
Follow the steps below to ensure a smooth installation and configuration process.

---

## ⚙️ Prerequisites

Before you begin, make sure you have the following:

* A supported database server (e.g., **PostgreSQL**, **MySQL**, or **SQLite**).
* **Administrative access** to the database server.
* **Database client tools** installed on your machine (e.g., `psql`, `mysql`, DBeaver).
* **Basic knowledge of SQL** and database management.
* **Access to application configuration files.**
* **Network access** to the database server (if hosted remotely).
* **Docker** and **Docker Compose** installed and properly configured.

---

## 🧩 Step 1: Configure the `.env` File

1. Locate the `.env` file in the root directory of your application.

2. Open it in your preferred text editor.

3. Define the following environment variables for your database connection:

   ```dotenv
   POSTGRES_DB=cmsd_db
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=your_password
   POSTGRES_HOST=localhost
   POSTGRES_PORT=5432
   ```

4. Save the file.

5. Restart your application or container environment to apply the new configuration.

---

## 🐳 Step 2: Initialize the Database with Docker

1. Open a terminal or command prompt.

2. Navigate to your application’s root directory.

3. Start the database container using Docker Compose:

   ```bash
   docker-compose up -d
   ```

4. Wait for the services to start, then verify their status:

   ```bash
   docker-compose ps
   ```

5. Once the database service is running, connect using your preferred database client tool or via the command line (e.g., `psql`).

---

## 👤 Step 3: Create a Superuser Account

If your application includes a management interface (e.g., Django Admin), you can create a superuser as follows:

1. Open a terminal or command prompt.

2. Navigate to your application’s root directory.

3. Run the following command:

   ```bash
   python manage.py createsuperuser
   ```

4. Follow the prompts to set the **username**, **email**, and **password**.

5. After successful creation, use these credentials to log in to the application’s admin interface.

6. Restart your application to ensure all changes take effect.

---

## ✅ Verification

To confirm that everything is working correctly:

* Run `docker logs <db_container_name>` to check for startup errors.
* Test a database connection using your client or application.
* Access the admin interface using your superuser credentials.

---

## 📄 Notes

* Always store your `.env` file securely and **never commit it to version control**.
* For production deployments, consider using **Docker secrets** or a **vault service** to manage credentials.
* Ensure your database ports and credentials are not exposed publicly.
