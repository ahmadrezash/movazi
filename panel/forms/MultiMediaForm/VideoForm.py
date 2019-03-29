from django.views.generic.edit import BaseFormView
from django.forms import ModelForm
from panel.models.MultiMedia.VideoModel import Video
from django.db import models

# import crispy_forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, Field
# from crispy_forms.bootstrap import (
    # PrependedText, PrependedAppendedText, FormActions)
# from crispy_forms.helper import FormHelper
# from crispy_forms.helper import FormHelper
from django.contrib.admin import widgets                                       

class VideoForm(ModelForm):
    # ModelForm.clea
    class Meta:
        model = Video
        fields = ['title','subtitle','discription','time','file','tags']
        labels = {
                    "title": "عنوان",
                    'subtitle':'زیرعنوان',
                    'time':'زمان',
                    'discription':'توضیحات',
                    'file':'فایل( به دقیقه)',
                    'tags':'تگ ها'
                }


    def __init__(self, *args, **kwargs):
            super(VideoForm, self).__init__(*args, **kwargs)
            self.fields['time'].widget = widgets.AdminTimeWidget()











        
        # fields = ['title','subtitle','image']
        #  widgets = {
        #     'form': forms.TextInput(attrs={'class': ''}),
        # }
        # error_messages = {
            # NON_FIELD_ERRORS: {
            #     'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            # }
        # }
