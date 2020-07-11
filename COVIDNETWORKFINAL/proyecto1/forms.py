from django import forms

class FormularioCovid(forms.ModelForm):
    class Meta:
        model = Covid
        fields = '__all__'
        widget = {'fecha de nacimiento': forms.DateInput(attrs={'type':'date'})}