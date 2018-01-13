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
            #Avec le request.POST["blabla"]
            """
            contact_name = request.POST["contact_name"]
            contact_email = request.POST["contact_email"]
            email_subject = request.POST["email_subject"]
            email_content = request.POST["email_content"]
            """
            #Avec le form.cleaned_data["blabla"]
            contact_name = form.cleaned_data["contact_name"]
            contact_email = form.cleaned_data["contact_email"]
            #email_subject = form.cleaned_data["email_subject"]
            email_content = form.cleaned_data["email_content"]

            email_subject = "camp NextGen Contact"
            destinataire = ["vincent.bedard.9@ulaval.ca"]
            email_message = email_content + "\n\nFrom " + contact_name

            send_mail(email_subject, email_message, contact_email, destinataire)
            
            # redirect to a new URL:
            return redirect(reverse("inscription:contact_merci")) #est-ce qu'on doit mettre les guillemets ou non dans reverse() ?

    context = {"form": form}
    return render(request, "inscription/index.html", context)


# name="contact_merci"
class ContactMerciView(TemplateView):
    """
    Après un message envoyé avec succès
    """
    template_name = "inscription/contact_merci.html"


# name="inscription"
def inscription(request):
    """
    Page d'inscription
    """
    return render(request, "inscription/inscription.html")

# name="resultat"
class ResultatView(TemplateView):
    """
    Après une inscription avec succès
    """
    template_name = "inscription/resultat.html"





def form_test(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            #do something
            print("validation success")
            print("NAME: "+ form.cleaned_data["name"])
            print("EMAIL: "+ form.cleaned_data["email"])
            print("TEXT: "+ form.cleaned_data["text"])

    return render(request, "inscription/form_test.html", {"form": form})
