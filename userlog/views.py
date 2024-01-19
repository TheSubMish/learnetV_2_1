from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView,FormView
from django.urls import reverse_lazy
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
import json
import uuid

from .forms import CustomUserForm,LogInForm
from .models import CustomUser,MailToken
from .validation import signValidate,emailPasswordValidate
from .mail import send_forgot_password_mail
from course.models import Course
from student.models import Student
from teacher.models import Teacher

class IndexPage(ListView):
    template_name = 'index.html'
    model = Course
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            pic = CustomUser.objects.get(username=self.request.user.username).profilepic
            context['pic'] = pic
        courses = Course.objects.all()[:4]
        context['courses'] = courses
        return context

class SignUpPage(CreateView):
    template_name = 'signup.html'
    model = CustomUser
    form_class = CustomUserForm
    
    def post(self, request, *args, **kwargs):
        form_data = self.form_class(request.POST)
        if form_data.is_valid():
            if error_msg:=signValidate(form_data.cleaned_data):
                return render(request, self.template_name, {"form": form_data,'error': error_msg})
            user = form_data.save()
            login(request,user)
            role = form_data.cleaned_data['role']
            newUser = CustomUser.objects.get(username=form_data.cleaned_data['username'])
            if role:
                Teacher.objects.create(user=newUser)
                return redirect('teacher_dashboard')
            else:
                Student.objects.create(user=newUser)
                return redirect('student_dashboard')
        else:
            error_msg = emailPasswordValidate(form_data.errors.as_json())
            return render(request, self.template_name, {"form": form_data,'error': error_msg})

class LogInPage(FormView):
    form_class = LogInForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form_data = self.form_class(request.POST)
        if form_data.is_valid():
            username = form_data.cleaned_data['username']
            password = form_data.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect(self.success_url)
        else:
            error_msg_dict = json.loads(form_data.errors.as_json())
            error_msg = error_msg_dict['__all__'][0]['message']
            return render(request,self.template_name,{'form':self.form_class, 'error':error_msg})

def logoutPage(request):
    logout(request)
    # Get the previous page URL from the request headers
    previous_page = request.META.get('HTTP_REFERER', '/')
    return redirect(previous_page)

class RedirectDashboard(RedirectView):
    
    def get_redirect_url(self,*args,**kwargs):
        user = self.request.user
        try:
            Student.objects.get(user=user)
            return '/student/dashboard/'
        except Student.DoesNotExist:
            Teacher.objects.get(user=user)
            return '/teacher/dashboard/'
        except Teacher.DoesNotExist:
            return '/login/'
        
class ForgotPassword(View):
    def get(self,request):
        return render(request,'forgot.html')
    
    def post(self,request):
        email = request.POST['email']
        if not CustomUser.objects.filter(email=email).first():
            return redirect('signup')
        
        token = str(uuid.uuid4())
        send_forgot_password_mail(email,token)
        user = CustomUser.objects.get(email=email)
        try:
            if MailToken.objects.get(user=user):
                deleteToken = MailToken.objects.get(user=user)
                deleteToken.delete()
        except:
            MailToken.objects.create(user = user,token = token)
        
        return render(request,'forgot.html',{'mailsent': True})
    
class ChangePassword(View):
    def get(self,request,uuid):
        return render(request,'change.html')
    
    def post(self,request,uuid):
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        if password == '':
            return render(request,'change.html',{'error':'Enter a password'})

        if password != cpassword:
            return render(request,'change.html',{'error':'Password did not matched'})
        user = MailToken.objects.get(token=uuid)
        deleteToken = MailToken.objects.get(token=user.token)
        deleteToken.delete()
        changepassuser = CustomUser.objects.get(username=user.user)
        changepassuser.password = make_password(password)
        changepassuser.save()
        return redirect('login')