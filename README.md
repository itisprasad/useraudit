# User Audit
This is a set of backend services consisting various endpoints to perform CRUD operations to a user table

# Setting up the app
## Pull the source code
```bash
$ git clone git@github.com:itisprasad/useraudit.git
```

## Build the app
```bash
$ docker-compose up --build
```    

In case, you run into an error while startup, do the following
```bash
$ docker-compose down
$ docker-compose up -d
$ docker-compose up --build
```    

## Test the endpoints
### Create user
```bash
$ curl -X POST http://localhost:8000/users/ \
-H "Content-Type: application/json" \
-d '{"name": "John Doe", "email": "john@example.com"}'
{"name":"John Doe","email":"john@example.com","id":1}
``` 

### List all users
```bash
$  curl -X GET http://localhost:8000/users/
[{"name":"John Doe","email":"john@example.com","id":1}]
``` 

### Update user
```bash
$ curl -X PUT http://localhost:8000/users/1 \
-H "Content-Type: application/json" \
-d '{"name": "Jane Doe", "email": "jane@example.com"}'
{"name":"Jane Doe","email":"jane@example.com","id":1}
``` 

### Delete user
```bash
$ curl -X DELETE http://localhost:8000/users/1
{"detail":"User deleted"}
``` 

### List audit logs
```bash
$ curl -X GET http://localhost:8000/audit/
[{"id":1,"action":"CREATE","details":"User created: <app.models.User object at 0x7f8de17294d0>","timestamp":"2025-01-14T03:25:32.074879"},{"id":2,"action":"UPDATE","details":"User updated: <app.models.User object at 0x7f8de13fb6d0>","timestamp":"2025-01-14T03:29:06.095250"},{"id":3,"action":"DELETE","details":"User deleted: <app.models.User object at 0x7f8de0f07450>","timestamp":"2025-01-14T03:30:05.494082"}]
``` 

## Running test case
Ensure pytest module is installed.
You may install pytest as follows

```bash
pip install pytest
``` 

```bash
$ cd app/tests
$ pytest
=================================================================== test session starts ====================================================================
platform linux -- Python 3.11.11, pytest-7.4.2, pluggy-1.5.0
rootdir: /app/app/tests
plugins: anyio-4.8.0
collected 3 items

test_main.py ...                                                                                                                                     [100%]

==================================================================== 3 passed in 0.86s =====================================================================
```
