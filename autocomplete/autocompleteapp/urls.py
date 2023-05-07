from django.urls import path
from . import views
urlpatterns = [
    
# ------------------------------------------------------------------------------------------------
# Admin
# ------------------------------------------------------------------------------------------------
# Admin Dashboard
    path('admin_dashboard',views.Admin_Dashboard,name='Admin_Dashboard'),
# ------------------------------------------------------------------------------------------------
# Globel Shortcuts
# ------------------------------------------------------------------------------------------------
    path('',views.home_page,name='home_page'),
    path('globle_shortcut',views.shortcut,name='shortcut'),
    path('shortcut_select',views.shortcut_select),
    path('shortcut_insert',views.shortcut_insert),
    path('shortcut_load_for_update/<int:shortcut_id>',views.shortcut_load_for_update),
    path('shortcut_update',views.shortcut_update),
    path('shortcut_disable',views.shortcut_disable),
    path('shortcut_search',views.shortcut_search),
# search Shortut
    path('apply_global_shortcut',views.apply_globle_shortcut_page),
    path('apply_globle_shortcut',views.apply_globle_shortcut),
# ------------------------------------------------------------------------------------------------
# Personal Shortcuts
# ------------------------------------------------------------------------------------------------
    path('personal_shortcut',views.personal_shortcut,name='personal_shortcut'),
    path('personal_shortcut_select',views.personal_shortcut_select),
    path('personal_shortcut_insert',views.personal_shortcut_insert),
    path('personal_shortcut_search',views.personal_shortcut_search),

# search Shortut
    path('apply_personal_shortcut',views.apply_personal_shortcut_page),
    path('apply_personal_shortcut_val',views.apply_personal_shortcut_val),

# ------------------------------------------------------------------------------------------------
# User Profile
# ------------------------------------------------------------------------------------------------
# User
    path('users', views.users, name='users' ),
    path('select_all_users', views.select_all_users), 
    
# ------------------------------------------------------------------------------------------------
# Individual
# ------------------------------------------------------------------------------------------------
# Individual Dashboard
    path('individual_dashboard',views.individual_dashboard),
# ------------------------------------------------------------------------------------------------
# Individual Personal Shortcuts
# ------------------------------------------------------------------------------------------------
    path('individual_personal_shortcut',views.individual_personal_shortcut,name='individual_personal_shortcut'),
    # path('personal_shortcut_select',views.personal_shortcut_select),
    # path('personal_shortcut_insert',views.personal_shortcut_insert),

# search Shortut
    path('apply_individual_personal_shortcut',views.apply_individual_personal_shortcut),
    path('apply_individual_personal_shortcut_val',views.apply_individual_personal_shortcut_val),
# ------------------------------------------------------------------------------------------------
# User Profile
# ------------------------------------------------------------------------------------------------
# User
    path('users', views.users, name='users' ),
    path('select_all_users', views.select_all_users), 
    
# ------------------------------------------------------------------------------------------------
# Company 
# ------------------------------------------------------------------------------------------------
# Company Dashboard
    path('company_dashboard',views.company_dashboard),
    path('company_user_dashboard',views.company_user_dashboard),
# ------------------------------------------------------------------------------------------------
# Company Personal Shortcuts
# ------------------------------------------------------------------------------------------------
    path('company_personal_shortcut',views.company_personal_shortcut,name='company_personal_shortcut'),
    path('company_personal_shortcut_select',views.company_personal_shortcut_select),
# Apply Company Global Shortcuts
    path('apply_company_personal_shortcut_page',views.apply_company_personal_shortcut_page),
    path('apply_company_personal_shortcut',views.apply_company_personal_shortcut),
# ------------------------------------------------------------------------------------------------
# Company Global Shortcuts
# ------------------------------------------------------------------------------------------------
    path('company_globle_shortcut',views.company_globle_shortcut,name='company_globle_shortcut'),
    path('company_globle_shortcut_select',views.company_globle_shortcut_select),
    path('company_globle_shortcut_search',views.company_globle_shortcut_search),
# Apply Company Global Shortcuts
    path('apply_company_globle_shortcut_page',views.apply_company_globle_shortcut_page),
    path('apply_company_globle_shortcut',views.apply_company_globle_shortcut),
# ------------------------------------------------------------------------------------------------
# Company Users
# ------------------------------------------------------------------------------------------------
    path('company_users', views.company_users, name='company_users' ),
    path('select_company_users', views.select_company_users), 
    path('insert_company_user',views.insert_company_user),
# ------------------------------------------------------------------------------------------------
# Login , Logout , User Registraion
# ------------------------------------------------------------------------------------------------
    path('login',views.insert_login,name = 'login'),
    path('logout', views.logout_user , name='logout'),
    path('insert_user', views.user_registration),
    path('registration', views.registration),
    path('user_disable/<int:user_id>',views.user_disable),
# ------------------------------------------------------------------------------------------------
# Email Group Creation
# ------------------------------------------------------------------------------------------------
    path('email_group_creation',views.email_group_creation,name = 'email_group_creation'),
    
]