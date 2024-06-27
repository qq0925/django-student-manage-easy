from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'gender', 'age', 'student_id', 'major']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '请输入姓名'}),
            'gender': forms.Select(),
            'age': forms.NumberInput(attrs={'placeholder': '请输入年龄'}),
            'student_id': forms.TextInput(attrs={'placeholder': '请输入学生ID'}),
            'major': forms.TextInput(attrs={'placeholder': '请输入专业'}),
        }

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label='用户名')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='密码')
