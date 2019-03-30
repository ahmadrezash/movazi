from django.views.generic.edit import BaseFormView
from django.forms import ModelForm
from panel.models.MultiMedia.PosterModel import Poster
from panel.models.Courses.CourseModel import Course

from django.db import models

# import crispy_forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, Field
# from crispy_forms.bootstrap import (
    # PrependedText, PrependedAppendedText, FormActions)
# from crispy_forms.helper import FormHelper
# from crispy_forms.helper import FormHelper


class CourseMainForm(ModelForm):
    # ModelForm.clea
    class Meta:
        model = Course
        fields = ['title','subtitle','summery','speaker'
        ,'session','holding_loc','holding_date','audience'
        ,'scientific_level','prerequisite','table_of_content'
        ,'resources','category','image_index'
        ,'tags']
        labels = {
                    "title": "عنوان",
                    'subtitle':'زیرعنوان',
                    'summery':'چکیده',
                    'speaker':'سخنران',
                    'session':'تعداد جلسات',
                    'holding_loc':'مکان برگزاری',
                    'holding_date':'زمان برگزاری',
                    'audience':'مخاطبین',
                    'scientific_level':'سطح علمی',
                    'prerequisite':'پیش‌نیاز علمی',
                    'table_of_content':'فهرست',
                    'resources':'منبع مکتوب',
                    'category':'دسته بندی',
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
