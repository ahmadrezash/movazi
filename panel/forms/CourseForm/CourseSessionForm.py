from django.views.generic.edit import BaseFormView
from django.forms import ModelForm
from panel.models.Courses.CourseSessionModel import CourseSession
from django.forms import ModelForm

from django.db import models

# from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
# from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

class CourseSessionForm(ModelForm):
    class Meta:
        model = CourseSession
        fields = ['title','subtitle','summery','speaker'
        ,'time','audience'
        ,'table_of_content'
        ,'resources','image_index'
        ,'tags']
        labels = {
                    "title": "عنوان",
                    'subtitle':'زیرعنوان',
                    'summery':'چکیده',
                    'speaker':'سخنران',
                    'audience':'مخاطبین',
                    'table_of_content':'فهرست',
                    'resources':'منبع مکتوب',
                    'file': 'فایل تصویری',
                    'image_index':'تصویر شاخص',
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
