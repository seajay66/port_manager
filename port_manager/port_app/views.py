from django.shortcuts import render,HttpResponse,redirect
from port_app import models
from port_app.pager import Pagination


# 查询所有端口
def ports(request):
    port_list = models.Port.objects.all()
    return render(request, "get_ports.html", {"port_list": port_list})

# 查询所有端口分组
def ports_group(request):
    ports_group_list = models.PortGroup.objects.all()
    return render(request, "get_ports_group.html", {"ports_group_list": ports_group_list})

# 生成所有端口数据列表
USER_LIST = models.Port.objects.all()

#按照既定方式进行分页显示
def fenye(request):
    current_page = request.GET.get("p")
    page_obj = Pagination(401,current_page)
    data_list = USER_LIST[page_obj.start():page_obj.end()]
    return render(request,"pager.html",{'data_list':data_list,'page_obj':page_obj,'current_page':current_page})

# 删除该端口号
def delete_port(request):
    nid = request.GET.get('nid')
    print(nid)
    current_page = request.GET.get('current_page')
    models.Port.objects.filter(id=nid).update(project='')
    return redirect('/fenye/?p=%s'%current_page)

def add(request):
    print(request.POST)
    pro_id = request.POST.get('data-id')
    project_name = request.POST.get('name')
    pro_id = int(pro_id)
    models.Port.objects.filter(id=pro_id).update(project=project_name)
    return HttpResponse('ok')

def select(request):
    a = request.POST.get('a')
    select_result1 = models.Port.objects.filter(project__contains=a)
    select_result2 = models.Port.objects.filter(port__contains=a)
    select_result3 = models.Port.objects.filter(id__contains=a)
    select_result = select_result1 | select_result2 | select_result3
    current_page = request.GET.get("p")
    page_obj = Pagination(401, current_page)
    data_list = select_result[page_obj.start():page_obj.end()]
    return render(request,'pager.html',{'data_list':data_list,'page_obj':page_obj,'current_page':current_page})


