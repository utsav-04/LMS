from django.shortcuts import redirect,render
from app.models import categories,Course,Level


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
    context={
        'category':category,
        'level':level,
        'course':course,
    }
    return render(request,'Main/single_course.html',context)


def contact_us(request):
    return render(request,'Main/contact_us.html')


def about_us(request):
    return render(request,'Main/about_us.html')