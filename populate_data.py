import os
import django
import faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject_connect_to_azuredb.settings')
django.setup()

from myapp.models import Person

fake = faker.Faker()

def populate(n):
    for _ in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        address = fake.address()
        city = fake.city()

        Person.objects.create(first_name=first_name, last_name=last_name, email=email, address=address, city=city)

if __name__ == '__main__':
    populate(10)  # Populate with 10 fake entries

