import random
from car_search_service.celery import app
from cars.functions import loc_list_create
from cars.models import Car


@app.task
def change_location():
    cars = Car.objects.all()
    loc_list = loc_list_create()

    for car in cars:
        car.location_id = random.choice(loc_list)
        car.save()

# celery -A car_search_service worker -l INFO -P eventlet  -запуск celery

# celery -A car_search_service beat -l info -S django   - запуск celerybeat
