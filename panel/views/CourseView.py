#Basic
from django.contrib.auth.models            import User
from django.shortcuts                      import redirect, render
from django.template.response              import TemplateResponse
from django.utils.text                     import slugify
#Model     
from panel.models.CategoryModels           import Category
from panel.models.Courses.CourseModel      import Course
#Form
from panel.forms.CourseForm.CourseMainForm import CourseMainForm
#Other
from django.core.paginator                 import Paginator
from jalali_date import datetime2jalali, date2jalali

def index(request):
    posts = Course.objects.order_by('pub_date')[:3]
    t = TemplateResponse(request, 'home.html', {'posts':posts})
    return HttpResponse(t)

def all_course(request):
    course_list = Course.objects.all().order_by('-pub_date')
    paginator = Paginator(course_list, 10)
    page = request.GET.get('page')
    course_list = paginator.get_page(page)
    # return render(request, 'test.html', {'a': course_list})
    # print('sdsdsfs')
    return render(request, 'ContentManage/CourseMainTable.html', {'posts': course_list,'content':"course"})


# create_course
def create_course(request):
    saved = False
    if request.method == "POST":
        form = CourseMainForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.author = request.user
            a.category = Category.objects.all()[0]
            a.slug = slugify(a.title,allow_unicode=True)
            a.save()
            return redirect('all_course')
            # return render(request, 'test.html', {'a':'مقاله با موفقست ثبت شد' })
        return render(request, 'test.html', {'a': form.errors})
    else:
        form = CourseMainForm()
        # jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d')
        # form.holding_date = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d')
        return render(request, 'Forms/CourseMainForm.html', {'form': form})



def update_course(request,slug):
    saved = False
    tmp = Course.objects.filter(slug=slug)[0]

    if request.method == "POST":
        form = CourseMainForm(data=request.POST, files=request.FILES,instance = tmp)
        if form.is_valid():
            a = form.save(commit=False )
            a.author = request.user
            a.category = Category.objects.all()[0]
            a.slug = slugify(a.title,allow_unicode=True)
            a.save()
            return redirect('all_course')
        return render(request, 'test.html', {'a': 'ظاهرا مشکلی پیش آمده'})
    else:
        form = CourseMainForm(instance=tmp)
        return render(request, 'Forms/CourseMainForm.html', {'form': form})

def delete_course(request,slug):
    Course.objects.filter(slug=slug)[0].delete()
    # print('resiiiiiid')
    return redirect('all_course')
    # return render(request, 'test.html', {'a': slug})
