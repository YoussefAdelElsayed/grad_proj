from django import forms
from .models import Result,Student


class StudentForm(forms.ModelForm):
    sitting_number = forms.IntegerField(label='رقم الجلوس', help_text='اذا لم تتذكر رقم جلوسك تواصل معنا عبر الفيس بوك')
    
    class Meta:
        model = Student
        fields = ('sitting_number',)

    def clean_sitting_number(self):
        sitting_number = self.cleaned_data['sitting_number']
        if sitting_number==" ":
            raise forms.ValidationError('من فضلك ادخل رقم الجلوس')
        return sitting_number
