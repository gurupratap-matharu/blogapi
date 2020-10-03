from django.urls import path

from pages.views import AboutPageView, ContactUsView, HomePageView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
]
