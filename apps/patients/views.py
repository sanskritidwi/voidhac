from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.





def patient_profile(request):
	return render(request, 'patients/patient_profile.html')

def patient_login(request):
	return render(request, 'patients/patient_login.html')

def video_call(request):
    return render(request, 'video/video_call.html')
    #return HttpResponse("This is Video call page")

def meeting(request):
    return render(request, 'video/meeting.html')

def patient_edit(request):
	return render(request, 'patients/patient_edit.html')