cd /Users/laurentvignaux/django_docs/venv-recettes-vinsetcepage 

$ python3 -m venv myvenv


$ source myvenv/bin/activate
cd vinetcepage

python manage.py makemigrations

python manage.py migrate


$ python manage.py runserver

//
env1/bin/python -m pip freeze > requirements.txt
env2/bin/python -m pip install -r requirements.txt

python manage.py createsuperuser

username : admin
email : admin@example.com
psw : totototo

username : admin1
email : admin@example.com
psw : titititi

// cloudinary
lvdesign
laurent.vignaux@wanadoo.fr
totoLV7894*

//

heroku login
sudo heroku login
heroku config:set DISABLE_COLLECTSTATIC=1

git push heroku

//db
heroku run python manage.py migrate
heroku run python manage.py createsuperuser


https://vinetcepage.herokuapp.com/ | https://git.heroku.com/vinetcepage.git
// Run the collectstatic command for the first time to compile all the static file directories 
// and files into one self-contained unit suitable for deployment.
python manage.py collectstatic




// doc cartes
https://fr.wikipedia.org/wiki/Viticulture_en_France


//
https://res.cloudinary.com/lvcloud/image/upload/v1624885333/vinslv/Capture_decran_2021-06-28_a_15.01.46_daj09h.png



Here is a recap of what we’ve done so far:
• add environment variables via environs[django]
Chapter 16: Deployment 264
• set DEBUG to False
• set ALLOWED_HOSTS
• use environment variable for SECRET_KEY
• update DATABASES to use SQLite locally and PostgreSQL in production
• configure static files
• install whitenoise for static file hosting
• install gunicorn for production web server
These steps apply to Django deployments on any server or platform; they are not Herokuspecific.