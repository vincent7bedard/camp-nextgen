from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(attrs={"class":"form-control g-brd-none g-brd-bottom g-brd-white g-brd-primary--focus g-color-white g-bg-transparent g-placeholder-gray-light-v5 rounded-0 g-py-13 g-px-0 mb-2", "placeholder":"Nom"}),
    )
    contact_email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class":"form-control g-brd-none g-brd-bottom g-brd-white g-brd-primary--focus g-color-white g-bg-transparent g-placeholder-gray-light-v5 rounded-0 g-py-13 g-px-0 mb-2", "placeholder":"Email"}),
    )
    email_content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={"class":"form-control g-brd-none g-brd-bottom g-brd-white g-brd-primary--focus g-color-white g-bg-transparent g-placeholder-gray-light-v5 g-resize-none rounded-0 g-py-13 g-px-0 mb-5","rows":"5", "placeholder":"Message"}),
    )


# Choix pour les "Select Fields"
POSITION_CHOIX = (
    ("QB", "QB"),
    ("RB", "RB"),
    ("WR", "WR"),
    ("TE", "TE"),
    ("OL", "OL"),
    ("DB", "DB"),
    ("LB", "LB"),
    ("DL", "DL"),
)
GRANDEUR_TSHIRT_CHOIX = (
    ("sm", "SM"),
    ("md", "MD"),
    ("lg", "LG"),
    ("xl", "XL"),
    ("xxl", "XXL"),
    ("xxxl", "XXXL"),
)

class InscriptionForm(forms.Form):
    parent_prenom = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(attrs={"class":"form-control form-control-md rounded-0", "placeholder":"Prénom Parent"}),
    )
    parent_nom = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(attrs={"class":"form-control form-control-md rounded-0", "placeholder":"Nom Parent"}),
    )
    enfant_prenom = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(attrs={"class":"form-control form-control-md rounded-0", "placeholder":"Prénom"}),
    )
    enfant_nom = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(attrs={"class":"form-control form-control-md rounded-0", "placeholder":"Nom"}),
    )
    enfant_ecole = forms.CharField(
        required=True,
        max_length=400,
        widget=forms.TextInput(attrs={"class":"form-control form-control-md rounded-0", "placeholder":"École"}),
    )
    enfant_email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class":"form-control form-control-md rounded-0", "placeholder":"Email"}),
    )
    enfant_age = forms.IntegerField(
        required=True,
        min_value=12,
        max_value=22,
        widget=forms.NumberInput(attrs={"class":"form-control form-control-md rounded-0", "placeholder":"Âge"})
    )
    enfant_position = forms.ChoiceField(
        required=True,
        choices=POSITION_CHOIX,
        widget=forms.Select(attrs={"class":"form-control rounded-0",})
    )
    enfant_grandeur_tshirt = forms.ChoiceField(
        required=True,
        choices=GRANDEUR_TSHIRT_CHOIX,
        widget=forms.Select(attrs={"class":"form-control rounded-0",})
    )
    numero_telephone = forms.RegexField(
        required=True,
        regex=r'^\d{3}-\d{3}-\d{4}$',
        error_messages = {"invalid": "Vous devez entrer votre numéro de téléphone dans le format XXX-XXX-XXXX. Exemple: 418-666-1234"},
        widget=forms.TextInput(attrs={"class":"form-control form-control-md rounded-0", "placeholder":"XXX-XXX-XXXX"}),
    )
    decharge = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={"class":"form-check-input mr-1",})
    )
