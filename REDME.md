git clone the project.
virtualenv env --no-site-packages
source env/bin/activate
pip3 install -r requirements.txt
run python3 manage.py runserver
cd into the project directory where there is manage.py on your terminal
To upload the json file to rest api run:
	Content-POST -H "Content-Type: application/json" http://127.0.0.1:8000/userlist/ -d  @usertest.json
to retrieve a specific user from the Json file using the rest api run/:
	curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8000/userlist/?name=Kui%20Muthoni -d  @usertest.json
