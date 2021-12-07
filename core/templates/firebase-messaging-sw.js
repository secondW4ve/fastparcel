importScripts('http://www.gstatic.com/firebasejs/8.2.1/firebase-app.js');
importScripts('http://www.gstatic.com/firebasejs/8.2.1/firebase-messaging.js');

firebase.initializeApp({
  apiKey: "AIzaSyBeaETmTu4c6rB2VLPoODa0bzTfFPhP1gg",
    authDomain: "fastparcel-bcc39.firebaseapp.com",
    projectId: "fastparcel-bcc39",
    storageBucket: "fastparcel-bcc39.appspot.com",
    messagingSenderId: "211315605214",
    appId: "1:211315605214:web:d34791ba6fa394b100cc4f"
});

const messaging = firebase.messaging();