from django.contrib import admin
from .models import Department
from .models import Employee
from .models import Attendance
from .models import LeaveRequest

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(LeaveRequest)