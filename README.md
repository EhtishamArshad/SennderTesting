<h1>Studio Ghibli API</h1>

This is basically a small scale python based flask application to retrieve movies list along side the list of people
casted in the movie

Following is the guide to successfully run this project on you local machine:

<h3>Pre-requisites</h3>
As this is a Python application, python3 needs to be installed in the system.

Download and install python3 based on your operating system by following steps on:
```
https://www.python.org/downloads/
```

<h3>Package dependencies</h3>

Following packages are required to install globally on your system in order to run the application:

<h4>flask</h4>

```
pip3 install Flask
```
<h4>requests</h4>

```
pip3 install requests
```
<h4>APScheduler</h4>

```
pip3 install Flask-APScheduler
```
**Use pip instead of pip3 on windows if you have set the environment variable for python3

<h3>Run application</h3>
Run application directly from project directory with following command:

Linux/Unix
```
python3 app.py
```
Windows
```
python app.py
```

<h4>Testing</h4>

In order to run test, install the following dependency:

```
pip3 install unittest
```

Run the tests as 

```
python3 test.py
```


** If you experience any timezone errors during running application on linux based OS, configure your time zone using
following command

```
sudo dpkg-reconfigure tzdata
```


