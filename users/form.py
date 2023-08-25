from django import forms
from .models import Medicine
from .models import Patient
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput, SelectDateWidget, ModelForm

from django.contrib.auth.forms import UserCreationForm
from .models import User, Analyse, surveillance, Laboratoire,VisiteReprise,Notes

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
from django import forms
from .models import DossierMedical

class DossierMedicalForm(forms.ModelForm):
    class Meta:
        model = DossierMedical
        fields = ['numero', 'patient']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-select mr-sm-8'}),
         }
from django import forms
from .models import info

class InfoForm(forms.ModelForm):
    class Meta:
        model = info
        fields = '__all__'
        widgets = {
            'numero': forms.Select(attrs={'class': 'form-select mr-sm-2'}),
         }
from django import forms
from .models import systematique

class SystematiqueForm(forms.ModelForm):
    analyses = forms.ModelMultipleChoiceField(
            queryset=Analyse.objects.all(),
            widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
            required=False
        )
    class Meta:
        model = systematique
        fields = '__all__'

#########PatientForm
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'date_of_birth', 'start_date', 'age', 'origin', 'company', 'address', 'job_position', 'family_status', 'department', 'photo','area', 'risk']
        widgets = {
            'area': forms.Select(attrs={'class': 'form-select mr-sm-2'}),
         }
###Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['N_lot','name', 'quantity',  'expiration_date', 'presentation', 'dosage']
        

    
# ambulance

from django import forms
from .models import AmbulanceItem ,AmbulanceMedicine

class AmbulanceItemForm(forms.ModelForm):
    class Meta:
        model = AmbulanceItem
        fields = ['name','quantity', 'purchase_date']
        


class AmbulanceMedicineForm(forms.ModelForm):
    class Meta:
        model = AmbulanceMedicine
        fields = ['N_lot','name', 'quantity', 'expiration_date', 'presentation', 'dosage']
        

################visite###########################            
from django import forms
from .models import VisiteMedicaleSpontanee
class VisiteMedicaleSpontaneeForm(forms.ModelForm):
    class Meta:
        model = VisiteMedicaleSpontanee
        fields = ['patient', 'visit_date', 'temperature', 'blood_pressure', 'oxygen_saturation', 'heart_rate', 'blood_glucose', 'symptoms', 'observations']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-select mr-sm-2'}),
         }
  #############OUT#########################
from django import forms
from .models import OutStockMedicine
class OutStockMedicineForm(forms.ModelForm):
    class Meta:
        model = OutStockMedicine
        fields = ['patient', 'medicine', 'date', 'quantity' , 'remark']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-select mr-sm-2'}),
            'medicine': forms.Select(attrs={'class': 'form-select mr-sm-2'})
        }  
  ###################CheckInHistory#########################      
from django import forms
from .models import CheckInHistory

class CheckInHistoryForm(forms.ModelForm):
    remark = forms.CharField(max_length=200, required=False)

    class Meta:
        model = CheckInHistory
        fields = ['file_pdf','other_file']  



class VisiteRepriseForm(forms.ModelForm):
    class Meta:
        model = VisiteReprise
        fields = ['choix', 'texte_certificat']
        widgets = {
            'choix': forms.RadioSelect(choices=VisiteReprise.CHOICES),

            'texte_certificat': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }





class SurveillanceForm(forms.ModelForm):
    class Meta:
        model = surveillance
        fields = ['date','taille','poids','T_A','A_V','pouls','Glycemie','Albumin','Glucose','Medecin_de_travail']

        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control','type': 'date','style': 'width: 600px'}),  # Utiliser un sélecteur de date
            'taille': forms.NumberInput(attrs={'class': 'form-control','step': '0.0001','style': 'width: 600px'}),  # Utiliser un champ numérique avec 4 décimales
            'poids': forms.NumberInput(attrs={'class': 'form-control','step': '0.0001','style': 'width: 600px'}),  # Utiliser un champ numérique avec 4 décimales
            'T_A': forms.NumberInput(attrs={'class': 'form-control','step': '0.0001','style': 'width: 600px'}),  # Utiliser un champ numérique avec 4 décimales
            'A_V': forms.NumberInput(attrs={'class': 'form-control','step': '0.0001','style': 'width: 600px'}),  # Utiliser un champ numérique avec 4 décimales
            'pouls': forms.NumberInput(attrs={'class': 'form-control','step': '0.0001','style': 'width: 600px'}),  # Utiliser un champ numérique avec 4 décimales
            'Glycemie': forms.NumberInput(attrs={'class': 'form-control','step': '0.0001','style': 'width: 600px'}),  # Utiliser un champ numérique avec 4 décimales
            'Albumin': forms.NumberInput(attrs={'class': 'form-control','step': '0.0001','style': 'width: 600px'}),  # Utiliser un champ numérique avec 4 décimales
            'Glucose': forms.NumberInput(attrs={'class': 'form-control','step': '0.0001','style': 'width: 600px'}),  # Utiliser un champ numérique avec 4 décimales
            'Medecin_de_travail': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nom du médecin de travail','style': 'width: 600px'}),
            # Utiliser un champ de texte avec un placeholder
        }

class NotesForm(ModelForm):
    heading = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder":"Enter Title"
    }))
    text = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
         "class": "form-control", "placeholder":"Enter Notes", "rows":"8"
    }))
    class Meta:
        model = Notes
        fields = ['heading', 'text']


class LaboratoireForm(forms.ModelForm):
    class Meta:
        model = Laboratoire
        fields = ['fichier']

 