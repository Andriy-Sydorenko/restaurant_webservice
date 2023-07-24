from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from restaurant.models import Dish, DishType

DISH_URL = reverse("restaurant:dish-list")
DISH_TYPE_URL = reverse("restaurant:dish-type-list")
COOK_URL = reverse("restaurant:cook-list")


class PublicTests(TestCase):

    def assert_login_required_prep(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_dish_list_login_not_required(self):
        self.assert_login_required_prep(DISH_URL)

    def test_dish_type_list_login_not_required(self):
        self.assert_login_required_prep(DISH_TYPE_URL)

    def test_cook_list_login_not_required(self):
        self.assert_login_required_prep(COOK_URL)


class PrivateTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "password12345"
        )
        self.dish_type1 = DishType.objects.create(name="test_dish_type1")
        self.dish_type2 = DishType.objects.create(name="test_dish_type2")
        self.client.force_login(self.user)

    def test_retrieve_dishes(self):
        Dish.objects.create(name="test name 1",
                            description="test description 1",
                            price=9.99,
                            dish_type=self.dish_type1)
        Dish.objects.create(name="test name 2",
                            description="test description 2",
                            price=9.50,
                            dish_type=self.dish_type2)

        response = self.client.get(DISH_URL)
        dishes = Dish.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["dish_list"]),
                         list(dishes))
        self.assertTemplateUsed(response, "restaurant/dish_list.html")

    def test_retrieve_dish_types(self):
        response = self.client.get(DISH_TYPE_URL)
        dish_types = DishType.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["dish_type_list"]),
                         list(dish_types))
        self.assertTemplateUsed(response, "restaurant/dish_type_list.html")

    def test_retrieve_cooks(self):
        get_user_model().objects.create_user(
            username="test username",
            password="passwd"
        )
        response = self.client.get(COOK_URL)
        cooks = get_user_model().objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["cook_list"]),
                         list(cooks))
        self.assertTemplateUsed(response, "restaurant/cook_list.html")
