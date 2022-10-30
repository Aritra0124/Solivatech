from rest_framework import serializers
from .models import Dog, Breed


class BreedSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=250)
    # size = serializers.CharField()
    # friendliness = serializers.IntegerField()
    # trainability = serializers.IntegerField()
    # sheddingamount = serializers.IntegerField()
    # exerciseneeds = serializers.IntegerField()

    class Meta:
        model = Breed
        fields = ('__all__')


class DogSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=250)
    # age = serializers.IntegerField()
    # breed = serializers.SlugRelatedField()
    # gender = serializers.CharField(max_length=250)
    # color = serializers.CharField(max_length=250)
    # favoritefood = serializers.CharField(max_length=250)
    # favoritetoy = serializers.CharField(max_length=250)

    class Meta:
        model = Dog
        fields = ('__all__')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['breed'] = BreedSerializer(instance.breed).data
        return response
