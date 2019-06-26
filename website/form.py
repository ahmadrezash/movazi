from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='نام')
    email = forms.EmailField(label='ایمیل')
    message = forms.CharField(widget=forms.Textarea, label='پیام')
    phone_number = forms.CharField(max_length=100, label='شماره تلفن')
    # labels = {
    #     "name": "نام    "
    # }
