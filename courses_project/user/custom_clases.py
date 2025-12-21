from django.contrib.auth.views import LoginView
from django.contrib import messages

class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        response.set_cookie(
            key="user_picture",
            value="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_InUxO_6BhylxYbs67DY7-xF0TmEYPW4dQQ&s",
            max_age=480,
            httponly=False,
            samesite="Lax",
        )
        messages.success(
            self.request,
            "Вхід успішний! Ласкаво просимо 🎉"
        )
        return response