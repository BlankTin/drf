from rest_framework import serializers
from article.models import Article
# class ArticleListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(allow_blank=True,max_length=100)
#     body = serializers.CharField(allow_blank=True)
#     created = serializers.DateTimeField()
#     updated = serializers.DateTimeField

class ArticleListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = [
                'id',
                'title',
                'body',
                'created'
            ]

class ArticleDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = '_all_'
