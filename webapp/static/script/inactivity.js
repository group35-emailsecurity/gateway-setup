function idleTimer() {
    var t;
    //window.onload = resetTimer;
    window.onmousemove = resetTimer; // catches mouse movements
    window.onmousedown = resetTimer; // catches mouse movements
    window.onclick = resetTimer;     // catches mouse clicks
    window.onscroll = resetTimer;    // catches scrolling
    window.onkeypress = resetTimer;  //catches keyboard actions

    function logout() {
        window.location.href = '/login.html';
        alert("You have been logged out due to inactivity");
    }

   function resetTimer() {
        clearTimeout(t);
        t = setTimeout(logout, 5000);  // time is in milliseconds (1000 is 1 second)
    }
}
//idleTimer();