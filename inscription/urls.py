from django.conf.urls import url
from . import views

app_name = "inscription"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^merci/$', views.ContactMerciView.as_view(), name="contact_merci"),
    url(r'^inscription/$', views.inscription, name="inscription"),
    url(r'^inscription/decharge$', views.InscriptionDechargeView.as_view(), name="inscription_decharge"),
    url(r'^inscription/merci$', views.InscriptionMerciView.as_view(), name="inscription_merci"),
]