from django.db import models

# Create your models h





class Task(models.Model):
    title = models.CharField('Какоето название', max_length=51)
    task = models.TextField('Какоето Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'