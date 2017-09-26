from  django.conf.urls import url

from . import views
urlpatterns=[
    url(r'^index/$',views.index,name='index'),
    url(r'^teachers/$', views.view_teacher,name='view_teacher'),
    url(r'^about/$',views.view_about,name='view_about'),
    url(r'^admissions/$',views.view_admissions,name='view_admissions'),
    url(r'^404/$',views.view_404,name='view_404'),
    url(r'^contact/$',views.view_contact,name='view_contact'),
    url(r'^view_register/$',views.view_register,name='view_register'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.view_login,name='view_login'),
    url(r'^scene_pick_up/$',views.scene_pick_up,name='scene_pick_up'),
    url(r'logout/$',views.view_logout,name='view_logout'),
    url(r'^tryLogin/$',views.loginAuth,name='try_login'),
    url(r'^updateinfo/$',views.update_info,name='update_info'),
    url(r'^afterLogin/$',views.view_afterLogin,name='view_afterLogin'),
    url(r'^classroomsg/(?P<class_id>[0-9]+)$',views.view_class_room_single,name='view_classroom_single'),
    url(r'^stusg/(?P<stu_id>[0-9]+)$', views.view_stu_single, name='view_stu_single'),
    url(r'^parent/(?P<par_id>[0-9]+)$', views.view_parent, name='view_parent'),
    url(r'^afterLogin/action_take/(?P<stu_id>[0-9]+)(?P<par_id>[0-9]+)$',views.take_to,name='take_to'),
    url(r'^afterLogin/action_pick/(?P<stu_id>[0-9]+)(?P<par_id>[0-9]+)$',views.pick_up,name='pick_up')
]