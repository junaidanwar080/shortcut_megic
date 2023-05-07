from django.shortcuts import render , redirect
from django.http import HttpResponse ,JsonResponse
from .models import Shortcuts , Userprofile ,Company
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
x=datetime.now()
import re
y=x.strftime('%Y-%m-%d')
from django.forms.models import model_to_dict

#---------------------------------------------------------------------------------
# Admin
#---------------------------------------------------------------------------------
# Admin Dash Board
#---------------------------------------------------------------------------------
@login_required(login_url='/login')
def Admin_Dashboard(request):
    username = request.user.username
    return render(request,'admin_penal/admin_dashboard.html',{'username':username})

#------------------------------------------------------------------------
# Globle Shortcut
#------------------------------------------------------------------------
# shortcut page call
@login_required(login_url='/login')
def shortcut(request):
    user= request.user
    return render(request,'admin_penal/shortcuts/shortcuts.html',{'user':user})

# shortcut Insert
def shortcut_insert(request):
    if request.method == 'POST':
        id = request.POST['id']
        Name = request.POST['Name']
        Description = request.POST['Description']
        Name = Name.upper()
        Is_Enable=1
        Shortcut_type=1 # 1 mean globel 2 mean individual
        if Name=='' or Description=='' :
            return JsonResponse('Plese Fill Required Fields',safe=False)
        else:
            insert_shortcut = Shortcuts( Name = Name , Description = Description , Is_Enable=1 ,Shortcut_type=Shortcut_type , Created_on = y,Created_by = id)
            insert_shortcut.save()
            return JsonResponse("Shortcut Created",safe=False)

# shortcut select
def shortcut_select(request):
    shortcut_select = Shortcuts.objects.filter(Is_Enable=1,Shortcut_type=1)
    return render(request,'admin_penal/shortcuts/shortcut_select.html' , {'shortcut_select':shortcut_select})

# shortcut load data for update
def shortcut_load_for_update(request , shortcut_id):
    data = Shortcuts.objects.get(Shortcut_id = shortcut_id)
    return JsonResponse(model_to_dict(data))

# shortcut Update
def shortcut_update(request):
    if request.method == 'POST':
        Shortcut_id = request.POST['edit_Shortcut_id']
        Name = request.POST['edit_Name']
        Description = request.POST['edit_Description']
        Is_Enable=1
        if Name == '' or Description== '':
            return JsonResponse('Please Enter Required fields' , safe = False)
        else:
            update = Shortcuts.objects.get(Shortcut_id = Shortcut_id)
            update.Name = Name
            update.Description = Description
            update.Is_Enable = Is_Enable
            update.Updated_on = y
            update.save()
            return JsonResponse('Shortcut Updated',safe=False)

# shortcut Disable/Enable
def shortcut_disable(request):
    if request.method == 'POST':
        Shortcut_id = request.POST['id']
        Is_Enable=0
        update = Shortcuts.objects.get(Shortcut_id = Shortcut_id)
        update.Is_Enable = Is_Enable
        update.Updated_on = y
        update.save()
        return JsonResponse('Shortcut Updated',safe=False)
    
#------------------------------------------------------------------------
# Personal Shortcut
#------------------------------------------------------------------------
# shortcut page call
@login_required(login_url='/login')
def personal_shortcut(request):
    user = request.user
    return render(request,'admin_penal/shortcuts/personalshortcut/personalshortcut.html',{'user':user})

# shortcut Insert
def personal_shortcut_insert(request):
    if request.method == 'POST':
        id = request.POST['id']
        Name = request.POST['Name']
        Description = request.POST['Description']
        Is_Enable=1
        Name = Name.upper()
        Shortcut_type=2 # 1 mean globel 2 mean individual
        if Name=='' or Description=='' :
            return JsonResponse('Plese Fill Required Fields',safe=False)
        else:
            insert_shortcut = Shortcuts( Name = Name , Description = Description , Is_Enable=1 ,Shortcut_type=Shortcut_type, Created_on = y,Created_by = id)
            insert_shortcut.save()
            return JsonResponse("Shortcut Created",safe=False)

# shortcut select
def personal_shortcut_select(request):
    user = request.user
    shortcut_select = Shortcuts.objects.filter(Is_Enable=1,Shortcut_type=2,Created_by=user.id)
    return render(request,'admin_penal/shortcuts/personalshortcut/personalshortcut_select.html' , {'shortcut_select':shortcut_select})

#---------------------------------------------------------------------------------
# Apply Globle ShortCut 
#---------------------------------------------------------------------------------
# Search ShortCut Page
@login_required(login_url='/login')
def apply_globle_shortcut_page(request):
    username = request.user.username
    return render(request,'admin_penal/shortcuts/globalshortcutapply.html', {'username':username})

# Load Shortcut for Edit
def apply_globle_shortcut(request):
    if request.method == 'POST':
        id = request.POST['item_id']
    shortcut_select = Shortcuts.objects.get(Name=id,Is_Enable=1,Shortcut_type=1)
    return JsonResponse(model_to_dict(shortcut_select))

#---------------------------------------------------------------------------------
# Apply Personal ShortCut 
#---------------------------------------------------------------------------------
# Search ShortCut Page
@login_required(login_url='/login')
def apply_personal_shortcut_page(request):
    username = request.user.username
    return render(request,'admin_penal/shortcuts/personalshortcut/personalshortcutapply.html', {'username':username})
# Search ShortCut
@login_required(login_url='/login')
def personal_shortcut_search(request):
    if request.method == 'POST':
        Shortcut = request.POST['shortcut']
        user = request.user
        shortcut_select = Shortcuts.objects.filter(Name__icontains=Shortcut,Is_Enable=1,Shortcut_type=2,Created_by=user.id)
        return render(request,'admin_penal/shortcuts/personalshortcut/personalshortcut_select.html' , {'shortcut_select':shortcut_select})
        # return JsonResponse(model_to_dict(search))

# Load Shortcut for Edit
def apply_personal_shortcut_val(request):
    if request.method == 'POST':
        id = request.POST['item_id']
    shortcut_select = Shortcuts.objects.get(Name=id,Is_Enable=1,Shortcut_type=2)
    return JsonResponse(model_to_dict(shortcut_select))

#---------------------------------------------------------------------------------
# Users
#---------------------------------------------------------------------------------
# User
@login_required(login_url='/login')
def users(request):
    username = request.user.username
    total_users = User.objects.filter(is_active=1,is_superuser=0).count()
    return render(request,'admin_penal/user/users.html',{'username':username , 'total_users':total_users})

# Load data User 
# @login_required(login_url='/login')
def user_profile(request , id):
    username = request.user.username
    return render(request,'admin_penal/user/user_profile.html',{'username':username })

# Edit User Profile
def update_user_profile(request):
    if request.method == "POST":
        edit_user_id = request.POST['user_id']
        fname = request.POST['fname']
        lname = request.POST['lname']
        if (fname=='' or lname==''):
            return JsonResponse("Please Fill Required Fields",safe=False)
        else:
            user_id = User.objects.get( id = edit_user_id)
            user_id.first_name = fname
            user_id.last_name = lname
            user_id.save()
            
            
            return JsonResponse("User Data Saved",safe=False)
        
def select_all_users(request):
    allusers = Userprofile.objects.all()
    return render(request,'admin_penal/user/select_all_users.html', {'User_table': allusers})

#--------------------------------------------------------------------------------------
# User
#---------------------------------------------------------------------------------
# @login_required(login_url='/login')
def user_profile1(request , user_id):
    username = request.user.username
    return render(request,'user_penal/registration_form.html',{'username':username})
        
# Edit User Profile
def edit_user_profile(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        fname = request.POST['fname']
        lname = request.POST['lname']
        room_id = request.POST['room_id']
        cnic = request.POST['cnic']
        contact = request.POST['contact']
        temporary_address = request.POST['temporary_address']
        permanent_address = request.POST['permanent_address']
        emergency_contact = request.POST['emergency_contact']
        birth_date = request.POST['birth_date']
        guardian_name = request.POST['guardian_name']
        Guardian_contact = request.POST['Guardian_contact']
        Guardian_relation = request.POST['Guardian_relation']
        if (fname=='' or lname=='' or cnic=='' or contact=='' or permanent_address=='' or emergency_contact=='' or birth_date=='' or guardian_name=='' or Guardian_relation==''):
            return JsonResponse("Please Fill Required Fields",safe=False)
        else:
            user_id = User.objects.get( id = user_id)
            user_id.first_name = fname
            user_id.last_name = lname
            user_id.save()
            return JsonResponse("User Data Saved",safe=False)

#-------------------------------------------------------------------------------
#Log in , Logout , Registraion
#-------------------------------------------------------------------------------
# login page display
def login_form(request):
    return render(request, 'login.html')

# Login
def insert_login(request):
    # if request.user.id:
    #     redirect_url= '/admin_dashboard' if request.user.is_superuser else '/'
    #     return redirect(redirect_url,permanent=True)
    message=''
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            user_detail = Userprofile.objects.get(user=user.id)
            assert user.check_password(password)
            print(user , user_detail.Company_id_id)
            if user is not None:
                login(request,user)
                if user.is_active:
                    if user.is_superuser==True:
                        return redirect('/admin_dashboard',permanent=True)
                    elif user_detail.user_type=='4' and user.is_superuser==False and user.is_staff==True:
                        return redirect('/company_user_dashboard',permanent=True)
                    elif user_detail.user_type=='2' and user.is_superuser==False:
                        return redirect('/company_dashboard',permanent=True)
                    
                    elif user_detail.user_type=='3' and user.is_superuser==False:
                        return redirect('/individual_dashboard',permanent=True)
                else:
                    message = 'Account Temorarily Blocked'
        except (User.DoesNotExist , AssertionError):
            message = "Invaid Credentials"
    return render(request , 'login.html' , context = {'message':message})
        
# logout
def logout_user(request):
        logout(request)
        return redirect('/',permanent=True)

# Registration page load
def registration(request):
    return render(request , 'register.html')

# Registration
def user_registration(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        user_name = request.POST['user_name']
        user_name = user_name.lower()
        Email = request.POST['Email']
        Password = request.POST['Password']
        Confirm_Password = request.POST['Confirm_Password']
        user_type = request.POST['user_type']
        if(user_id =='0'):
            is_active = 0
        else:
            is_active = 1
        is_superuser = 0
        Name = 'Shortcut Magic'
        Company_type = user_type
        # 1 for globle user
        # 2 for company user
        # 3 for individual user
        user_name_res = bool(re.search(r"\s", user_name))
        user_name_res = str(user_name_res)
        
        if (user_name == '' or Email == '' or Password == '' or Confirm_Password==''):
            return JsonResponse('Please Fill Required Fields',safe=False)
        elif (user_type=='0'):
            return JsonResponse('Please Select User Type',safe=False)
        elif (user_name_res=='True'):
            return JsonResponse('Username Should Not contain space',safe=False)
        elif ( Password != Confirm_Password):
            return JsonResponse('Password and Confirm Password are not same',safe=False)
        else:
            # creating company
            add_company = Company( Name = Name , Company_type = Company_type)
            add_company.save()
            latest_company_id = Company.objects.latest('Company_id')
            # creating user
            register = User.objects.create_user( username = user_name, email = Email,  password = Password, is_superuser= is_superuser , is_active = is_active)
            register.save()
            
            obj = User.objects.latest('id')
            register_complete = Userprofile.objects.get( user_id = obj.id)
            register_complete.user_type = user_type
            register_complete.created_on = y
            register_complete.created_by = user_id
            register_complete.Company_id_id = latest_company_id.Company_id
            register_complete.save()
            # return JsonResponse(obj.Company_id,safe=False)
            return JsonResponse("New User Created",safe=False)
        
def user_disable(request , user_id):
    if request.method == 'POST':
        is_active = request.POST['is_active']
        Is_Enable=0
        update = User.objects.get(id = user_id)
        update.Is_Enable = Is_Enable
        update.Updated_on = y
        update.is_active = is_active
        update.save()
        return JsonResponse('Shortcut Updated',safe=False) 
#-------------------------------------------------------------------------------
# Individual
#-------------------------------------------------------------------------------
@login_required(login_url='/login')
def individual_dashboard(request):
    user = request.user
    return render(request,'individual_penal/individual_dashboard.html',{'user':user})
#------------------------------------------------------------------------
# Individual Personal Shortcut
#------------------------------------------------------------------------
# shortcut page call
@login_required(login_url='/login')
def individual_personal_shortcut(request):
    user = request.user
    return render(request,'individual_penal/shortcuts/personalshortcut/personalshortcut.html',{'user':user})

# shortcut Insert
def personal_shortcut_insert(request):
    user = request.user
    if request.method == 'POST':
        id = request.POST['id']
        Name = request.POST['Name']
        Description = request.POST['Description']
        Is_Enable=1
        Name = Name.upper()
        Shortcut_type=2 # 1 mean globel 2 mean individual
        user_detail = Userprofile.objects.get(user=user.id)
        Company_id_id = user_detail.Company_id_id
        if Name=='' or Description=='' :
            return JsonResponse('Plese Fill Required Fields',safe=False)
        else:
            insert_shortcut = Shortcuts( Name = Name , Description = Description , Is_Enable=1 ,Shortcut_type=Shortcut_type, Created_on = y,Created_by = id , Company_id_id = Company_id_id)
            insert_shortcut.save()
            return JsonResponse("Shortcut Created",safe=False)

# shortcut select
def personal_shortcut_select(request):
    user = request.user
    user_detail = Userprofile.objects.get(user=user.id)
    Company_id_id = user_detail.Company_id_id
    shortcut_select = Shortcuts.objects.filter(Is_Enable=1,Shortcut_type=2,Created_by=user.id,Company_id_id=Company_id_id)
    return render(request,'admin_penal/shortcuts/personalshortcut/personalshortcut_select.html' , {'shortcut_select':shortcut_select})

# Search ShortCut
@login_required(login_url='/login')
def shortcut_search(request):
    if request.method == 'POST':
        Shortcut = request.POST['shortcut']
        shortcut_select = Shortcuts.objects.filter(Name__icontains=Shortcut,Is_Enable=1,Shortcut_type=1)
        return render(request,'admin_penal/shortcuts/shortcut_select.html' , {'shortcut_select':shortcut_select})

#---------------------------------------------------------------------------------
# Apply Individual Personal ShortCut 
#---------------------------------------------------------------------------------
# Search ShortCut Page
@login_required(login_url='/login')
def apply_individual_personal_shortcut(request):
    username = request.user.username
    return render(request,'individual_penal/shortcuts/personalshortcut/personalshortcutapply.html', {'username':username})

# Load Shortcut for Edit
def apply_individual_personal_shortcut_val(request):
    if request.method == 'POST':
        print('came here')
        user = request.user
        user_detail = Userprofile.objects.get(user=user.id)
        Company_id_id = user_detail.Company_id_id
        id = request.POST['item_id']
    shortcut_select = Shortcuts.objects.get(Name=id,Is_Enable=1,Shortcut_type=2,Created_by=user.id,Company_id_id=Company_id_id)
    return JsonResponse(model_to_dict(shortcut_select))

#-------------------------------------------------------------------------------
# Company
#-------------------------------------------------------------------------------
@login_required(login_url='/login')
def company_dashboard(request):
    user = request.user
    return render(request,'company_penal/company_dashboard.html',{'user':user})
#Comapny User
@login_required(login_url='/login')
def company_user_dashboard(request):
    user = request.user
    msg = "This part is Under Development"
    return render(request,'company_penal/company_user/company_user_dashboard.html',{'user':user, 'msg':msg})

#------------------------------------------------------------------------
# Company Personal Shortcut
#------------------------------------------------------------------------
# shortcut page call
@login_required(login_url='/login')
def company_personal_shortcut(request):
    user = request.user
    return render(request,'company_penal/shortcuts/personalshortcut/personalshortcut.html',{'user':user})

# Company Personal shortcut select
def company_personal_shortcut_select(request):
    user = request.user
    user_detail = Userprofile.objects.get(user=user.id)
    Company_id_id = user_detail.Company_id_id
    shortcut_select = Shortcuts.objects.filter(Is_Enable=1,Shortcut_type=2,Created_by=user.id,Company_id_id=Company_id_id)
    return render(request,'company_penal/shortcuts/personalshortcut/personalshortcut_select.html' , {'shortcut_select':shortcut_select})

#------------------------------------------------------------------------
# Company Global Shortcut
#------------------------------------------------------------------------
# shortcut page call
@login_required(login_url='/login')
def company_globle_shortcut(request):
    user = request.user
    return render(request,'company_penal/shortcuts/globalshortcut/globalshortcuts.html',{'user':user})

# Company Global Shortcut select
def company_globle_shortcut_select(request):
    shortcut_select = Shortcuts.objects.filter(Is_Enable=1,Shortcut_type=1)
    return render(request,'company_penal/shortcuts/globalshortcut/global_shortcut_select.html' , {'shortcut_select':shortcut_select})

# Company Global Shortcut Search
@login_required(login_url='/login')
def company_globle_shortcut_search(request):
    if request.method == 'POST':
        Shortcut = request.POST['shortcut']
        shortcut_select = Shortcuts.objects.filter(Name__icontains=Shortcut,Is_Enable=1,Shortcut_type=1)
        return render(request,'company_penal/shortcuts/globalshortcut/global_shortcut_select.html' , {'shortcut_select':shortcut_select})

#---------------------------------------------------------------------------------
# Apply Company Global ShortCut 
#---------------------------------------------------------------------------------
# Search Global ShortCut Page
@login_required(login_url='/login')
def apply_company_globle_shortcut_page(request):
    username = request.user.username
    return render(request,'company_penal/shortcuts/globalshortcut/globalshortcutapply.html', {'username':username})

# Load Shortcut for Edit
def apply_company_globle_shortcut(request):
    if request.method == 'POST':
        print('came here')
        id = request.POST['item_id']
    shortcut_select = Shortcuts.objects.get(Name=id,Is_Enable=1,Shortcut_type=1)
    return JsonResponse(model_to_dict(shortcut_select))

#---------------------------------------------------------------------------------
# Apply Company Personal ShortCut 
#---------------------------------------------------------------------------------
# Apply personal ShortCut Page load
@login_required(login_url='/login')
def apply_company_personal_shortcut_page(request):
    username = request.user.username
    return render(request,'company_penal/shortcuts/personalshortcut/personalshortcutapply.html', {'username':username})

# Load Shortcut for Edit
def apply_company_personal_shortcut(request):
    if request.method == 'POST':
        print('came here')
        user = request.user
        user_detail = Userprofile.objects.get(user=user.id)
        Company_id_id = user_detail.Company_id_id
        id = request.POST['item_id']
    shortcut_select = Shortcuts.objects.get(Name=id,Is_Enable=1,Shortcut_type=2,Created_by=user.id,Company_id_id=Company_id_id)
    return JsonResponse(model_to_dict(shortcut_select))

#---------------------------------------------------------------------------------
# Users
#---------------------------------------------------------------------------------
# User
@login_required(login_url='/login')
def company_users(request):
    user = request.user
    return render(request,'company_penal/user/company_users.html')

def insert_company_user(request):
    user = request.user
    if request.method == "POST":
        user_id = request.POST['user_id']
        user_name = request.POST['user_name']
        user_name = user_name.lower()
        Email = request.POST['Email']
        Password = request.POST['Password']
        Confirm_Password = request.POST['Confirm_Password']
        user_detail = Userprofile.objects.get(user=user.id)
        Company_id_id = user_detail.Company_id_id
        print('Comapny Id: ',Company_id_id)
        user_type = 4
        if(user_id =='0'):
            is_active = 0
        else:
            is_active = 1
        is_superuser = 0
        is_staff = 1
        Name = 'Shortcut Magic'
        Company_type = user_type
        # 2 for company admin
        # 4 for company individual
        # 3 for individual user
        user_name_res = bool(re.search(r"\s", user_name))
        user_name_res = str(user_name_res)
        
        if (user_name == '' or Email == '' or Password == '' or Confirm_Password==''):
            return JsonResponse('Please Fill Required Fields',safe=False)
        elif (user_name_res=='True'):
            return JsonResponse('Username Should Not contain space',safe=False)
        elif ( Password != Confirm_Password):
            return JsonResponse('Password and Confirm Password are not same',safe=False)
        else:
            # creating user
            register = User.objects.create_user( username = user_name, email = Email,  password = Password, is_superuser= is_superuser , is_active = is_active , is_staff = is_staff)
            register.save()
            obj = User.objects.latest('id')
            # Updating User Profile
            register_complete = Userprofile.objects.get( user_id = obj.id)
            register_complete.user_type = user_type
            register_complete.created_on = y
            register_complete.created_by = user_id
            register_complete.Company_id_id = Company_id_id
            register_complete.save()
            return JsonResponse('New User Created',safe=False)
# Load data User 
# @login_required(login_url='/login')
# def user_profile(request , id):
#     username = request.user.username
#     return render(request,'admin_penal/User/user_profile.html',{'username':username })

# Edit User Profile
# def update_user_profile(request):
#     if request.method == "POST":
#         edit_user_id = request.POST['user_id']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         if (fname=='' or lname==''):
#             return JsonResponse("Please Fill Required Fields",safe=False)
#         else:
#             user_id = User.objects.get( id = edit_user_id)
#             user_id.first_name = fname
#             user_id.last_name = lname
#             user_id.save()
            
            
#             return JsonResponse("User Data Saved",safe=False)
        
def select_company_users(request):
    user = request.user
    user_detail = Userprofile.objects.get(user=user.id)
    Company_id_id = user_detail.Company_id_id
    print("came here")
    allusers = Userprofile.objects.filter(Company_id_id=Company_id_id)
    return render(request,'company_penal/user/select_all_users.html', {'User_table': allusers})

#--------------------------------------------------------------------------------------
# User
#---------------------------------------------------------------------------------
# @login_required(login_url='/login')
# def user_profile1(request , user_id):
#     username = request.user.username
#     return render(request,'user_penal/registration_form.html',{'username':username})
        
# Edit User Profile
# def edit_user_profile(request):
#     if request.method == "POST":
#         user_id = request.POST['user_id']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         room_id = request.POST['room_id']
#         cnic = request.POST['cnic']
#         contact = request.POST['contact']
#         temporary_address = request.POST['temporary_address']
#         permanent_address = request.POST['permanent_address']
#         emergency_contact = request.POST['emergency_contact']
#         birth_date = request.POST['birth_date']
#         guardian_name = request.POST['guardian_name']
#         Guardian_contact = request.POST['Guardian_contact']
#         Guardian_relation = request.POST['Guardian_relation']
#         if (fname=='' or lname=='' or cnic=='' or contact=='' or permanent_address=='' or emergency_contact=='' or birth_date=='' or guardian_name=='' or Guardian_relation==''):
#             return JsonResponse("Please Fill Required Fields",safe=False)
#         else:
#             user_id = User.objects.get( id = user_id)
#             user_id.first_name = fname
#             user_id.last_name = lname
#             user_id.save()
#             return JsonResponse("User Data Saved",safe=False)

#-------------------------------------------------------------------------------
# Public
#-------------------------------------------------------------------------------
# @login_required(login_url='/login')
def home_page(request): 
    return render(request,'home_page.html')

def email_group_creation(request):
    return render(request,'admin_penal/email_group_creation/email_group_creation.html')