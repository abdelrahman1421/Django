from django.urls import path
from cars.views import CarIndex,CarDetailsView,CreateCarView,EditCarView,DeleteCarView
urlpatterns = [
    path('index', CarIndex),
    path('create',CreateCarView.as_view()),
    path('show/<int:pk>', CarDetailsView.as_view(), name='car.show'),
    path('edit/<int:pk>', EditCarView.as_view(), name='car.edit'),
    path('delete/<int:pk>', DeleteCarView.as_view(), name='car.delete')

]