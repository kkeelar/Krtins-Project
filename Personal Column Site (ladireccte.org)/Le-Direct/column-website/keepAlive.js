import { initializeApp } from "firebase/app";
import { getDatabase, ref, set } from "firebase/database";


const firebaseConfig = {
  apiKey: "AIzaSyBRttUjBL-BBVc1OlQOXRzImMRc66t6r1o",
  authDomain: "ledirect-d1772.firebaseapp.com",
  databaseURL: "https://ledirect-d1772-default-rtdb.firebaseio.com",
  projectId: "ledirect-d1772",
};

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);

setInterval(() => {
  set(ref(db, "keepAlive"), { timestamp: Date.now() })
    .then(() => console.log("Keep-alive ping sent to Firebase"))
    .catch((error) => console.error("Error:", error));
}, 1000 * 60 * 30); // Runs every 30 minutes