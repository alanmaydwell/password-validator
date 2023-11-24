# Password Validate

Simple password validator created for an exercise.

`validate_password` function in `password_validate.py` takes password string as a parameter and returns  True or False depending on whether any of the following password criteria fail:
 
- Has more than 8 characters  
- Contains a capital letter  
- Contains a lowercase letter  
- Contains a number  
- Contains an underscore  

The response just confirms whether the password is valid or not but does not give the reason(s) why.

## Requirements
Password validator written using just default Python 3.11 without any optional or third-party modules. Might not work with earlier versions of Python due to way type-hinting used.

Note the unit tests and linting do require third-party modules which can be installed using the pipfile as described below.


## Unit Tests and Linting
These require pytest and flake8 which can be installed using the supplied pipfile.     
`pipenv install --dev`

After install unit tests can be run using:  
`pipenv run pytest`

Linting can be run using:  
`pipenv run python -m flake8 . -v`