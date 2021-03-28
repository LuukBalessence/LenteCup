from django.shortcuts import render, redirect

from LenteCup.forms import ChangeFirstNameForm, StandInvoerForm


def home(request):
    return render(request, "LenteCup/home.html",)


def explain(request):
    return render(request, "LenteCup/explain.html", )


def about(request):
    return render(request, "LenteCup/about.html", )


def myaccount(request):
    manager = request.user

    try:
        firstname = request.user.first_name
    except:
        firstname = ""


    return render(
        request=request,
        template_name="Lentecup/myaccount.html",
        context={"manager": manager, "firstname": firstname})


def changefirstname(request):
    if request.method == 'POST':
        form = ChangeFirstNameForm(request.POST)
        if form.is_valid():
            namedata = form.cleaned_data
            currentuser = request.user
            currentuser.first_name = namedata.get('firstname')
            currentuser.save()
            return redirect(to="myaccount")
        else:
            return render(request, "LenteCup/changefirstname.html", {'form': ChangeFirstNameForm})

    else:
        return render(request, template_name="LenteCup/changefirstname.html")

def standinvoer(request):
    currentuser = request.user
    if request.method == 'POST':
        form = StandInvoerForm(request.POST)
        if form.is_valid():
            namedata = form.cleaned_data
            currentuser = request.user
            currentuser.first_name = namedata.get('score')
            currentuser.save()
            return redirect(to="jouwuitslagen")
        else:
            return render(request, "LenteCup/standinvoer.html", {'form': StandInvoerForm})

    else:
        return render(request, template_name="LenteCup/standinvoer.html")


def jouwuitslagen(request):
    currentuser = request.user
    return render(request, template_name="LenteCup/standinvoer.html")
