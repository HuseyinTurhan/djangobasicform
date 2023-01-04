from django.shortcuts import render
from . import forms
from .models import User
# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #do something
            User.objects.get_or_create(name=form.cleaned_data["name"],
                                        email=form.cleaned_data["email"],
                                        text=form.cleaned_data["text"],
                                        date=form.cleaned_data["date"])[0]
        else:
            print("The form is invalid..")


    return render(request, 'basicapp/form_page.html', {'form':form})