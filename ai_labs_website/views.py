from django.core.validators import validate_email
from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
from django.conf import settings

try:
    from ai_labs_website.asynchronous_mail import send_mail
except:
    from django.core.mail import send_mail

# Create your views here.


def home(request):
    template = 'home.html'
    context_dict = {}
    return render(request, template, context_dict)


def email(request):
    if request.method == 'POST':
        success = 0
        message = ''
        _request = request.POST
        json = {}

        name = _request.get('name')
        email = _request.get('email')
        phone = _request.get('phone')
        content_msg = _request.get('message')

        if not name:
            message = 'Name is required.'
        elif len(name) <= 3:
            message = 'Name must be atleast 3 character.'
        elif not email:
            message = 'Email is required.'

        elif email:
            try:
                validate_email(email)
            except:
                message = 'Email is invalid.'

            if not phone:
                message = 'Phone is required.'
            elif len(phone) < 7:
                message = 'Phone must be atleast 7 character.'
            elif not content_msg:
                message = 'Message is required'
            else:
                success = 1
                title = 'Inquiry has been send. Our Administrator will be in touch.'
                message = title
                email_data = {}
                email_data['name'] = name
                email_data['email'] = email
                email_data['phone'] = phone
                email_data['message'] = content_msg
                msg_html = render_to_string(
                    'email/contact-form.html', email_data)
                emails = ['sales@ai-labs.co', 'jabonete1771@gmail.com']
                send_mail(title, '', settings.EMAIL_HOST_USER, [
                          emails], fail_silently=False, html_message=msg_html)
    else:
        return HttpResponseForbidden()

    json['success'] = success
    json['message'] = message
    return JsonResponse(json)


def meetup_events(request):
    template = 'meetup_events.html'
    context_dict = {}
    return render(request, template, context_dict)
