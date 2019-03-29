from django.views.generic.edit import BaseFormView
from django.forms import ModelForm
from panel.models.MultiMedia.PosterModel import Poster
from django.db import models

# import crispy_forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, Field
# from crispy_forms.bootstrap import (
    # PrependedText, PrependedAppendedText, FormActions)
# from crispy_forms.helper import FormHelper
# from crispy_forms.helper import FormHelper


class PosterForm(ModelForm):
    # ModelForm.clea
    class Meta:
        model = Poster
        fields = ['title','subtitle','discription','image','tags']
        labels = {
                    "title": "عنوان",
                    'subtitle':'زیرعنوان',
                    'discription':'توضیحات',
                    'image':'تصویر',
                    'tags':'تگ ها'
                }













        
        # fields = ['title','subtitle','image']
        #  widgets = {
        #     'form': forms.TextInput(attrs={'class': ''}),
        # }
        # error_messages = {
            # NON_FIELD_ERRORS: {
            #     'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            # }
        # }
