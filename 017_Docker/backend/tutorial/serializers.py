from rest_framework import serializers
from .models import Tutorial

class TutorialSerializer(serializers.ModelSerializer):
    # abc = serializers.IntegerField(default=1)
    class Meta:
        model=Tutorial
        fields="__all__"

# class TutorialSerializer(serializers.Serializer):
#     id= serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     description = serializers.CharField()
    
#     def create(self, validated_data):
#         return Tutorial.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.description = validated_data.get('description',instance.description)
#         instance.save()
#         return instance
#     def validate(self,data):#?object level validation yapmak için override ediyoruz  
#         if data['title'] == data['description']:
#             raise serializers.ValidationError('Title and description must not be same')
#         return data
