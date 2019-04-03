from django.views.generic.edit import BaseFormView
from django.forms import ModelForm
from panel.models.Published.PublishedModel import  Published
from django.db import models

# import crispy_forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, Field
# from crispy_forms.bootstrap import (
    # PrependedText, PrependedAppendedText, FormActions)
# from crispy_forms.helper import FormHelper
# from crispy_forms.helper import FormHelper


class PublishedForm(ModelForm):
    # ModelForm.clea
    class Meta:
        model = Published
        fields = ['title','subtitle','subject','summery','full_text','publishing_date','image_index','image_cover','tags']
        labels = {
                    "title": "عنوان",
                    'subtitle':'زیرعنوان',
                    'subject':'موضوع',
                    'summery':'چکیده',
                    'full_text':'متن',
                    'publishing_date':'تاریخ انتشار',
                    'image_index':'تصویر شاخص',
                    'image_cover':'تصویر جلد',
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
