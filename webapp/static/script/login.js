const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "a" && password === "a") {
        alert("You have successfully logged in.");
        document.location = '/'
    } else {
        alert("Wrong Username and/or Password!")
    }
})