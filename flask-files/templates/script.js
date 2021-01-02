import firebase from "firebase/app";
import "firebase/database";


let config = {
    apiKey: "AIzaSyC8iaO8kb95S5mnUa2WLSCrCO-2Vq7RWiE",
    authDomain: "amherst-hangout.firebaseapp.com",
    projectId: "amherst-hangout",
    databaseURL: "https://amherst-hangout.firebaseio.com",
};
if (!firebase.apps.length) {
    firebase.initializeApp(config);
}

this.database = firebase.database();
function addParticipant(eventID, name, email) {
  let userRef = this.database.ref('Events/' + eventID);

  // emptylist = [];
  // //Create participants list
  // userRef.child('Participants').set(emptylist)

  // Update (push participant to list)
  userRef.child('Participants').push({'Name': name, 'Email':email})

  let part = userRef.once('Participants');

  let min = userRef.once('min');

  let doc = null
  if length(part) == min {
    // call python script

    // fakefunction(userRef.once());

  }

}

function createEvent(eventID, eventTitle, eventTime, eventLocation, eventMin, eventMax, eventDescription) {
  let userRef = this.database.ref('Events/');

  let emptylist = [];


  userRef.child(eventID).set({
    'EventID': eventID,
      'Time': eventTime,
      'Location': eventLocation,
      'Title' : eventTitle,
      'Description': eventDescription,
      'min': eventMin,
      'max': eventMax,
      'Participants' : emptylist
  });

}