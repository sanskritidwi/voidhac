from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Login, Profile
from django.db.models import Q
# Create your views here.

def booking(request):
	data1=Profile.objects.filter(name='Manisha Verma')
	return render(request, 'doctor/view_profile.html',{'data1':data1})

@permission_required('doctor.partner_with', raise_exception=True)
def partner(request):
	if request.method == 'POST':
		name = request.POST['name']
		spec = request.POST['spec']
		address = request.POST['address']
		experience = request.POST['experience']
		phone_no = request.POST['phone_no']
		email= request.POST['email']
		desc= request.POST['desc']
		thumbnail= request.FILES.get('thumbnail')
		login = Login(
            name=name, spec=spec, address=address, experience=experience, phone_no=phone_no, email=email, desc=desc,thumbnail=thumbnail, )
		login.save()
		messages.success(request, "Doctor added successfully!")
		return redirect('doctors:add_blog')

	return render(request, 'doctor/partner_with_us.html')

def blog(request):
	return render(request, 'blog/blog.html')

def blog_add(request):
	return render(request, 'blog/blog_register.html')

def edit_profile(request):
	if request.method == 'POST':
		name = request.POST['name']
		hos_name = request.POST['hos_name']
		spec = request.POST['spec']
		address = request.POST['address']
		experience = request.POST['experience']
		phone_no = request.POST['phone_no']
		email= request.POST['email']
		fee= request.POST['fee']
		time= request.POST['time']
		thumbnail= request.FILES.get('thumbnail')
		edit = Profile(
            name=name, hos_name= hos_name, spec=spec, address=address, experience=experience, phone_no=phone_no, email=email, fee=fee, time=time, thumbnail=thumbnail)
		edit.save()
		messages.success(request, "Doctor added successfully!")
		return redirect('doctors:add_blog')
	return render(request, 'doctor/profile/edit_profile.html')

def doctor(request):
	search_post = request.GET.get('search')
	
	if search_post:
		data = Profile.objects.filter(Q(spec__icontains=search_post))

	else:
		data = Profile.objects.all()

	return render(request, 'doctor/doctor_list.html',{'data':data})

def schedule_meet(request):
	return render(request, 'doctor/profile/schedule.html')