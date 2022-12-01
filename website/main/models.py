from django.db import models


class Task(models.Model):
    number = models.CharField('Номер по порядку', max_length=10)
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    category = models.CharField('Категория', max_length=25)
    date_time = models.DateTimeField('Дата и время')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'