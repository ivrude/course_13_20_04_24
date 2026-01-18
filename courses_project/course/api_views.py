from django.contrib.auth import login
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Bucket
from .serializer import CourseSerializer, BucketSerializer
from courses_project.secret import oauth


from user.models import CustomUser


class CourseListAPI(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class BucketListAPI(generics.ListAPIView):
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer


class CourseCreateAPI(generics.CreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class GoogleLoginView(APIView):
    def get(self, request):
        redirect_uri = request.build_absolute_uri(
            '/api/auth/google/callback/'
        )
        return oauth.google.authorize_redirect(request, redirect_uri)

class GoogleCallbackView(APIView):
    def get(self, request):
        token = oauth.google.authorize_access_token(request)
        resp = oauth.google.get(
            "https://openidconnect.googleapis.com/v1/userinfo",  # повний URL
            token=token
        )
        user_info = resp.json()

        email = user_info['email']
        name = user_info.get('name', '')
        picture = user_info.get('picture', '')
        sub = user_info.get('sub')

        user, created = CustomUser.objects.get_or_create(
            email=email,
            defaults={
                'username': email,
                'first_name': name,
            }
        )

        login(request, user)
        response = redirect("course:list_courses")
        if picture:
            response.set_cookie(
                key="user_picture",
                value=picture,
                max_age=480,
                httponly=False,
                samesite="Lax",
            )

        return response

