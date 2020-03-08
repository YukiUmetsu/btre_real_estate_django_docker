# btre_real_estate_django_docker
mock real estate company website with django and docker.

This is a real estate application where realtors can list their properties and people can look at it. They can also contact realtors from the contact form.

# Technology stack
Python, Django, Postgres, Linix (alpine), Docker
(gunicorn and nginx)

# start up the server on dev
<code>docker-compose up</code>

# Check the app on the browser
access to localhost:1337

# Load initial data
<code>python manage.py loaddata btre/fixtures/initial_data.json</code>

# .env file
create a .env.dev file in btre folder according to .env.sample.

