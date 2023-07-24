from django.urls import path

from restaurant.views import (IndexView,
                              SignUpView,

                              DishListView,
                              DishCreateView,
                              DishDetailView,
                              DishUpdateView,
                              DishDeleteView,

                              DishTypeListView,
                              DishTypeDetailView,
                              DishTypeCreateView,
                              DishTypeUpdateView,
                              DishTypeDeleteView,
                              DishUpdateCookView,

                              CookListView,
                              CookDetailView,
                              CookCreateView,
                              CookUpdateView,
                              CookDeleteView)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),

    path("dishes/",
         DishListView.as_view(),
         name="dish-list"),
    path("dishes/<int:pk>/",
         DishDetailView.as_view(),
         name="dish-detail"),
    path("dishes/create/",
         DishCreateView.as_view(),
         name="dish-create"),
    path("dishes/<int:pk>/update/",
         DishUpdateView.as_view(),
         name="dish-update"),
    path("dishes/<int:pk>/delete/",
         DishDeleteView.as_view(),
         name="dish-delete"),
    path("dishes/<int:pk>/update-cook/",
         DishUpdateCookView.as_view(),
         name="dish-update-cook"),

    path("dish-types/",
         DishTypeListView.as_view(),
         name="dish-type-list"),
    path("dish-types/<int:pk>/",
         DishTypeDetailView.as_view(),
         name="dish-type-detail"),
    path("dish-types/create/",
         DishTypeCreateView.as_view(),
         name="dish-type-create"),
    path("dish-types/<int:pk>/update/",
         DishTypeUpdateView.as_view(),
         name="dish-type-update"),
    path("dish-types/<int:pk>/delete/",
         DishTypeDeleteView.as_view(),
         name="dish-type-delete"),

    path("cooks/",
         CookListView.as_view(),
         name="cook-list"),
    path("cooks/<int:pk>/",
         CookDetailView.as_view(),
         name="cook-detail"),
    path("cooks/create/",
         CookCreateView.as_view(),
         name="cook-create"),
    path("cooks/<int:pk>/update/",
         CookUpdateView.as_view(),
         name="cook-update"),

    path("cooks/<int:pk>/delete/",
         CookDeleteView.as_view(),
         name="cook-delete"),

    path("signup/", SignUpView.as_view(), name="signup")
]


app_name = "restaurant"
