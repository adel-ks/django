from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('blog/', post_list, name = 'list_of_posts'),
    path('blog/update_post/<post_id>/',update_post, name = 'update_post'),
    path('blog/create_post/', create_post),
    path('blog/delete_post/<post_id>/', delete_post, name = 'delete_post'),
    path('blog/<post_id>/', post_details, name='post_details'),
]
