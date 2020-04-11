from django import forms

from groupes.models import Groupe


class GroupeForm(forms.ModelForm):
    class Meta:
        model = Groupe
        fields = ('name', 'head', 'email', 'phone')