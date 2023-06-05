from rest_framework import serializers

from cargos.models import Cargo
from cars.models import Car
from geopy.distance import geodesic as GD


class CargoSerializer(serializers.ModelSerializer):
    nearest_cars = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = (
            "id",
            "pick_up",
            "delivery",
            "weight",
            "description",
            "nearest_cars",
        )

    def get_nearest_cars(self, instance):
        cargo_location = (
            instance.pick_up.lat,
            instance.pick_up.lng,
        )

        all_cars = Car.objects.all()

        all_nearest_cars = {}

        for car in all_cars:
            car_location = (
                car.location.lat,
                car.location.lng
            )
            distance = GD(cargo_location, car_location).miles
            format_distance = f"{round(distance, 1)} miles to cargo"
            if distance <= 450:
                all_nearest_cars[car.uid] = format_distance

        return all_nearest_cars


class CargosSerializer(serializers.ModelSerializer):
    count_cars = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = (
            "id",
            "pick_up",
            "delivery",
            "count_cars",
            "weight",

        )

    def get_count_cars(self, instance):
        cargo_location = (
            instance.pick_up.lat,
            instance.pick_up.lng,
        )

        all_cars = Car.objects.all()

        count_car = 0

        for car in all_cars:
            car_location = (
                car.location.lat,
                car.location.lng
            )
            distance = GD(cargo_location, car_location).miles

            if distance <= 450:
                count_car += 1
        return count_car


class CargoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = (
            "weight",
            "description",
        )
