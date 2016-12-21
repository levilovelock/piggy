# piggy - A simple PigLatin translator webservice


### How it Works

This simple server listens on port 80 (8080 for tests) and has a single endpoint `/translate`. The endpoint expects a `POST` request with one piec of form data labelled *message*. This webservice will take any string in that message parameter and translate it to PigLatin.

  Example

  ``` bash
  ~$ curl -XPOST -d "message=hi mang" localhost:80/translate
  ihay angmay
  ```

### How To Run

###### Requirements
 - Python 2.7
 - virtualenv
 - privileges to listen on port 80

###### Setting up Virtual Environment + Dependencies
1. Clone this repository to your own machine
2. Create a virtualenv within the repo directory like:
  ```
  virtualenv venv
  ```
3. Activate virtualenv
  ```
  source venv/bin/activate
  ```
4. Install dependencies
  - Production mode
  ```
  pip install -r requirements.txt
  ```
  - Development mode
  ```
  pip install -r dev-requirements.txt
  ```

##### Running the server

After setting up and activating the virtualenv, run the following command with escalated priveleges
```
python pigserver/pigserver.py
```

###### Running tests

The tests can be found within the `tests` directory. Activate the virtualenv and run the following command (remember you need to install dev-requirements.txt rather than the regular requirements.txt)
```
python tests/pigserver_tests.py
```
