from django import forms
from UserModel_1184077.models import User
from captcha.fields import CaptchaField

PILIHAN = [
		('BUMN', 'PEGAWAWI'),
		('SWASTA', 'KARIYAWAN'),
]

class NewUserForm(forms.ModelForm):
	captcha = CaptchaField()
	institusi = forms.ChoiceField(choices=PILIHAN)
	class Meta:
		model = User
		fields = '__all__'
		