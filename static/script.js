var myInput = document.getElementById("password");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");
var sampel = document.getElementById("sampel");
var confirmation = document.getElementById("password_confirmation");
var confiarm = document.getElementById("confiarm");

// When the user clicks on the password field, show the message box
myInput.onfocus = function () {
  document.getElementById("message").style.display = "block";
}

// When the user clicks outside of the password field, hide the message box
myInput.onblur = function () {
  document.getElementById("message").style.display = "none";
}




// When the user starts to type something inside the password field
myInput.onkeyup = function () {
  // Validate lowercase letters
  var lowerCaseLetters = /[a-z]/g;
  if (myInput.value.match(lowerCaseLetters)) {
    letter.classList.remove("invalid");
    letter.classList.add("valid");
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
  }

  // Validate capital letters
  var upperCaseLetters = /[A-Z]/g;
  if (myInput.value.match(upperCaseLetters)) {
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }

  // Validate numbers
  var numbers = /[0-9]/g;
  if (myInput.value.match(numbers)) {
    number.classList.remove("invalid");
    number.classList.add("valid");
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }

  // Validate length
  if (myInput.value.length >= 8) {
    length.classList.remove("invalid");
    length.classList.add("valid");
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }
  var special_char = ["$", "@", "#", "%", "&", "*"]
  for (let i = 0; i < myInput.value.length; i++) {
    console.log(myInput.value[i]);
    if (special_char.includes(myInput.value[i])) {
      sampel.classList.remove("invalid");
      sampel.classList.add("valid");
      break;
    } else {

      sampel.classList.remove("valid");
      sampel.classList.add("invalid");
    }
  }



}

// When the user clicks on the password field, show the message box
confirmation.onfocus = function () {
  document.getElementById("message2").style.display = "block";
}
// confiarm
// When the user clicks outside of the password field, hide the message box
confirmation.onblur = function () {
  document.getElementById("message2").style.display = "none";
}

confirmation.onkeyup = function () {
  // validate confiarm password

  if (myInput.value === confirmation.value) {

    confiarm.classList.remove("invalid");
    confiarm.classList.add("valid");
  } else {
    confiarm.classList.remove("valid");
    confiarm.classList.add("invalid");
  }


}


// show password
function show_password() {
  if (myInput.type === "password" || confirmation.type === "password") {
    myInput.type = "text";
    confirmation.type = "text";
  } else {
    myInput.type = "password";
    confirmation.type = "password";
  }
}


  





// apai for model add 
var companyname = document.getElementById('companyname');

companyname.addEventListener('blur', async function () {
  console.log(companyname.value)

  let response = await fetch('/model?companyname=' + companyname.value);
  let shows = await response.json();
  console.log(shows)
  let brand_type_optian = '<option selected value="null">Open this select menu</option>';
  for (let i in shows) {
    brand_type_optian += `
    <option value="`+ shows[i].brand_type + `">` + shows[i].brand_type + `</option>
    `
  };
  document.querySelector('#brand_type').innerHTML = brand_type_optian;
})


var brand_type = document.getElementById('brand_type')
brand_type.addEventListener('blur', async function () {
  let response = await fetch('/model?brandType=' + brand_type.value);
  let brandName = await response.json();
 
  let brand_name_optian = '<option selected value="null">Open this select menu</option>';
  for (let i in brandName) {
    brand_name_optian += `
    
    <option value="`+ brandName[i].brand_id + `">` + brandName[i].brand_name + `</option>
   `
  }
  document.querySelector('#brand_name').innerHTML = brand_name_optian;

})



var fram_box = document.getElementById("fram_box");

var brand_type = document.getElementById("brand_type");

var contactLens = document.getElementById("contactLens");
// When the user clicks outside of the password field, hide the message box
brand_type.onblur = function () {
  if (brand_type.value == 'Frams') {
    fram_box.style.display = "block";
  }
  else {
    fram_box.style.display = "none";
  }

  if (brand_type.value == 'Lens') {
    lens_box.style.display = "block";
  }
  else {
    lens_box.style.display = "none";
  }
  // [ 'Frams', 'Lens', 'Contact Lens', 'Devices', 'Accessories', 'Othar']
  if (brand_type.value == 'ContactLens') {
    contactLens.style.display = "block";
  }
  else {
    contactLens.style.display = "none";
  }
}


// smoall modeal functian 
$("#buttonId").click(function () {
  $("#modal").show();
})
