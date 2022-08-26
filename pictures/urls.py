from django.urls import path
from . import views
urlpatterns = [
    path('', views.MainPage, name="mainpage"),
    path('photo-detail/<int:pk>/<str:tags>',
         views.PhotoDetails, name="photo-detail"),
    path('categories', views.categore, name="categore"),
    path('/', views.SearchPage, name="search"),

    path('Contact/', views.about, name="contact"),
    path('about', views.about, name="about"),
    path('use-agreement', views.UseAgreement, name="use-agreement"),
    path('PrivacyPolicy', views.PrivacyPolicy, name="PrivacyPolicy"),
]
