from django.shortcuts import render,render_to_response
from .models import *
from django.http import HttpResponse
from datetime import datetime
from . import models

import json


def index(request):
    return render(request,'index.html')

def view_admissions(request):
    return render(request,'admissions.html')

def view_teacher(request):
    teachers=models.Teacher.objects.all()
    return render(request,'teachers.html',{'teachers':teachers})

def view_about(request):
    return render(request,'about.html')

def view_404(request):
    return render(request,'404.html')

def view_contact(request):
    return render(request,'contact.html')

def register(request):
    user_state = request.POST.get('register_state', '教师')
    user_nick = request.POST.get('user_nick', '风吹屁屁凉')
    pas = request.POST.get('pas', 'wozhua00')
    user_name = request.POST.get('user_name', '江明泽')
    user_sex = request.POST.get('user_sex','Male')
    user_tel = request.POST.get('user_tel', '110')
    parent = Parent.objects.filter(par_nickname=user_nick)
    teacher = Teacher.objects.filter(tea_nickname=user_nick)
    if(parent or teacher):
        return HttpResponse('用户名已被注册')
    if(user_state == '家长'):
        user = Parent.objects.create(par_nickname=user_nick,par_password=pas,par_sex=user_sex,par_name=user_name,par_tel=user_tel)
        user.save()
        return render(request,'login.html')
    elif(user_state == '教师'):
        tea = Teacher.objects.create(tea_nickname=user_nick,tea_pas=pas,tea_sex=user_sex,tea_name=user_name,tea_tel=user_tel)
        tea.save()
        return render(request,'login.html')
    else:
        return HttpResponse('传递数据出错，请检查网络')


def view_login(request):
    return render(request,'login.html')

def view_register(request):
    return render(request,'register.html')

def view_logout(request):
    pass
def login(request):
        user = request.POST.get('user','风吹屁屁凉')
        pas = request.POST.get('pas','wozhua00')
        loginState = request.POST.get('loginState','教师')
        print(loginState)
        if loginState == '教师':
            tea_user = Teacher.objects.filter(tea_nickname__exact = user,tea_pas__exact= pas)
            reco_list = []
            if tea_user:
                for classroom in ClassRoom.objects.filter(cla_tea=tea_user):
                #for classroom in tea_user.cla_tea.all():
                    for student in classroom.syu_cla_set.all():
                        for record in student.stu_deliver_set.all():
                            reco_list.append(record)
                            # stu_list.append(reco_list)
                #跳转到登陆后界面
                request.session['user'] = user
                response = render(request,'afterLogin.html',{'user':tea_user[0],'state':'tea','reco_list':reco_list})
                return response
            else:
                return HttpResponse('登录失败，检查用户名密码')

        elif loginState == '家长':
            par_user = Parent.objects.filter(par_nickname__exact=user, par_password__exact=pas)
            if par_user:
                # 跳转到登陆后界面
                request.session['user'] = user
                response = render(request, 'afterLogin.html',{'user':par_user[0],'state':'par'})
                # response.set_cookie('username', user, 3600)
                return response
            else:
                return HttpResponse('登录失败，检查用户名密码')
        else:
            return HttpResponse('传递数据出错，请检查网络')

def update_info(request):
    user_id = request.POST.get('user_id')
    user_nickname = request.POST.get('user_nickname')
    user_name = request.POST.get('user_name')
    user_sex = request.POST.get('user_sex')
    user_age = request.POST.get('user_age')
    user_tel = request.POST.get('user_tel')
    user_flag = request.POST.get('user_flag')
    if(user_flag == 'par'):
        parent = models.Parent.objects.get(pk=user_id)
        parent.par_nickname = user_nickname
        parent.par_name = user_name
        parent.par_sex = user_sex
        parent.par_age = user_age
        parent.par_tel =user_tel
        parent.save()
        return render(request, 'afterLogin.html', {'user': parent, 'state': user_flag})
    elif(user_flag == 'tea'):
        teacher = models.Teacher.objects.get(pk=user_id)
        teacher.tea_nickname = user_nickname
        teacher.tea_name = user_name
        teacher.tea_sex = user_sex
        teacher.tea_age = user_age
        teacher.tea_tel =user_tel
        teacher.save()
        return render(request,'afterLogin.html',{'user':teacher,'state':user_flag})

def view_afterLogin(request):
    return render(request,'afterLogin.html')

def view_class_room_single(request,class_id):
    classroom = models.ClassRoom.objects.get(pk=class_id)
    return render(request,'classroom.html',{'classroom':classroom})

def view_stu_single(request,stu_id):
    student = models.Student.objects.get(pk=stu_id)
    stu_cla = ClassRoom.objects.filter(syu_cla_set__stu_id__exact=stu_id)
    stu_par = Parent.objects.filter(stu_par_set__stu_id=stu_id)
    return render(request,'stusg.html',{'stu_cla':stu_cla,'stu_par':stu_par,'stu':student})

def view_parent(request,par_id):
    parent = models.Parent.objects.get(pk=par_id)
    return render(request,'parent.html',{'parent':parent})

def isClaDate():
    now = datetime.now()
    if(now.isoweekday()<6):
        return True
    return False

#考虑上学时间
def take_to(request,stu_id,par_id):
    student = models.Student.objects.get(pk=stu_id)
    parent = models.Parent.objects.get(pk=par_id)
    if(student.stu_isAtSch == False):
        if(isClaDate() == True):
            student.stu_isAtSch = True
            student.save()
            deliver_record = models.deliverRecord.objects.create(deliver_stu=student,deliver_par=parent,deliver_choice='送')
            deliver_record.save()
            #等待老师同意
            return HttpResponse('送好了')
        else:
            return HttpResponse('不是上学时间')
    else:
        return HttpResponse('孩子已在学校')
    #return render(request,'404.html')

def isEndCla():
    now = datetime.now()
    if(9<now.hour<11 or 14<now.hour<16):
        return False
    else:
        return True

def pick_up(request,stu_id,par_id):
    student = models.Student.objects.get(pk=stu_id)
    parent = models.Parent.objects.get(pk=par_id)
    #http_response = ''
    if(isClaDate() == False):
        return HttpResponse('不是上课日期:')
    if (student.stu_isAtSch == True):
        if(isEndCla() == True):
            student.stu_isAtSch = False
            student.save()
            deliver_record = models.deliverRecord.objects.create(deliver_stu=student, deliver_par=parent,deliver_choice='接')
            deliver_record.save()
            # 等待老师同意
            return HttpResponse( '已接')
        else:
            return HttpResponse('未到下课时间')
    else:
        return HttpResponse('孩子不在学校内')
        #return HttpResponse()
    #return render(request,'404.html',{'response':json.dump(http_response)})
#这不是跳转回去之后会要求重新输入表单
def scene_pick_up(request):
    if request.method == "POST":
            stu_id = request.POST.get('stu_id')
            par_id =request.POST.get('par_id')
            status = 0
            result = "Error!"
            student = models.Student.objects.get(pk=stu_id)
            parent = models.Parent.objects.get(pk=par_id)
            http_response = ''
            if (isClaDate() == False):
                result = '不是上课日期:'
            if (student.stu_isAtSch == True):
                if (isEndCla() == True ):
                    student.stu_isAtSch = False
                    student.save()
                    deliver_record = models.deliverRecord.objects.create(deliver_stu=student, deliver_par=parent,
                                                                         deliver_choice='接')
                    deliver_record.save()
                    # 等待老师同意
                    status = 1
                    result = '已接'
                else:
                    result = '已接'
            else:
                result = '孩子不在学校内'
            return HttpResponse(json.dumps({
                "status": status,
                "result": result
            }))