
let btns = document.getElementsByClassName('addtocart');
for(let i=0;i<btns.length;i++){
   btns[i].addEventListener('click',function(){
       let book_id = this.dataset.book;
       let action = this.dataset.action;
    //    debugger;
    //    location.reload()
       
       
       if (user === "AnonymousUser"){
           console.log("user is not logged in");

        }
        else{
            updateCart(book_id,action);
            checkout(book_id);
        }
   }) 
}

function updateCart(book_id,action,quantity){
    let url = "/updateCart"
    fetch(url, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken":csrftoken,
        },
        body: JSON.stringify({"book_id":book_id, "action": action,"quantity":quantity})
    })
    .then(response => response.json())
    .then(data => console.log(data))
}

let quantityField = document.getElementsByClassName('quantity');
for(let i=0;i<quantityField.length;i++){
    quantityField[i].addEventListener('change',function(){
        let quantityFieldValue = quantityField[i].value;
        let quantityFieldBook = quantityField[i].parentElement.parentElement.children[1].children[0].innerText;
        location.reload();
        let url = "/updatequantity";
        fetch(url,{
            method: 'POST',
            headers:{
                "Content-Type":"application/json",
                "X-CSRFToken":csrftoken,
            },
            body:JSON.stringify({"qfv":quantityFieldValue,"qfp":quantityFieldBook})
        })
        .then(respons => response.json())
        .then(data => console.log(data))
    });
}

// $('.delete-cart-item').on('click',function(e){
//     e.preventDefault();
//     var cartItemId = $(this).attr('data-cartitem');
//     debugger;
//     $.ajax({
//         type:'POST',
//         url:"/deletecartitem/"+cartItemId,
//         beforeSend: function(xhr){
//             xhr.setRequestHeader("X-CSRFToken",getCookie("csrftoken")); 
//         },
       
//     });
// });


