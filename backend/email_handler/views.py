from django.shortcuts import render

# Create your views here.
# views.py

from django.http import JsonResponse
from google.auth.transport.requests import Request
from google.oauth2.id_token import verify_oauth2_token
from django.conf import settings
import json

def google_login(request):
    if request.method == 'POST':
        # Get the token sent by the frontend
        token = request.data.get('token')

        try:
            # Verify the token using Google's API
            data = json.loads(request.body)
            token = data.get('token')
            
            if not token:
                return JsonResponse({'success': False, 'message': 'Token is required'}, status=400)

            id_info = verify_oauth2_token(token, Request(), settings.GOOGLE_CLIENT_ID)

            # Extract user details
            user_email = id_info.get('email')
            user_name = id_info.get('name')

            # For now just return a success response
            return JsonResponse({'success': True, 'user': {'email': user_email, 'name': user_name}})

        except ValueError:
            # Invalid token
            return JsonResponse({'success': False, 'message': 'Invalid token'}, status=400)
    #When request method is not post    
    return JsonResponse({'success': False, 'message': 'Bad request'}, status=400)
