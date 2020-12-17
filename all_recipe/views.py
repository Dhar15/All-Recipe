from django.shortcuts import render
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.db import IntegrityError
from .models import User, Feedback
from django.contrib.auth.decorators import login_required

# class AddRecipeForm(forms.Form):
#     title = forms.CharField(label="",
#         widget=forms.TextInput(attrs={'placeholder': ' Recipe Name*', 
#             'style': 'width:90%'})) 
#     description = forms.CharField(label="",
#         widget=forms.Textarea(attrs={'placeholder': ' Description*', 
#             'style': 'width:90%'}))
#     image = forms.ImageField()
#     ingredients = forms.CharField(label="",
#         widget=forms.Textarea(attrs={'placeholder': ' Ingredients*', 
#             'style': 'width:90%'}))
#     recipe = forms.CharField(label="",
#         widget=forms.Textarea(attrs={'placeholder': ' Recipe*', 
#             'style': 'width:90%'}))

class FeedbackForm(forms.Form):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': ' Name*', 'style': 'width:90%'})) 
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': ' Email*', 'style': 'width:90%'})) 
    phno = forms.IntegerField(label="",required=False, widget=forms.TextInput(attrs={'placeholder': ' Phone Number', 'style': 'width:90%'}))
    message =  forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Leave us a feedback*', 'style': 'width:90%'}))

# Create your views here.
def index(request):
    # Authenticated users view their inbox
    if request.user.is_authenticated:
        return render(request, "all_recipe/main_page.html",{
            "user": request.user.username
        })

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "all_recipe/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "all_recipe/login.html")

def register(request):
    if request.method == "POST":
        # username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "all_recipe/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "all_recipe/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "all_recipe/register.html")

def kashmiri(request):
    return render(request, "all_recipe/indian/kashmiri.html")

def andhra(request):
    return render(request, "all_recipe/indian/andhra.html")

def chettinad(request):
    return render(request, "all_recipe/indian/chettinad.html")

def gujarati(request):
    return render(request, "all_recipe/indian/gujarati.html")

def maharashtrian(request):
    return render(request, "all_recipe/indian/maharashtrian.html")

def punjabi(request):
    return render(request, "all_recipe/indian/punjabi.html")

def continental(request):
    return render(request, "all_recipe/continental.html")

#ANDHRA RECIPES
def pepperChicken(request):
    return render(request, "all_recipe/recipes/andhra/pepperChicken.html")
def andhraChicken(request):
    return render(request, "all_recipe/recipes/andhra/andhraChicken.html")
def andhraBhindi(request):
    return render(request, "all_recipe/recipes/andhra/andhraBhindi.html")
def hyderabadiBiriyani(request):
    return render(request, "all_recipe/recipes/andhra/hyderabadiBiriyani.html")
def panasaPuttu(request):
    return render(request, "all_recipe/recipes/andhra/panasaPuttu.html")
def kebabs(request):
    return render(request, "all_recipe/recipes/andhra/kebabs.html")

#CHETTINAD RECIPES
def aatukkariKuzhambu(request):
    return render(request, "all_recipe/recipes/chettinad/aatukkariKuzhambu.html")
def chettinadChicken(request):
    return render(request, "all_recipe/recipes/chettinad/chettinadChicken.html")
def eggCurry(request):
    return render(request, "all_recipe/recipes/chettinad/eggCurry.html")
def mushroom(request):
    return render(request, "all_recipe/recipes/chettinad/mushroom.html")
def fishFry(request):
    return render(request, "all_recipe/recipes/chettinad/fishFry.html")
def paalPayasam(request):
    return render(request, "all_recipe/recipes/chettinad/paalPayasam.html")

#GUJARATI RECIPES
def aamShrikand(request):
    return render(request, "all_recipe/recipes/gujarati/aamShrikand.html")
def dalDhokli(request):
    return render(request, "all_recipe/recipes/gujarati/dalDhokli.html")
def dhokla(request):
    return render(request, "all_recipe/recipes/gujarati/dhokla.html")
def khandvi(request):
    return render(request, "all_recipe/recipes/gujarati/khandvi.html")
def thepla(request):
    return render(request, "all_recipe/recipes/gujarati/thepla.html")
def handvo(request):
    return render(request, "all_recipe/recipes/gujarati/handvo.html")

#KASHMIRI RECIPES
def dumAloo(request):
    return render(request, "all_recipe/recipes/kashmiri/dumAloo.html")
def saag(request):
    return render(request, "all_recipe/recipes/kashmiri/saag.html")
def roganJosh(request):
    return render(request, "all_recipe/recipes/kashmiri/roganJosh.html")
def khatteBaingan(request):
    return render(request, "all_recipe/recipes/kashmiri/khatteBaingan.html")
def muttonRibs(request):
    return render(request, "all_recipe/recipes/kashmiri/muttonRibs.html")
def nadrooYakhni(request):
    return render(request, "all_recipe/recipes/kashmiri/nadrooYakhni.html")

#MAHARASHTRIAN RECIPES
def aamti(request):
    return render(request, "all_recipe/recipes/maharashtrian/aamti.html")
def batataVada(request):
    return render(request, "all_recipe/recipes/maharashtrian/batataVada.html")
def pudachiWadi(request):
    return render(request, "all_recipe/recipes/maharashtrian/pudachiWadi.html")
def puranPoli(request):
    return render(request, "all_recipe/recipes/maharashtrian/puranPoli.html")
def pavBhaji(request):
    return render(request, "all_recipe/recipes/maharashtrian/pavBhaji.html")
def misalPav(request):
    return render(request, "all_recipe/recipes/maharashtrian/misalPav.html")

#PUNJABI RECIPES
def butterChicken(request):
    return render(request, "all_recipe/recipes/punjabi/butterChicken.html")
def amritsariFish(request):
    return render(request, "all_recipe/recipes/punjabi/amritsariFish.html")
def tandooriChicken(request):
    return render(request, "all_recipe/recipes/punjabi/tandooriChicken.html")
def choleBhature(request):
    return render(request, "all_recipe/recipes/punjabi/choleBhature.html")
def sarsonSaag(request):
    return render(request, "all_recipe/recipes/punjabi/sarsonSaag.html")
def dalMakhani(request):
    return render(request, "all_recipe/recipes/punjabi/dalMakhani.html")

#CONTINENTAL
def bruschetta(request):
    return render(request, "all_recipe/recipes/continental/bruschetta.html")
def margherita(request):
    return render(request, "all_recipe/recipes/continental/margherita.html")
def batterfriedfish(request):
    return render(request, "all_recipe/recipes/continental/batterfriedfish.html")
def chickenmanchurian(request):
    return render(request, "all_recipe/recipes/continental/chickenmanchurian.html")
def schezwanfriedrice(request):
    return render(request, "all_recipe/recipes/continental/schezwanfriedrice.html")

def about(request):
    return render(request, "all_recipe/about.html")

def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phno = form.cleaned_data['phno']
            message = form.cleaned_data['message']
            instance = Feedback(name=name, email=email, phno=phno, message=message)
            instance.save()
            return HttpResponseRedirect(reverse("index"))

    return render(request, "all_recipe/feedback.html", {
        "form": FeedbackForm()
    })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))