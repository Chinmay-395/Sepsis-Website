# Index

    1) What is the project about
    2)How to configure
        a)Locally
        b)On Docker
            i)Without Dockerfile
                The postgres-docker name is sep-postgres;
                The redis-docker name is sep-redis.
                (1)Initialize the postgres docker:
                    docker run --name sep-postgres -p 5432:5432 \
                     -e POSTGRES_USER=sepsis -e POSTGRES_DB=sepsis -e POSTGRES_PASSWORD=taxi -d postgres
                     1.1)Initialize the redis docker
                     docker run --name sep-redis -p 6379:6379 -d redis
                (2)start both the docker for postgres and redis
                    docker restart sep-postgres sep-redis
                (3)Configure the database variables in the command line
                    export PGDATABASE=sepsis \
                    export PGUSER=sepsis \
                    export PGPASSWORD=taxi
                (4)superuser details
                    user_type >>>>> chinmay
                    email >>>>>> chinmay@gmail.com
                    password >>>>> test@1234
            ii)With Dockerfile

# How to configure

    ## a)Locally

# What is the project about

Parameters: -
Gender, age, heart rate,O2Sat, temperature,blood pressure, respiration rate,mean arterial pressure, fraction of inspired oxygen, hospital admission time, intensive care unit length of stay

### API level working

    ###### To call the doctor
        127.0.0.1:8000/docsdoc/<doc_id>

    ###### To call the patient
        127.0.0.1:8000/patspat/<pat_id>

user = get_user_model().objects.create_user('test.user@example.com', 'test_username', 'pa$$w0rd', 'PATIENT')

sepsis_data_generating_on_loop
