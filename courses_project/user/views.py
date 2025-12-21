from django.contrib.auth import login
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, CustomUserForm
from .models import CustomUser
from django.contrib import messages


# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                "Реєстрація успішна! Ласкаво просимо 🎉"
            )
            response = redirect("course:list_courses")

            response.set_cookie(
                key="user_picture",
                value="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_InUxO_6BhylxYbs67DY7-xF0TmEYPW4dQQ&s",
                max_age=480,
                httponly=False,
                samesite="Lax",
            )

            return response
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, error)
    form = RegistrationForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile_view(request):
    return render(request, "users/profile.html")


@login_required
def edit_profile_view(request):
    form = CustomUserForm(instance=request.user)
    if request.method == "POST":
        form = CustomUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("auth:profile")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, error)
    return render(request, "users/edit_profile.html", {"form": form})

def google_login(request):
    fastapi_login_url = "http://127.0.0.1:8001/login/google"
    return redirect(fastapi_login_url)

def login_from_fastapi(request):
    email = request.GET.get("email")
    name = request.GET.get("name")
    picture = request.GET.get("picture")
    sub = request.GET.get("sub")
    if not email:
        return redirect("auth:login")  # або HttpResponseForbidden
    user, created = CustomUser.objects.get_or_create(
        email=email,
        defaults={
            "full_name": name,
            "role": "ST",
            "password": "123",
            "is_active": True,
        }
    )
    messages.success(
        request,
        f"Ви увійшли як {user.full_name}🎉"
    )
    login(request, user)
    response = redirect("course:list_courses")
    if picture:
        response.set_cookie(
            key="user_picture",
            value=picture,
            max_age= 480,
            httponly=False,
            samesite="Lax",
        )

    return response



#    return redirect("course:list_courses")
#@login_required
#def password_reset_request(request):
#    if request.method == "POST":
#        password_reset_form = PasswordResetForm(request.POST)
#
#        if password_reset_form.is_valid():
#            email = password_reset_form.cleaned_data["email"]
#            users = User.objects.filter(Q(email=email))
#
#            if users.exists():
#                for user in users:
#                    context = {
#                        "email": user.email,
#                        "user": user,
#                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                        "token": default_token_generator.make_token(user),
#                        "protocol": "http",
#                        "domain": request.get_host(),
#                        "site_name": "Website",
#                    }
#
#                    message = render_to_string(
#                        "password/password_reset_email.txt",
#                        context
#                    )
#
#                    try:
#                        send_mail(
#                            subject="Password Reset Requested",
#                            message=message,
#                            from_email=settings.EMAIL_HOST_USER,
#                            recipient_list=[user.email],
#                            fail_silently=False,
#                        )
#                    except BadHeaderError:
#                        return HttpResponse("Invalid header found.")
#
#                return redirect("password_reset_done")
#
#    else:
#        password_reset_form = PasswordResetForm()
#
#    return render(
#        request,
#        "password/password_reset.html",
#        {"password_reset_form": password_reset_form},
#    )