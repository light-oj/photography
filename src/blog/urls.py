from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from posts.forms import PostForm
from django.urls import path, include
from filebrowser.sites import site

from posts.views import (
    index, blog, contact, blogdetail,
    blog_create, blog_update, blog_delete)

#about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name='blog-list'),
    path('blog/<id>/', blogdetail, name='blog-detail'),
    path('create/', blog_create, name='blog-create'),
    path('blog/<id>/update/', blog_update, name='blog-update'),
    path('blog/<id>/delete/', blog_delete, name='blog-delete'),
    path('tinymce/', include('tinymce.urls')),
    path('admin/filebrowser/', site.urls),
    path('accounts/', include('allauth.urls')),
    path('contact/', contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )