from django.urls import path

from main.apps import MainConfig
from rest_framework.routers import DefaultRouter

from main.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrievetAPIView, \
    LessonUpdateAPIView, \
    LessonDestroyAPIView, PaymentsListAPIView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView, create_payment, \
    retrieve_payment

app_name = MainConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
                  path('lesson/create', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/<int:pk>', LessonRetrievetAPIView.as_view(), name='lesson_get'),
                  path('lesson/update/<int:pk>', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson_delete'),

                  path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),

                  path('subscription/create', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
                  path('subscription/delete/<int:pk>', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),

                  path('create_payment/', create_payment, name='payment_create'),
                  path('retrieve_payment/', retrieve_payment, name='retrieve_create'),

              ] + router.urls
