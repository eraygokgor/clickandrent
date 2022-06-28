from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from pymongo import MongoClient
from base64 import b64encode

connect_string = "mongodb+srv://clickandrent:Se.Click123@cluster0.upwlw.mongodb.net/clickandrentDB?retryWrites=true&w=majority"


# Create your views here.
def index(request):
    my_client = MongoClient(connect_string)
    dbname = my_client['clickandrentDB']
    collection_name = dbname["ads"]

    data = collection_name.find().sort('_id', -1).limit(5)
    
    return render(request, 'clickandrent/index.html', {'auth': 0, "data": data})

def login(request):
    return render(request, "clickandrent/login.html")

def signup(request):
    return render(request, "clickandrent/signup.html")

def existing(request):
    return render(request, "clickandrent/existing.html")

def session(request):
    return render(request, "clickandrent/session.html")

def logout(request):
    auth_logout(request)
    return redirect("/")

def ads(request):
    my_client = MongoClient(connect_string)
    dbname = my_client['clickandrentDB']
    collection_name = dbname["ads"]
    data = collection_name.find({"user_id": request.user.id})
    return render(request, "clickandrent/ads.html", {"data": data})

def add(request):
    if request.method == "GET":
        return render(request, "clickandrent/add.html")

    if request.method == "POST":
        # Conn
        my_client = MongoClient(connect_string)
        dbname = my_client['clickandrentDB']
        collection_name = dbname["ads"]

        # Data
        title = request.POST['title']
        description = request.POST['description']
        fee = request.POST['fee']
        phone = request.POST['phone']
        location = request.POST['location']
        photo = request.FILES['photo'].read()
        category = request.POST['category']
        data = {
            "user_id" : request.user.id,
            "title": title,
            "description": description,
            "fee": fee,
            "phone": phone,
            "photo": b64encode(photo).decode('utf-8'),
            "location": location,
            "category": category,
            "name": request.user.first_name,
            "last_name": request.user.last_name,
        }
        if category == "Real Estate":
            est_rooms = request.POST['est_rooms']
            est_area = request.POST['est_area']
            est_age = request.POST['est_age']
            data["est_rooms"] = est_rooms
            data["est_area"] = est_area
            data["est_age"] = est_age
            collection_name.insert_one(data)

        elif category == "Vehicle":
            vehicle_year = request.POST['vehicle_year']
            vehicle_brand = request.POST['vehicle_brand']
            vehicle_model = request.POST['vehicle_model']
            vehicle_gear = request.POST['vehicle_gear']
            vehicle_fuel = request.POST['vehicle_fuel']
            vehicle_color = request.POST['vehicle_color']
            data["vehicle_year"] = vehicle_year
            data["vehicle_brand"] = vehicle_brand
            data["vehicle_model"] = vehicle_model
            data["vehicle_gear"] = vehicle_gear
            data["vehicle_fuel"] = vehicle_fuel
            data["vehicle_color"] = vehicle_color
            collection_name.insert_one(data)
        elif category == "Computer":
            comp_year = request.POST['comp_year']
            comp_brand = request.POST['comp_brand']
            comp_model = request.POST['comp_model']
            comp_capacity = request.POST['comp_capacity']
            comp_resolution = request.POST['comp_resolution']
            data["comp_year"] = comp_year
            data["comp_brand"] = comp_brand
            data["comp_model"] = comp_model
            data["comp_capacity"] = comp_capacity
            data["comp_resolution"] = comp_resolution
            collection_name.insert_one(data)
        elif category == "Home Appliance":
            home_year = request.POST['home_year']
            home_brand = request.POST['home_brand']
            home_model = request.POST['home_model']
            home_power = request.POST['home_power']
            data["home_year"] = home_year
            data["home_brand"] = home_brand
            data["home_model"] = home_model
            data["home_power"] = home_power
            collection_name.insert_one(data)
        elif category == "Book":
            book_year = request.POST['book_year']
            book_edition = request.POST['book_edition']
            book_language = request.POST['book_language']
            book_publisher = request.POST['book_publisher']
            book_writer = request.POST['book_writer']
            data["book_year"] = book_year
            data["book_edition"] = book_edition
            data["book_language"] = book_language
            data["book_publisher"] = book_publisher
            data["book_writer"] = book_writer
            collection_name.insert_one(data)
        elif category == "Musical Instrument":
            music_type = request.POST['music_type']
            music_year = request.POST['music_year']
            music_brand = request.POST['music_brand']
            music_model = request.POST['music_model']
            data["music_type"] = music_type
            data["music_year"] = music_year
            data["music_brand"] = music_brand
            data["music_model"] = music_model
            collection_name.insert_one(data)
        elif category == "Other":
            other_year = request.POST['other_year']
            other_brand = request.POST['other_brand']
            data["other_year"] = other_year
            data["other_brand"] = other_brand
            collection_name.insert_one(data)
        return redirect("add")


def settings(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, "clickandrent/settings.html", {"email": user.email})

def register_user(request):
    if request.method == 'POST':
        if User.objects.filter(email=request.POST.get("inputEmail")).exists():
            return render(request, "clickandrent/signup.html", {'existing': 1})
        else:
            username = request.POST.get("inputEmail")
            email = request.POST.get("inputEmail")
            password = request.POST.get("inputPassword")
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = request.POST.get("inputName")
            user.last_name = request.POST.get("inputLastName")
            user.save()
            return render(request, "clickandrent/register.html")

def signin(request):
    if request.method == 'POST':
        try:
            username = request.POST["inputEmail"]
            password = request.POST["inputPassword"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                name = user.first_name
                lastname = user.last_name
                auth_login(request, user)
                # return render(request, "clickandrent/index.html", {'name':name, 'lastname': lastname, 'auth' : 1})
                return redirect("/")
            else:
                return render(request, 'clickandrent/login.html', {'auth': 0})
        except:
            return render(request, 'clickandrent/login.html', {'auth': 0})
    if request.method == 'GET' and request.user.is_authenticated:
        user = request.user
        return render(request, 'clickandrent/profile.html', {'name': user.first_name, 'lastname': user.last_name,})


def changes(request):
    if request.method == "POST":
        try:
            new_password = request.POST["inputPassword"]
            user = request.user
            if new_password != '':
                user.set_password(new_password)
            user.save()
            return redirect("/")
        except:
            print(e)
            return render(request, 'clickandrent/profile.html')

def delete(request):
    my_client = MongoClient(connect_string)
    dbname = my_client['clickandrentDB']
    collection_name = dbname["ads"]
    user_id = request.user.id
    request.user.delete()
    collection_name.delete_many({'user_id': int(user_id)})
    auth_logout(request)
    return redirect("/")

def deletead(request):
    my_client = MongoClient(connect_string)
    dbname = my_client['clickandrentDB']
    collection_name = dbname["ads"]
    id = request.POST.get("object_id")
    import bson
    collection_name.remove({"_id": bson.objectid.ObjectId(id)})
    return redirect("/")

def adverts(request, objectid):
    from bson.objectid import ObjectId
    my_client = MongoClient(connect_string)
    dbname = my_client['clickandrentDB']
    collection_name = dbname["ads"]
    data = collection_name.find_one({"_id": ObjectId(objectid)})
    return render(request, 'clickandrent/advert.html', {'data': data})

def search(request):
    search = request.POST['search']
    location = request.POST['location']
    category = request.POST['category']
    my_client = MongoClient(connect_string)
    dbname = my_client['clickandrentDB']
    collection_name = dbname["ads"]

    query = {}
    query['$and'] = []

    if search != '':
        query['$and'].append({'title': {'$regex': search, '$options' : 'i'}})
    if location != 'City...' and location != '':
        query['$and'].append({'location': location})
    if category != 'Category...':
        query['$and'].append({'category': category})

    print(query)
    search_result = collection_name.find(query)
    return render(request, 'clickandrent/search.html', {'data': search_result})