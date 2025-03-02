from django.shortcuts import render

from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse

def sms_reply(request):
    """Respond to incoming SMS with a simple text message."""
    # Create a Twilio response
    resp = MessagingResponse()

    # Add a message to the response
    resp.message("The Robots are coming! Head for the hills!")

    # Return the TwiML response as an HTTP response
    return HttpResponse(str(resp), content_type='application/xml')

