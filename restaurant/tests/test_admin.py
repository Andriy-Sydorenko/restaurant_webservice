from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from restaurant.models import DishType, Dish


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="test12345"
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="cook",
            password="cook12345",
            years_of_experience=12
        )
        self.dish_type = DishType.objects.create(name="test dish type")
        self.dish = Dish.objects.create(name="Test dish",
                                        description="Test description",
                                        price=9.99,
                                        dish_type=self.dish_type)

    def test_cook_years_of_experience_listed(self):
        """
        Tests that cook's years_of_experience is in list display on cook admin page
        """
        url = reverse("admin:restaurant_cook_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.cook.years_of_experience)

    def test_cook_detailed_years_of_experience_listed(self):
        """
        Tests that cook's years_of_experience is on cook detail admin page
        """
        url = reverse("admin:restaurant_cook_change", args=[self.cook.id])
        response = self.client.get(url)

        self.assertContains(response, self.cook.years_of_experience)

    def test_dish_type_name_listed(self):
        url = reverse("admin:restaurant_dishtype_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.dish_type.name)

    def test_detailed_dish_type_name_listed(self):
        url = reverse("admin:restaurant_dishtype_change", args=[self.dish_type.id])
        response = self.client.get(url)

        self.assertContains(response, self.dish_type.name)

    def test_dish_info_listed(self):
        url = reverse("admin:restaurant_dish_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.dish.name)
        self.assertContains(response, self.dish.description)
        self.assertContains(response, self.dish.price)
        self.assertContains(response, self.dish.dish_type)

    def test_detailed_dish_info_listed(self):
        url = reverse("admin:restaurant_dish_change", args=[self.dish.id])
        response = self.client.get(url)

        self.assertContains(response, self.dish.name)
        self.assertContains(response, self.dish.description)
        self.assertContains(response, self.dish.price)
        self.assertContains(response, self.dish.dish_type)
