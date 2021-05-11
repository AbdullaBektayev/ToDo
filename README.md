# ToDo

This Django application is a simple app for to-do notes. You can write, change, delete your todos. And you can do all login stuff like login, logout, reset the password, change password or email, and so on (for that I use django-rest-authemail).
If a task is done the app will send notifications to the email of user. For that you need to configure main mail, I leave the instructions below.

In this project I use Docker for building the project, Postgres as Database, Redis as a message broker, and Celery as a task queue.

And added Swagger but now Swagger not so informative because I don't configure views for this

# Prepare email (in this case gmail)

give to accaount permition to Unsafe apps
    
    https://myaccount.google.com/u/3/lesssecureapps?pli=1&rapt=AEjHL4NIg6dPANYQHLwRJqHEPkuVHB9OPXWLuCOd4JDMUo1yqzsl2gMs1UMCuZKNslZlDr49pxhsc6l3t6pOOxk5w_Th6Mu7Fg
    
Turned on a IMAP
    
    On your computer, open Gmail.
    In the top right, click Settings and then See all  settings.
    Click the Forwarding and POP/IMAP tab.
    In the "IMAP access" section, select Enable IMAP.
    Click Save Changes.


# Prepare env file

you need to create and write your own credentials to the ToDo/.env file in the project. In here EMAIL_HOST, EMAIL_PORT, EMAIL_USE_TLS and EMAIL_USE_SSL 
for Gmail users, if you use another mailbox you need to change those too.


    SECRET_KEY= <your secret key>
    DEBUG=on

    EMAIL_FROM=<your email>
    EMAIL_BCC=<your email>

    EMAIL_HOST=smtp.gmail.com 
    EMAIL_PORT=587
    EMAIL_HOST_USER=<your email>
    EMAIL_HOST_PASSWORD=<your password for email>
    EMAIL_USE_TLS=on
    EMAIL_USE_SSL=off

# Start the Project

    docker-compose build
    docker-compose up
    
