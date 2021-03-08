from django.db import models
from django.core.validators import MinLengthValidator

class Question(models.Model):
    question_text = models.CharField(
        max_length=265,
        help_text= 'Input your question',
        validators=[MinLengthValidator(1, 'Input 1 character and above')]
    )

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=256)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
        