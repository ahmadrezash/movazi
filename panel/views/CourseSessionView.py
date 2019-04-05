#Basic
from django.contrib.auth.models            import User
from django.shortcuts                      import redirect, render
from django.template.response              import TemplateResponse
from django.utils.text                     import slugify
#Model     
from panel.models.CategoryModels           import Category
from panel.models.Courses.CourseSessionModel      import CourseSession
from panel.models.Courses.CourseModel import Course
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
    c = Course.objects.filter(slug=course)[0]
    course_list = CourseSession.objects.filter(course=c)
    # .all().order_by('-pub_date')
    paginator = Paginator(course_list, 10)
    page = request.GET.get('page')
    course_list = paginator.get_page(page)
    # return render(request, 'test.html', {'a': course_list})
    # print('sdsdsfs')
    return render(request, 'ContentManage/CourseSessionTable.html', {'posts': course_list,'title':c.title,'slug':c.slug})


# create_course_session
def create_course_session(request,course):
    c = Course.objects.filter(slug=course)[0]
    saved = False
    if request.method == "POST":
        form = CourseSessionForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.author = request.user
            a.category = Category.objects.all()[0]
            a.slug = slugify(a.title,allow_unicode=True)
            a.course = c
            a.save()
            # return render(request, 'test.html', {'a':c })
            return redirect('all_course_session',course=c.slug)
        return render(request, 'test.html', {'a': form.errors})
    else:
        form = CourseSessionForm()
        # return render(request, 'test.html', {'a': c})
        return render(request, 'Forms/CourseSessionForm.html', {'form': form})



def update_course_session(request,course,session):
    c = Course.objects.filter(slug=course)[0]
    saved = False
    tmp = CourseSession.objects.filter(slug=session)[0]

    if request.method == "POST":
        form = CourseSessionForm(data=request.POST, files=request.FILES,instance = tmp)
        if form.is_valid():
            a = form.save(commit=False )
            a.course = c
            a.author = request.user
            a.category = Category.objects.all()[0]
            a.slug = slugify(a.title,allow_unicode=True)
            a.save()
            return redirect('all_course_session',course=c.slug)
        return render(request, 'test.html', {'a': 'ظاهرا مشکلی پیش آمده'})
    else:
        form = CourseSessionForm(instance=tmp)
        return render(request, 'Forms/CourseSessionForm.html', {'form': form})

def delete_course_session(request,course,session):
    c = Course.objects.filter(slug=course)[0]
    CourseSession.objects.filter(slug=session)[0].delete()
    return redirect('all_course_session',course=c.slug)
