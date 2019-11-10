from django import forms

CHOICES=[('Social Event','Social Event'),
         ('Food Sale','Food Sale'),
         ('Activity','Activity'),
         ('Presentation','Presentation'),]
class FilteredCategoryForm(forms.Form):
    #selected = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'Radio'}))
    #selected = forms.ChoiceField(label="Choose a category", widget=forms.RadioSelect(choices=CHOICES))
    selected = forms.ChoiceField(label="Choose a category", choices = CHOICES)