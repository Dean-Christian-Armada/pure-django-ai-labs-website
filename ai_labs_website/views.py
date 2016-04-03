from django.core.validators import validate_email
from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
	# return HttpResponse("HomePage")

def email(request):
	if request.method == 'POST':
		success = 0
		message = ''
		_request = request.POST
		json = {}

		name = _request['name']
		email = _request['email']
		phone = _request['phone']
		message = _request['message']

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
			elif not message:
				message = 'Message is required'
			else:
				success = 1
				message = 'Inquiry has been send. Our Administrator will be in touch.'
				email_data = {}
				email_data['name'] = name
				email_data['email'] = email
				email_data['phone'] = phone
				email_data['message'] = message
				msg_html = render_to_string('email/contact-form.html', email_data)
				# The email below is the original and should be the one being sent by an email
				# emails = ["info@ai-labs.co, sales@ai-labs.co, jabonete1771@gmail.com"]
				# emails = email
				emails = "armadadean@yahoo.com"

				# settings.EMAIL_HOST_USER si currently deanarmada@gmail.com set at the settings.py
				send_mail("Sample Email Title", '', settings.EMAIL_HOST_USER, [emails], fail_silently=False, html_message=msg_html)

	json['success'] = success
	json['message'] = message
	return JsonResponse(json)