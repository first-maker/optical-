
// apai for model add 
var companyname = document.getElementById('companyname');

companyname.addEventListener('blur', async function () {
  console.log(companyname.value)

  let response = await fetch('/model?companyname=' + companyname.value);
  let shows = await response.json();
  // console.log(shows)
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


var maxIteam = document.getElementById("maxIteam");
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
    maxIteam.style.display = "block";
  }
  else {
    lens_box.style.display = "none";
    maxIteam.style.display = "none";
  }
  // [ 'Frams', 'Lens', 'Contact Lens', 'Devices', 'Accessories', 'Othar']
  if (brand_type.value == 'ContactLens') {
    contactLens.style.display = "block";
    maxIteam.style.display = "block";
  }
  else {
    contactLens.style.display = "none";
    maxIteam.style.display = "none";
  }
  if (brand_type.value == 'Lens' || brand_type.value == 'ContactLens') {
    maxIteam.style.display = "block";
  } else {
    maxIteam.style.display = "none";
  }
}


// smoall modeal functian 
$("#buttonId").click(function () {
  $("#modal").show();
})

