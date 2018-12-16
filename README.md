# Django - ITR

introtorhythm.com, but reimagined as a Django application!

### Dependencies

Install the following using `pip install`

-   django (duh!)
-   django-storages
-   boto3
-   djangorestframework
-   Pillow (for ImageField/ FileField access in models)
-   configparser

### Local installation and usage

-   Clone this repo `$ git clone https://github.com/seanpierce/django-itr`
-   Install the dependencies that are listed above
-   From the project's root, run `$ python manage.py migrate` to generate the database
-   Start the Django development server by running `$ python manage.py runserver`
-   Create an admin user by running `$ python manage.py createsuperuser` and follow the provided instructions
-   Visit <a href="http://localhost:8000/">localhost:8000</a> in your preferred browser

### AWS storage

Admin-uploaded files are stored in an AWS S3 bucket. This functionality is possible using the **boto3** and **django-storages** python packages.
See implementation docs <a href="https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html">here</a>.

### Environment Variables

Using <a href="https://docs.python.org/3/library/configparser.html">configparser</a>, the settings.py file imports a configuration file named `settings.ini`, located in the application's sibling folder called `environments`.

ex: settings.py
```python
import configparser

CONFIG = configparser.RawConfigParser()
CONFIG.read('../environments/settings.ini')

DEBUG = bool(CONFIG.get('Environment', 'DEBUG'))
```

ex: environments/settings.ini
```python
[Test Keys]
SECRET_STRING = somestring
SECRET_ARRAY = some,example,array

[Environment]
DEBUG = True
```

### Deployments

The application will be hosted on a DigitalOcean droplet cloud server running Ubuntu (16.04.5 x64). See Ubuntu setup documentation <a href="https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-16-04">here</a>. The application is served using <a href="https://www.nginx.com/">Nginx</a> and <a href="https://gunicorn.org/">Gunicorn</a>. See webserver configuration documentation <a href="https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04">here</a>.

After deploying code, or making updates on the server, restart nginx and gunicorn by running `sudo systemctl restart nginx gunicorn`

### REST API

An integrated REST API is implemented using **djangorestframework** installed via pip. See implementation docs <a href="https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-32fcf40231e5">here</a>.

Currently exposed routes:

| Method |   Endpoint    |             Result             |
| :----: | :-----------: | :----------------------------: |
|  GET   | /api/episodes | All episode numbers and titles |
