from django.contrib import admin
from django.urls import path
from blog.views import home, post_list,post_details,create_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('blog/', post_list),
    path('blog/create_post/', create_post),
    path('blog/<post_id>/', post_details),
]
