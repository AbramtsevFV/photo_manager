from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Photo, UserName
from .serializers import PhotoSerializer, UserNameSerializer


class GetPhotoList(APIView):
    """Список фотографий пользователя"""
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        username = self.request.user
        user_id = User.objects.get(username=username).id
        usernames = [photo.photo.url for photo in Photo.objects.filter(user_id=user_id)]
        print(usernames)
        return Response(usernames)


class PhotoViewSet(ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticated,)

    def build_filter(self):
        """Метод возвращает словарь с фильтрами"""
        username = self.request.user
        user_id = User.objects.get(username=username).id
        filters = {'user_id': user_id}

        """Получаем query_params и строим по ним фильтр"""
        data = self.request.query_params
        if data.get('date', None):
            filters['date_load'] = data.get('date')
        if data.get('name', None):
            filters['names_of_people__name'] = data.get('name')
        if data.get('geo_location', None):
            filters['geo_location'] = data.get('geo_location')
        return filters

    def get_queryset(self):
        filters = self.build_filter()
        # Photo.objects.filter(names_of_people__name=)
        return Photo.objects.filter(**filters)


class PhotoGetIdViewSet(ReadOnlyModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticated,)


class NameViewSet(ModelViewSet):
    serializer_class = UserNameSerializer
    queryset = UserName.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        data = self.request.query_params
        if data.get('name', None):
            return UserName.objects.filter(name__icontains=data['name'])

        return self.queryset
