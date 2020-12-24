# ALL RECIPE WEBSITE

## ABOUT 

This website is the outcome of my Web Development (17CS71) mini-project, built using HTML, CSS, JavaScript, Bootstrap and Python built upon Django Framework. It is a Recipe Website, built in these unprecented pandemic period with the motive of giving everyone an opportunity to learn something new to cook, specially recipes out of their usual domain, keeping the recipes informative, super fun and easy to cook for them!  

## FUNCTIONALITIES

- `Log In / Register` - Implemented the Register and Log In functionality for users to create an account.

- `Main Page` - The main page consists of a navbar which presents the user with two main categories - Indian and Continental. The Indian menu, consists of six cuisines from six different states of India. They are - Andhra, Chettinad, Kashmiri, Gujarati, Maharashtrian and Punjabi. Each cuisine currently consists of only six recipes each. The Continental category consists of five dishes from various different countries.

- `Recipe Page` - The recipe page of each dish consists of a detailed information about the dish and its recipe. It gives a brief description of the dish selected, the ingredients required to prepare it, nutrition info, along with nutrition facts of the dish, and finally - a summarized recipe to cook it along with necessary images.

- `Feedback Page` - Users can give their review about the website by filling a feedback form. The details would get stored in the Django Admin interface.

- `Meet the team` - This page introduces the users to the developers. Users can view the creators and their role, and can also connect with them through various platforms like LinkedIn, GitHub or can mail them in case of a query. 

- `Share Page` - At the bottom of each recipe, users will find various social media platform buttons which they can click on to share the whole recipe page using the desired networking site. Few of them are Facebook, Twitter, Reddit, etc.

### RUNNING THE PROJECT

In order to run the all-recipe project, first make all migrations to load the models into database by running the following commands on terminal - 
```
python manage.py makemigrations
```
```
python manage.py migrate
```

To run the server, type this line your terminal - 
```
python manage.py runserver
```
Finally, visit the browser and enter `http://127.0.0.1:8000/all_recipe/` to view the project. 
