from django.urls import path
from login.views import login,  auth_view, loggedin,  registration, home, index, displaydetails, \
    showconfirmation, deleteaccount, accountdeleted, logout_view, updatedetails
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('', index),
    path('login/', login),
    path('login/auth/', auth_view),
    path('loggedin/', loggedin),
    path('registration/', registration),
    path('home/', home),
    path('home/updatedetails', updatedetails),
    path('home/displaydetails',displaydetails),
    path('home/confirm', showconfirmation),
    path('home/deleteaccount', deleteaccount),
    path('home/deleted', accountdeleted),
    path('resetpassword/', auth_views.PasswordResetView.as_view(template_name="forgotpasswordforemail.html"), name="password_reset"),
    path('resetemailsent/', auth_views.PasswordResetDoneView.as_view(template_name="resetlinksent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="newpassword.html"), name="password_reset_confirm"),
    path('passwordconfirmed/', auth_views.PasswordResetCompleteView.as_view(template_name="passwordconfirmed.html"), name="password_reset_complete"),
    path('logout/', logout_view)
]
