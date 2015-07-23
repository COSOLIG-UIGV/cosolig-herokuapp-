from rest_framework import serializers
from .models import Post,Miembros

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'url', 'titulo', 'contenido','fecha_evento','fecha_evento','banner_grande','lugar',)

class MiembrosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Miembros
        fields = ('id', 'url','cargo','nombre','apellido','perfil_json','correo','miembro_activo',)

