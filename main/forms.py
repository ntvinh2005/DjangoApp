from django import forms

class CreateNewSub(forms.Form):
    name=forms.CharField(max_length=300, widget=forms.TextInput(attrs={'placeholder': 'Add title of paper here'}))
    learning=forms.BooleanField(required=False)
    working=forms.BooleanField(required=False)
    idea=forms.BooleanField(required=False)
    life=forms.BooleanField(required=False)