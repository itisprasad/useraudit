# User Audit
This is a set of backend services consisting various endpoints to perform CRUD operations to a user table

# Pre-requisites
```
docker installed and Running
docker-compose toool installed
```


# Setting up the app
## Pull the source code
```bash
$ git clone git@github.com:itisprasad/useraudit.git
```

## Build the app
```bash
$ cd useraudit
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
``` 

Output
```bash
{"name":"John Doe","email":"john@example.com","is_deleted":false,"id":1}i
``` 

### Query a specific user
```bash
$  curl -X GET http://localhost:8000/users/1
```

Output
```bash
[{"name":"John Doe","email":"john@example.com","id":1}]
```


### List all users
```bash
$  curl -X GET http://localhost:8000/users/
``` 

Output
```bash
[{"name":"John Doe","email":"john@example.com","is_deleted":false,"id":1},{"name":"Jane Doe","email":"jane@example.com","is_deleted":false,"id":2}]i
``` 

### Update user
```bash
$ curl -X PUT http://localhost:8000/users/2 -H "Content-Type: application/json" -d '{"name": "Jane Doe", "email": "jane1@example.com"}'
``` 

Output
```bash
{"name":"Jane Doe","email":"jane1@example.com","is_deleted":false,"id":2}
``` 

### Delete user
This is a soft delete operation where in the user will be marked as deleted by updating is_deleted attribute to True.  This way, the user data is persisted.
```bash
$ curl -X DELETE http://localhost:8000/users/1
``` 

Output
```bash
{"detail":"User deleted"}
``` 

### List audit logs
```bash
$ curl -X GET http://localhost:8000/audit/
``` 

Output
```bash
[{"id":1,"action":"CREATE","details":"User created: <app.models.User object at 0x7f9fbb1346d0>","timestamp":"2025-01-15T01:46:35.817502"},{"id":2,"action":"CREATE","details":"User created: <app.models.User object at 0x7f9fbb174b50>","timestamp":"2025-01-15T01:52:13.623000"},{"id":3,"action":"UPDATE","details":"User updated: <app.models.User object at 0x7f9fba905050>","timestamp":"2025-01-15T01:54:16.762529"},{"id":4,"action":"UPDATE","details":"User updated: <app.models.User object at 0x7f9fba906d10>","timestamp":"2025-01-15T01:54:51.029560"},{"id":5,"action":"DELETE","details":"User deleted: <app.models.User object at 0x7f9fba9068d0>","timestamp":"2025-01-15T01:56:21.506760"}]
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
