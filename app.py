



# Django imports
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models

# Django model
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

# Function to create the database table if it doesn't exist
def create_table():
    # Django migration yapısını kullanarak modeli oluştur
    pass

# View function for rendering the index page
def index(request):
    return render(request, 'index.html')

# View function for handling the form submission
def kaydet(request):
    if request.method == 'POST':
        try:
            auth_username = request.POST['auth_username']
            auth_password = request.POST['auth_password']

            # Django modeli kullanarak veritabanına ekle
            User.objects.create(username=auth_username, password=auth_password)

            print("Data saved successfully")
            return redirect('index')
        except Exception as e:
            print(f"Error: {str(e)}")
            return HttpResponse("An error occurred while saving data.")

    return HttpResponse("Invalid request method.")

