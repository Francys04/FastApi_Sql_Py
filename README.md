
## Fast API + SQL
This project describe the main functionalities of operations with API interface and data base integration. FastAPI with SQL integration allow to build web applications that can interact with SQL databases to perform various CRUD (Create, Read, Update, Delete) operations. With this setup, I create API that handle data storage and retrieval in an efficient and organized manner.

## Start Project
### Installation packages
 - Install FastAPI ```pip install fastapi[all]``` 
 It is designed to be easy to use, efficient, and highly scalable, making it an excellent choice for developing web applications and microservices. FastAPI is built on top of standard Python type hints and leverages Python 3.7+ features, which allows for automatic data validation, serialization, and documentation generation.
 - Install SQLAlchemy ```pip install sqlalchemy```
 SQLAlchemy is an open-source Object-Relational Mapping (ORM) library for Python. It provides a set of tools and abstractions to interact with SQL databases in a more Pythonic way, allowing developers to work with databases using Python classes and objects.
 - You will find all the packages in requirements.txt and for easy start this project tou can type this command for install all dependency packages for this app: ```pip install requirements.txt```
Let's go through the key functionalities of a FastAPI application with SQL integration:

### Next step of project

1. Database Connection: First, set up a database connection using SQLAlchemy and provide the database URL. The URL can point to various SQL databases such as SQLite, PostgreSQL, MySQL, etc. In the example above, we used SQLite as an example.

2. Database Models: Next, you define database models as Python classes that inherit from `models.py` (a declarative base provided by SQLAlchemy). These models represent tables in the database and define the columns and their data types. Each model class corresponds to a table, and each instance of the class represents a row in that table.

3. CRUD Operations: You can create functions to perform CRUD operations on the database. For example:

   - Create (POST): Define an endpoint to handle HTTP POST requests and create new records in the database using data provided in the request body.

   - Read (GET): Define endpoints to handle HTTP GET requests and retrieve data from the database. You can fetch data for all records, a specific record, or based on certain filtering criteria.

   - Update (PUT/PATCH): Define endpoints to handle HTTP PUT or PATCH requests and update existing records in the database.

   - Delete (DELETE): Define endpoints to handle HTTP DELETE requests and remove records from the database.

4. Dependency Injection: I use dependency injection to manage database sessions in FastAPI. This ensures that each API request gets its own database session and commits or rolls back changes accordingly.

5. API Endpoints: Create FastAPI endpoints that handle incoming HTTP requests and call the corresponding database operations. These endpoints can perform data validation, error handling, and return responses in JSON format.

6. Run the Application: First activate the env ```env/scripts/activate``` and after change directory to `src`. To run the FastAPI application, use the `uvicorn` command.

   ```
   uvicorn main:app --reload
   ```

   Where `main` refers to the filename (`main.py`) and `app` refers to the FastAPI application instance.

By integrating FastAPI with SQL databases, I can efficiently manage data storage and retrieval for your web applications. The combination of FastAPI's performance and SQL databases' reliability makes it a powerful choice for building modern web applications with database support.
## Schemas -> Pydantic Models
- In `schemas.py`, I have defined several Pydantic models (schemas) that represent the data structure for creating and interacting with posts and users in your FastAPI application. Pydantic is a data validation and parsing library, and FastAPI uses Pydantic models extensively to handle request and response data.
- These Pydantic models define the data structure and validation rules for creating and interacting with posts and users in your FastAPI application. They help ensure that the incoming data is valid and can be easily converted to and from database models when performing database operations.
## Docker
- Docker and dockerization are concepts related to containerization in software development and deployment.
- Docker is a platform and a set of tools that enables developers to create, deploy, and run applications inside containers. A container is a lightweight and standalone executable unit that contains all the necessary dependencies, libraries, and configurations needed to run an application. Docker uses containerization technology to package applications and their dependencies into a single container image, making it easy to deploy and run applications consistently across different environments.
- In src directory run next command: ```docker compose up --build```, after install packages from requirements.txt, open docker descktop and click to the link of src container which was created by dockerfile and docker-compose.