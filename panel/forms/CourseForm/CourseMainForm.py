from django.views.generic.edit import BaseFormView
from django.forms import ModelForm
from panel.models.MultiMedia.PosterModel import Poster
from panel.models.Courses.CourseModel import Course


from django.db import models

from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime



class CourseMainForm(ModelForm):
    # ModelForm.clea
    class Meta:
        model = Course
        fields = ['title','subtitle','summery','speaker'
        ,'session','holding_loc','holding_date','audience'
        ,'scientific_level','prerequisite','table_of_content'
        ,'resources','image_index'
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
                    'image_index':'تصویر شاخص',
                    'tags':'تگ ها'
                }

    def __init__(self, *args, **kwargs):
        super(CourseMainForm, self).__init__(*args, **kwargs)
        self.fields['holding_date'] = JalaliDateField(
            label=('تاریخ برگزاری'),
            widget=AdminJalaliDateWidget # optional, for user default datepicker
        )
        # self.fields['holding_date'].widget.attrs.update({'class': 'jalali_date-date'})
        # you can added a "class" to this field for user your datepicker!
        # self.fields['holding_date'].widget.attrs.update({'class': 'jalali_date-date'})

        # self.fields['date_time'] = SplitJalaliDateTimeField(label=('date time'), 
        #     widget=AdminSplitJalaliDateTime # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
        # )

