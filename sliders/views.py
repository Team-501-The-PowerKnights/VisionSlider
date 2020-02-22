from django.shortcuts import render, HttpResponse
from .forms import ContactForm


# def home(request):
#     return render(request, "sliders/sliders.html")

def contact(request):
    form = ContactForm()
    return render(request, "sliders.html", {"form": form})
