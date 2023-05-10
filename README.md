# Py-quote API

Py-quote API is a Python Flask API which returns randomly chosen quotes and allows the user to add more quotes to the database.

# Installation

```
$ git clone https://github.com/mlodycegla/python-random-quote
$ cd python-random-quote
$ pip install -r requirements.txt
```

# Getting started

To launch the API for development:

```
$ cd flaskr
$ flask --app flaskr run --debug
```

# Methods


| URL       | Method | Data params                           | Example response                                                                                                                                          |
| ----------- | -------- | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /quote    | `GET`  |                                       | `{"quote": "When everything seems to be going against you, remember that the airplane takes off against the wind, not with it.", "author": "Henry Ford"}` |
| /addquote | `POST` | `{"quote": "text", "author": "text"}` | `200 OK`                                                                                                                                                  |

Quotes from https://gist.github.com/nasrulhazim/54b659e43b1035215cd0ba1d4577ee80
