from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Genders
from .models import Genders, Users
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse

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

def user_list(request):
    try:
        users_data = Users.objects.select_related('gender').all().order_by('user_id')
        data = {'users': users_data}
        return render(request, 'user/UserList.html', data)
    except Exception as e:
        return HttpResponse(f"Error occurred: {e}")

def add_user(request):
    try:
        genders = Genders.objects.all().order_by('gender')
        if request.method == 'POST':
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            gender_id = request.POST.get('gender')
            username = request.POST.get('username')
            birth_date = request.POST.get('birth_date')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            address = request.POST.get('address')
            contact_number = request.POST.get('contact_number')
            profile_picture  = request.FILES.get('profile_picture')

            

            if password != confirm_password:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'user/AddUser.html', {'genders': genders})

            gender_obj = Genders.objects.get(gender_id=gender_id)

            Users.objects.create(
                full_name=full_name,
                email=email,
                gender=gender_obj,
                username=username,
                birth_date=birth_date,
                password=make_password(password), 
                address=address,
                contact_number=contact_number,
                profile_picture = profile_picture,
                
            )
            messages.success(request, 'User added successfully!')
            return redirect('/user/list')
        return render(request, 'user/AddUser.html', {'genders': genders})
    except Exception as e:
        return HttpResponse(f"Error occurred during add user: {e}")
    
def edit_user(request, pk):
    try:
        user_obj = Users.objects.get(user_id=pk)
        genders = Genders.objects.all().order_by('gender')
       
        if request.method == 'POST':
            user_obj.full_name = request.POST.get('full_name')
            user_obj.email = request.POST.get('email')
            gender_id = request.POST.get('gender')
            user_obj.gender = Genders.objects.get(gender_id=gender_id)
            user_obj.username = request.POST.get('username')
            user_obj.birth_date = request.POST.get('birth_date')
            user_obj.address = request.POST.get('address')
            user_obj.contact_number = request.POST.get('contact_number')
            
            new_picture = request.FILES.get('profile_picture')
            if new_picture:
                user_obj.profile_picture = new_picture             # only replace if new one provided

            new_password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if new_password:
                if new_password != confirm_password:
                    messages.error(request, 'Passwords do not match.')
                    return render(request, 'user/EditUser.html', {'user': user_obj, 'genders': genders})
                user_obj.password = make_password(new_password)

            user_obj.save()
            messages.success(request, 'User updated successfully!')
            return redirect('/user/list')
        return render(request, 'user/EditUser.html', {'user': user_obj, 'genders': genders})
    except Exception as e:
        return HttpResponse(f"Error occurred during edit user: {e}")


def delete_user(request, pk):
    try:
        user_obj = Users.objects.get(user_id=pk)
        if request.method == 'POST':
            user_obj.delete()
            messages.success(request, 'User deleted successfully!')
            return redirect('/user/list')
        return render(request, 'user/DeleteUser.html', {'user': user_obj})
    except Exception as e:
        return HttpResponse(f"Error occurred during delete user: {e}")
    
def check_username(request):
    username = request.GET.get('username', '')
    exists = Users.objects.filter(username=username).exists()
    return JsonResponse({'exists': exists})

# def check_email(request):
#     email = request.GET.get('email', '')
#     exists = Users.object.filter(email = email).exists()
#     return JsonResponse({'exists': exists})
