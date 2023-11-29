from django.contrib import admin

from main.models import Course, Subscription
from users.models import User


# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'course',)



