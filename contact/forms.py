from django import forms


class MailForm(forms.Form):
    name = forms.CharField(label="Name", max_length=125)
    subject = forms.CharField(label="Subject", max_length=125)
    email = forms.EmailField(label="Email")
    text = forms.CharField(widget=forms.Textarea)

