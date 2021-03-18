from django.db import models

class Question(models.Model):
    text=models.CharField(max_length=300)
    file=models.FileField(null=True, blank=True)
    pub_date=models.DateTimeField(help_text='Release Date')

    def __str__(self):
        return self.text

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    text=models.CharField(max_length=300)
    vote=models.IntegerField(default=0)

    def __str__(self):
        return self.text
