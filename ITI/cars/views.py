from django.shortcuts import render
from cars.models import Car
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from cars.forms import CarModelForm


# Create your views here.

def CarIndex(request):
    allCars = Car.getAllCars()
    return render(request, 'cars/index.html', context={"cars": allCars})


class CarDetailsView(DetailView):
    model = Car
    template_name = "cars/show.html"


class CreateCarView(CreateView):
    template_name = "cars/create.html"
    form_class = CarModelForm
    success_url = '/cars/index'


class EditCarView(UpdateView):
    template_name = "cars/edit.html"
    form_class = CarModelForm
    success_url = '/cars/index'
    model = Car


class DeleteCarView(DeleteView):
    template_name = "cars/delete.html"
    form_class = CarModelForm
    model = Car
