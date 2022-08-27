# Countries web scraper
Know your city: SDI's Community Driven Data on Slums \
Scrapping data from [sdinet.org](https://sdinet.org/) and exporting It to csv and shp files

## Table of Content
- [Countries web scraper](#Countries-web-scraper)
  * [Tools](#tools)
  * [How to run]
  * [Author](#author)

## Tools
1. Python
2. Flask
3. SQLAlchemy
4. CSS
5. JavaScript
6. Bootstrap

## How to run
* Enter the directory where the script is located then type the following to the console
```sh
$ https://github.com/sherif-abdallah/countries-web-scraper countries-web-scraper
```
* Install Python 3.8 venv, pip and compiler

```sh
$ sudo apt-get install python3.8 python3.8-venv python3-venv
```

* Create a virtual environment to install dependencies in and activate it:

```sh
$ python3.8 -m venv venv
$ source venv/bin/activate
```

* Then install the dependencies:

```sh
(venv)$ cd flask-blog
(venv)$ python -m pip install --upgrade pip
(venv)$ python -m pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Replace `kenya` in those arguments with `--output-file` and `?country=` the country you want to scrape 
```sh
wget --output-file=kenya.txt --recursive --spider --include-directories="/settlement/,/explore-our-data/country/" http://sdinet.org/explore-our-data/country/?country=kenya
```

* Finally run The Software
```sh
(venv)$ python main.py
```

## Author
[Sherif Abdullah](https://github.com/sherif-abdallah)

