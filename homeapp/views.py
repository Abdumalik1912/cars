from django.shortcuts import render

# Create your views here.


def home(request):
    context = {"cars": [
        {"name": "Nexia3", "brand": "Chevrolet", "company": "GMmotors", "cost": 17000},
        {"name": "Matiz", "brand": "Chevrolet", "company": "GMmotors", "cost": 3000},
        {"name": "Mustang", "brand": "Ford", "company": "Ford", "cost": 59000},
        {"name": "Supra", "brand": "Toyota", "company": "Toyota Motor Corporation", "cost": 57000}
    ]}
    return render(request, "home.html", context)
