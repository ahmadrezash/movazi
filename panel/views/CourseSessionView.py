#Basic
from django.contrib.auth.models            import User
from django.shortcuts                      import redirect, render
from django.template.response              import TemplateResponse
from django.utils.text                     import slugify
#Model     
from panel.models.CategoryModels           import Category
from panel.models.Courses.CourseSessionModel      import CourseSession
#Form
from panel.forms.CourseForm.CourseSessionForm import CourseSessionForm
#Other
from django.core.paginator                 import Paginator

def index(request):
    posts = CourseSession.objects.order_by('pub_date')[:3]
    t = TemplateResponse(request, 'home.html', {'posts':posts})
    t.render()
    return HttpResponse(t)

def all_course_session(request,course):
    course_list = CourseSession.objects.all().order_by('-pub_date')
    paginator = Paginator(course_list, 10)
    page = request.GET.get('page')
    course_list = paginator.get_page(page)
    # return render(request, 'test.html', {'a': course_list})
    # print('sdsdsfs')
    return render(request, 'ContentManage/CourseMainTable.html', {'posts': course_list,'content':"course"})


# create_course_session
def create_course_session(request,course):
    saved = False
    if request.method == "POST":
        form = CourseSessionForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.author = request.user
            a.category = Category.objects.all()[0]
            a.slug = slugify(a.title,allow_unicode=True)
            a.save()
            return redirect('all_course_session')
            # return render(request, 'test.html', {'a':'مقاله با موفقست ثبت شد' })
        return render(request, 'test.html', {'a': form.errors})
    else:
        form = CourseSessionForm()
        return render(request, 'Forms/CourseSessionForm.html', {'form': form})



def update_course_session(request,course,slug):
    saved = False
    tmp = CourseSession.objects.filter(slug=slug)[0]

    if request.method == "POST":
        form = CourseSessionForm(data=request.POST, files=request.FILES,instance = tmp)
        if form.is_valid():
            a = form.save(commit=False )
            a.author = request.user
            a.category = Category.objects.all()[0]
            a.slug = slugify(a.title,allow_unicode=True)
            a.save()
            return redirect('all_course_session')
        return render(request, 'test.html', {'a': 'ظاهرا مشکلی پیش آمده'})
    else:
        form = CourseSessionForm(instance=tmp)
        return render(request, 'Forms/CourseSessionForm.html', {'form': form})

def delete_course_session(request,course,slug):
    CourseSession.objects.filter(slug=slug)[0].delete()
    # print('resiiiiiid')
    return redirect('all_course_session')
    # return render(request, 'test.html', {'a': slug})
