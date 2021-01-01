//TODO: Add SDKs for Firebase products that you want to use https://firebase.google.com/docs/web/setup#available-libraries
var firebaseConfig = {
  apiKey: "AIzaSyC8iaO8kb95S5mnUa2WLSCrCO-2Vq7RWiE",
  authDomain: "amherst-hangout.firebaseapp.com",
  projectId: "amherst-hangout",
  storageBucket: "amherst-hangout.appspot.com",
  messagingSenderId: "396712529274",
  appId: "1:396712529274:web:043222572d7137bc939ac3"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
var database = firebase.database();