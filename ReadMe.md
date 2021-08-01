# Clinical Decision Support System
11 million people die each year because of sepsis. 80% of deaths can be prevented by early prediction of sepsis. "Sepsis" is the body trying to fight infection, that infection has got out of control, and the patient is in a state of attrition warfare.

## About
Since, early prediction of sepsis is a classic problem and many different iterations of ML scripts have tested with vivid algorithms which were made to compete with each other to figure out which could predict more accurately; their have been several studies and literature paper on the same, therefore we took a different outlook on the subject by creating an AI to not only manage but to make decision using Expert-System

### Scope and Feature

##### ***Scope:-*** 
Building an interface called a “sepsis-diagnostic system” for doctors and patients and AI based decision-making process. 
##### ***Feature***
* Early prediction of sepsis using ML
* Event Driven System based on an *"Expert System"* and making a decision
* Data analytics and visualization web-app of patient data in real-time


### Target Market

* Hospitals which have the facility to conduct tests on patients but lack the doctoral-decision
* A notification alert system for doctors and medical staff alike.
* Creating a real-time data visualization dashboard app for data analytics and tracking patient's detoriating health.

### Societal Impact
* Sepsis claims nearly 3 million lives yearly throughout the World. Early detection and antibiotic treatment of sepsis are critical for improving sepsis outcomes, where each hour of delayed treatment has been associated with roughly an 4-8% increase in mortality rate.
* Early prediction of Sepsis can save upto 60 percent of the total lives which are lost yearly.
* Our project aims to predict sepsis at least 6 hours prior to Clinical Prediction.

*The tracking of Sepsis of a patient in today's environment is pedantic and finicky and no system is capable of achieving a human level intelligence and intuition. But through domain experts  knowledge and our product we would be able to generalize it for other diseases. Thus, learning the optimal partnership is among the patient, family, caregiver and computer.*


## Links

[Github Link](https://github.com/Chinmay-395/Sepsis-Website/)
[Wiki page](https://github.com/Chinmay-395/Sepsis-Website/wiki)

# Index

1. [Project Architecture](https://github.com/Chinmay-395/Sepsis-Website/wiki)
2. How to configure
   1. Locally
   2. On Docker
      1. Without Dockerfile
      2. With Dockerfile

# How to configure

   1. ### Locally
      ```
      installation
      pip install -r requirements.txt
      ```

   2. ### On Docker
      1) without dockerfile
         The postgres-docker name is sep-postgres;
         The redis-docker name is sep-redis.
         1. Initialize the postgres docker:
            ```
            docker run --name sep-postgres -p 5432:5432 \
            -e POSTGRES_USER=sepsis -e POSTGRES_DB=sepsis -e POSTGRES_PASSWORD=sepsis -d postgres
            ```
         2. Initialize the redis docker
            ```
            docker run --name sep-redis -p 6379:6379 -d redis
            ```
         3. start both the docker for postgres and redis
            ```
            docker restart sep-postgres sep-redis
            ```
         4. Configure the database variables in the command line(bash)
            ```
            export PGDATABASE=sepsis \
            export PGUSER=sepsis \
            export PGPASSWORD=sepsis
            ```
         5. Create a superuser details
            ```
            python manage.py createsuperuser

            # superuser email: test@gmail.com
            # superuser password: test
            ```
      

      2) with dockerfile
         ``` ```
