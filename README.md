# Validus

## Setup + Startup

This project was set up using [virtualenv](https://virtualenv.pypa.io/en/stable/). Just clone this project into the standard virtualenv django project location.

1. Activate the project environment
1. Run migrations `python mange.py migrate`
1. Star the local server up `python manage.py runserver`
1. Visit localhost:8000

## Admin

If you wish to create an admin account `python manage.py createsuperuser`.

You can visit the admin page at `localhost:8000/admin` using the credentials you created. All that you can do there is modify users and view / create the `Currency` objects created in the migration.

## Data

The data is generated from the CSVs during the second migration. It could be generated using a separate script but it seemed like a reasonable location considering the purpose of this project.

## Models

The only model in this project is the `Currency` model. It is probably not named very well but I don't know the finance terminology.

## Urls and Views

Nothing special is implemnented in the urls or views, depending on the url a different page is served to the browser.

Navigation in the `base.html` is used to link all of the different parts of the project into an easily accessible website.

## Visualizations

NVD3 was used for quick easy graphing.