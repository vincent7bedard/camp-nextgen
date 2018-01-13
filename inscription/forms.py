from django import forms
#from .models import Parent, Enfant


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.Form):
    contact_name = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(attrs={"class":"form-control g-brd-none g-brd-bottom g-brd-white g-brd-primary--focus g-color-white g-bg-transparent g-placeholder-gray-light-v5 rounded-0 g-py-13 g-px-0 mb-2","placeholder":"Nom"}),
    )
    contact_email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class":"form-control g-brd-none g-brd-bottom g-brd-white g-brd-primary--focus g-color-white g-bg-transparent g-placeholder-gray-light-v5 rounded-0 g-py-13 g-px-0 mb-2","placeholder":"Email"}),
    )
    # email_subject = forms.CharField(required=True)
    email_content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={"class":"form-control g-brd-none g-brd-bottom g-brd-white g-brd-primary--focus g-color-white g-bg-transparent g-placeholder-gray-light-v5 g-resize-none rounded-0 g-py-13 g-px-0 mb-5","rows":"5","placeholder":"Message"}),
    )

"""
class ParentForm(forms.ModelForm):
    class Meta():
        model = Parent
        #fields = ("prenom_parent", "nom_parent")

        widget = {
            "prenom_parent": forms.TextInput(attrs={"class": "text-input-class"}),
            "nom_parent": forms.TextInput(attrs={"class": "blabla okok nom classe"}),
        }



POSITIONS_FOOTBALL = (
    "QB",
    "Running back",
    "Receiver" "Offensive Line",
    "Defensive line",
    "Linebacker",
    "Defensive Back")

class EnfantForm(forms.ModelForm):
    class Meta():
        model = Enfant
        fields = ("prenom_enfant", "nom_enfant", "ecole", "position_football", "age", "adresse_email")

        widget = {
            "prenom_enfant": forms.TextInput(attrs={"class": "text-input-class"}),
            "nom_enfant": forms.TextInput(attrs={"class": "blabla okok nom classe"}),
            "ecole": forms.TextInput(attrs={"class": "blabla okok nom classe"}),
            "position_football": forms.Select(
                choices=POSITIONS_FOOTBALL,
                attrs={"class": "blabla okok nom classe"},
                ),
            "age": forms.NumberInput(attrs={"class": "blabla okok nom classe"}),
            "adresse_email": forms.EmailInput(attrs={"class": "blabla okok nom classe"}),
        }
"""
