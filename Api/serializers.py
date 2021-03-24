from Avalancheutfpr.models import *
from Blog.models import *
from rest_framework import serializers

class EventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = eventos
        fields = (
            'id',
            'name',
            'previa',
            'descricao',
            'image',
            'data',
            'pub_date',
            'Status',
        )


class ModalidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = modalidades
        fields = (
            'id',
            'name',
            'previa',
            'descricao',
            'image',
            'data',
            'pub_date',
            'Status',
        )


class ModalidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = modalidades
        fields = (
            'id',
            'name',
            'previa',
            'descricao',
            'image',
            'data',
            'pub_date',
            'Status',
        )

class CampanhasSerializer(serializers.ModelSerializer):
    class Meta:
        model = campanhas
        fields = (
            'id',
            'name',
            'previa',
            'descricao',
            'image',
            'data',
            'pub_date',
            'Status',
        )


class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = games
        fields = (
            'id',
            'name',
            'previa',
            'descricao',
            'image',
            'data',
            'pub_date',
            'Status',
        )


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = posts
        fields = (
            'id',
            'name',
            'previa',
            'conteudo',
            'image',
            'pub_date',
        )