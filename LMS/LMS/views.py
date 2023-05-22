from django.shortcuts import redirect,render
from app.models import categories,Course,Level
from django.template.loader import render_to_string
from django.http import JsonResponse


def BASE(request):
    return render(request,'base.html')


def HOME(request):
    category=categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status='PUBLISH').order_by('-id')

    context = {
        'category':category,
        'course': course,
    }
    return render(request,'Main/home.html',context)


def SINGLE_COURSE(request):
    category = categories.get_all_category(categories)
    level=Level.objects.all()
    course=Course.objects.all()
    FreeCourseCount =Course.objects.filter(price=0).count()
    PaidCourseCount=Course.objects.filter(price__gte=1).count()
    context={
        'category':category,
        'level':level,
        'course':course,
        'FreeCourseCount':FreeCourseCount,
        'PaidCourseCount':PaidCourseCount,
    }
    return render(request,'Main/single_course.html',context)


def filter_data(request):
    categories = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')


    if price == ['pricefree']:
        course = Course.objects.filter(price=0)
    elif price == ['pricepaid']:
        course = Course.objects.filter(price__gte=1)
    elif price == ['priceall']:
        course = Course.objects.all()
    elif categories:
       course = Course.objects.filter(category__id__in=categories).order_by('-id')
    elif level:
       course = Course.objects.filter(level__id__in = level).order_by('-id')
    else:
       course = Course.objects.all().order_by('-id')

    context={
        'course':course
    }

    t = render_to_string('ajax/course.html', context)

    return JsonResponse({'data': t})

def contact_us(request):
    return render(request,'Main/contact_us.html')


def about_us(request):
    return render(request,'Main/about_us.html')