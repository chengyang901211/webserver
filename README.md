# Sample web service

The web service accepts a number, n, as input and returns the first n Fibonacci numbers, starting from 0. 

## Live Demo
  http://webserver-production.us-west-2.elasticbeanstalk.com/Fibonacci/5/

## Getting Started

This is the guide to setting up your local Python development environment, checking out the GIT repositories, and running the dev server. 

### Prerequisites

* *brew*
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
Enable cache :
```
$ memcached -d
```
Now to start our Django development server!
```
python manage.py runserver
``` 
Browse http://127.0.0.1:8000/Fibonacci/5/   to see a sample result.

## Running the tests

Run unit test (Test cases detail in 'Fibonacci/test.py'):

```
./manage.py test
```

## Deployment

Additional notes about how to deploy this on a live system

I have precreated an AWS account with a staging and production server running on it. Each server has their own loadbalancer and cache for scaling and preformance improvement. (PS: All instances are on t1.micro(slow) )

Temporary AWS account(Expired on 3/17/2018):
*  Account: yangcheng901211@gmail.com
*  Password: Temp4now!


## Authors

* **Cheng Yang**
