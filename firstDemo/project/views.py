from django.shortcuts import render  
from jdango_Second.models import Stu  
# Create your views here.  
def showInfo(request):  
    stu_list = Stu.objects.all()  
    content = {'list':stu_list}  
    return render(request,'index.html',content)  