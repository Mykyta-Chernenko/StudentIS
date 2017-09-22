from django.contrib import admin
from student_table.models import Student, Group

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

class StudentInline(admin.TabularInline):
    model  = Student
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [StudentInline,]