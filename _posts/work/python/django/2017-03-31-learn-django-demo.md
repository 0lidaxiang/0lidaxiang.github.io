---
layout: post
title:  "Learn Django by Demo"
rootCate: "work"
categories:
- Python
tags:
- work
- Python
- Django
---

> StartTime: 2017-03-31,ModifyTime:2017-04-02

You need to have installed apache, python, pip, django, mariadb and one text editor.
<!---more--->

##Install Maridab And Django
```
pip install Django
cd Django-1.x.y
sudo python setup.py install

Output:……
Processing dependencies for Django==1.x.y
Finished processing dependencies for Django==1.x.y
```

2. test
```
django-admin.py startproject testdj
cd testdj # 切换到我们创建的项目
$ python manage.py runserver

Output:……
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Create a Database and Database User
```
dnf install python-pip python-dev mariadb-server libmariadbclient-dev
libssl-dev
sudo mysql_secure_installation
mysql -u root -p
> CREATE USER myprojectuser@localhost IDENTIFIED BY 'password';
> GRANT ALL PRIVILEGES ON myproject.* TO myprojectuser@localhost;
> FLUSH PRIVILEGES;
> exit
```

## Connect Django With Database
1.  Install the mysqlclient package that will allow us to use the database we configured:
```
pip install django mysqlclient
```
2.  Start a Django project within our myproject directory. This will create a child directory of the same name to hold the code itself, and will create a management script within the current directory. Make sure to add the dot at the end of the command
```
django-admin.py startproject <font color=#E66466>myproject</font> .

```

3.Modfify the main Django project settings file
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<font color=#E66466>myproject</font>',
        'USER': '<font color=#E66466>myprojectuser</font>',
        'PASSWORD': '<font color=#E66466>password</font>',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

## Migrate the Database and Test your Project
4.
```
cd ~/myproject
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
http://server_domain_or_IP:8000
```
5.Append /admin to the end of the URL and you should be able to access the login screen to the admin interface.

## Reference
[How To Use MySQL or MariaDB with your Django Application on Ubuntu 14.04]:https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04
