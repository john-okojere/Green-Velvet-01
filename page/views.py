from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

def get_menus(request):
    with connection.cursor() as cursor:
        # Fetch menu for Restaurant
        cursor.execute("SELECT id, name, main_category, description, price FROM Restaurant_menu WHERE main_category != 'Drink'")
        restaurant_menu = cursor.fetchall()

        # Fetch menu for Restaurant_A
        cursor.execute("SELECT id, name, main_category, description, price FROM Restaurant_A_menu WHERE main_category != 'Drink'")
        restaurant_a_menu = cursor.fetchall()
        
        # Fetch menu for Drink
        cursor.execute("SELECT id, name, main_category, description, price FROM Restaurant_menu WHERE main_category == 'Drink'")
        drink_menu = cursor.fetchall()

    # Format data
    menu_data = {
        "Restaurant": [{"id": item[0], "name": item[1], "main_category": item[2], "description" : item[3], "price" : item[4] } for item in restaurant_menu],
        "Restaurant_A": [{"id": item[0], "name": item[1], "main_category": item[2], "description" : item[3], "price" : item[4]  } for item in restaurant_a_menu],
        "Drink": [{"id": item[0], "name": item[1], "main_category": item[2], "description" : item[3], "price" : item[4]  }for item in drink_menu]
    }, 
    return JsonResponse(menu_data, safe=False)

def homepage(request):
    return render(request, 'index.html')

def africanMenu(request):
    return render(request, 'africaMenu.html')

def internationalMenu(request):
    return render(request, 'Menu.html')

def drinkMenu(request):
    return render(request, 'Drinks.html')