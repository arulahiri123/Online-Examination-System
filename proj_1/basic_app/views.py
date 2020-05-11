from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm
from basic_app.models import Exams,Question,UserProfileInfo
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView,DetailView,ListView
# Create your views here.

class ExamViewList(ListView):
    model = Exams
    template_name = 'basic_app/listview.html'

class ExamDetailView(DetailView):
    context_object_name = 'sch'
    model = Exams
    template_name = 'basic_app/detailview.html'


def about(req):
    return render(req,'basic_app/about.html')
def index(request):
    my_d={'insert_me': 'You have to go the /form page to submit the form'}
    return render(request,'basic_app/index.html',context = my_d)

def register(request):

    registered = False
    if request.method == 'POST':

        user1 = UserForm(data = request.POST)
        profile1 = UserProfileInfoForm(data = request.POST)

        if user1.is_valid() and profile1.is_valid():
            user = user1.save()
            user.set_password(user.password)
            user.save()

            profile = profile1.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
                print(user1.errors, profile1.errors)

    else:
            user1 = UserForm()
            profile1 = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',{'user_form':user1 ,'profile_form': profile1,'registered':registered})

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice !!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print('User is not active')

        else:
            print('Someone tried and failed with username {} and password {}'.format(username,password))
            return HttpResponse('invalid log in details')
    else:
        return render(request,'basic_app/login.html',{})

@login_required
def courses(req):
    return render(req,'basic_app/courses.html')
