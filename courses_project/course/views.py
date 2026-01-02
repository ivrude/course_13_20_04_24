from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CourseForm, CategoryForm
from .models import Course, Category, Bucket
from .filters import CourseFilter
from django.core.mail import send_mail



# Create your views here.

@login_required
def add_course_view(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()
            return redirect('course:list_courses')
    else:
        form = CourseForm()
    return render(request, 'course/add_course.html', {'form': form})



def list_courses_view(request):
    courses = Course.objects.all()
    course_filter = CourseFilter(request.GET, queryset=courses)
    courses = course_filter.qs
    return render(request, 'course/list_courses.html', {'courses': courses})


@login_required
def add_category_view(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course:list_categories')
    else:
        form = CategoryForm()
    return render(request, 'category/add_category.html', {'form': form})


def list_categories_view(request):
    categories = Category.objects.all()
    return render(request, 'category/list_categories.html', {'categories': categories})


def course_detail_view(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'course/course_detail.html', {'course': course})

@login_required
def add_to_busket(request, course_id):
    course = Course.objects.get(id=course_id)
    Bucket.objects.create(course=course, user=request.user)
    from_email = settings.EMAIL_HOST_USER
    message = f'Ви додали курс {course.title} в корзину'
    to_email = request.user.email
    send_mail(
        "Курс додано в корзину",
        message,
        from_email,
        [to_email],
        fail_silently=False,
    )
    messages.success(request, "Курс додано в корзину 🛒")
    return redirect("course:list_courses")

@login_required
def bucket_view(request):
    courses = Bucket.objects.filter(user=request.user).select_related("course")
    return render(request, 'course/bucket.html', {'courses': courses})

@login_required
def delete_bucket(request, course_id):
    Bucket.objects.filter(course_id=course_id, user=request.user).delete()
    return redirect('course:bucket')

@login_required
def buy_course(request, course_id):
    course = Course.objects.get(id=course_id)
    Bucket.objects.filter(course_id=course_id, user=request.user).update(status="W")
    from_email = settings.EMAIL_HOST_USER
    message = (f'Ваша квитанція на оплату {course.title} на суму {course.price}. Просимо оплатити за наступними'
               f'credetinals ..... та надіслати квитанцію на пошту {from_email}')
    to_email = request.user.email
    send_mail(
        "Квитанція на оплату",
        message,
        from_email,
        [to_email],
        fail_silently=False,
    )
    return redirect('course:bucket')