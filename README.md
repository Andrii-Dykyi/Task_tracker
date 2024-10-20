## Task tracker sample project

### Technologies used:
- Python 3.11
- Fast API
- PostgreSQL

### Directory structure
```
└── 📁app
    └── 📁api
        └── __init__.py
        └── boards.py
        └── tickets.py
        └── users.py
    └── 📁core
        └── __init__.py
        └── config.py
        └── hash.py
        └── security.py
    └── 📁database
        └── __init__.py
        └── base.py
        └── session.py
    └── 📁models
        └── __init__.py
        └── base.py
        └── boards.py
        └── tickets.py
        └── users.py
    └── 📁schemas
        └── __init__.py
        └── boards.py
        └── tickets.py
        └── users.py
    └── 📁services
        └── __init__.py
        └── board_service.py
        └── ticket_service.py
        └── user_service.py
    └── 📁tasks
        └── __init__.py
        └── emails.py
    └── 📁tests
        └── __init__.py
└── .gitignore
└── docker-compose.yml
└── Dockerfile
└── main.py
└── README.md
└── requirements.txt
```

### Before you start, make sure the following is installed on your local machine:
 - Docker
 - Docker Compose


### Create a `.env` file in the root directory containing such env variables:
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=task_tracker
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

### Run:
```sh
$ docker-compose build
$ docker-compose up -d
```

### Access the API documentation at:
```
http://127.0.0.1:8000/docs
```

### Demonstration flow:
```
1) Creating a new user in the system
2) Creating a new board that belongs to the user
3) Creating a new ticker that belongs to the user and is linked to the board
```

### Stop:
```sh
$ docker-compose down 
```