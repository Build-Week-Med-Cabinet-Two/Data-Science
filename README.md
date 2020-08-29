![Imgur](https://i.imgur.com/Lp5ehld.png)
# What is Med Cabinet?

Med Cabinet is an app for people who are new to using cannabis as a way to curtail certain medical conditions
and ailments.  This app will help patients find the right strain for them, and give a description of the strain as well as 
the effects, flavor and type. MedCabinet will suggest 10 strains based on user input. This app was built using Flask, as well 
as a PostgreSQL database hosted on ElephantSQL. My team (DS Unit 3) was asked to build the Flask app and the Postgres database. 
The DS Unit 4 team was responsible for the predictive model used in this app.

## How to install and run:

### Using pipenv:
**1**Within a CLI, clone the repository -> git clone https://github.com/CurdtMillion/Data-Science.git<br> 
**2**Once the repo is saved to your local machine, navigate to the correct directory -> cd data-science<br>
**3**Create a pip environment with your CLI using Python 3.7 -> pipenv --python 3.7<br> 
**4**Install requried dependencies -> pipenv install [dependency name here]<br> 
**5**Activate the shell -> pipenv shell

### Run
$ gunicorn -w 4 medcab:APP -t 300