from rest_framework import serializers

from main.models import Course, Lesson, Payments, Subscription
from main.validators import validator_links


class LessonSerializer(serializers.ModelSerializer):
    link = serializers.URLField(validators=[validator_links])
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)
    lesson_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'