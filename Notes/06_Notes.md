# Flask to integrate backend and frontend

- Flask is a web framework which makes it easy to make a web application. We can make front-end using HTML templates with some placeholders for variables and we can define API endpoints and routers to run some logic, access a database and so on.

- Do `flask run` and this will start a web server on `localhost:5000`. Refer: https://flask.palletsprojects.com/en/1.1.x/quickstart/

- On powershell to enable debug mode `$env:FLASK_ENV = "development"`, this will reload the application automatically. Reference: https://stackoverflow.com/a/63056713/9719106

- Flask templates are `jinja2` templates. [Jinja Documentation](https://jinja.palletsprojects.com/en/3.0.x/)

- In flask we create a folder `templates` and we want all of our flask templates to go in this folder. Same for data and static files we have directories.

- We use `render_template` to return the files and we use `url_for('static',filename='name.ext')` to return the static file. `{{}}` are placeholders used as per jinja2 templates.
