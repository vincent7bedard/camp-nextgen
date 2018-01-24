from django.conf.urls import url
from . import views

app_name = "inscription"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^merci/$', views.ContactMerciView.as_view(), name="contact_merci"),
    url(r'^inscription/$', views.inscription, name="inscription"),
    url(r'^inscription/attente$', views.InscriptionAttenteView.as_view(), name="inscription_attente"),
    url(r'^inscription/annulation$', views.InscriptionAnnulationView.as_view(), name="inscription_annulation"),
    url(r'^inscription/decharge$', views.InscriptionDechargeView.as_view(), name="inscription_decharge"),
    url(r'^inscription/paiement$', views.InscriptionPaiementView.as_view(), name="inscription_paiement"),
    url(r'^inscription/merci$', views.InscriptionMerciView.as_view(), name="inscription_merci"),
    #pour la verification de Google Search Console (webmaster tools)
    url(r'^google64b73e3e98e79ca8.html$', views.GoogleSearchConsoleView.as_view(), name="google_verification"),

]