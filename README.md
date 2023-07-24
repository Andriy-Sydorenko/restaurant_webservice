# Restaurant webservice
> It's a website where you can share your favourite recipes and upgrade your cooking skills.


## Installing / Getting started

A quick introduction of the setup you need to get run a project.
1. Fork a repo.
2. Use this command ```git clone the-link-from-your-forked-repo```. 
   - You can get the link by clicking the Clone or download button in your repo.
3. Open the project folder in your IDE.
4. Open a terminal in the project folder. 
5. If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
    - For Windows:
    ```shell
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```
   - For Mac OS:
    ```shell
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
6. Run create migration file, using 
    ```shell
    python manage.py makemigrations
    ```
    Then migrate file, using
    ```shell
    python manage.py migrate
    ```
7. Then, to run a project, use this command:
    ```shell
    python manage.py runserver 
    ```







## Features

What's all the bells and whistles this project can perform?
* What's the main functionality
* You can also do another thing
* If you get really randy, you can even do this


## Contributing

When you publish something open source, one of the greatest motivations is that
anyone can just jump in and start contributing to your project.

These paragraphs are meant to welcome those kind souls to feel that they are
needed. You should state something like:

"If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome."

If there's anything else the developer needs to know (e.g. the code style
guide), you should link it here. If there's a lot of things to take into
consideration, it is common to separate this section to its own file called
`CONTRIBUTING.md` (or similar). If so, you should say that it exists here.

## Links

Even though this information can be found inside the project on machine-readable
format like in a .json file, it's good to include a summary of most useful
links to humans using your project. You can include links like:

- Project homepage: https://your.github.com/awesome-project/
- Repository: https://github.com/your/awesome-project/
- Issue tracker: https://github.com/your/awesome-project/issues
  - In case of sensitive bugs like security vulnerabilities, please contact
    my@email.com directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!
- Related projects:
  - Your other project: https://github.com/your/other-project/
  - Someone else's project: https://github.com/someones/awesome-project/


## Licensing

One really important part: Give your project a proper license. Here you should
state what the license is and how to find the text version of the license.
Something like:

"The code in this project is licensed under MIT license."