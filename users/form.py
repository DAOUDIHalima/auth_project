from django import forms
from .models import Medicine
from .models import Patient
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput, SelectDateWidget, ModelForm

from django.contrib.auth.forms import UserCreationForm
from .models import User

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


 