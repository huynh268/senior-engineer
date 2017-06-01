# Senior Engineer Interview Task
Clipboard Health Senior Engineer Interview Task

### Introduction:
This project is divided into two components:
1. A Python data ingestion pipeline for converting entries in a CSV file to MongoDB documents:

As is true of a lot of our user generated data, it is not standardized. So as part of this process you will need to standardize the data, it is up to you how you choose to handle data that cannot be machine parsed. Then, you will populate a Mongo DB.

The fields you will be populating are: Wage, Patient:Nurse Ratio

Wages: Please standardize to Hourly

Ratio: Notice values some may be reversed, i.e. 5:1 vs 5

Additionally, you may also populate Department and Location.

Once you've done so, you can answer the following questions:
* What’s the average per hour salary
* What are the top 10 nursing departments?
* What percentage of nurses have bachelor’s v. associate’s?



2. An Express web server with unimplemented API endpoints and a prebuilt react application.

You will be serving the data that you just loaded into your Mongo DB and serving it to a react application where you will visualized nicely. Think of it as a page a nurse might want to see to learn about their fellow nurses. We recommend using D3.

Please use the visualization that you see as most appropriate (for example, location should be on a map) but feel free to be creative! (There's nothing wrong with a histogram!)

### Notes:
You are not expected to finish everything. I repeat: **You are not expected to finish everything**

Please make a new commit for each task (with a relevant commit message).

**Please spend no longer than four hours on this task.**

You can spend as much or as little time on each section and you may work out in the order you see fit.

You may additionally write tests as you fit.

### Before you begin:

* rename this file to TASKS.md
* initialize an empty repository
* add TASKS.md to a .gitignore (you may also want to add node_modules, github maintains a node gitignore [here](https://github.com/github/gitignore/blob/master/Node.gitignore))
* push the repository to github (and send me a link to it!)

## Dependencies
* Python 3.5
* Virtualenv
* Node.js (>= v6.0.0)
* mongodb >= 3.4.0
* Yarn

## Installation
* Set up a virtual enviroment with:
  ```bash
  virtualenv venv
  source venv/bin/activate
  ```
* Install python dependencies in requirements.txt by:
  ```bash
  pip install -r requirements.txt
  ```
* Install node dependencies with:
  ```bash
  npm install
  ```

### Running in development mode
1. Start webpack-dev-sever by typing ```npm start```
2. With your virtual enviroment enabled, run ```flask run``` and navigate to [localhost:5000](http://localhost:5000)

### Running in production mode
1. set `NODE_ENV=production` in your `.env` file
2. Compile webpack using ```npm run build```
3. With your virtual enviroment enabled, run ```flask run``` and navigate to [localhost:5000](http://localhost:5000)


1. ``` cp sample.env .env ``` and set values as appropriate.

2. Run `npm run forever-start` and navigate to `<ip>:<port> (default=7999)`.

###  Developing:
1. Set `NODE_ENV=development` in `.env`.
2. Run `npm run dev`
