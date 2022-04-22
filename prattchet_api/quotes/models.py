"""
Приложение quotes.
Модель для цитат из произведений Терри Пратчетта.
"""
from django.db import models


class Quote(models.Model):
    quote = models.TextField()
    heroes_of_the_excerpt = models.TextField()
    book = models.TextField(max_length=50)
    book_author = models.TextField()

    def __str__(self):
        return self.quote
