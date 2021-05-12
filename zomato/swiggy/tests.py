#from django.test import TestCase
# Create your tests here.
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
db=firebase.database()
auth=firebase.auth()

n=int(input('Enter choice : '))
if(n==0):
  e = input('Enter email')
  p = input('Enter password')
  try:
    #user = auth.current_user
    auth.sign_in_with_email_and_password(e,p)
    #uid=user['localId']
    print("Email Verified")
  except Exception as exp:
    print(exp)
else:
  e = input('Enter email : ')
  p = input('Enter password : ')
  # try:
  user=auth.create_user_with_email_and_password(e,p)
  data={'mail':e,'pass':p}
  db.child("swiggy").child(user['localId']).set(data)
# except Exception:
    # print(Exception)