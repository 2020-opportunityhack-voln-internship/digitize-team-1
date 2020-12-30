Check this for the source of this project: https://github.com/nicholaskajoh/React-Django

# Setup
In the same root folder where this directory is installed, create a file called 'setup.py' and copy-paste the following code into it:
```
from setuptools import setup, find_packages

setup(name='digitize_team_1', version='1.0', packages=find_packages())
```
Then, run the following commands in command prompt in the root folder:
```
npm install
pip install -r requirements.txt
pip install -e .
npm install axios
```

# To Develop React app
`npm run start` allows you to run the front-end code at http://localhost:3000/


# To Build this server
Compile React frontend code into server Django app (adds compiled code into `build/static`)
`npm run build`

Start Django server app
`python3 manage.py runserver`
