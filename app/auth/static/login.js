import { initializeApp } from "https://www.gstatic.com/firebasejs/11.2.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.2.0/firebase-analytics.js";
import {
  getAuth,
  GoogleAuthProvider,
  signInWithPopup,
} from "https://www.gstatic.com/firebasejs/11.2.0/firebase-auth.js";

// Initialize Firebase
const firebaseConfig = {
  apiKey: "AIzaSyDkRFvN9z3xZwksBmZCfnJaOeUPZ-ki4Fk",
  authDomain: "identity-all-around-id.firebaseapp.com",
  databaseURL: "https://identity-all-around-id-default-rtdb.firebaseio.com",
  projectId: "identity-all-around-id",
  storageBucket: "identity-all-around-id.appspot.com",
  messagingSenderId: "904416766196",
  appId: "1:904416766196:web:3f9fbfbe2833ea296c56a1",
  measurementId: "G-S01Z1HQMN1",
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
auth.languageCode = "en";
const provider = new GoogleAuthProvider();

// Check if the Google Sign-in button exists before adding an event listener
document.addEventListener("DOMContentLoaded", function () {
  event.preventDefault(); // Prevent form submission
  const signInWithGoogle = document.getElementById("google-sign-in");

  if (signInWithGoogle) {
    signInWithGoogle.addEventListener("click", function () {
      signInWithPopup(auth, provider)
        .then((result) => {
          const credential = GoogleAuthProvider.credentialFromResult(result);
          const user = result.user;
          console.log(user);
          window.location.href = "/auth/gen-register";
        })
        .catch((error) => {
          const errorCode = error.code;
          const errorMessage = error.message;
          console.error(`Error ${errorCode}: ${errorMessage}`);
        });
    });
  } else {
    console.error("Google Sign-In button not found");
  }
});
