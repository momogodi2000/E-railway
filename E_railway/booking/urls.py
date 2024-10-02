from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import forgot_password, verify_reset_code, reset_password, profile_admin
from .views import manage_contact, reply_contact, delete_contact, add_ticket, ticket_form_view, get_communication_details



urlpatterns = [
    path('', views.home, name='home'), # Root URL routed to the home view
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('Privacy/', views.Privacy, name='Privacy'),
    path('term/', views.term, name='term'),
    path('services/', views.services, name='services'),
    path('route/', views.route, name='route'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('verify-reset-code/', verify_reset_code, name='verify_reset_code'),
    path('reset-password/', reset_password, name='reset_password'), 
    path('logout/', views.logout, name='logout'),


    path('panel/admin/', views.admin_panel, name='admin_panel'),
    path('panel/maintenance/', views.maintenance_panel, name='maintenance_panel'),
    path('panel/passenger/', views.passenger_panel, name='passenger_panel'),
    path('panel/employer/', views.employer_panel, name='employer_panel'),

    path('route/<int:route_id>/', views.route_detail, name='route_detail'),

    path('user-management/', views.user_management, name='user_management'),
    path('add-user/', views.add_user, name='add_user'),
    path('edit-user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('security/', views.security, name='security'),
    path('profile_admin/', profile_admin, name='profile_admin'),
    path('manage_contact/', manage_contact, name='manage_contact'),
    path('reply_contact/<int:contact_id>/', reply_contact, name='reply_contact'),
    path('delete_contact/<int:contact_id>/', delete_contact, name='delete_contact'),

    path('add_ticket/', add_ticket, name='add_ticket'),
    path('ticket_form/', ticket_form_view, name='ticket_form'),
    path('add_ticket/', views.add_ticket, name='add_ticket'),
    path('view_tickets/', views.view_tickets, name='view_tickets'),
    path('delete_ticket/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),
    path('edit_ticket/<int:ticket_id>/', views.edit_ticket, name='edit_ticket'),

    path('assign_task/', views.assign_task, name='assign_task'),
    path('tasks/', views.task_list, name='task_list'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('apply_sanction/<int:task_id>/', views.apply_sanction, name='apply_sanction'),

    path('employer-tasks/', views.employer_task_list, name='employer_task_list'),
    path('assign-task/', views.assign_task, name='assign_task'),
    path('edit-task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),

    path('add_communication/', views.add_communication, name='add_communication'),
    path('edit_communication/<int:pk>/', views.edit_communication, name='edit_communication'),
    path('delete_communication/<int:pk>/', views.delete_communication, name='delete_communication'),
    path('communication_list/', views.communication_list, name='communication_list'),
    path('policy/', views.policy, name='policy'),
    path('gov/', views.gov, name='gov'),

## passenger url
    path('security_cleints/', views.security_cleints, name='security_cleints'),
    path('profile_clients/', views.profile_clients, name='profile_clients'),
    path('communications/', views.communication_list, name='communication_list'),
    path('download_pdf/<int:communication_id>/', views.download_pdf, name='download_pdf'),
    path('get_communication_details/<int:communication_id>/', get_communication_details, name='get_communication_details'),
    path('my-report/', views.my_report, name='my_report'),
    path('ticket-selection/', views.ticket_selection, name='ticket_selection'),
    # Payment page for buying or reserving tickets
    path('ticket/payment/<int:ticket_id>/', views.ticket_payment, name='ticket_payment'),
    # URL for generating the PDF receipt
    path('ticket/generate_pdf/', views.generate_pdf_receipt, name='generate_pdf'),
    path('rewards/', views.rewards_fidelity, name='rewards_fidelity'),
    path('history/', views.ticket_history, name='ticket_history'),


## employer url
    path('setting_security/', views.setting_security, name='setting_security'),
    path('profile_employer/', views.profile_employer, name='profile_employer'),

    path('communications_employer/', views.communication_list_employer, name='communication_list_employer'),
    path('download_pdf_employer/<int:communication_id>/', views.download_pdf_employer, name='download_pdf_employer'),
    path('get_communication_details_employer/<int:communication_id>/', views.get_communication_details_employer, name='get_communication_details_employer'),
    path('notifications/', views.notifications, name='notifications'),


]