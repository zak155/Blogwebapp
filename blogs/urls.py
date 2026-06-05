from django.urls import URLPattern, include, path

from django.conf import settings

from blogs import views
urlpatterns=[
    path('<int:category_id>/',views.post_by_category,name='post_by_category'),
]