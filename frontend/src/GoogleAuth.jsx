import React from "react";
import { GoogleOAuthProvider, GoogleLogin } from "@react-oauth/google";

const clientId = "64418966689-19v9ub4d8k6ou039i88nut2pfohnuejv"; 

const responseGoogle = (response) => {
  console.log("Login Success:", response);
  fetch("http://localhost:8000/auth/google/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ token: response.credential }), // Updated key
  })
    .then((res) => res.json())
    .then((data) => console.log("Backend response:", data))
    .catch((error) => console.error("Error sending token to backend:", error));
};

const GoogleAuth = () => (
  <GoogleOAuthProvider clientId={clientId}>
    <GoogleLogin
      onSuccess={responseGoogle}
      onError={() => console.log("Login Failed")}
    />
  </GoogleOAuthProvider>
);

export default GoogleAuth;