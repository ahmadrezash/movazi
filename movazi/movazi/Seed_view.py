from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from panel.models.ArticleModels import Article
from panel.models.CategoryModels import Category
from django.core.paginator import Paginator
from django.shortcuts import render
# from 

def seeding(request):
    # a = Category()
    # a.name_english = "biology"
    # a.name_persian = 'زیست شناسی'
    # # a.create_date = 
    # # a.parent = 0
    # a.save()

    # a = Category()
    # a.name_english = "physics"
    # a.name_persian = 'فیزیک'
    # # a.parent = 0
    # a.save()

    a = Article()
    a.title =  'پست۳'
    a.subtitle = 'زیرتیتر'
    a.full_text = 'لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد. کتابهای زیادی در شصت و سه درصد گذشته، حال و آینده شناخت فراوان جامعه و متخصصان را می طلبد تا با نرم افزارها شناخت بیشتری را برای طراحان رایانه ای علی الخصوص طراحان خلاقی و فرهنگ پیشرو در زبان فارسی ایجاد کرد. در این صورت می توان امید داشت که تمام و دشواری موجود در ارائه راهکارها و شرایط سخت تایپ به پایان رسد و زمان مورد نیاز شامل حروفچینی دستاوردهای اصلی و جوابگوی سوالات پیوسته اهل دنیای موجود طراحی اساسا مورد استفاده قرار گیرد. لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد. کتابهای زیادی در شصت و سه درصد گذشته، حال و آینده شناخت فراوان جامعه و متخصصان را می طلبد تا با نرم افزارها شناخت بیشتری را برای طراحان رایانه ای علی الخصوص طراحان خلاقی و فرهنگ پیشرو در زبان فارسی ایجاد کرد. در این صورت می توان امید داشت که تمام و دشواری موجود در ارائه راهکارها و شرایط سخت تایپ به پایان رسد و زمان مورد نیاز شامل حروفچینی دستاوردهای اصلی و جوابگوی سوالات پیوسته اهل دنیای موجود طراحی اساسا مورد استفاده قرار گیرد. '
    a.save()
    # a = Category.objects.all()
    a.author = request.user
    a = Article.objects.all()
    return render(request, 'test.html', {'a': a})

def blog_main(request):
    t = TemplateResponse(request, 'blog/index.html', {})
    t.render()
    return HttpResponse(t)


def article_pagination(request):
    article_list = Article.objects.all()
    # paginator = Paginator(article_list, 10)
    # a = article_list
    # page = request.GET.get('page')
    # contacts = paginator.get_page(page)
    # return render(request, 'article_list.html', {'article_list': article_list})
    return render(request, 'blog/index.html', {'posts': article_list})

