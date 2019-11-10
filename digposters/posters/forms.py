from django import forms
from posters.models import Poster, CategoryModel

class UploadForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = ['eventName', 'description', 'group', 'location', 'date', 'time_start', 'time_end', 'poster', 'category_tag']

CHOICES=[('Social Event','Social Event'),
         ('Food Sale','Food Sale'),
         ('Activity','Activity'),
         ('Presentation','Presentation'),]

#class FilteredCategoryForm(forms.ModelForm):
class FilteredCategoryForm(forms.Form):
    #selected = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'Radio'}))
    selected = forms.CharField(label="Choose a category", widget=forms.RadioSelect(choices=CHOICES))
    '''
        class Meta:
        model = Poster
        fields = ['category_tag']

    '''
