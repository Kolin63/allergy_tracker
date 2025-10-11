from django.urls import path
from . import views

urlpatterns = [
    # Main / index
    path('', views.index, name='index'),


    # Auth
    path('login/', views.login, name='login'),
    path('callback/', views.callback, name='callback'),
    path('logout/', views.logout, name='logout'),

    # Users
    path('users/', views.users, name='users'),
    path('users/<int:id>/', views.details, name='details'),

    # Restaurants
    path('restaurants/<int:user_id>/', views.Restaurants, name='restaurants'),
    path('restaurants/<int:id>/delete/', views.delete_restaurants, name='delete_restaurant'),
    path('restaurants/<int:id>/update/', views.update_restaurant, name='update_restaurant'),
    path('restaurants/<int:id>/details/', views.restaurant_details, name='restaurant_details'),

    # Menus
    path('menus/<int:user_id>/', views.menus, name='menus'),
    path('menus/<int:id>/delete/', views.delete_menu, name='delete_menu'),
    path('menus/<int:id>/update/', views.update_menu, name='update_menu'),
    path('menus/<int:id>/details/', views.menu_details, name='menu_details'),

    # Menu Sections
    path('menu_sections/<int:user_id>/', views.menu_sections, name='menu_sections'),
    path('menu_sections/<int:id>/delete/', views.delete_menu_section, name='delete_menu_section'),
    path('menu_sections/<int:id>/update/', views.update_menu_section, name='update_menu_section'),
    path('menu_sections/<int:id>/details/', views.menu_section_details, name='menu_section_details'),

    # Foods
    path('foods/<int:user_id>/', views.Foods, name='foods'),
    path('foods/<int:id>/delete/', views.delete_foods, name='delete_foods'),
    path('foods/<int:id>/update/', views.update_foods, name='update_foods'),
    path('foods/<int:id>/details/', views.foods_details, name='foods_details'),

    # Food Allergens
    path('food_allergens/<int:food_allergen_id>/', views.food_allergens, name='food_allergens'),
    path('food_allergens/<int:id>/delete/', views.delete_food_allergen, name='delete_food_allergen'),
    path('food_allergens/<int:id>/update/', views.update_food_allergen, name='update_food_allergen'),
    path('food_allergens/<int:id>/details/', views.food_allergen_details, name='food_allergen_details'),
    
    path('search-restaurants/', views.search_restaurants, name='search_restaurants'),

    # Test session
    path('test-session/', views.test_session, name='test_session'),
]