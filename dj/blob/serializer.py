from rest_framework import serializers
class PostSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'text']
