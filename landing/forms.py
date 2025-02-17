from django import forms


class LandingForm(forms.Form):
    ebook_form_name = forms.CharField()
    ebook_email = forms.EmailField()
