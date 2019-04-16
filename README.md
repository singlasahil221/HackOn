# HackOn

Hack On is a prefest hacking and penetration testing event for Elements Culmyca' 19, the annual cultural and technical fest of YMCA University of Science and Technology, Faridabad.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirments.
 ```bash
 pip install -r requirements.txt
 ```
 
## Usage

You need to set the database variable in hackon/settings.py, preferably you can use elephantsql for online datbase or you can use sqlite as default.
Then set the Google_auth key and secret in the same file.

Now, you are just three steps away from running it on localhost.

### Run Command

To detect changes in models.py file,
```bash
python manage.py makemigrations
```

To reflect changes in database,
```bash
python manage.py migrate
```

To run the server on the localhost:
```bash
python manage.py runserver
```

(OPTIONAL) To create admin user from terminal:
```bash
python manage.py createsuperuser
```
