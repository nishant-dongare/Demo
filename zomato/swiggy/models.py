from django.shortcuts import render
import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyB5jnpgecmxcn7Ievpkp85sBrHVZLC0_gc",
  'authDomain': "swiggy-af371.firebaseapp.com",
  'databaseURL': "https://swiggy-af371-default-rtdb.firebaseio.com",
  'projectId': "swiggy-af371",
  'storageBucket': "swiggy-af371.appspot.com",
  'messagingSenderId': "392430883755",
  'appId': "1:392430883755:web:9d27f3e006e36d3569f8ee",
  'measurementId': "G-JXTKT3DYHD"
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

def login(request):
  e = request.POST['email']
  p = request.POST['pass']
  try:
    user=auth.sign_in_with_email_and_password(e,p)
    #uid=user['localId']
    return render(request,"home.html")
  except:
    return render(request,"signup.html")

def register(request):
  db=firebase.database()
  e = request.POST['e']
  p = request.POST['p']
  user=auth.create_user_with_email_and_password(e,p)
  #auth.send_email_verification(user['idToken'])
  data={'mail':e,'pass':p}
  db.child("swiggy").child(user['localId']).set(data)
  return render(request,"signin.html")