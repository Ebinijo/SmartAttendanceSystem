from django.shortcuts import render, redirect
from .models import *
from datetime import date
def register(request):

    departments = Department.objects.all()

    if request.method == "POST":

        Employee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            department=Department.objects.get(
                id=request.POST['department']
            ),
            password=request.POST['password']
        )

        return redirect('login')

    return render(
        request,
        'register.html',
        {'departments': departments}
    )
def login_view(request):

    if request.method == "POST":

        email = request.POST['email']
        password = request.POST['password']

        try:

            employee = Employee.objects.get(
                email=email,
                password=password
            )

            request.session['employee_id'] = employee.id

            return redirect('dashboard')

        except:

            return render(
                request,
                'login.html',
                {'error': 'Invalid Credentials'}
            )

    return render(request,'login.html')
def dashboard(request):

    employee = Employee.objects.get(
        id=request.session['employee_id']
    )

    return render(
        request,
        'dashboard.html',
        {'employee': employee}
    )
def logout_view(request):

    request.session.flush()

    return redirect('login')
def mark_attendance(request):

    employee = Employee.objects.get(
        id=request.session['employee_id']
    )

    if request.method == "POST":

        Attendance.objects.create(
            employee=employee,
            date=date.today(),
            status="Present"
        )

        return redirect('attendance_history')

    return render(
        request,
        'mark_attendance.html'
    )
def attendance_history(request):

    employee = Employee.objects.get(
        id=request.session['employee_id']
    )

    records = Attendance.objects.filter(
        employee=employee
    )

    return render(
        request,
        'attendance_history.html',
        {'records': records}
    )
def apply_leave(request):

    employee = Employee.objects.get(
        id=request.session['employee_id']
    )

    if request.method == "POST":

        LeaveRequest.objects.create(
            employee=employee,
            from_date=request.POST['from_date'],
            to_date=request.POST['to_date'],
            reason=request.POST['reason']
        )

        return redirect('leave_status')

    return render(
        request,
        'apply_leave.html'
    )
def leave_status(request):

    employee = Employee.objects.get(
        id=request.session['employee_id']
    )

    leaves = LeaveRequest.objects.filter(
        employee=employee
    )

    return render(
        request,
        'leave_status.html',
        {'leaves': leaves}
    )
def profile(request):

    employee = Employee.objects.get(
        id=request.session['employee_id']
    )

    return render(
        request,
        'profile.html',
        {'employee': employee}
    )
def admin_dashboard(request):

    total_employees = Employee.objects.count()

    total_attendance = Attendance.objects.count()

    total_leaves = LeaveRequest.objects.count()

    return render(
        request,
        'admin_dashboard.html',
        {
            'total_employees': total_employees,
            'total_attendance': total_attendance,
            'total_leaves': total_leaves
        }
    )
def add_employee(request):

    if request.method == "POST":

        Employee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            password=request.POST['password']
        )

        return redirect('view_employees')

    return render(
        request,
        'add_employee.html'
    )
def view_employees(request):

    employees = Employee.objects.all()

    return render(
        request,
        'view_employees.html',
        {'employees': employees}
    )
def update_employee(request,id):

    employee = Employee.objects.get(id=id)

    if request.method == "POST":

        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.phone = request.POST['phone']

        employee.save()

        return redirect('view_employees')

    return render(
        request,
        'update_employee.html',
        {'employee': employee}
    )
def delete_employee(request,id):

    employee = Employee.objects.get(id=id)

    if request.method == "POST":

        employee.delete()

        return redirect('view_employees')

    return render(
        request,
        'delete_employee.html',
        {'employee': employee}
    )
def view_attendance(request):

    attendance = Attendance.objects.all()

    return render(
        request,
        'view_attendance.html',
        {'attendance': attendance}
    )
def leave_requests(request):

    requests = LeaveRequest.objects.all()

    return render(
        request,
        'leave_requests.html',
        {'requests': requests}
    )
def approve_leave(request,id):

    leave = LeaveRequest.objects.get(id=id)

    leave.status = "Approved"

    leave.save()

    return redirect('leave_requests')
def reject_leave(request,id):

    leave = LeaveRequest.objects.get(id=id)

    leave.status = "Rejected"

    leave.save()

    return redirect('leave_requests')
def register(request):

    if request.method == "POST":

        Employee.objects.create(

            name=request.POST['name'],

            email=request.POST['email'],

            phone=request.POST['phone'],

            department=request.POST['department'],

            password=request.POST['password']

        )

        return redirect('login')

    return render(request, 'register.html')
