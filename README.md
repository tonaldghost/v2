# v2
Django application that will solve all problems at work. Currently in creation and debug.

Install the dependencies with the command pip install -r requirements.txt.

Also for developers I would advise adding a python linting to Pylint Args.
    - If you are using VS Code this is quite straight forward. As follows.
    
    Go to User preferences, paste this:
        {"python.linting.pylintArgs": [      "--load-plugins=pylint_django" ],}
    
    into the search bar add this as the item:
        --load-plugins=pylint_django
    
    This will also assist in conforming your code to pep guidelines which is great for future development.

