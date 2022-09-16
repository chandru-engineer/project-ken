from django.shortcuts import render, redirect
from .models import OrderModel
from datetime import date

def current_date():
    today = str(date.today())
    return today


def home(request):
    return render(request, 'home.html')

def order(request):
    customer_id_data = 0
    customer_name = 'chandru'
    phone_number = '+91 9791394624'
    address = 'Murugan Kovil Street, kakkoor, ramanathapuram'
    if request.method =='POST':
        chicken_kg = request.POST['quantity']
        chicken_category = request.POST['category']
        chicken_cutting = request.POST['cutting']
        goat_kg = request.POST['quantity']
        goat_category = request.POST['goat_category']
        goat_cutting = request.POST['goat_cutting']
        date = request.POST['date']
        # print(chicken_kg)
        # print(chicken_category)
        # print(chicken_cutting)
        # print()
        # print(goat_kg)
        # print(goat_category)
        # print(goat_cutting)
        # print(date)
        object = OrderModel.objects.create(
            customer_name = customer_name,
            customer_id = customer_id_data,
            phone_number = phone_number,
            delivery_date = date,
            current_date = current_date(),
            delivery_time = '08:34',
            address = address,
            chicken_kg = chicken_kg,
            chicken_category = chicken_category, 
            chicken_citting = chicken_cutting,
            mutton_kg = goat_kg,
            mutton_category = goat_category,
            mutton_cutting = goat_cutting,
            status = False,
            delivered = False,
            amount = 100,
            review = "")

        object.save()
        return redirect('test')
    else:
        return render(request, 'order.html')


def test(request):
    return render(request, 'test.html')


