from django.shortcuts import render,HttpResponse

# Create your views here.

def visit_profile(request):
    return render(request, 'visit_profile.html')
    #return HttpResponse("This is Visit profile page")

def partner_with_us(request):
    return render(request, 'partner_with_us.html')
    #return HttpResponse("This is Partner with us page")

def video_call(request):
    return render(request, 'video_call.html')
    #return HttpResponse("This is Video call page")