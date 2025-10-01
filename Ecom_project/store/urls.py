from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('about/',views.about,name="About"),
    path('signup/',views.register_view,name='register'),
    path('verify/<str:token>/', views.verify_email, name="verify_email"),
    path('Userprofile/',views.Userprofile,name='userprofile'),
    path('update_user',views.update_user,name='update_user'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('product/<int:pk>',views.specific_product,name='product'),
    path('categories/',views.Categories,name='Category'),
    path('change_password/',views.PasswordChange,name='password_change'),
    path('Forget_password/',views.ForgetPassword,name='forget_password'),
    path('OTP_verfication',views.Verify_otp,name="OTP"),

]