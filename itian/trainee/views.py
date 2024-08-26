from django.shortcuts import render, redirect, get_object_or_404
# from .models import Trainee

def trainees_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/traineesList.html', {'trainees': trainees})

def trainee_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Trainee.objects.create(name=name, email=email)
        return redirect('trainee_list')
    return render(request, 'trainee/createTrainee.html')

def trainee_update(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    if request.method == 'POST':
        trainee.name = request.POST.get('name')
        trainee.email = request.POST.get('email')
        trainee.save()
        return redirect('trainee_list')
    return render(request, 'trainee/updateTrainee.html', {'trainee': trainee})

def trainee_delete(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    if request.method == 'POST':
        trainee.delete()
        return redirect('trainee_list')
    return render(request, 'trainee/deleteTrainee.html', {'trainee': trainee})

def trainee_details(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    return render(request, 'trainee/traineeDetails.html', {'trainee': trainee})
