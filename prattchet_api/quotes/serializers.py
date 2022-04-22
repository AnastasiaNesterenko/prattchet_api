"""
Приложение quotes.
Сериализаторы для модели цитат из произведений Терри Пратчетта.
"""
from rest_framework import serializers

from .models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('quote', 'heroes_of_the_excerpt', 'book', 'book_author')
