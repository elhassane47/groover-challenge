# ChallengeBackend

Your goal is to create an app using the [spotify web api](https://developer.spotify.com/documentation/web-api/). You can make for example a [Flask](https://flask.palletsprojects.com/en/1.1.x/) or [Django rest framework](https://www.django-rest-framework.org/) project, it has to be able to authenticate to Spotify to fetch the new releases. Your job is to add two new features:
- A way to fetch data from spotify’s new releases API (/v1/browse/new-releases) and persist in a Postgresql DB (mandatory)
- A route : `/api/artists/` returning a JSON containing informations about artists that have released new tracks recently, from your local copy of today’s spotify’s new releases.

## Project Structure
The spotify auth is provided by us: (follows spotify web api.): it is located in `spotify_auth.py`.
The flow ends with a call to `/auth/callback/` which will give you the necessary access tokens.
To use it, we will provide you with the necessary: CLIENT_ID and CLIENT_SECRET.
Feel free to move it and re-organise as you please, we expect a well organised and clean code. Keep in mind that we want an Authorization Code Flow to see how you handle user authorization.
  
  
## Tech Specifications
- Be smart in your token usage (no unnecessary refreshes)
- Don’t request spotify artists at each request we send you
- The way you store the artists in Postgresql DB is going to be important use an ORM.
- As stated above, to test your server we will `GET /api/artists/` and we expect a nicely organised payload of artists. Make sure to use proper serialization and handle http errors.

All stability, performance, efficiency adds-up are highly recommended.

## Run project using virtualenv



* env - using virtualenv here but any env manager should work

      $ sudo apt install build-essential python3.7 python-dev python3.7-dev python3-venv python3-pip  # depends on distro/os a lot
      $ pip3 install virtualenv
      $ python3 -m virtualenv env
      $ source env/bin/activate  
      $ pip install -r requirements.txt  

* Create postgresql database

* add env variables
     
      $ export CLIENT_ID=spotify_client_id
      $ export CLIENT_SECRET=spotify_secret_id
      $ export POSTGRES_DB=db_name
      $ export POSTGRES_USER=db_user
      $ export POSTGRES_PASSWORD=db_password
  

* Create the sql tables

      $ python manage.py migrate

* Create a user
	
      $ python manage.py createsuperuser

* Run the server on port 5000

      $ python manage.py runserver 5000

The website should be accessible at http://localhost:5000/  

* login to spotify to get your access token

 http://localhost:5000/login_spotify
 
* get new releases

 http://localhost:5000/artists/new_releases/
 
* all artists :
http://localhost:5000/artists


