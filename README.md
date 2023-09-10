# To active the venv run
$ source env/bin/activate

# To run the management commands cd into the project directory 
$ cd backstage_test/

# To migrate the database changes run
$ ./manage.py migrate

# To run the service 
$ ./manage.py runserver 0.0.0.0:8231

# To access the difference endpoint run the following in your browser (n is 10 in this example)
http://localhost:8231/math-ops/difference/?number=10

# To run unit tests run
$ ./manage.py test
