from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm, UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('login')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student_list')
            else:
                form.add_error(None, '用户名或密码错误')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def student_list(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(name__icontains=query) | Student.objects.filter(student_id__icontains=query)
    else:
        students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})
