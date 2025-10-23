# 🎓 Caso de Estudio: College Management System Distribuido

## 1. 🧭 Introducción

En las instituciones universitarias, los procesos administrativos y académicos suelen implicar grandes volúmenes de información, tareas repetitivas y operaciones que demandan eficiencia, escalabilidad y disponibilidad constante.

El **College Management System Distribuido (CMSD)** surge como una solución moderna para automatizar y optimizar la gestión integral de una universidad, permitiendo manejar desde la matrícula hasta la generación de reportes, con una arquitectura distribuida y tolerante a fallos.

El sistema adopta una **arquitectura modular y orientada a servicios**, donde cada componente (autenticación, gestión académica, notificaciones, reportes) puede escalar de manera independiente. Gracias al uso de **Django**, **Celery** y **Redis**, el CMSD logra ejecutar tareas críticas en paralelo, mejorar el rendimiento y mantener una experiencia fluida para los usuarios finales.

---

## 2. 🎯 Objetivo General

Diseñar e implementar un **sistema distribuido de gestión universitaria** que automatice los procesos académicos y administrativos de una institución, empleando una arquitectura basada en **Django, Celery y Redis** para garantizar escalabilidad, eficiencia y resiliencia.

---

## 3. 🎯 Objetivos Específicos

1. Implementar un backend modular en **Django**, dividido en microservicios orientados a funciones específicas.
2. Configurar **Celery** para el manejo de tareas asíncronas y distribuidas (envío de correos, generación de reportes, procesamiento de datos).
3. Integrar **Redis** como sistema de mensajería y caché para mejorar el rendimiento del sistema.
4. Diseñar una **API RESTful** que permita la interoperabilidad con aplicaciones móviles o sistemas externos.
5. Desarrollar un **panel administrativo** para visualizar métricas, estadísticas y reportes.
6. Asegurar la **tolerancia a fallos y escalabilidad** mediante la distribución de cargas de trabajo entre múltiples workers.

---

## 4. 📍 Alcance

El proyecto abarcará el desarrollo de los principales módulos funcionales del sistema universitario:

- Registro y autenticación de usuarios con distintos roles.
- Gestión de cursos, matrículas, asistencia y calificaciones.
- Emisión de notificaciones automáticas a estudiantes y docentes.
- Generación de reportes en segundo plano (PDF o Excel).
- Monitoreo en tiempo real de tareas distribuidas y métricas del sistema.

**Fuera del alcance inicial:**

- Desarrollo de aplicación móvil nativa.
- Integración con sistemas financieros o externos.
- Implementación de inteligencia artificial o analítica avanzada (fase futura).

## 5. 👥 Actores Principales

| Actor                        | Rol                                | Funcionalidades                                                                  |
|------------------------------|------------------------------------|----------------------------------------------------------------------------------|
| **Estudiante**               | Usuario final del sistema.         | Registro, matrícula, consulta de notas, asistencia y notificaciones.             |
| **Docente**                  | Encargado de cursos y evaluación.  | Registro de calificaciones, asistencia, avisos a estudiantes.                    |
| **Administrador / HOD**      | Personal académico-administrativo. | Creación de cursos, asignación de docentes, aprobación de matrículas.            |
| **Sistema (Celery Workers)** | Procesos automáticos.              | Envío de correos, generación de reportes, limpieza de caché, tareas programadas. |

## 6. 🧱 Módulos del Sistema (Microservicios)

| Módulo                   | Descripción                                                              | Tecnologías                                |
|--------------------------|--------------------------------------------------------------------------|--------------------------------------------|
| **Auth Service**         | Gestión de usuarios, roles y autenticación mediante JWT.                 | Django, DRF, djangorestframework-simplejwt |
| **Academic Service**     | Administración de cursos, matrículas, calificaciones y asistencia.       | Django ORM, PostgreSQL                     |
| **Notification Service** | Envío de notificaciones por correo o SMS y gestión de colas de mensajes. | Celery, Redis                              |
| **Report Service**       | Generación de reportes en segundo plano y exportación a PDF o Excel.     | Celery, Pandas, xhtml2pdf                  |
| **Monitoring Service**   | Seguimiento de tareas, logs y rendimiento.                               | Flower, Prometheus, Grafana                |
| **Gateway / API Layer**  | Capa de acceso centralizada para comunicación entre módulos y frontend.  | Django REST Framework                      |

## 7. ⚙️ Requerimientos Funcionales

1. Registro y autenticación de usuarios (estudiantes, docentes, administradores).
2. Creación, edición y eliminación de cursos.
3. Asignación de docentes a cursos.
4. Matrícula de estudiantes.
5. Registro de calificaciones y asistencia.
6. Generación automática de reportes de notas y asistencia.
7. Envío automático de notificaciones (vía correo o SMS).
8. Panel de control para administradores con estadísticas del sistema.
9. Exposición de una API REST para integración con clientes externos.

## 8. 🧩 Requerimientos No Funcionales

| Categoría          | Descripción                                                                          |
|--------------------|--------------------------------------------------------------------------------------|
| **Escalabilidad**  | El sistema debe soportar el aumento de usuarios agregando más workers o nodos Redis. |
| **Disponibilidad** | Redis y Celery deben estar configurados para tolerancia a fallos.                    |
| **Seguridad**      | Cifrado de contraseñas, tokens JWT, sanitización de entradas y uso de HTTPS.         |
| **Rendimiento**    | Cacheo de consultas frecuentes y uso eficiente de workers.                           |
| **Mantenibilidad** | Código modular y desacoplado basado en apps Django.                                  |
| **Portabilidad**   | Despliegue mediante contenedores Docker.                                             |
| **Observabilidad** | Métricas expuestas para Prometheus y dashboard con Grafana.                          |

## 9. 🧰 Tecnologías a Utilizar

| Categoría                          | Tecnologías                               |
|------------------------------------|-------------------------------------------|
| **Backend principal**              | Django, Django REST Framework             |
| **Mensajería / Tareas asíncronas** | Celery                                    |
| **Broker / Cache**                 | Redis                                     |
| **Base de datos**                  | PostgreSQL                                |
| **Contenedores**                   | Docker, Docker Compose                    |
| **Monitoreo y métricas**           | Flower, Prometheus, Grafana               |
| **Autenticación**                  | JWT (djangorestframework-simplejwt)       |
| **Reportes**                       | Pandas, xhtml2pdf, openpyxl               |
| **Infraestructura (opcional)**     | Kubernetes o Docker Swarm (fase avanzada) |

## 10. 🗓️ Cronograma Tentativo (por Fases)

| Fase                                          | Descripción                                                                 | Duración estimada |
|-----------------------------------------------|-----------------------------------------------------------------------------|-------------------|
| **Fase 1: Análisis y diseño**                 | Identificación de requerimientos, actores, módulos y arquitectura general.  | 1 semana          |
| **Fase 2: Configuración base del entorno**    | Instalación de Django, Redis, Celery, PostgreSQL y estructura del proyecto. | 1 semana          |
| **Fase 3: Desarrollo de módulos principales** | Implementación de Auth, Academic y Notification Service.                    | 3 semanas         |
| **Fase 4: Integración de Celery y Redis**     | Configuración de tareas distribuidas y workers.                             | 2 semanas         |
| **Fase 5: Reportes y monitoreo**              | Implementación de generación de reportes y monitoreo con Flower/Grafana.    | 2 semanas         |
| **Fase 6: Pruebas y despliegue**              | Pruebas funcionales, contenedorización y despliegue.                        | 1 semana          |
| **Duración total estimada:**                  | —                                                                           | **10 semanas**    |

## 11. 🧾 Resultados Esperados

- Un sistema distribuido funcional, escalable y modular basado en Django + Celery + Redis.
- Reducción del tiempo de respuesta en operaciones intensivas gracias al procesamiento en paralelo.
- Administración académica centralizada, segura y accesible desde una API REST.
- Panel de control con métricas y tareas en ejecución en tiempo real.
- Código mantenible y fácilmente extensible para futuras versiones o integración con apps móviles.

## 12. Diseño lógico base de datos (orientado al sistema distribuido)

## 13. 🧱 Arquitectura lógica *College Management System Distribuido*

![Logical architecture](./assets/LogicalArchitecture.png)

![img.png](./assets/LogicalArchitecture2.png)

### 🧩 **1. Nivel de Presentación (Frontend / API Gateway)**

- **Next.js (React + Tailwind + MUI)**: Interfaz para estudiantes, docentes y administradores.
- Se comunica con la API Django mediante peticiones **REST** o **GraphQL**.
- Implementa autenticación basada en **JWT**.
- Renderizado híbrido (SSR/CSR) para rendimiento y SEO.

---

### ⚙️ **2. Nivel de Aplicación (Backend Principal – Django)**

- **Django REST Framework** actúa como la **capa de orquestación**.
- Gestiona la lógica de negocio, validaciones y operaciones CRUD.
- Expone endpoints para los módulos:
    - **Auth Service** → Usuarios, roles, permisos.
    - **Academic Service** → Cursos, matrículas, calificaciones, asistencia.
    - **Notification Service (API endpoint)** → Encola notificaciones (correos, SMS).
    - **Report Service (API endpoint)** → Solicita generación de reportes asíncronos.

---

### 🧵 **3. Nivel de Procesamiento Distribuido (Celery Workers)**

- **Celery** ejecuta tareas asíncronas distribuidas:
    - Envío de correos automáticos.
    - Generación de reportes PDF/Excel.
    - Procesamiento de datos masivos (ej. importación de matrículas).
- **Workers** desplegados en contenedores o nodos independientes.
- Cada worker se conecta a **Redis (broker)** para recibir tareas.
- Los resultados pueden almacenarse en **Redis** o en la base de datos PostgreSQL.

---

### 💾 **4. Nivel de Datos y Persistencia**

- **PostgreSQL**: Base de datos principal (usuarios, cursos, calificaciones, matrículas, logs).
- **Redis**:
    - Actúa como **message broker** para Celery.
    - También se usa como **cache layer** para acelerar consultas y sesiones.
- Se pueden implementar índices y vistas materializadas para mejorar rendimiento en reportes.

---

### 🧠 **5. Nivel de Monitoreo y Observabilidad**

- **Flower**: Monitorea el estado de las tareas Celery (pendientes, completadas, fallidas).
- **Prometheus + Grafana**: Recolectan métricas de rendimiento y disponibilidad.
- **Logs estructurados** con `logging` de Django y envío opcional a Elastic Stack.

---

### 🧰 **6. Integración y Orquestación**

- **Docker Compose**: Despliegue local o inicial, definiendo servicios (web, db, redis, worker, flower).
- **Kubernetes (fase avanzada)**: Orquestación, autoescalado y tolerancia a fallos.

---

### 🔗 **Resumen de la Interacción entre Componentes**

1. El **usuario** (desde el frontend) envía una solicitud a través de la API Django.
2. Django **procesa la lógica** y, si la operación es intensiva, envía una **tarea a Redis**.
3. **Celery Worker** toma la tarea desde Redis y la ejecuta.
4. Los resultados se almacenan en PostgreSQL o Redis.
5. **Flower** y **Prometheus** permiten monitorear las tareas y el rendimiento en tiempo real.
6. El usuario recibe retroalimentación inmediata (estado, progreso o resultado).

---

## 14. Arquitectura de despliegue

![Deployment architecture](./assets/DeploymentArchitecture.png)

## 1. Descripción general

El sistema **CMSD** se despliega en una infraestructura distribuida basada en contenedores, donde cada componente del ecosistema (API, workers, base de datos, broker, monitoreo) se ejecuta como un servicio independiente dentro de un **cluster orquestado** (Docker Swarm o Kubernetes).

El objetivo principal de esta arquitectura es garantizar **escalabilidad horizontal**, **resiliencia** ante fallos y **mantenibilidad modular**.

---

## 2. Capas de la arquitectura

### 🧱 2.1. Capa de Infraestructura

Esta capa representa el entorno físico o virtual donde el sistema opera.

**Componentes principales:**

- **Cluster en la Nube:** entorno orquestado con *Docker Swarm* o *Kubernetes*, encargado de distribuir los contenedores y mantener alta disponibilidad.
- **Balanceador de Carga (Nginx / Traefik):** recibe el tráfico entrante HTTPS y distribuye las solicitudes entre las instancias del backend Django.
- **Red Privada (VPC / Overlay Network):** proporciona aislamiento de red entre los microservicios internos, garantizando seguridad y rendimiento.

**Rol conceptual:**

Esta capa abstrae la infraestructura y permite escalar dinámicamente los servicios según la demanda, además de proteger las comunicaciones internas del sistema.

---

### ⚙️ 2.2. Capa de Servicios Principales

En esta capa se despliegan los contenedores que conforman la **lógica central del sistema**.

**Componentes principales:**

- **Django API / Web Server:** núcleo del sistema, encargado de manejar peticiones HTTP/REST, lógica de negocio, y comunicación con la base de datos.
- **Celery Workers (1 y 2):** procesos dedicados a ejecutar tareas asíncronas como envío de notificaciones, generación de reportes o validación de matrículas.
- **Celery Beat:** planificador de tareas periódicas, responsable de ejecutar rutinas automáticas (por ejemplo, limpieza de registros antiguos o envío diario de correos).
- **Redis (Broker y Caché):** actúa como sistema de mensajería entre Django y los workers Celery, además de almacenar datos temporales para acelerar consultas.
- **PostgreSQL:** base de datos relacional principal donde se almacenan usuarios, cursos, matrículas, calificaciones y registros administrativos.

**Rol conceptual:**

Permite desacoplar el procesamiento síncrono del asíncrono, aumentando la capacidad de respuesta y evitando bloqueos durante operaciones intensivas.

---

### 📊 2.3. Capa de Monitoreo y Gestión

Proporciona visibilidad sobre el estado, rendimiento y salud del sistema.

**Componentes principales:**

- **Flower:** interfaz web para monitorear las tareas y el estado de los workers de Celery.
- **Prometheus:** recopila métricas del sistema (uso de CPU, RAM, tiempos de respuesta, tareas ejecutadas, etc.).
- **Grafana:** visualiza dashboards con métricas y alertas generadas por Prometheus.
- **ELK Stack (Elasticsearch, Logstash, Kibana):** registra logs de auditoría y permite análisis en tiempo real de errores o accesos.

**Rol conceptual:**

Garantiza la observabilidad del sistema, facilitando la detección temprana de fallos, el análisis de desempeño y la trazabilidad operativa.

---

### 👥 2.4. Capa de Acceso de Usuarios

Es la interfaz entre los usuarios finales y los servicios internos del CMSD.

**Componentes principales:**

- **Navegador Web / Cliente:** interfaz usada por estudiantes y docentes para acceder al portal principal.
- **Panel Administrador:** interfaz dedicada para personal administrativo (gestión de cursos, matrículas, usuarios, etc.).
- **Aplicación Móvil:** canal externo que consume los endpoints REST del backend Django.

**Rol conceptual:**

Facilita la interacción de distintos perfiles de usuario con el sistema, asegurando accesibilidad desde múltiples dispositivos.

---

## 3. Flujo de despliegue y comunicación

1. **El tráfico HTTPS** llega al *Load Balancer*, que redirige las solicitudes hacia las instancias de Django disponibles.
2. Django procesa la solicitud y, si requiere tareas de fondo, **envía mensajes a Redis**, que los distribuye entre los *Celery Workers*.
3. Los *Workers* ejecutan las tareas y **almacenan resultados en PostgreSQL**.
4. Los componentes de monitoreo recolectan y visualizan métricas en tiempo real (Prometheus + Grafana + ELK).
5. Los usuarios acceden al sistema a través de un navegador o aplicación móvil, con autenticación segura mediante HTTPS y tokens JWT.

---

## 4. Beneficios del diseño

- 🔁 **Escalabilidad horizontal:** cada componente puede replicarse independientemente.
- 🧩 **Modularidad:** los servicios son autónomos y fácilmente actualizables.
- 🔒 **Seguridad:** el tráfico se canaliza por redes privadas y balanceadores configurados.
- 📈 **Observabilidad:** métricas y logs en tiempo real facilitan la gestión operativa.
- ⚡ **Alto rendimiento:** Redis y Celery permiten procesamiento distribuido sin bloquear el flujo principal de usuarios.