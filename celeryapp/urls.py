from django.urls import path
from celeryapp import views

urlpatterns = [
    path('', views.test, name='test'),
    path('sendmail/', views.SendEmail.as_view(), name="sendmail"),
    # path('sendmail/', views.send_mail_to_all, name="sendmail"),

]