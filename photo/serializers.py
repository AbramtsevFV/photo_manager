from django.contrib.auth.models import User
from rest_framework import serializers

from photo.models import UserName, Photo




class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserName
        fields = "__all__"

    def create(self, validated_data):
        name, _ = UserName.objects.get_or_create(**validated_data)
        return name


class PhotoSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    date_load = serializers.DateField(read_only=True)
    geo_location = serializers.CharField(read_only=True)

    class Meta:
        model = Photo
        fields = ('id', 'user', 'photo', 'geo_location', 'description', 'names_of_people', 'date_load')

    def create(self, validated_data):
        username = self.context.get('request').user
        user_id = User.objects.get(username=username).id
        ph = Photo.objects.create(user_id=user_id,
                                  photo=validated_data['photo'],
                                  geo_location=validated_data['geo_location'],
                                  description=validated_data['description'],
                                  )
        user_data = validated_data.get('names_of_people', None)
        if user_data:
            for i in user_data:
                ph.names_of_people.add(i)
        return ph


class PhotoidSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserName
        fields = "__all__"
