from django.urls import path
from . import views

urlpatterns = [

    path('', views.login_view, name='login'),

    path('register/', views.register, name='register'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('logout/', views.logout_view, name='logout'),

    path('mark-attendance/',
         views.mark_attendance,
         name='mark_attendance'),

    path('attendance-history/',
         views.attendance_history,
         name='attendance_history'),

    path('apply-leave/',
         views.apply_leave,
         name='apply_leave'),

    path('leave-status/',
         views.leave_status,
         name='leave_status'),

    path('profile/',
         views.profile,
         name='profile'),

    path('admin-dashboard/',
         views.admin_dashboard,
         name='admin_dashboard'),

]
path('add-employee/',
     views.add_employee,
     name='add_employee'),

path('view-employees/',
     views.view_employees,
     name='view_employees'),

path('update-employee/<int:id>/',
     views.update_employee,
     name='update_employee'),

path('delete-employee/<int:id>/',
     views.delete_employee,
     name='delete_employee'),

path('view-attendance/',
     views.view_attendance,
     name='view_attendance'),

path('leave-requests/',
     views.leave_requests,
     name='leave_requests'),

path('approve-leave/<int:id>/',
     views.approve_leave,
     name='approve_leave'),

path('reject-leave/<int:id>/',
     views.reject_leave,
     name='reject_leave'),