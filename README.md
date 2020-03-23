**Starting**


*  **First step:**

*  `git clone git@github.com:kaday506s/TestPlaneks.git` - SSH
*  `git clone https://github.com/kaday506s/TestPlaneks.git` - HTTP

* Command to create tables:
  * `python manage.py makemigrations`
  * `python manage.py migrate`

* Command to start redis server:
  * `redis-server`

* Command to start celery:
  * `celery -A config worker -l info -B`


**Enviroment configuration**

  * `DEBUG=`
  * `SECRET_KEY=`
  
  * `DB_NAME=`
  * `DB_USER=`
  * `DB_PASSWORD=`
  * `DB_HOST=`
  * `DB_PORT=`
  
  * `DJANGO_SETTINGS_MODULE=`
  * `DJANGO_CONFIGURATION=`

  * `EMAIL_USER=` 
  * `EMAIL_PASSWORD=` 
  * `EMAIL_HOST=` 
  * `EMAIL_PORT=`
  
  
**Creating Template Instructions**
    
   * `python manage.py createtest.py `
 