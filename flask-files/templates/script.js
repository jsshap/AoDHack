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

function createEvent(eventId, eventTitle, eventTime, eventLocation, eventMin, eventMax, eventDescription) {
  firebase.database().ref('Events/' + eventId).set({
    "Time": eventTime,
    "Location": eventLocation,
    "Title" : eventTitle,
    "Description": eventDescription,
    "min": eventMin,
    "max": eventMax,
  });
}

function addParticipants(eventId, participantsToAdd){
  firebase.database().red('Events/' + eventID).set()


}