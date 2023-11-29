from datetime import datetime

from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='main/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE)
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='main/', verbose_name='превью', **NULLABLE)
    link = models.URLField(verbose_name='ссылка', **NULLABLE)


class Payments(models.Model):
    PAYMENT_METHOD = [
        ('cash', 'Наличные'),
        ('card', 'Перевод'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='пользователь')
    date = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE)
    amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    method = models.CharField(max_length=4, choices=PAYMENT_METHOD, verbose_name='метод оплаты')


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='курс')
