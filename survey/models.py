from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


questions = (
    ('text_field', 'Ответ текстом'),
    ('radio', 'Один вариант'),
    ('check_boxes', 'Выбор нескольких вариантов')
)


class Question(models.Model):
    text = models.TextField()
    type = models.CharField(
        choices=questions,
        verbose_name='Тип вопроса',
        max_length=20
    )

    def __str__(self):
        return self.text


class Choice(models.Model):
    text = models.TextField(verbose_name='Вариант ответа')
    questions = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        return self.text


class Survey(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    start_date = models.DateField(auto_now_add=True, verbose_name='Start date')
    end_date = models.DateField(verbose_name='End date')
    description = models.CharField(max_length=200, verbose_name='Description')
    question = models.ForeignKey(
        Question, blank=True, on_delete=models.CASCADE,
        related_name="surveys",
    )

    def __str__(self):
        return self.name


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users', default=0)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='survey', default='')
    many_choice = models.ManyToManyField(Choice, related_name='many_answer')
    one_choice = models.ForeignKey(Choice, null=True, on_delete=models.CASCADE, related_name='one_answer')
    text = models.TextField(null=True)

    def __str__(self):
        return self.text
