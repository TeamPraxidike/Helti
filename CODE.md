# Code

Registration function

```js
// Registration function
function register() {
    //We begin by taking all infromation fron the <input> tags
    email = document.getElementById('email_field').value;
    pass = document.getElementById('pass_field').value;
    fname = document.getElementById('name_field').value;
    gender = document.getElementById('sex_field').value;
    let rbs = document.querySelectorAll('input[name="acc_type"]')
    let acc_type_value;
    for (let rb of rbs) {
      if(rb.checked) {
        acc_type_value = rb.value;
        break;
      }
    }

    // Validation
    if (validate_email(email) == false || validate_password(pass) == false) {
        alert('Email or pass is not good');
        return;
    }

    // Then we use the createUserWithEmailAndPassword function from Firebase
    auth.createUserWithEmailAndPassword(email, pass)
    .then(function() {

        // We take information from the current user.
        var user = auth.currentUser;

        // We make an empty element in the appointments array.
        var appointment_template = {
          pregled: '-',
          doctor: '-',
          bolest: '-',
          info: '-',
          mqsto: '-'
        }

        // Make a user object that will be entered in the database
        var user_data = {
            email: email,
            fname: fname,
            gender: gender,
            acc_type: acc_type_value,
            appointments: [appointment_template],
            last_login: Date.now()
        }

        // Finally we append the user's information to the database
        database_ref = database.ref();
        database_ref.child('users/' + user.uid).set(user_data);

    })
    .catch(function(err) {
        // Error handling goes here
        var error_code = err.code;
        var err_mess = err.message;
        alert(err_mess);
    });
}
```

Login function

```js
// Login function
function login() {
    // We take the information from the <input> tags
    email = document.getElementById('email_field').value;
    pass = document.getElementById('pass_field').value;

    // Validation
    if (validate_email(email) == false || validate_password(pass) == false) {
        alert('Email or pass is not good');
        return;
    }
    
    // We use the setPersistance function to make the user stayed logged in until signing out.
    firebase.auth().setPersistence(firebase.auth.Auth.Persistence.LOCAL)
    .then(() => {
      auth.signInWithEmailAndPassword(email, pass)
      .then(function() {
          // We take the login date
          var user = auth.currentUser;
          var user_data = {
              last_login: Date.now()
          }

        // ... and then update it on the Database
          database_ref = database.ref();
          database_ref.child('users/' + user.uid).update(user_data);
          
      })
      .catch(function(err) {
          // Error handling goes here
          var error_code = err.code;
          var err_mess = err.message;
          alert(err_mess);
      });
    }).catch((err) => {
      // Error handling goes here
      var errCode = err.code;
      alert(err.message);
    })
    
}
```

Sign out function

```js
// It goes without explanation
function logout() {
  auth.signOut();
}
```

Validating functions

```js
// Using Regular expressions.
function validate_email(email) {
    expression = /^[^@]+@\w+(\.\w+)+\w$/
    if (expression.test(email) == true) {
      // Email is good
      return true
    } else {
      // Email is not good
      return false
    }
  }
  
  function validate_password(password) {
    // Firebase only accepts lengths greater than 6
    if (password < 6) {
      return false
    } else {
      return true
    }
  }
  
  function validate_field(field) {
    if (field == null) {
      return false
    }
  
    if (field.length <= 0) {
      return false
    } else {
      return true
    }
  }
  ```

Handling panel

```js
// Listening to authorization change
auth.onAuthStateChanged(function(user) {
        // This code executes when a user is logged in
        if(user) {
            // We make certain parts of the panel visible and other not
            document.getElementById('panel').style.display = 'block';
            document.getElementById('please_login').style.display = 'none';

            var user_ref_data = database.ref('users/' + user.uid);
            user_ref_data.on('value', (snapshot) => {
                var data = snapshot.val();
                // We take value from the <input> tags
                document.getElementById("usear_span").innerText = data.fname;
                document.getElementById("info_email").innerText = data.email;
                document.getElementById("info_name").innerText = data.fname;
                document.getElementById("info_gender").innerText = data.gender;
                document.getElementById("info_disease").innerText = data.disease;
                document.getElementById("info_acc_type").innerText = data.acc_type;
                
                if (data.acc_type === "patient") {
                    // We make certain parts of the panel visible and other not
                    document.getElementById('panel_information_patient').style.display = 'grid';
                    document.getElementById('map_with_stats').style.display = 'block';
                    document.getElementById('panel_information_doc').style.display = 'none';
                } else {
                    // We make certain parts of the panel visible and other not
                    document.getElementById('panel_information_patient').style.display = 'none';
                    document.getElementById('map_with_stats').style.display = 'none';
                    document.getElementById('panel_information_doc').style.display = 'block';
                }
            })

            
            } else {
                // This code executes when there is no user logged in.
                document.getElementById('panel').style.display = 'none';
                document.getElementById('please_login').style.display = 'block';

                document.getElementById("usear_span").innerText = "none";
            }
        });

        // Adding information to the database
        function addRecordOf() {
            let user = auth.currentUser;
            var user_ref_data = database.ref('users/' + user.uid);
            let current_record = [];
            user_ref_data.on('value', snapshot => {
                var data = snapshot.val();

                current_record = data.appointments;
            });

            // We take value from the <input> tags
            let pregled_info = document.getElementById('pregled').value;
            let doctor_info = document.getElementById('doctor').value;
            let bolest_info = document.getElementById('bolest').value;
            let info_info = document.getElementById('info').value;
            let mqsto_info = document.getElementById('mqsto').value;

            let pregled_unit = {
                pregled: pregled_info,
                doctor: doctor_info,
                bolest: bolest_info,
                info: info_info,
                mqsto: mqsto_info
            }

            current_record.push(pregled_unit);

            let user_updated_data = {
                appointments: current_record
            }

            database.ref().child('users/' + user.uid).update(user_updated_data);
        }

        // Getting information from the database
        function getRecordOf() {
            var users_ref = database.ref('/');
            let specfic_user_email = document.getElementById('patient_number').value;
            users_ref.on('value', snapshot => {
                var data = snapshot.val();
                let specific_uses = Object.values(Object.values(data)[0]).find(el => el.email === specfic_user_email);
                if (specific_uses === undefined) return alert('no such patient');


                let doc_table = document.getElementById('doc_table');
                doc_table.innerHTML = "<tr><td>Appointment</td><td>Doctor</td><td>Disease</td><td>Information</td><td>Taken place at</td></tr>";
                let i = 1;
                let y = 0;
                specific_uses.appointments.forEach(elem => {
                    // Adding elements to the table on the panel.
                    let row = doc_table.insertRow(i);

                    let cell_mqsto = row.insertCell(y);
                    let cell_info = row.insertCell(y);
                    let cell_bolest = row.insertCell(y);
                    let cell_doctor = row.insertCell(y);
                    let cell_pregled = row.insertCell(y);

                    cell_pregled.innerText = elem.pregled;
                    cell_doctor.innerText = elem.doctor;
                    cell_bolest.innerText = elem.bolest;
                    cell_info.innerText = elem.info;
                    cell_mqsto.innerText = elem.mqsto;
                });
            });
        }
```
