from django.shortcuts import render

def home(request):
  return render(request,"home.html")
 
def signin(request):
  return render(request,"signin.html")

def signup(request):
  return render(request,"signup.html")

def thumbnail(request):
  return render(request,"thumbnail.html")

def aboutus(request):
  return render(request,"aboutus.html")

def bestofcity(request):
  return render(request,"bestofcity.html")

def career(request):
  return render(request,"career.html")

def contact(request):
  return render(request,"contact.html")

def dish(request):
  return render(request,"dish.html")

def microbreweries(request):
  return render(request,"microbreweries.html")

def sportscreening(request):
  return render(request,"sportscreening.html")

def trending(request):
  return render(request,"trending.html")

def zomatopro(request):
  return render(request,"zomatopro.html")
