from django.urls import path

from userlog.views import IndexPage,SignUpPage,LogInPage,logoutPage,RedirectDashboard,ForgotPassword,ChangePassword

urlpatterns = [
    path('',IndexPage.as_view(),name='home'),
    path('signup/',SignUpPage.as_view(),name='signup'),
    path('login/',LogInPage.as_view(),name='login'),
    path('logout/',logoutPage,name='logout'),
    path('dashboard/',RedirectDashboard.as_view(),name='dashboard'),
    path('forgot/password/',ForgotPassword.as_view(),name='forgot'),
    path('change/password/<uuid:uuid>/',ChangePassword.as_view(),name='changepassword')
]