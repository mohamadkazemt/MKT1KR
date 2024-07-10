from django import forms
from .models import Machine

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['code', 'name', 'type', 'is_active']
        labels = {
            'code': 'کد دستگاه',
            'name': 'نام دستگاه',
            'type': 'نوع دستگاه',
            'is_active': 'فعال',
        }
