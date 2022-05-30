from django import forms
from .models import Ask 
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from edu.models import Year

class AskForm(forms.ModelForm, forms.Form):
    year = forms.ModelChoiceField(queryset=Year.objects.all(),label='الفرقة', required=True)
    name= forms.CharField(label="الاسم", required=True)
    message = forms.CharField(
        label="رسالتك", widget=forms.Textarea(), required=True)
    class Meta:
        model = Ask
        fields = ('name','year','message',)


class AnswerAskForm(forms.ModelForm, forms.Form):
    answer = forms.CharField(
        label="الاجابة", widget=forms.Textarea(), required=False)

    class Meta:
        model = Ask
        fields = ('answer','show',)