from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import product1Bidding,product2Bidding,product3Bidding,product4Bidding,product5Bidding,product6Bidding,product7Bidding
# Create your views here.
def home(reqest):
    return render(reqest,'home.html')

def basic(reqest):
    return  render(reqest,'basic.html')

#products functions
def product1(reqest):
     bids = product2Bidding.objects.all()
     
     return render(reqest,'product1.html',{'bids':bids})   

def product(reqest):
    bids = product1Bidding.objects.all()
    k=0
    c=0
    for item in bids:
        c+=1
        k+=item.rating
    print(k)
    print(c)
    if k/c>=0 and k/c <=1:
        loop=1
    if k/c>1 and k/c <=2:
        loop=2
    if k/c>2 and k/c <=3:
        loop=3
    if k/c>3 and k/c <=4:
        loop=4
    if k/c>4 and k/c <=5:
        loop=5
    print(loop)
    l=[]
    for i in range(0,loop):
        l.append(i)
    print(loop)
    return render(reqest,'product.html',{'bids':bids})
    

def product3(reqest):
    bids = product3Bidding.objects.all()
    return render(reqest,'product3.html',{'bids':bids})

def product4(reqest):
    bids = product4Bidding.objects.all()
    return render(reqest,'product4.html',{'bids':bids})

def product5(reqest):
    bids = product5Bidding.objects.all()
    return render(reqest,'product5.html',{'bids':bids})

def product6(reqest):
    bids = product6Bidding.objects.all()
    return render(reqest,'product6.html',{'bids':bids})

def product7(reqest):
    bids = product7Bidding.objects.all()
    return render(reqest,'product7.html',{'bids':bids})


def signin(reqest):
    if reqest.method == 'POST':
        username = reqest.POST['username']
        password = reqest.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(reqest,user)
            return redirect('home')
        else:
            messages.info(reqest,'Invalid credantials')
            return redirect('signin')
    else:
        return render(reqest,'signin1.html')
 

def signup(reqest):
    if reqest.method == "POST":
        first_name = reqest.POST['first_name']
        last_name = reqest.POST['last_name']
        username = reqest.POST['username']
        email = reqest.POST['email']
        password1 = reqest.POST['password1']
        password2 = reqest.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(reqest,'user taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(reqest,'Email Exists')
                return redirect('signup')
            else:
                 user =User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                 user.save()
                 return redirect('signin')
        else:
            messages.info(reqest,'Password is nat matching...')
            return redirect('signup')
        return redirect('/')
    else:
        return render(reqest, 'signup1.html')






#bidding functions 
def addbidding(reqest):
    if reqest.method == 'POST':
        username =reqest.POST['username']
        email = reqest.POST['email']
        pnumber = reqest.POST['pnumber']
        price = reqest.POST['price']
        rating=reqest.POST['rating']
        newbid = product1Bidding(username=username,email=email,phonenumber=pnumber,bprice=price,rating=rating)
        newbid.save()

        return redirect('product')
    else:
        return render(reqest,'addbidding.html')

def addbidding1(reqest):
    if reqest.method == 'POST':
        username =reqest.POST['username']
        email = reqest.POST['email']
        pnumber = reqest.POST['pnumber']
        price = reqest.POST['price']
        newbid = product2Bidding(username=username,email=email,phonenumber=pnumber,bprice=price)
        newbid.save()

        return redirect('product1')
    else:
        return render(reqest,'addbidding1.html')

def addbidding3(reqest):
    if reqest.method == 'POST':
        username =reqest.POST['username']
        email = reqest.POST['email']
        pnumber = reqest.POST['pnumber']
        price = reqest.POST['price']
        newbid = product3Bidding(username=username,email=email,phonenumber=pnumber,bprice=price)
        newbid.save()

        return redirect('product3')
    else:
        return render(reqest,'addbidding3.html')

def addbidding4(reqest):
    if reqest.method == 'POST':
        username =reqest.POST['username']
        email = reqest.POST['email']
        pnumber = reqest.POST['pnumber']
        price = reqest.POST['price']
        newbid = product4Bidding(username=username,email=email,phonenumber=pnumber,bprice=price)
        newbid.save()

        return redirect('product4')
    else:
        return render(reqest,'addbidding4.html')

def addbidding5(reqest):
    if reqest.method == 'POST':
        username =reqest.POST['username']
        email = reqest.POST['email']
        pnumber = reqest.POST['pnumber']
        price = reqest.POST['price']
        newbid = product5Bidding(username=username,email=email,phonenumber=pnumber,bprice=price)
        newbid.save()

        return redirect('product5')
    else:
        return render(reqest,'addbidding5.html')

def addbidding6(reqest):
    if reqest.method == 'POST':
        username =reqest.POST['username']
        email = reqest.POST['email']
        pnumber = reqest.POST['pnumber']
        price = reqest.POST['price']
        newbid = product6Bidding(username=username,email=email,phonenumber=pnumber,bprice=price)
        newbid.save()

        return redirect('product6')
    else:
        return render(reqest,'addbidding6.html')

def addbidding7(reqest):
    if reqest.method == 'POST':
        username =reqest.POST['username']
        email = reqest.POST['email']
        pnumber = reqest.POST['pnumber']
        price = reqest.POST['price']
        user=auth.authenticate(username=username)
        if user is not None:
            auth.login(reqest,user)
            newbid = product7Bidding(username=username,email=email,phonenumber=pnumber,bprice=price)
            newbid.save()
            return redirect('product7')
        else:
            messages.info(reqest,'Invalid username')
            return redirect('addbidding7')
    else:
        return render(reqest,'addbidding7.html')