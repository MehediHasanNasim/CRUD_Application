from django.shortcuts import render
from first_app import forms 

def index(request):
    diction = {'title': "Nasim's index"}
    return render(request, 'first_app/index.html', context=diction)

    
def student_form(request):
    form = forms.StudentForm()

    if request.method == "POST":
        form = forms.StudentForm(request.POST)
    
        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title': "student_form", "student_form":form}
    return render(request, 'first_app/student_form.html', context=diction)
