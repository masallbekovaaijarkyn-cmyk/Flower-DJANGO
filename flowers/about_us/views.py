from django.shortcuts import render
from .models import About_us, Contact


def about_view(request):
    about = About_us.objects.first()
    contact = Contact.objects.first()

    return render(request, "about_list.html", {"about": about,
                                          "contact": contact})




