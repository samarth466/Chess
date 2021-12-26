from django import forms

class JoinGameForm(forms.Form):
    code = forms.CharField(250,label="Enter a game code.",min_length=1)