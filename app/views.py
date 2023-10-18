from django.shortcuts import render

# Create your views here.
def echo_page(requeset):
    return render(requeset, "app/echo_page.html")