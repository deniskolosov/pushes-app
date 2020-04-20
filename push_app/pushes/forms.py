from django import forms
from django.forms.widgets import FileInput
from django.utils.safestring import mark_safe
from .models import Push


class PushForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Укажите заголовок'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'placeholder': 'Введите текст уведомления'}))
    push_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control custom-file-input',
                                                                'id': 'push-image-upload'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Укажите имя'}))
    send_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control',
                                                                    'type': 'date'}))

    class Meta:
        model = Push
        exclude = ['is_sent', 'times_sent', 'created_at']
