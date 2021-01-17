# Index

1. What is the project about
2. [How to configure](https://github.com/Chinmay-395/Sepsis-Website/wiki)
    1. Locally
    2. On Docker
        1. Without Dockerfile
        2. With Dockerfile

# How to configure

1) ### without dockerfile
    The postgres-docker name is sep-postgres;
    The redis-docker name is sep-redis.
    1) Initialize the postgres docker:
        ```
        docker run --name sep-postgres -p 5432:5432 \
        -e POSTGRES_USER=sepsis -e POSTGRES_DB=sepsis -e POSTGRES_PASSWORD=taxi -d postgres
        ``` 
    2) Initialize the redis docker
        ```
        docker run --name sep-redis -p 6379:6379 -d redis
        ```
    3) start both the docker for postgres and redis
        ```
        docker restart sep-postgres sep-redis
        ```
    4) Configure the database variables in the command line
        ```
        export PGDATABASE=sepsis \
        export PGUSER=sepsis \
        export PGPASSWORD=taxi
        ```
    5) superuser details
        ```
        user_type >>>>> chinmay
        email >>>>>> chinmay@gmail.com
        password >>>>> test@1234
        ```
    
~~2) ### with dockerfile

