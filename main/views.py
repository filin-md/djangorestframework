from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework_simplejwt.views import TokenObtainPairView

from config.settings import STRIPE_SECRET_KEY
from main.models import Course, Lesson, Payments, Subscription
from main.paginators import MainPaginator
from main.permissions import IsOwnerOrStaff
from main.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer, SubscriptionSerializer, \
    MyTokenObtainPairSerializer


# stripe.api_key = STRIPE_SECRET_KEY


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsOwnerOrStaff]
    pagination_class = MainPaginator


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]
    pagination_class = MainPaginator


class LessonRetrievetAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['date', ]
    filterset_fields = ('course', 'lesson', 'method',)


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()


def create_payment():
    stripe.PaymentIntent.create(
        amount=2000,
        currency="pln",
        automatic_payment_methods={"enabled": True},
    )


def retrieve_payment():
    stripe.PaymentIntent.retrieve(
        "pi_1JDmWxJX9HHJ5bycpCPrP2t5",
    )

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer