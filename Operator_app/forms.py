from django import forms
from .models import Operator

class OperatorForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = ['personnel_code', 'first_name', 'last_name', 'contact_number', 'position', 'work_group', 'delivered_device', 'avatar']
        labels = {
            'personnel_code': 'کد پرسنلی',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'contact_number': 'شماره تماس',
            'position': 'سمت',
            'work_group': 'گروه کاری',
            'delivered_device': 'دستگاه تحویلی',
            'avatar': 'تصویر اپراتور',
        }
