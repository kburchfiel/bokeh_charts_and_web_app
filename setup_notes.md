## Heroku deployment notes:


1. The following links were helpful:
a. Flask Heroku deployment guide: https://realpython.com/flask-by-example-part-1-project-setup/
b. Heroku Python setup guide--doesn't actually mention Flask but the same principles still apply: https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true
c. https://www.kdnuggets.com/2020/09/flask-app-using-python-heroku.html (which provided the snippet that I needed to enter into my Procfile in order for the app to work)

2. I didn't use the git commands specified in these overviews to update my repository. Instead, I used the git tools included in Visual Studio Code, since (A) I was more familiar with them and (B) I also used them to upload my code to GitHub. 

3. Including a Procfile was necessary. The template specified at https://www.kdnuggets.com/2020/09/flask-app-using-python-heroku.html worked for me. This template is also available at https://devcenter.heroku.com/articles/python-gunicorn ("web: gunicorn hello:app")

4. I didn't create a virtual environment [although I probably should have], but I **did** need to define which libraries my code used within a requirements.txt file. Instead of using pip freeze > requirements.txt command, I just manually entered the several libraries that my code imported. (Other libraries got added in automatically during the deployment process.) I used the 'conda list' command within my main Conda environment to figure out which releases I needed to enter within requirements.txt, but it's possible that I didn't need to specify a release for each one.

5. In my case, I needed to use git push heroku master instead of git push heroku main in order to deploy the app.

6. If you didn't specify a name when creating your app (e.g. you only entered 'heroku create'), you can rename your app later on, as explained at https://devcenter.heroku.com/articles/renaming-apps#updating-git-remotes