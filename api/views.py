# import json
import uuid

from django.apps import apps
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings

from .api_helpers import *

Episode = apps.get_model('episodes', 'Episode')
SubscriptionRequest = apps.get_model('subscribers', 'SubscriptionRequest')
Subscriber = apps.get_model('subscribers', 'Subscriber')


def get_episodes(request):
    episodes = Episode.objects.all()
    res = serializers.serialize("json", episodes)
    return HttpResponse(res, content_type='application/json')


@csrf_exempt
def create_new_subscription_request(request):
    if not valid_method('POST', request):
    	return error_response('Error: Method must be POST', 405)

    email = request.POST.get('email', False)
    if not email:
        return error_response('Error: No email provided in request', 422)

    subscription_request, created_new = SubscriptionRequest.objects.get_or_create(
        email=email)

    if not created_new:
        subscription_request.token = uuid.uuid4()
        subscription_request.save()

    if send_confirmation_email(subscription_request):
        return response('Email sent to ' + email)
    else:
        return error_response('Unable to send email to ' + email, 500)


def create_subscriber(request):
    email = request.GET.get('email', False)
    token = request.GET.get('token', False)

    if (not email or not token):
        return error_response("Error: Unable to process request. Missing information", 422)

    subscription_request = SubscriptionRequest.objects.get(email=email, token=token)
    if not subscription_request:
        return error_response("Error: Subscription request not found", 404)

    subscriber, created_new = Subscriber.objects.get_or_create(email=email)

    if created_new:
    	exists = 'False'
    else:
    	exists = 'True'

    return redirect('/thanks/?email=' + email + '&exists=' + exists)

def thanks(request):
	root = settings.HOST_URL
	email = request.GET.get('email', False)
	exists = request.GET.get('exists', False)
	return render(request,
		'api/thanks.html',
		{
			'email': email,
			'root': root,
			'exists': exists
		})
