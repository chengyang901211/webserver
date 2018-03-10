# Sample web service

The web service accepts a number, n, as input and returns the first n Fibonacci numbers, starting from 0. 

## Getting Started

This is the guide to setting up your local Python development environment, checking out the GIT repositories, and running the dev server. 

### Prerequisites

* [brew](https://brew.sh/)d
* *Python 2.7.10*
* [virtualenv virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
* *git*

### Installing

A step by step series of examples that tell you have to get a development env running

Create a virtualenv
```
$ mkproject webserver
```
Create a git repository: 
```
$ git init
```
Add the remote repository:
```
$ git remote add origin https://github.com/chengyang901211/webserver.git
```
Pull down the repository:
```
$ git pull origin master
```
Create a production branch: 
```
$ git branch production
```
Switch to the production branch: 
```
$ git checkout production
```
Pull down the production branch of the repository: 
```
$ git pull origin production
```
Create a staging branch: 
```
$ git branch staging
```
Switch to the staging branch: 
```
$ git checkout staging
```
Pull down the staging branch of the repository: 
```
$ git pull origin staging
```
Now let's install required library with: 
```
$ pip install -r requirements.txt
```
Now to start our Django development server!
```
python manage.py runserver
``` 
Browse http://127.0.0.1:8000/Fibonacci/5/   to see a sample result.

## Running the tests

Run unit test from (Test cases detail in 'Fibonacci/test.py'):

```
./manage.py test
```

## Deployment

Add additional notes about how to deploy this on a live system


## Authors

* **Cheng Yang**
