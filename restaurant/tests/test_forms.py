from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from decimal import Decimal

from restaurant.models import Dish, DishType
from restaurant.forms import CookCreationForm, DishForm, DishTypeForm


class FormsTests(TestCase):

    def test_cook_creation_form_is_valid(self):
        form_data = {
            "username": "test_username",
            "password1": "user123test",
            "password2": "user123test",
            "first_name": "Test first",
            "last_name": "Test last",
            "years_of_experience": 15
        }
        form = CookCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class LoggedInFormsTests(TestCase):
    form_data = {}

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_superuser(
            "test_admin",
            "password"
        )
        self.client.force_login(self.user)

    def test_create_cook_when_form_is_empty(self):
        form = CookCreationForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_create_cook(self):
        form_data = {
            "username": "new_user",
            "password1": "user123test",
            "password2": "user123test",
            "first_name": "Test first",
            "last_name": "Test last",
            "years_of_experience": 15
        }

        self.client.post(reverse("restaurant:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.years_of_experience,
                         form_data["years_of_experience"])

    def test_create_dish_when_form_is_empty(self):
        form = DishForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_create_dish_valid(self):
        dish_type = DishType.objects.create(name="Test dish type")
        form_data = {
            "name": "new dish",
            "description": "Test description",
            "price": "9.99",
            "dish_type": dish_type
        }

        form = DishForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        new_dish = Dish.objects.get(name=form_data["name"])

        self.assertEqual(new_dish.description, form_data["description"])
        self.assertEqual(new_dish.price, Decimal(form_data["price"]))
        self.assertEqual(new_dish.dish_type, dish_type)

    def test_create_dish_type_when_form_is_empty(self):
        form = DishTypeForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_create_dish_type_valid(self):
        form_data = {
            "name": "test name"
        }
        form = DishTypeForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

        new_dish_type = DishType.objects.get(name=form_data["name"])
        self.assertEqual(new_dish_type.name, form_data["name"])


class DishDishTypeSearchFormTests(TestCase):
    """
    Test cases to test the work of dish-list and dish-type-list search forms
    """

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_superuser(
            "test",
            "password"
        )
        self.client.force_login(self.user)

        dish_type = DishType.objects.create(name="Test dish type")
        DishType.objects.create(name="Cake")
        DishType.objects.create(name="Beverage")

        Dish.objects.create(name="Baguette",
                            description="Test description",
                            price=9.99,
                            dish_type=dish_type)
        Dish.objects.create(name="Carrot cake",
                            description="Test description",
                            price=9.99,
                            dish_type=dish_type)
        Dish.objects.create(name="Pizza",
                            description="Test description",
                            price=9.99,
                            dish_type=dish_type)

        get_user_model().objects.create_user(
            "test_username1",
            "passwd12345"
        )
        get_user_model().objects.create_user(
            "test_username2",
            "passwd12345"
        )
        get_user_model().objects.create_user(
            "test_username3",
            "passwd12345"
        )

    def test_valid_dish_search_form_search(self):
        url = reverse("restaurant:dish-list")

        response = self.client.get(url, {"name": "Baguette"})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "form")
        self.assertContains(response, 'value="Baguette"')

        self.assertContains(response, "Baguette")
        self.assertNotContains(response, "Carrot cake")
        self.assertNotContains(response, "Pizza")

    def test_valid_dish_type_search_form_search(self):
        url = reverse("restaurant:dish-type-list")

        response = self.client.get(url, {"name": "Test dish type"})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "form")
        self.assertContains(response, 'value="Test dish type"')

        self.assertContains(response, "Test dish type")
        self.assertNotContains(response, "Cake")
        self.assertNotContains(response, "Beverage")

    def test_valid_cook_search_form_search(self):
        url = reverse("restaurant:cook-list")

        response = self.client.get(url, {"username": "test_username1"})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "form")
        self.assertContains(response, 'value="test_username1"')

        self.assertContains(response, "test_username1")
        self.assertNotContains(response, "test_username2")
        self.assertNotContains(response, "test_username3")

    def test_blank_dish_search(self):
        url = reverse("restaurant:dish-list")
        response = self.client.get(url, {"name": ""})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "form")

        self.assertContains(response, "Baguette")
        self.assertContains(response, "Carrot cake")
        self.assertContains(response, "Pizza")

    def test_blank_dish_type_search(self):
        url = reverse("restaurant:dish-type-list")
        response = self.client.get(url, {"name": ""})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "form")

        self.assertContains(response, "Test dish type")
        self.assertContains(response, "Cake")
        self.assertContains(response, "Beverage")

    def test_blank_cook_search(self):
        url = reverse("restaurant:cook-list")
        response = self.client.get(url, {"username": ""})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "form")

        self.assertContains(response, "test_username1")
        self.assertContains(response, "test_username2")
        self.assertContains(response, "test_username2")

    def test_invalid_dish_search(self):
        url = reverse("restaurant:dish-list")
        response = self.client.get(url, {"name": "InvalidDish"})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "form")
        self.assertContains(response, 'value="InvalidDish"')

        self.assertNotContains(response, "Baguette")
        self.assertNotContains(response, "Carrot cake")
        self.assertNotContains(response, "Pizza")

    def test_invalid_dish_type_search(self):
        url = reverse("restaurant:dish-type-list")
        response = self.client.get(url, {"name": "InvalidDishType"})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "form")
        self.assertContains(response, 'value="InvalidDishType"')

        self.assertNotContains(response, "Test dish type")
        self.assertNotContains(response, "Cake")
        self.assertNotContains(response, "Beverage")

    def test_invalid_cook_search(self):
        url = reverse("restaurant:cook-list")
        response = self.client.get(url, {"username": "InvalidCook"})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "form")
        self.assertContains(response, 'value="InvalidCook"')

        self.assertNotContains(response, "test_username1")
        self.assertNotContains(response, "test_username2")
        self.assertNotContains(response, "test_username2")
