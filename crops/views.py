from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from disease.models import disease
from disease1.models import disease1
from Medicine.models import Medicine
from ship.models import ship
from Research.models import Research
from About.models import About
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth import authenticate, login
import keras
import numpy as np
from PIL import Image
from django.core.files.storage import FileSystemStorage
import os
import h5py as h5
from Contact.models import Contact




media = "media"
model = keras.models.load_model("potatoes.h5")


def makepredictions(path):

    img = Image.open(path)

    img_d = img.resize(244, 244)

    if len(np.array(img_d).shape) < 4:
        rgb_img = Image.new("RGB", img_d.size)
        rgb_img.paste(img_d)
    else:
        rgb_img = img_d

    rgb_img = np.array(rgb_img, dtype=np.float64)
    rgb_img = rgb_img.reshape(1, 244, 244, 3)

    predictions = model.predict(rgb_img)
    a = int(np.argmax(predictions))
    if a == 1:
        a = "Result: Early Blight"
    elif a == 2:
        a = "Result:Late Blight"
    elif a == 3:
        a = "Result:Healthy Potato"
    else:
        a = "Result:no Result"
    return a





def index(request):
    diseaseData = disease.objects.all()
    disease1Data = disease1.objects.all()
    Medicinedata = Medicine.objects.all()
    Researchdata = Research.objects.all()
    AboutData = About.objects.all()

    data = {
        'diseaseData': diseaseData,
        'disease1Data': disease1Data,
        'Medicinedata': Medicinedata,
        'Researchdata': Researchdata,
        'AboutData': AboutData


    }
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        return HttpResponse("<h1>Thanks For Contact US</h1>")
       

    return render(request, 'index.html', data)


def account(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        Email = request.POST.get('Email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            return HttpResponse("Your Password is not Equal to confirm Password")
        else:
            my_user = User.objects.create_user(fname, Email, pass1)
            my_user.save()

            return redirect('login')

    return render(request, 'Create account.html')


def doctor(request):
    return render(request, 'Doctor.html')


def Amistar(request, Amistarid):

    MedicineData = Medicine.objects.get(id=Amistarid)
    data = {
        'MedicineData': MedicineData

    }
    return render(request, 'Amistar Top.html', data)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Username or Password is Incorrect!!!")
    return render(request, 'login.html')


def Medicine2(request):
    return render(request, 'Medicine.html')


def order1(request):
    n = ''

    if request.method == 'POST':

        fname = request.POST.get('fname')
        Lname = request.POST.get('Lname')
        Email = request.POST.get('Email')
        Address = request.POST.get('Address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        Postal_code = request.POST.get('Postal Code')
        Select_Medicine = request.POST.get('Medicine')
        Payment = request.POST.get('Payment')
        en = ship(First_Name=fname, Last_Name=Lname, Email=Email, Address=Address, city=city,
                  state=state, Postal_code=Postal_code, Select_Medicine=Select_Medicine, Payment=Payment)
        en.save()
        n = 'Order has been Placed Successfully'

    return render(request, 'order.html', {'n': n})


def logoutpage(request):
    logout(request)
    redirect('login')


def change_password(request):
    if request.method == "POST":
        pass1 = PasswordChangeForm(user=request.user, data=request.POST)
        if pass1.is_valid():
            pass1.save()
        return HttpResponseRedirect('/home/')
    else:
        pass1 = PasswordChangeForm(user=request.user)
    return render(request, 'changepassword.html', {'form': pass1})


def diseasedetail(request, diseaseid):
    print(diseaseid)
    diseaseData = disease1.objects.get(id=diseaseid)
    data = {
        'diseaseData': diseaseData
    }

    return render(request, 'disease.html', data)


def Researchdetail(request, Researchid):
    Researchdata = Research.objects.get(id=Researchid)
    data = {
        'Researchdata': Researchdata
    }
    return render(request, 'Research.html', data)


def Researchuploader(request):

    return render(request, 'Research Uploader.html')


def Research1(request):

    return render(request, 'Research 1.html')


def About1(request, Aboutid):

    AboutData = About.objects.get(id=Aboutid)
    data = {
        'AboutData': AboutData
    }

    return render(request, 'About.html', data)


def detect(request, detectid):
    return render(request, 'Detector.html')


def detect1(request, detect1id):
    return render(request, 'detect1.html')

def video(request):
    return render(request,'video.html')
