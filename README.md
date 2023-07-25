# Restaurant webservice
> It's a website where you can share your favourite recipes and upgrade your cooking skills.

## Features
* Chef Registration: Aspiring chefs can easily sign up and create their profiles, showcasing their culinary specialties.
* Add a Dish: Chefs can add their signature dishes to the platform, along with detailed recipes and descriptions.
* Explore Dishes: Users can browse through a wide range of dishes uploaded by various chefs, learning about different cuisines and cooking styles.
* Search: Users can use search option to find specific dishes or chefs.

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
7. Create superuser to see extended functionality of the website:
    ```shell
    python manage.py createsuperuser
    ```
    Also, you can create a regular user, using registration form on the website.

8. Then, to run a project, use this command:
    ```shell
    python manage.py runserver 
    ```

## Links

Even though this information can be found inside the project on machine-readable
format like in a .json file, it's good to include a summary of most useful
links to humans using your project. You can include links like:

- Repository: https://github.com/Andriy-Sydorenko/restaurant_webservice
- Issue tracker: https://github.com/Andriy-Sydorenko/restaurant_webservice/issues
  - In case of sensitive bugs like security vulnerabilities, please contact
    sidorenkoandrij217@gmail.com directly instead of using issue tracker. I value your effort
    to improve the security and privacy of this project!
- Here is the link to the deployed website: https://www.example.com


## Licensing

One really important part: Give your project a proper license. Here you should
state what the license is and how to find the text version of the license.
Something like:

"The code in this project is licensed under MIT license."