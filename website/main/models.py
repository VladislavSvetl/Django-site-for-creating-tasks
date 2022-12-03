from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    category = models.CharField('Категория', max_length=25)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Comment(models.Model):
    username = models.CharField('Имя', max_length=30)
    text = models.TextField('Текст')

    def __str__(self):
        return self.username
