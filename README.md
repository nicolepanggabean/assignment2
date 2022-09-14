Heroku app link: https://pbp-assignment-2-catalog.herokuapp.com/katalog/

diagram link: https://www.canva.com/design/DAFMOV6_uLI/6df5H0bh500ywN8prtcSSQ/view?utm_content=DAFMOV6_uLI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

1. Explain the flow of the diagram and how the `urls.py`, `views.py`, `models.py` and HTML files connected each other.

    In the diagram, we see that when a client makes a request to a Django web app, it gets sent to the Django framework. When it reaches urls.py, it extracts arguments from the request and conducts URL routing to deliver the arguments to the necessary files.
The views.py file essentially receives these arguments and generates a response through written code. It extracts data from models.py, which contains data stored in tables from the database.
Then, the processed data is converted to HTML format and saved in HTML files, which is then sent back to the client as a web page.

2. Explain why do we use virtual environments? Let's say, if we do not use the virtual environments, can we still create a Django web application?

    A virtual environment ensures that whatever packages we install _only_ apply to the current project we're working on. This also means that we can organize our packages and only keep or install the ones necessary.
If we do not use virtual environments, it is still be possible, but it is not as effective. Due to there being no isolation, one issue that could arise is the amount of unnecessary python packages piling up.
Another issue is the lack of isolation. For example, if an app is already deployed and currently running, but we need to make updates, using two separate virtual environments could let the original deployed app keep running while we work on deploying the newer version. Without the virtual environment, any changes made would interrupt the already deployed app.

3. Explain how did you implement the steps on point 1 to point 4 above.

    STEP 1: To create a function that can query into models and return the data into an HTML file, I used the render() function from django.shortcuts.
This function takes in one argument, which is request. Within the function, I saved the data from models.py into a variable called data_catalog_item. I then created a context variable that will help fill out missing data in the HTML file.

    STEP 2: Then, I edited the urlpatterns in the urls.py file that is located in the katalog application folder by ensuring that it includes the views.py function.
    I also edited the urls.py file in the project_django folder by ensuring that the urls.py file that is in the katalog application folder is also included in this one.
    
    STEP 3: I edited the HTML file to make sure it loops through all the data within models.py and displays them in an organized manner. I also made sure it was able to display my name and student ID.
    
    STEP 4: To deploy, I created an app on HEROKU and took the API key. I then added the API key and the app name and put it into the repository secrets, which is then read by the dpl.yml file.
