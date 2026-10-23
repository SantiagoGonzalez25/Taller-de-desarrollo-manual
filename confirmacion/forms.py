from django import forms
class FormularioCedula(forms.Form):
    cedula = forms.CharField(max_length=15, label="Cédula")
    def clean_cedula(self):
        cedula = self.cleaned_data["cedula"].strip()
        if not cedula.isdigit():
            raise forms.ValidationError("La cédula debe contener solo números")
        return cedula
