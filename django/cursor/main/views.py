from django.shortcuts import render
from .models import MenuItem, SliderItem
from django.conf import settings
import os


def main(request):
    menu_items = MenuItem.objects.all()
    slider_image = SliderItem.objects.all()
    return render(request, "index.html", {"menu_items": menu_items, "slider_image": slider_image})