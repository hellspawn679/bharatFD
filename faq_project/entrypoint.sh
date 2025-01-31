#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable

# Create the superuser without prompting for password
python manage.py createsuperuser --noinput --username admin --email admin@example.com

# Set the password for the superuser
python manage.py shell <<EOF
from django.contrib.auth.models import User
user = User.objects.get(username='admin')
user.set_password('admin') 
user.save()
EOF

# Run the Django development server
echo "Starting the Django server..."
python manage.py runserver 0.0.0.0:8000
