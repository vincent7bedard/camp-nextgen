from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.core.mail import send_mail
from . import forms

# Create your views here.


# name="index"
def index(request):
    """
    Homepage
    """
    form = forms.ContactForm() #parentheses ou non à la fin !?!?
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #do something if is valid
            # Soit avec le request.POST["blabla"]
            # exemple : contact_name = request.POST["contact_name"]

            #Soit avec le form.cleaned_data["blabla"] (MEILLEURE OPTION)
            contact_name = form.cleaned_data["contact_name"]
            contact_email = form.cleaned_data["contact_email"]
            email_content = form.cleaned_data["email_content"]

            email_subject = "Contact - Camp NextGen"
            # Il faut mettre le compte Gmail de CampNextGen ici
            adresse_email_campnextgen = "vincent.bedard.9@ulaval.ca"
            email_message = email_content + "\n\nDe " + contact_name + "\n" + contact_email

            # Envoie un email de la part du client (Si Gmail le permet) vers Camp NextGen.
            send_mail(email_subject, email_message, contact_email, [adresse_email_campnextgen])
            
            # redirect to a new URL:
            return redirect(reverse("inscription:contact_merci"))

    context = {"form": form}
    return render(request, "inscription/index.html", context)


# name="inscription"
def inscription(request):
    """
    Page d'inscription
    """
    form = forms.InscriptionForm() #parentheses ou non à la fin !?!?
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = forms.InscriptionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #do something if is valid
            #Avec le request.POST["blabla"]
            #Avec le form.cleaned_data["blabla"]

            # Parent
            parent_prenom = form.cleaned_data["parent_prenom"]
            parent_nom = form.cleaned_data["parent_nom"]

            # Enfant
            enfant_prenom = form.cleaned_data["enfant_prenom"]
            enfant_nom = form.cleaned_data["enfant_nom"]
            enfant_ecole = form.cleaned_data["enfant_ecole"]
            enfant_email = form.cleaned_data["enfant_email"]
            enfant_age = form.cleaned_data["enfant_age"]
            enfant_position = form.cleaned_data["enfant_position"]
            enfant_grandeur_tshirt = form.cleaned_data["enfant_grandeur_tshirt"]
            numero_telephone = form.cleaned_data["numero_telephone"]
            decharge = form.cleaned_data["decharge"]

            email_subject = "Inscription - Camp NextGen"
            adresse_email_client = enfant_email
            # Il faut mettre le compte Gmail de CampNextGen ici
            adresse_email_campnextgen = "vincent.bedard.9@ulaval.ca"
            
            email_message = "Email: {}\nNuméro de téléphone: {}\nA accepté la décharge: {}\nNom parent: {} {}\n\nNom enfant: {} {}\nÉcole enfant: {}\nÂge enfant: {} ans\nPosition enfant: {}\nGrandeur de T-shirt enfant: {}\n\n\n\nMerci de votre inscription.\n\nL'équipe du Camp NextGen".format(enfant_email, numero_telephone, decharge, parent_prenom, parent_nom, enfant_prenom, enfant_nom, enfant_ecole, enfant_age, enfant_position, enfant_grandeur_tshirt)

            # Envoie un email de la part de Camp NextGen vers Camp NextGen et vers le client pour que les gars sachent qui est inscrit et pour que le client recoivent une corfirmation..
            send_mail(email_subject, email_message, adresse_email_campnextgen, [adresse_email_client, adresse_email_campnextgen])

            
            # redirect to a new URL:
            return redirect(reverse("inscription:inscription_merci")) #est-ce qu'on doit mettre les guillemets ou non dans reverse() ?

    context = {"form": form}
    return render(request, "inscription/inscription.html", context)


# name="inscription_decharge"
class InscriptionDechargeView(TemplateView):
    """
    Lecture de la décharge
    """
    template_name = "inscription/inscription_decharge.html"


# name="contact_merci"
class ContactMerciView(TemplateView):
    """
    Après un message envoyé avec succès
    """
    template_name = "inscription/contact_merci.html"


# name="inscription_merci"
class InscriptionMerciView(TemplateView):
    """
    Après une inscription avec succès
    """
    template_name = "inscription/inscription_merci.html"
