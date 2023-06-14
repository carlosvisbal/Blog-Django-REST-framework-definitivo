from apps.blog.models import (Etiqueta, Categoria, Entrada, Comentario, CategoriaEntrada, MeGustaEntrada, MeGustaComentario, EtiquetaEntrada)
from apps.users.models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Django REST Framework
from rest_framework import serializers # type: ignore




class EtiquetaSerializer(serializers.ModelSerializer):

    nombre = serializers.CharField(min_length=8, max_length=50)
    class Meta:
        model = Etiqueta
        fields = '__all__'
        read_only_fields = ['created', 'updated', 'activo']


class CategoriaSerializer(serializers.ModelSerializer):

    nombre = serializers.CharField(min_length=8, max_length=50)
    class Meta:
        model = Categoria
        fields = '__all__'
        read_only_fields = ['created', 'updated', 'activo']


class CategoriaEntradaSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoriaEntrada
        fields = '__all__'
        read_only_fields = ['created', 'updated', 'activo']


class MeGustaEntradaSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeGustaEntrada
        fields = '__all__'
        read_only_fields = ['created', 'updated', 'activo']


class MeGustaComentarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeGustaComentario
        fields = '__all__'
        read_only_fields = ['created', 'updated', 'activo']


class ComentarioSerializer(serializers.ModelSerializer):

    megustas = MeGustaComentarioSerializer(many=True, read_only=True)
    text = serializers.CharField(min_length=8, max_length=500)

    class Meta:
        model = Comentario
        fields = '__all__'
        read_only_fields = ['created', 'updated', 'activo']


class EntradaSerializer(serializers.ModelSerializer):
    etiquetas = serializers.PrimaryKeyRelatedField(queryset=Etiqueta.objects.all(), many=True,  required=False)
    categorias = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), many=True,  required=False)

    comentarios = serializers.SerializerMethodField()

    megustasentradas = serializers.SerializerMethodField()

    class Meta:
        model = Entrada
        fields = '__all__'
        read_only_fields = ['created', 'updated', 'activo']

    def create(self, validated_data):
        etiquetas = validated_data.pop('etiquetas', [])
        categorias = validated_data.pop('categorias', [])
        entrada = super().create(validated_data)

        for etiqueta in etiquetas:
            EtiquetaEntrada.objects.create(entrada=entrada, etiqueta=etiqueta)

        for categoria in categorias:
            CategoriaEntrada.objects.create(entrada=entrada, categoria=categoria)

        return entrada
    

    def get_comentarios(self, entrada):
        comentarios = Comentario.objects.filter(entrada=entrada)
        comentarios_serializer = ComentarioSerializer(comentarios, many=True, context=self.context)

        # Agrupar comentarios con sus MeGustaComentario
        comentarios_data = comentarios_serializer.data
        for comentario_data in comentarios_data:
            comentario_id = comentario_data['id']
            megusta_comentarios = MeGustaComentario.objects.filter(comentario_id=comentario_id)
            megusta_comentarios_serializer = MeGustaComentarioSerializer(megusta_comentarios, many=True)
            comentario_data['megusta_comentarios'] = megusta_comentarios_serializer.data

        return comentarios_data
    
    def get_megustasentradas(self, entrada):
        megustasentradas = MeGustaEntrada.objects.filter(entrada=entrada)
        megustasentradas_serializer = MeGustaEntradaSerializer(megustasentradas, many=True, context=self.context)
        megustasentradas_data = megustasentradas_serializer.data
        return megustasentradas_data




class EtiquetaEntradaSerializer(serializers.ModelSerializer):

    class Meta:
        model = EtiquetaEntrada
        fields = '__all__'
        read_only_fields = ['created', 'updated', 'activo']

