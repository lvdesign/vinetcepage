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

// 
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'



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

heroku config:set SECRET_KEY='$m5**lk!_v@98no9*+25kqaj5c%t&9zppb1!yk%fo(!41!!6+l'


//db
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
adminLV
vinetcepage
vinetcepage

// check
heroku run python manage.py check --deploy

https://vinetcepage.herokuapp.com/ | https://git.heroku.com/vinetcepage.git
// Run the collectstatic command for the first time to compile all the static file directories 
// and files into one self-contained unit suitable for deployment.

python manage.py collectstatic

// identifier lien de depots
git remote -v
git remote rm heroku

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



heroku ps

heroku logs

heroku logs --tail

heroku ps:scale web=1

//heroku ps:scale worker=1

heroku run python manage.py check --deploy






at=error code=H10 desc="App crashed" method=GET path="/" host=vinetcepage.herokuapp.com request_id=0e6424ec-dd1d-4031-a13e-6ae21dbd53af fwd="82.121.172.98" dyno= connect= service= status=503 bytes= protocol=https


web: gunicorn config.wsgi --log-file -

web: gunicorn config.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate

at=error code=H10 desc="App crashed" method=GET path="/" host=vinetcepage.herokuapp.com request_id=7704a416-357b-4155-866a-c6e99fc182d5 fwd="82.121.172.98" dyno= connect= service= status=503 bytes= protocol=https



python -c 'import secrets; print(secrets.token_urlsafe())'




// comments






         {# comment #}
        
        {% if user.is_authenticated %}
        <br clear="all"/>
        <p>
        {% load crispy_forms_tags %}
        <form method="post" action="{% url 'vins:vin_comment_create' vin.id %}">
            {% csrf_token %}
            {{ comment_form|crispy }}
        <input type="submit" value="Submit">
        <input type="submit" value="All Forums" onclick="window.location.href='{% url 'vins:vin_list' %}';return false;">
        </form>
        </p>
        {% endif %}

        {% for comment in comments %}
        <p> {{ comment.text }} 
        ({{ comment.updated_at }})
        {% if user == comment.author %}
        <a href="{% url 'vins:vin_comment_delete' comment.id %}"><i class="fa fa-trash"></i></a>
        {% endif %}
        </p>
        {% endfor %}

        {# comment #}