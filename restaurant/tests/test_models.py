from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from restaurant.models import Dish, DishType


class ModelsTests(TestCase):

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="Test dish type"
        )
        dish = Dish.objects.create(
            name="Test dish",
            description="Test description",
            price=9.99,
            dish_type=dish_type
        )
        self.assertEqual(str(dish), f"{dish.name} (price: {dish.price}, "
                                    f"type: {dish.dish_type.name})")

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="Test dish type"
        )
        self.assertEqual(str(dish_type), dish_type.name)

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="Test username",
            password="testpasswd",
            first_name="Rick",
            last_name="Sanchez"
        )
        self.assertEqual(str(cook), f"{cook.username} "
                                    f"({cook.first_name} {cook.last_name})")

    def test_create_cook_with_years_of_experience(self):
        username = "Test username"
        password = "testpasswd"
        first_name = "Rick"
        last_name = "Sanchez"
        years_of_experience = 4.5
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            years_of_experience=years_of_experience
        )
        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)
