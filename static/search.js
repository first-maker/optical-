
  search_value = document.querySelector('#search');
  search_value.addEventListener('input', async function() {
     console.log(search_value.value)

      let response = await fetch('/search?value=' + search_value.value);
      let data = await response.json();
      let html = '';
      console.log(data)
      
      for (let i in data) {
          // let type = data[id].type.replace('<', '&lt;').replace('&', '&amp;');
          html +=

          `
          <div class="card card-view" >
          <img class="card-img-top img_view" id="`+ data[i].media_id + `" src=static/uploads/` + data[i].imagelink + ` alt="` + data[i].imagelink + `" >
          <div class="top-left top-left p-2 bg-danger text-bg-dark " >`+ data[i].discount + `%</div>
          <div class="card-body"> 
          <h5 class="card-title" style="float: left;">` +data[i].brand_name.toUpperCase() +` `  +  data[i].framCotegery.toUpperCase() +` for ` +  data[i].Collection_name+ `</h5>
          <div style="clear:both;"></div>
          <p class="card-text" style="float: left;" >Before <s style="color: red;">`+ Number(data[i].retialPrice) + ` SR</s> </p>
          <p style="float: right;">Now `+ (Number(data[i].retialPrice) - (Number(data[i].retialPrice) * (Number(data[i].discount / 100)))) + ` SR </p>
          <div style="clear:both;"></div>
          
          <form action="/item"  method="post"> 
          <input type="text" name="item_id" value="`+ data[i].product_id + ` " hidden >
          
          <div class="middle"> <div class="text">
          <button class="btn"   type="submit">View</button>
          </div></div>
          </form>
          
          <form action="/cart"  method="POST"> 
          <input type="text" name="cart_id" value="`+ data[i].product_id + `" hidden >
          <button class="btn btn-outline-info"  style="float: left;"   type="submit">Add cart</button>
          </form>
          <p  class="card-text float-end bg-info p-2  rounded-circle"   > `+data[i].framCotegeryHistory+`</p>
          </div>
          </div>
          `
          };
      if(search_value.value.length > 0){
        document.querySelector('#ul').innerHTML = html;
        document.querySelector('#ul').style.display = "block";
        document.querySelector("#card_main").style.display = "none";
        document.querySelector("#crad_iteam").style.display = "none";
        document.querySelector("#cartpage").style.display = "none";
      }else{
        document.querySelector("#ul").style.display = "none";
        document.querySelector("#card_main").style.display = "block";
        document.querySelector("#crad_iteam").style.display = "block";
        document.querySelector("#cartpage").style.display = "block";
      }
      
     
  });

  var search_btn = document.getElementById("search_btn");
  search_btn.onclick = function() {
    if (document.getElementById("search_sectin").style.display === "block") {
      document.getElementById("search_sectin").style.display = "none";   
    } else {
      document.getElementById("search_sectin").style.display = "block";
      document.getElementById("navImagBar").style.display = "none";
    }
    console.log(document.getElementById("search_sectin").style.display);
  };
  

