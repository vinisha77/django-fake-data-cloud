from django.shortcuts import render
from .models import Person
from faker import Faker

fake = Faker()

def generate_fake_data(request):
    # Specify the number of fake data entries you want to create
    num_entries = 10

    for _ in range(num_entries):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        address = fake.address()
        city = fake.city()

        # Create and save the Person instance
        person = Person(first_name=first_name, last_name=last_name, email=email, address=address, city=city)
        person.save()

    return render(request, 'myapp/success.html')

def home(request):
    return render(request, 'myapp/home.html')
