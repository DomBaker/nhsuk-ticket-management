# Project for QA Summer 2022

## Application theme
This application is a ticket management system that is in the theme of NHS.UK, the app allows a standard user to register, login, create a ticket, delete a ticket and logout.
It allows an Admin user to complete the ticket, delete the ticket and view all the users of the application and all the current ticket that each user may have.

## The frontend 
The frontend is heavy based on the [NHSUK frontend](https://github.com/nhsuk/nhsuk-frontend)
Also following guidance from [NHS Digital Service Manual](https://service-manual.nhs.uk/)

## Tech stack
- [Python 3.10](https://docs.python.org/3/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Flask_login](https://flask-login.readthedocs.io/en/latest/)
- [Flask_WTF](https://flask-wtf.readthedocs.io/en/1.0.x/)
- [Flask_Testing](https://pythonhosted.org/Flask-Testing/)
- [Flask_SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/latest/)
- [Heroku](https://devcenter.heroku.com/)
- [SQLLite](https://www.sqlite.org/index.html)
- [Pipenv](https://pipenv.pypa.io/en/latest/)
- [Pytest](https://docs.pytest.org/en/7.1.x/)
- [Zap_Scan](https://www.zaproxy.org/)
- [Flake8](https://flake8.pycqa.org/en/latest/)
- [Black](https://black.readthedocs.io/en/stable/)


## Deployment
- [Docker](https://www.docker.com/)
- [Heroku deployed app](https://uni-nhsuk-ticket-system.herokuapp.com/)
- [Github_Actions](https://github.com/DomBaker/nhsuk-ticket-management/actions)

## users

### Admin user
- Email: admin@user.com
- Password: testing123
### standard user
- Email: standard@user.com
- Password: testing123

Also feel free to create your own standard user.

### Dummy users
- Generated using [Mockaroo](https://www.mockaroo.com/)
- Within the application you will find an array of dummy users these accounts can't be logged into as they're there for testing purpose only. The main reason these accounts can't be logged into is because of the pbkdf2_sha256 password verification, because the data has been imported into the database these users passwords have not been hashed, therefore are inaccessible.

## Steps to installing requirements and running the project locally
- Open terminal
- ``` git clone git@github.com:DomBaker/nhsuk-ticket-management.git ```  
- ``` cd nhs-ticket-management ``` to the directory
- ``` pip install pipenv ``` to install pipenv to be able to create a virtual env
- ``` pipenv shell ``` to activate the virtual env
- ``` pipenv install ``` to install the included pipfile.lock
- ``` python main.py ``` will run the application from the main.py this is because the website itself is a module
- ``` 127.0.0.1:5000 or localhost:5000``` use one of these urls to view the project in your browser

## DB connection 
The database is stored within the project repository, this isn't ideal for a production environment but for the purpose of the assignment is acceptable

## Testing
- Pytest 
- Run tests using ``` python -m pytest ``` in the base directory
- To run a coverage report ``` python -m pytest --cov-report term --cov=website . ``` this will output in the terminal a coverage report

## Flake8
- To run flake it ``` flake8 . ``` will run flake8 across the whole project directory

## Black
- To run Black ``` black . ``` will run Black across the whole directory. this will reformat any incorrect formatted files