from django.contrib import admin

from .models import Student,Teacher,Parent,ClassRoom,deliverRecord

class StudentAdmin(admin.ModelAdmin):
    list_display = ('stu_name','stu_perfer')
    list_filter = ('stu_cla',)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('tea_name','tea_intro')
    list_filter = ('tea_name',)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('par_name','par_sex')
    list_filter = ('par_name',)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('cla_name',)
    list_filter = ('cla_name',)
class DeliverRecord(admin.ModelAdmin):
    list_display = ('deliver_stu','deliver_par')
    list_filter = ('deliver_stu','deliver_par','deliver_choice')

admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Parent,ParentAdmin)
admin.site.register(ClassRoom,ClassRoomAdmin)
admin.site.register(deliverRecord,DeliverRecord)