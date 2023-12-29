var Nav_bar = [
    { href: "new", id: "new", name:"New",},
    { href: "offers", id: "offer", name:"Offers",},
    { href: "topSeller", id: "topSeller", name:"Top Seller",},
    { href: "sun", id: "sun", name:"Sun Glasses",},
    { href: "glasses", id: "glasses", name:"Eye Glasses",},
    { href: "ContactLens", id: "contactLenses", name:"Contact Lens",},
    { href: "Accessories", id: "accessory", name:"Accessory",},
]
  

var glaslist = [
  { type: "MEN ", imag: "menGlass.png", status: "New Glasses For ", },
  { type: "Women", imag: "womanGlass.png", status: "New Glasses For ", },
  { type: "Kids", imag: "kids.png", status: "New Glasses For ", },]

var sunlist = [
  { type: "MEN ", imag: "menSun.png", status: "Sun Glasses For ", },
  { type: "Women", imag: "womanSun.png", status: "Sun Glasses For ", },
  { type: "Kids", imag: "kidSun.webp", status: "Sun Glasses For ", },]
var newList = [
  { type: "MEN ", imag: "newMen.png", status: "New collection For ", },
  { type: "Women", imag: "newWoman.png", status: "New collection For ", },
  { type: "Kids", imag: "newKid.png", status: "New collection For ", },]

var offelist = [
  { type: "hotsell", imag: "bestSeller.jpg", status: "HOt Sell ", },
  { type: "offers", imag: "offer.jpg", status: "Offers  Collection ", },]

var topSeller = [
    { type: "topSeller", imag: "bestSeller.jpg", status: "Top Seller For Month ", },
    { type: "topSeller", imag: "offer.jpg", status: "Top Seller For Year ", },]
  

var contactLenses = [
  { type: "Color", imag: "color.jpg", status: "Contact Lenses ", },
  { type: "Clear", imag: "clear.png", status: "Contact Lenses ", },]
var accessory = [
  { type: "Women", imag: "accessory.webp", status: "Accessory For ", },
  { type: "Kids", imag: "accessorykid.jpg", status: "Accessory For ", },]



var navImagBar = document.getElementById("navImagBar");

function mousoutFunc(x) {
  x.style.backgroundColor = "#e9ecef";
}

function navImagDisplayNone(x) {

  navImagBar.style.display = "none";

}

var footerSoiaclMedia = [
  { href: "https://www.facebook.com/hasin.taha", id: "facebook", src: "f.png"},
  { href: "https://twitter.com/Hasintaha", id:"X", src: "x.png",name:"X",},
  { href: "https://maps.app.goo.gl/kP9bE6MiZy6ABRHZ9", id: "maps", src: "m.png"},
  { href: "https://www.instagram.com/hasin.taha/", id:"instagram", src: "i.png"},
  { href: "https://www.linkedin.com/in/elhusseini2023/", id:"linkedin", src: "l.png"},
  { href: "https://www.youtube.com/@hussaintaha9184", id: "youtube", src:"y.png"},
  { href: "/whatsUp", id: "whatsUp", src:"w.png"},
  { href: "https://github.com/first-maker", id: "github", src:"g.png"},

]
var footeroiaclMedia=document.getElementById('footeroiaclMedia')
var html='';
for(var i in footerSoiaclMedia){
  
  html +=`
  <a href="`+footerSoiaclMedia[i].href+`"class=" footerA" bg-body  target="_blank">
  <img  class="footerImg"  src="/static/imag/sosial/`+footerSoiaclMedia[i].src+`" alt="`+footerSoiaclMedia[i].id+`">
</a>
  `;
}
footeroiaclMedia.innerHTML=html

var footerContacts = [{ Addres: "Ksa-Jeddah-10401", Tell: "00966540919725", Fax: "00966126600148",Email: "hasin3112@email.com" ,loctian:"https://maps.app.goo.gl/kP9bE6MiZy6ABRHZ9" },]
var elemnt='';
var footerContact=document.getElementById('footerContact')
for(var i in footerContacts){
  elemnt+=`
  <p><i class="fas fa-phone me-3"></i><a class=" footerA" href="`+footerContacts[i].loctian+`" target="_blank">`+footerContacts[i].Addres+`</a></p>
  <p><i class="fas fa-phone me-3"></i><a class=" footerA" href="tel:`+footerContacts[i].Tell+`">`+footerContacts[i].Tell+`</a></p>
  <p><i class="fas fa-phone me-3"></i><a class=" footerA" href="mailto:`+footerContacts[i].Email+`">`+footerContacts[i].Email+`</a></p>
  <p><i class="fas fa-phone me-3"></i><a class=" footerA" href="tel:`+footerContacts[i].Fax+`">`+footerContacts[i].Fax+`</a></p>`
};
footerContact.innerHTML=elemnt;




function Dark_modefunc() {
    // var Dark_mode = document.getElementById("Dark_mode");

      if( document.body.style.backgroundColor == 'white'){
        document.body.style.backgroundColor= '#1d2a35'
        document.body.style.color= '#1d2a35'

      }else{
        document.body.style.backgroundColor= 'white'
        document.body.style.color= 'black'

      }

 
}





function nav_bar_add(){
    let nav_link=''
    let nav_link_smll=''
 
   
    for(let i in Nav_bar ){
        nav_link += `<a class="nav-item nav-link"  id="`+Nav_bar[i].id +`" onload="dataADD(this)" onmouseout="mousoutFunc(this)" onmouseover="mouseOn(this)" 
        href="/`+Nav_bar[i].href +`">`+Nav_bar[i].name +`
       </a> `
    }
       
    for(let i in Nav_bar ){
      nav_link_smll += `<a class="nav-link"  id="`+Nav_bar[i].id +`" onload="dataADD(this)" onmouseout="mousoutFunc(this)" onmouseover="mouseOn(this)" 
      href="/`+Nav_bar[i].href +`">`+Nav_bar[i].name +`
     </a> `
  }
  
    
   
document.getElementById('nav_link').innerHTML+=nav_link;
document.getElementById('nav_link_smll').innerHTML+=nav_link;
}

nav_bar_add()
//  nav bar functian to show an hide 
function mouseOn(x) {
  navImagBar.style.display = "block";
  x.style.backgroundColor = "#9de2d1";
  let navImag = "";
  if (x.id == "new") { 
      for (let i in newList) {
          navImag +=
              `
              <a class="nav-item nav-link"   href="/new_` +
              newList[i].type +
              `">
              <div class="card nav_sectin_image">
          <img class="card-img-top nav_img_view" src="/static/imag/`+ newList[i].imag + `" alt="Card image cap">
           <div class="card-body">
              <h5 class="card-title"> `+ newList[i].status + newList[i].type + `</h5>
          </div></div> </a>
          `;
      }
  } 
  else if (x.id == "offer") {
          for (let i in offelist) {
          navImag +=
              `
        <a class="nav-item nav-link"   href="/` +
              offelist[i].type +  `">
          <div class="card nav_sectin_image2">
      <img class="card-img-top nav_img_view" src="/static/imag/`+ offelist[i].imag + `" alt="Card image cap">
       <div class="card-body">
          <h5 class="card-title">` +
              offelist[i].status +
              `</h5>
      </div></div> </a>
      `;
      }
  }
  else if (x.id == "topSeller") {
    for (let i in topSeller) {
    navImag +=
        `
  <a class="nav-item nav-link"   href="/` +
  topSeller[i].type +  `">
    <div class="card nav_sectin_image2">
<img class="card-img-top nav_img_view" src="/static/imag/`+ topSeller[i].imag + `" alt="Card image cap">
 <div class="card-body">
    <h5 class="card-title">` +
    topSeller[i].status +
        `</h5>
</div></div> </a>
`;
}
} else if (x.id == "glasses") {
    for (let i in glaslist) {
          navImag +=
              `
              <a class="nav-item nav-link"   href="/glasses_` +
              glaslist[i].type +
              `">
              <div class="card nav_sectin_image">
          <img class="card-img-top nav_img_view" src="/static/imag/`+ glaslist[i].imag + `" alt="Card image cap">
           <div class="card-body">
              <h5 class="card-title"> `+ glaslist[i].status + glaslist[i].type + `</h5>
          </div></div> </a>
   
          `;
      }
  } else if (x.id == "sun") {
       for (let i in sunlist) {
          navImag +=
              `
          <a class="nav-item nav-link"   href="/sun_` +
              sunlist[i].type +
              `">
          <div class="card nav_sectin_image">    
      <img class="card-img-top nav_img_view" src="/static/imag/`+ sunlist[i].imag + `" alt="Card image cap">
       <div class="card-body">
          <h5 class="card-title">` +
              sunlist[i].status + sunlist[i].type +
              `</h5>
      </div></div> </a>
      `;
      }
  } else if (x.id == "contactLenses") {
      for (let i in contactLenses) {
          navImag +=
              `
          <a class="nav-item nav-link"   href="/ContactLens_` +
              contactLenses[i].type +
              `">
          <div class="card nav_sectin_image2">
              
      <img class="card-img-top nav_img_view" src="/static/imag/`+ contactLenses[i].imag + `" alt="Card image cap">
       <div class="card-body">
          <h5 class="card-title">` +
              contactLenses[i].status + contactLenses[i].type +
              `</h5>
      
      </div></div> </a>

      `;
      }
  } else if (x.id == "accessory") {
      for (let i in accessory) {
          navImag +=
              `
          <a class="nav-item nav-link"   href="/Accessories_` +
              accessory[i].type +
              `">
          <div class="card nav_sectin_image2">
              
      <img class="card-img-top nav_img_view" src="/static/imag/`+ accessory[i].imag + `" alt="Card image cap">
       <div class="card-body">
          <h5 class="card-title">` +
              accessory[i].status + accessory[i].type +
              `</h5>
      </div></div> </a>
      `;
      }
  }
  navImagBar.innerHTML = navImag;
}






// get loctian and add to input 
const x = document.getElementById("location");
var locitanHerf=document.getElementById("locitanHerf")
// x.onblur = function () {
// }
   {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}
function getLocation(){
if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(showPosition);
} else { 
  x.innerHTML = "Geolocation is not supported by this browser.";
}
}


function showPosition(position) {
  let url='https://maps.google.com/?q='+position.coords.latitude + ","+
  position.coords.longitude;
  locitanHerf.href=url
  x.value =url
   
}

//  script for user pag vie invic and order track
OrderTrackhead=document.getElementById("OrderTrackhead")
OrderTrackhead.onclick = function () {
  if( document.getElementById("OrderTrackbody").style.display == "none")
  {
    document.getElementById("OrderTrackbody").style.display = "block";
  }else if( document.getElementById("OrderTrackbody").style.display == "block"){
    document.getElementById("OrderTrackbody").style.display = "none";
  }
}

OrderDatileshead=document.getElementById("OrderDatileshead")
OrderDatileshead.onclick = function () {
if( document.getElementById("OrderDatilesbody").style.display == "none")
{
  document.getElementById("OrderDatilesbody").style.display = "block";
}else if( document.getElementById("OrderDatilesbody").style.display == "block"){
  document.getElementById("OrderDatilesbody").style.display = "none";
}
}

eyeTest=document.getElementById("eyeTest")
eyeTest.onclick = function () {
if( document.getElementById("eyeTestbody").style.display == "none")
{
  document.getElementById("eyeTestbody").style.display = "block";
}else if( document.getElementById("eyeTestbody").style.display == "block"){
  document.getElementById("eyeTestbody").style.display = "none";
}
}

listviwer=['Company',  'Invoice' ,  'Branchs' , 'Broduct', 'Bayment' , 'Brands','Orders' , 'Users', ]

function displayDataOn(e){
  var id=e.id
  var body='body'+id
if( document.getElementById(body).style.display == "none")
{
  document.getElementById(body).style.display = "block";
}else if( document.getElementById(body).style.display == "block"){
  document.getElementById(body).style.display = "none";
}

}

function displayDataOff(e) {

  let id=e.id
  document.getElementById(id).style.display = "none";


}

//  script for cart page 
async function removeiteam(iteam) {

  if (iteam.id != null) {
      console.log("i", iteam.id)

      let response = await fetch('/cart?qcard=' + iteam.id);
      let shows = await response.json();
      console.log(shows)
      location.href = location.href;
  }
}

async function get_dat(iteam) {


  if (iteam.id != null) {
      let datil = [iteam.id, iteam.value]
      let response = await fetch('/cart?updat=' + datil);
      let shows = await response.json();
      if (shows == 'EDit') {
          console.log(shows)
          location.href = location.href;


      }


  }

}

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})