from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.views import PasswordResetView
from .models import CustomUser, AbstractUser
from .forms import CustomUserCreationForm
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from .forms import RegistrationForm
from .models import Contact
from .forms import ContactForm
from .models import CustomUser
from .models import Route
import yagmail


# Replace with your Gmail credentials
username = "yvangodimomo@gmail.com"
password = "pzls apph esje cgdl"

# Create a yagmail object
yag = yagmail.SMTP(username, password)



# Authentication view


def home(request):
    return render(request, 'home/home.html')


def services(request):
    return render(request, 'home/services.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('contact')  # Redirect to the same page after saving
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})


def about(request):
    return render(request, 'home/about.html')

def Privacy(request):
    return render(request, 'home/Privacy.html')

def term(request):
    return render(request, 'home/term.html')




def route(request):
    return render(request, 'home/route.html')


def route_detail(request, route_id):
    # Fetch the route details using route_id
    route = get_object_or_404(Route, id=route_id)
    
    # Pass the route data to the template
    context = {
        'route': route
    }
    
    return render(request, 'home/route_detail.html', context)



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()
    
    return render(request, 'auth/register.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
          
            if user.role == 'admin':
                return redirect('admin_panel')  # Adjust this to match your URL pattern name
            elif user.role == 'employer':
                return redirect('employer_panel')  
            elif user.role == 'maintenance':
                return redirect('maintenance_panel')  
            else:
                return redirect('passenger_panel')  # Adjust this to match your URL pattern name
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})



User = get_user_model()

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            reset_code = get_random_string(length=6)  # Generate a random code
            
            # Send email with reset code
            yag = yagmail.SMTP("yvangodimomo@gmail.com", "pzls apph esje cgdl")
            yag.send(to=email, subject="Password Reset Code", contents=f"Your reset code is: {reset_code}")

            # Store the reset code in the session temporarily
            request.session['reset_code'] = reset_code
            request.session['user_email'] = email
            
            return redirect('verify_reset_code')  # Redirect to code verification page
        except User.DoesNotExist:
            messages.error(request, "Email not associated with any account.")
    
    return render(request, 'auth/forgot_password.html')

def verify_reset_code(request):
    if request.method == 'POST':
        entered_code = request.POST.get('code')
        if entered_code == request.session.get('reset_code'):
            return redirect('reset_password')  # Redirect to reset password page
        else:
            messages.error(request, "Invalid reset code.")
    
    return render(request, 'auth/verify_reset_code.html')

def reset_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('password')
        email = request.session.get('user_email')
        user = User.objects.get(email=email)
        user.set_password(new_password)
        user.save()
        messages.success(request, "Password reset successfully.")
        return redirect('login')  # Redirect to login after successful reset
    
    return render(request, 'auth/reset_password.html')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'forgot_password.html'  # Specify your template here
    success_url = reverse_lazy('password_reset_done')  # Redirect after a successful reset request
    email_template_name = 'password_reset_email.html'  # Template for the password reset email



@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')


##  dashboard

@login_required
def employer_panel(request):
    return render(request, 'panel/employer/employer_panel.html')


@login_required
def admin_panel(request):
    return render(request, 'panel/admin/admin_panel.html')

    
@login_required
def passenger_panel(request):
    return render(request, 'panel/passenger/passenger_panel.html')


@login_required
def maintenance_panel(request):
    return render(request, 'panel/maintenance/maintenance_panel.html')


### admin panel

@login_required
def user_management(request):
    users = CustomUser.objects.all()
    return render(request, 'panel/admin/manage_user/user_management.html', {'users': users})

@login_required
def add_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_management')
    else:
        form = RegistrationForm()
    return render(request, 'panel/admin/manage_user/user_management.html', {'form': form})

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_management')
    else:
        form = RegistrationForm(instance=user)
    return render(request, 'panel/admin/manage_user/edit_user.html', {'form': form})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_management')
    return render(request, 'panel/admin/manage_user/confirm_delete.html', {'user': user})

@login_required
def security(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        current_password = request.POST.get('currentPassword')
        new_password = request.POST.get('newPassword')
        confirm_password = request.POST.get('confirmPassword')
        profile_picture = request.FILES.get('profile_picture')

        # Update name and email
        request.user.name = name
        request.user.email = email

        # Check current password for security
        if not request.user.check_password(current_password):
            context = {'error': 'Current password is incorrect'}
        else:
            # Update password if provided and valid
            if new_password and new_password == confirm_password:
                request.user.set_password(new_password)

            # Update profile picture if provided
            if profile_picture:
                request.user.profile_picture = profile_picture

            request.user.save()
            context = {'success': 'Settings updated successfully'}
            # Redirect to avoid resubmission on refresh
            return redirect('user_panel')
    else:
        context = {}

    return render(request, 'panel/admin/profile/security.html', context)

@login_required
def profile_admin(request):
    return render(request, 'panel/admin/profile/profile_admin.html', {'user': request.user})


# Yagmail credentials
username = "yvangodimomo@gmail.com"
password = "pzlsapphesjecgdl"  # Use your app-specific password

# Create a yagmail object
yag = yagmail.SMTP(username, password)

def manage_contact(request):
    contacts = Contact.objects.all()  # Fetch all contact messages
    return render(request, 'panel/admin/contact/manage_contact.html', {'contacts': contacts})

def reply_contact(request, contact_id):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send the reply email
        yag.send(
            to=email,
            subject='Reply to Your Contact Message',
            contents=message
        )

        return redirect('manage_contact')

def delete_contact(request, contact_id):

    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return redirect('manage_contact')


from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Ticket

def ticket_form_view(request):
    return render(request, 'panel/admin/ticket/ticket_form.html')  # The HTML template for the form

@csrf_exempt
def add_ticket(request):
    if request.method == 'POST':
        hour = request.POST['hour']
        departure = request.POST['departure']
        arrival = request.POST['arrival']
        classification = request.POST['classification']
        railway_name = request.POST['railway_name']

        # Create and save the ticket
        ticket = Ticket.objects.create(
            hour=hour,
            departure=departure,
            arrival=arrival,
            classification=classification,
            railway_name=railway_name
        )
        
        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'failed'}, status=400)

def view_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'panel/admin/ticket/view_tickets.html', {'tickets': tickets})

@csrf_exempt
def delete_ticket(request, ticket_id):
    if request.method == 'POST':
        ticket = get_object_or_404(Ticket, id=ticket_id)
        ticket.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)

def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    
    if request.method == 'POST':
        ticket.hour = request.POST.get('hour')
        ticket.departure = request.POST.get('departure')
        ticket.arrival = request.POST.get('arrival')
        ticket.classification = request.POST.get('classification')
        
        # Update price based on classification
        if ticket.classification == 'Standard':
            ticket.price = 2000
        elif ticket.classification == 'Premium':
            ticket.price = 4000
        elif ticket.classification == 'VIP':
            ticket.price = 10000

        ticket.save()
        return redirect('view_tickets')  # Redirect to the list of tickets after editing

    return render(request, 'panel/admin/ticket/edit_ticket.html', {'ticket': ticket})


from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from .models import MaintenanceTask

def assign_task(request):
    maintenance_users = get_user_model().objects.filter(role='maintenance')

    if request.method == 'POST':
        assigned_to_id = request.POST.get('assigned_to')
        task_name = request.POST.get('task_name')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        deadline = request.POST.get('deadline')
        
        assigned_to = get_object_or_404(get_user_model(), id=assigned_to_id)
        
        # Create task
        MaintenanceTask.objects.create(
            assigned_to=assigned_to,
            task_name=task_name,
            description=description,
            duration=duration,
            deadline=deadline
        )

        # Send email alert
        yag = yagmail.SMTP(username, password)
        yag.send(
            to=assigned_to.email,
            subject="New Maintenance Task Assigned",
            contents=f"Dear {assigned_to.username},\n\nYou have been assigned a new task: {task_name}. Please complete it before {deadline}."
        )

        return redirect('task_list')

    return render(request, 'panel/admin/maintenance/assign_task.html', {'maintenance_users': maintenance_users})

def task_list(request):
    tasks = MaintenanceTask.objects.all()
    return render(request, 'panel/admin/maintenance/task_list.html', {'tasks': tasks})

def edit_task(request, task_id):
    task = get_object_or_404(MaintenanceTask, id=task_id)

    if request.method == 'POST':
        task.task_name = request.POST.get('task_name')
        task.description = request.POST.get('description')
        task.duration = request.POST.get('duration')
        task.status = request.POST.get('status')
        task.save()
        return redirect('task_list')

    return render(request, 'panel/admin/maintenance/edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(MaintenanceTask, id=task_id)
    task.delete()
    return redirect('task_list')

def apply_sanction(request, task_id):
    task = get_object_or_404(MaintenanceTask, id=task_id)

    # Apply sanction (e.g., temporary ban)
    task.sanction_applied = True
    task.save()

    # Send email alert about the sanction
    yag = yagmail.SMTP(username, password)
    yag.send(
        to=task.assigned_to.email,
        subject="Maintenance Task Sanction",
        contents=f"Dear {task.assigned_to.username},\n\nDue to incomplete tasks, a temporary sanction has been applied to your account."
    )

    return redirect('task_list')


# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Task, CustomUser
from .forms import TaskForm

def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

@user_passes_test(is_admin)
def employer_task_list(request):
    employers = CustomUser.objects.filter(role='employer')
    tasks = Task.objects.all()

    return render(request, 'panel/admin/employer/employer_task_list.html', {
        'employers': employers,
        'tasks': tasks,
    })

@user_passes_test(is_admin)
def assign_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()

            # Send email alert using yagmail
            send_task_assignment_email(task)

            return redirect('employer_task_list')
    else:
        form = TaskForm()

    return render(request, 'panel/admin/employer/assign_task.html', {'form': form})

def send_task_assignment_email(task):
    username = "yvangodimomo@gmail.com"
    password = "pzlsapphesjecgdl"  # Your app-specific password
    yag = yagmail.SMTP(username, password)

    subject = f"New Task Assigned: {task.name}"
    content = f"""
    Dear {task.assigned_to.username},

    A new task has been assigned to you.

    Task Name: {task.name}
    Description: {task.description}
    Task Type: {task.get_task_type_display()}
    Ticket Quota: {task.ticket_quota}
    Is On Guard: {'Yes' if task.is_on_guard else 'No'}

    Please ensure this task is completed on time.

    Best Regards,
    Admin
    """
    yag.send(task.assigned_to.email, subject, content)

@user_passes_test(is_admin)
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('employer_task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'panel/admin/employer/edit_task.html', {'form': form})

@user_passes_test(is_admin)
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('employer_task_list')

    return render(request, 'panel/admin/employer/delete_task.html', {'task': task})


from .models import Communication
from .forms import CommunicationForm

# Add a communication
def add_communication(request):
    if request.method == 'POST':
        form = CommunicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = CommunicationForm()
    return render(request, 'panel/admin/communication/add_communication.html', {'form': form})

# Edit a communication
def edit_communication(request, pk):
    communication = get_object_or_404(Communication, pk=pk)
    if request.method == 'POST':
        form = CommunicationForm(request.POST, request.FILES, instance=communication)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = CommunicationForm(instance=communication)
    return render(request, 'panel/admin/communication/edit_communication.html', {'form': form, 'communication': communication})

# Delete a communication
def delete_communication(request, pk):
    communication = get_object_or_404(Communication, pk=pk)
    if request.method == 'POST':
        communication.delete()
        return redirect('communication_list')
    return render(request, 'panel/admin/communication/delete_communication.html', {'communication': communication})

# List all communications
def communication_list(request):
    communications = Communication.objects.all()
    return render(request, 'panel/admin/communication/communication_list.html', {'communications': communications})
