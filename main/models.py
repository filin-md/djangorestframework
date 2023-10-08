from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='main/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='main/', verbose_name='превью', **NULLABLE)
    link = models.URLField(verbose_name='ссылка', **NULLABLE)