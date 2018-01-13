from django.conf.urls import url
from . import views

app_name = "inscription"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^merci/', views.ContactMerciView.as_view(), name="contact_merci"),
    url(r'^form/', views.form_test, name="form_name"),
    url(r'^inscription/', views.inscription, name="inscription"),
    url(r'^resultat/', views.ResultatView.as_view(), name="resultat"),
]