from django.shortcuts import render


def home(request):
    return render(request, "LenteCup/home.html",)


def explain(request):
    return render(request, "LenteCup/explain.html", )


def about(request):
    return render(request, "LenteCup/about.html", )