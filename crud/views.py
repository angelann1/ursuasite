from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Genders

def gender_list(request):
    try:
        genders_data = Genders.objects.all().order_by('gender_id')
        data = {'genders': genders_data}
        return render(request, 'gender/GenderList.html', data)
    except Exception as e:
        return HttpResponse(f"Error occurred: {e}")

def add_gender(request):
    try:
        if request.method == 'POST':
            gender_val = request.POST.get('gender')
            if gender_val and gender_val.strip():
                Genders.objects.create(gender=gender_val.strip())
                messages.success(request, 'Gender added successfully!')
            else:
                messages.error(request, 'Gender field cannot be empty.')
            return redirect('/gender/list')
        else:
            return render(request, 'gender/AddGender.html')
    except Exception as e:
        return HttpResponse(f"Error occurred during add gender: {e}")

def edit_gender(request, pk):
    try:
        gender_obj = Genders.objects.get(gender_id=pk)
        if request.method == 'POST':
            gender_val = request.POST.get('gender')
            if gender_val and gender_val.strip():
                gender_obj.gender = gender_val.strip()
                gender_obj.save()
                messages.success(request, 'Gender updated successfully!')
            else:
                messages.error(request, 'Gender field cannot be empty.')
            return redirect('/gender/list')
        else:
            return render(request, 'gender/EditGender.html', {'gender': gender_obj})
    except Exception as e:
        return HttpResponse(f"Error occurred during edit gender: {e}")

def delete_gender(request, pk):
    try:
        gender_obj = Genders.objects.get(gender_id=pk)
        if request.method == 'POST':
            gender_obj.delete()
            messages.success(request, 'Gender deleted successfully!')
            return redirect('/gender/list')
        else:
            return render(request, 'gender/DeleteGender.html', {'gender': gender_obj})
    except Exception as e:
        return HttpResponse(f"Error occurred during delete gender: {e}")