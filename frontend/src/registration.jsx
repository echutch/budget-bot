import React from 'react';
import { GoogleLogin } from 'react-google-login';

const clientId = 'YOUR_CLIENT_ID'; // Replace with your Google OAuth Client ID

const responseGoogle = (response) => {
    console.log('Login Success:', response.profileObj);
    // Send the access token to your backend for further processing
    fetch('http://localhost:8000/auth/google/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ token: response.accessToken }),
    })
        .then((res) => res.json())
        .then((data) => console.log('Backend response:', data))
        .catch((error) => console.error('Error sending token to backend:', error));
};

const handleFailure = (error) => {
    console.log('Login Failed:', error);
};

const GoogleAuth = () => (
    <GoogleLogin
        clientId={clientId}
        buttonText="Sign in with Google"
        onSuccess={responseGoogle}
        onFailure={handleFailure}
        cookiePolicy={'single_host_origin'}
    />
);

export default GoogleAuth;