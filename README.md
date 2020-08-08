# README

This README would normally documents whatever steps necessary to get your application up and running.

## How do I set up?

* ### Dependencies:

	#### Django:
    		-> sudo yum install python3-pip python3-dev
    		-> sudo yum install language-pack-en libmysqlclient-dev
    		-> pip3 install virtualenv
    		-> pip3 install --upgrade pip

	#### Mysql:
    		-> (install mysql version 8)

* ### Project checkout:
            -> git clone https://github.com/vallikannu96/Activity.git

* ### Project setup:

	#### Django:
            -> go into root django directory
            -> virtualenv -p python3 avtivity_env
            -> source avtivity_env/bin/activate
            -> pip install -r requirements.txt
	        -> create a new database as "activity_db" in mysql
            -> configure database user, password in phoenix/settings.py
                DATABASES = {
                    'default': {
                        'NAME': 'avtivity_db',
                        'USER': 'your database username',
                        'PASSWORD': 'your database password',
                    }
                }
            -> python manage.py makemigrations
            -> python manage.py migrate
            -> python manage.py createsuperuser

* ### Run server:

	#### Django:
			-> go into root django directory
			-> python manage.py runserver