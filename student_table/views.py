from annoying.functions import get_object_or_None
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404

from StudentIS import settings
from student_table.models import Group, Student




def group_table(request):
    groups = Group.objects.all().order_by('head')
    return render(request,'student_table/group_table.html',context={'groups': groups},content_type="text/html")

def group_detail(request,group):
    group = get_object_or_404(Group,name=group)
    students = group.student_set.all()
    paginator = Paginator(students, 5)

    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    return render(request,'student_table/group_detail.html', {'students':students},content_type="text/html")

def get_photo(request,image_url):
    url = f'{settings.MEDIA_ROOT}/{image_url}'
    image = open(url,'rb').read()
    return HttpResponse(image,content_type='image/jpg')