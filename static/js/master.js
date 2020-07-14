
let update_buttons  = document.getElementsByClassName('update-choices');
let choice_buttons  = document.getElementsByName('choices');

var url = '/testseries/update-choice/';

// for(var i=0;i<update_buttons.length;i++){
//     update_buttons[i].addEventListener("click", function(){
      
//         console.log(this);
//         console.log(this.dataset.value);
//         if(user==='Anonymoususer'){
//             console.log("Not authenticated yet");
//         }
//         else{
//             console.log("User",user);
//             // update_choice(this.dataset.choice,this.dataset.value);
//         }
//       });
// }
for(var i=0;i<choice_buttons.length;i++){
  if(choice_buttons[i].value!=="None"){
    choice_buttons[i].checked = true;
    console.log(choice_buttons[i])
  }
  choice_buttons[i].addEventListener("click", function(){
      
      console.log(this.dataset.choice);
      console.log(this.dataset.value);

      if(user==='Anonymoususer'){
          console.log("Not authenticated yet");
      }
      else{
        console.log("User",user);
        update_choice(this.dataset.choice,this.dataset.value);
      }
    });
}



function update_choice(choice_id,value){
  console.log("Update choice function called")
    fetch(url, {
        method: 'POST', 
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken':csrftoken,
        },
       
        body: JSON.stringify({'choice_id':choice_id,'value':value}) 
      }).then(response => response.json())
      .then(data => {
        console.log('Success:', data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
      
}

