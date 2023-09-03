// Attempt 1!! (Yuvneet) error : .csv file not readable

// const loginForm = document.getElementById("login-form");
// const loginButton = document.getElementById("login-form-submit");

// document.addEventListener("DOMContentLoaded", function () {
//     const loginForm = document.getElementById("login-form");
  
// loginButton.addEventListener("click", (e) => {
//          e.preventDefault();
  
//       const usernameField = document.getElementById("username-field");
//       const passwordField = document.getElementById("password-field");
//       const username = usernameField.value;
//       const password = passwordField.value;
  
//       // Read and parse the CSV file
//       fetch("static/script/logindata.csv")
//         .then((response) => response.text())
//         .then((data) => {
//           // Parse CSV data into an array of objects
//           const users = parseCSV(data);
  
//           // Check if the entered username and password match any user in the CSV
//           const authenticatedUser = users.find(
//             (user) => user.username === username && user.password === password
//           );
//            if (authenticatedUser) {
//             // Successful login, redirect or perform other actions
//             alert("Login successful!");
//             // You can redirect the user to the dashboard or another page here.
//           } else {
//             // Invalid credentials, show an error message
//             alert("Invalid username or password. Please try again.");
//           }
//         })
//         .catch((error) => {
//           console.error("Error reading CSV file:", error);
//         });
//     });
  
//     // Function to parse CSV data into an array of objects
//     function parseCSV(csv) {
//       const lines = csv.split("\n");
//       const result = [];
//       const headers = lines[0].split(",");
//       for (let i = 1; i < lines.length; i++) {
//         const obj = {};
//         const currentLine = lines[i].split(",");
//         for (let j = 0; j < headers.length; j++) {
//           obj[headers[j].trim()] = currentLine[j].trim();
//         }
//         result.push(obj);
//       }
//       return result;
//     };
  
// Patrick's code: Doesnot support .csv

// loginButton.addEventListener("click", (e) => {
//     e.preventDefault();
//     const username = loginForm.username.value;
//     const password = loginForm.password.value;

//     if (username === "a" && password === "a") {
//         alert("You have successfully logged in.");
//         document.location = '/'
//     } else {
//         alert("Wrong Username and/or Password!")
//     }
// })

// Final working code (Yuvneet)
const loginForm = document.getElementById("login-form");
    const loginButton = document.getElementById("login-form-submit");

    loginButton.addEventListener("click", (e) => {
        e.preventDefault();
        const username = loginForm.username.value;
        const password = loginForm.password.value;

        // Read and parse the CSV file
        fetch("static/script/logindata.csv")  // Replace with the correct path to your CSV file if needed
            .then((response) => response.text())
            .then((data) => {
                // Parse CSV data into an array of objects
                Papa.parse(data, {
                    header: true, // Treat the first row as headers
                    dynamicTyping: true, // Automatically parse numbers and booleans
                    complete: function (results) {
                        const users = results.data;

                        // Check if the entered username and password match any user in the CSV
                        const authenticatedUser = users.find(
                            (user) => user.username === username && user.password === password
                        );

                        if (authenticatedUser) {
                            alert("You have successfully logged in.");
                            document.location = '/';
                        } else {
                            alert("Wrong Username and/or Password!");
                        }
                    },
                    error: function (error) {
                        console.error("Error parsing CSV:", error.message);
                    }
                });
            })
            .catch((error) => {
                console.error("Error reading CSV file:", error);
            });
    });
