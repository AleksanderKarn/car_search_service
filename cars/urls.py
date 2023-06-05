from django.urls import path

from cars.views import CarUpdateAPIView, CarListView, CarRetriveAPIView

urlpatterns = [
    path('car/', CarListView.as_view(), name='car_list'),
    path('car/<str:pk>/', CarRetriveAPIView.as_view(), name='car_view'),
    path('car/update/<str:pk>/', CarUpdateAPIView.as_view(), name='car_update'),
]
