from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,CustomerProfile,Category
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
import uuid
from .models import CustomerProfile
from .forms import ProfileForm
from django.db.models import Q
import json
from cart.cart import Cart
import random


def Home(request):
    query = request.GET.get('search', '')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query) 
        ).distinct()

    else:
        products = Product.objects.all()

    return render(request, 'core/home.html', {
        'products': products,'query':query
    })


def specific_product(request,pk):
    product=get_object_or_404(Product,pk=pk)
    return render(request,'core/specific_product.html',{'product':product})

def about(request):
    return render(request,'core/about.html',{})

def Categories(request):
    categories=Category.objects.all()
    return render(request,'core/category.html',{'categories':categories})


def Verify_otp(request):
    return render(request,'registration/otp_verification.html')

def ForgetPassword(request):
    if request.method =='POST':
        email = request.POST.get('email')
        if User.objects.filter(email = email).exists():
            user=User.objects.get(email=email)
            otp=random.randint(100000,999999)
            subject = "Your OTP for Verification- ShopyWorld"
            message = f'Hi User! \n \n Your OTP is :{otp} \n\n This OTP is valid for 5 minutes.'
            email_from = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request,'OTP Sent to mail')
            return render(request,'registration/otp_verification.html',{'user':user})

            

    
        else:
            messages.error(request,'Email is not registered.')

    return render(request,'registration/Forgetpassword.html')

def PasswordChange(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == "POST":
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2 :
                user.set_password(password2)
                user.save()
                update_session_auth_hash(request, user)  # keep user logged in
                messages.success(request, "Your password has been updated successfully.")
                return redirect("Home")
            else:
                messages.error(request, "Password does not match. Please retry again. ")
                return render(request,"registration/password_change.html")
                
    return render(request,"registration/password_change.html")

def Userprofile(request):
    user = request.user
    profile = getattr(user, 'customerprofile', None) 
    return render(request, "core/profile_view.html", {
        "user": user,
        "profile": profile
    })


def update_user(request):
    if request.user.is_authenticated:
        user = request.user
        profile = user.customerprofile 

        if request.method == "POST":
            user.first_name = request.POST.get("firstname", user.first_name)
            user.last_name = request.POST.get("lastname", user.last_name)
            user.email = request.POST.get("email", user.email)

            profile_form = ProfileForm(request.POST, instance=profile)

            if profile_form.is_valid():
                user.save()
                profile_form.save()
                login(request, user) 
                messages.success(request, "Profile updated successfully!")
                return redirect("userprofile")
            else:
                messages.error(request, "Please correct the errors below.")
        else:
            profile_form = ProfileForm(instance=profile)

        return render(request, "registration/update_user.html", {
            "user": user,
            "form": profile_form
        })

    

    

# ✅ Send email with token
def send_email_token(user):
    token = str(uuid.uuid4())
    profile = CustomerProfile.objects.get(user=user)
    profile.email_token = token
    profile.save()

    verify_url = settings.SITE_URL + reverse('verify_email', kwargs={'token': token})
    subject = "Verify your email - MyShop"
    message = f"Hi {user.username},\n\nClick the link below to verify your email:\n{verify_url}\n\nThanks!"
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]

    send_mail(subject, message, email_from, recipient_list)

def valid_password(password):
    d=False
    s=False
    l=False
    u=False
    if len(password) < 8 :
        return False
    elif password.isupper():
        u=True
    elif password.islower():
        l=True
    elif password.isdigit():
        d=True
    else:
        s=True
    return s and d and l and u
    


# ✅ Register new user
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if not valid_password(password):
            messages.error(request, "Password not according to requirments")
            return redirect("register")

        if password != confirm_password or not valid_password(password):
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect("register")

        # ✅ create user
        user = User.objects.create_user(username=username, email=email, password=password)
        CustomerProfile.objects.create(user=user)

        # send verification email
        send_email_token(user)
        messages.success(request, "Account created! Please check your email to verify.")
        return redirect("login")

    return render(request, "registration/signup.html")


# ✅ Verify email
def verify_email(request, token):
    try:
        profile = CustomerProfile.objects.get(email_token=token)
        profile.is_verified = True
        profile.email_token = None  
        profile.save()
        messages.success(request, "Email verified successfully! You can now login.")

        return render(request, "verification.html", {"verified": True})
    except CustomerProfile.DoesNotExist:
        messages.error(request, "Invalid or expired token.")


        return render(request, "core/verification.html", {"verified": False})



# ✅ Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            profile = CustomerProfile.objects.get(user=user)
            if not profile.is_verified:
                messages.error(request, "Email not verified! Check your inbox.")
                return redirect("login")

            login(request, user)
            #getting the current user
            current_user = CustomerProfile.objects.get(user__id=request.user.id)
            # get the saved cart data
            saved_cart = current_user.old_cart
            #converting json cart data into dictionary
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                # adding converted dictionary to our sessions
                
                cart = Cart(request)
                for key,value in converted_cart.items():
                    cart.db_add(product=key,quantity=value['quantity'])

                



            messages.success(request, f"Welcome {user.username}!")
            return redirect("Home")
        else:
            messages.error(request, "Invalid credentials!")
            return redirect("login")

    return render(request, "registration/login.html")


# ✅ Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("Home")



