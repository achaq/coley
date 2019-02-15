from django import forms
from django.contrib.auth.models import User
from .models import compound



class CompoundCreateForm(forms.ModelForm):
    class Meta:
        model = compound
        fields=['formula_name','extensibility','stability','ductibility','toughness','strenght','pvc_k','stabilizer_type','stabilizer','chalk','impact_modifier']
    def __init__(self, *args, **kwargs):
        super(CompoundCreateForm, self).__init__(*args, **kwargs)
        self.fields['extensibility'].required = False
        self.fields['stability'].required = False
        self.fields['ductibility'].required = False
        self.fields['toughness'].required = False