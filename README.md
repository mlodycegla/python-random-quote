# Py-quote API

Py-quote API is a Python Flask API which returns randomly chosen quotes and allows the user to add more quotes to the database.

# Installation

```
$ git clone https://github.com/mlodycegla/python-random-quote
$ cd python-random-quote
$ pip install -r requirements.txt
```

# Methods

- **URL:** /quote
- **Method:** `GET`

  | URL | Method | Data Params |
  | --- | --- | --- |
  | /quote | `GET` | ----------------------------------------------- |
  | /addquote | `POST` | `{ 'author': 'the author of the quote', 'quote': 'the quote' }` |

- **URL:** /addquote
- **Method:** `POST`
- **Data Params:** `{ 'author': 'the author of the quote', 'quote': 'the quote' }`

Quotes from https://gist.github.com/nasrulhazim/54b659e43b1035215cd0ba1d4577ee80
