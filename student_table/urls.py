from django.conf.urls import url
from student_table import  views
urlpatterns =[
    url(r'^group_table$', views.group_table,name='group_table'),
    url(r'^group_detail/(?P<group>[-\w+]+)', views.group_detail,name='group_detail'),
    url(r'^get_photo/(?P<image_url>.*)', views.get_photo,name='get_photo')
]