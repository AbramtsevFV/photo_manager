from django.urls import path

from photo.views import PhotoViewSet, NameViewSet, PhotoGetIdViewSet, GetPhotoList

app_name = 'photo'

urlpatterns = [
    path('photos/list', GetPhotoList.as_view(), name='photos_list'),
    path('photos/', PhotoViewSet.as_view({'get': 'list', 'post': 'create'}), name='photos'),
    path('photo/<int:pk>/', PhotoGetIdViewSet.as_view({'get':'retrieve'})),
    path('name/', NameViewSet.as_view({'get': 'list', 'post': 'create'}), name='name'),
]