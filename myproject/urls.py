from django.contrib import admin
from django.urls import path
from blog.views import home, post_list,post_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('blog/', post_list),
    path('blog/<post_id>/', post_details),
]
