from django.shortcuts import render, get_object_or_404
from .models import Flower


def flower_list(request):
    flowers = Flower.objects.all()
    return render(request, "flowers_list.html", {"flowers": flowers})

