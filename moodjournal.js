<script type="module">
    // Import the functions you need from the SDKs you need
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.14.0/firebase-app.js";
    import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.14.0/firebase-analytics.js";
    // TODO: Add SDKs for Firebase products that you want to use
    // https://firebase.google.com/docs/web/setup#available-libraries

    // Your web app's Firebase configuration
    // For Firebase JS SDK v7.20.0 and later, measurementId is optional
    const firebaseConfig = {
    apiKey: "AIzaSyCUrykO4Y-zEcAwpbi61GXtYZWIvPOyCCs",
    authDomain: "mood-journal-ab77b.firebaseapp.com",
    databaseURL: "https://mood-journal-ab77b-default-rtdb.firebaseio.com",
    projectId: "mood-journal-ab77b",
    storageBucket: "mood-journal-ab77b.appspot.com",
    messagingSenderId: "928385378881",
    appId: "1:928385378881:web:87d5204f01dcbfed3db4c0",
    measurementId: "G-42FF99L746"
    };

    // Initialize Firebase
    const app = initializeApp(firebaseConfig);
    const analytics = getAnalytics(app);
</script>