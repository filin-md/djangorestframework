from django.urls import path

from main.apps import MainConfig
from rest_framework.routers import DefaultRouter

from main.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrievetAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = MainConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='cars')

urlpatterns = [
                  path('lesson/create', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/<int:pk>', LessonRetrievetAPIView.as_view(), name='lesson_get'),
                  path('lesson/update/<int:pk>', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson_delete'),

              ] + router.urls
