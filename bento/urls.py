from django.urls import url
from bento import views


urlpatterns = [
    re_path(r'^image-upload/$', views.image_upload, name='bento-image-import'),
    re_path(r'^text-upload/$', views.text_upload, name='bento-text-import'),
    re_path(r'^text-edit/(?P<name>[\w-]+)/$', views.text_edit, name='bento-text-edit'),
    urre_path(r'^image-edit/(?P<name>[\w-]+)/$', views.image_edit, name='bento-image-edit'),
]
