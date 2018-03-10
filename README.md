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

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
