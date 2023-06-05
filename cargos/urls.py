from django.urls import path

from cargos.views import CargoListView, CargoRetriveAPIView, CargoCreateAPIView, CargoDestroyAPIView, CargoUpdateAPIView

urlpatterns = [
    path('cargo/', CargoListView.as_view(), name='cargo_list'),
    path('cargo/<int:pk>/', CargoRetriveAPIView.as_view(), name='cargo_view'),
    path('cargo/create/', CargoCreateAPIView.as_view(), name='cargo_create'),
    path('cargo/delete/<int:pk>/', CargoDestroyAPIView.as_view(), name='cargo_delete'),
    path('cargo/update/<int:pk>/', CargoUpdateAPIView.as_view(), name='cargo_update'),
]