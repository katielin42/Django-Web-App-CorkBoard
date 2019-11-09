from django import forms
from posters.models import Poster

class UploadForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = ['eventName', 'description']