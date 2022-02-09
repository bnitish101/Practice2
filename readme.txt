username: nio
email: nio@gmail.com
pass: nioadmin

comands to create super user

(env2) PS E:\Study\Python\Practices\Practice2\ProjectMain> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, appPrac
tice, auth, contenttypes, sessions
Running migrations:
n> python manage.py createsuperuser Username (leave blank to use 'admin'): nio
Email address: nio@gmail.com
Password:
Password (again):
Error: Your passwords didn't match.    pt     
Password:
Password (again):
Error: Your passwords didn't match.    ct     
Password:
Password (again):
Superuser created successfully.
(env2) PS E:\Study\Python\Practices\Practice2\ProjectMain>