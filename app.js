function get_gender() {
  var gender = document.getElementsByName("gender");
  for(var i in gender) {
    if(gender[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function predict() {
  console.log("predict_disease button clicked");
  var age = document.getElementById("age");
  var gender = get_gender();
  var symptoms1 = document.getElementById("symptoms1").value;
  var symptoms2 = document.getElementById("symptoms2").value;
  var symptoms3 = document.getElementById("symptoms3").value;
  var symptoms4 = document.getElementById("symptoms4").value;
  var symptoms5 = document.getElementById("symptoms5").value;
  var symptoms6 = document.getElementById("symptoms6").value;
  var symptoms=[symptoms1,symptoms2,symptoms3,symptoms4,symptoms5,symptoms6]
  console.log(symptoms)
  var disease = document.getElementById("predict_disease");
  var medicine = document.getElementById("medicine");
  // var url = "http://127.0.0.1:5000/predict"; //Use this if you are NOT using nginx which is first 7 tutorials
  var url = "http://127.0.0.1:5000/predict"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      age:parseInt(age.value),
      gender:gender,
      symptoms:symptoms
//      sqft: parseFloat(sqft.value),
//      bhk: bhk,
//      bath: bathrooms,
//      location: location.value
  },function(data, status) {
      console.log(data.disease);
      predict_disease.innerHTML = "<h2>" + data.disease.toString() ;
      console.log(status);
  });
}

function predict_drug() {
  console.log("predict_disease button clicked");
  var age = document.getElementById("age");
  var gender = get_gender();

  
  var resultElement = document.getElementById("predict_drug");
  //var medicine = document.getElementById("medicine");
  // var url = "http://127.0.0.1:5000/predict"; //Use this if you are NOT using nginx which is first 7 tutorials
  var url = "http://127.0.0.1:5000/predict_drug"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      age:parseInt(age.value),
      gender:gender,
      
//      sqft: parseFloat(sqft.value),
//      bhk: bhk,
//      bath: bathrooms,
//      location: location.value
  },function(data, status) {
      console.log(data.drug);
      resultElement.innerHTML = "<h2>" +Object.values(data.drug)[0] ;
      console.log(status);
  });
}
function onPageLoad() {
  console.log( "document loaded" );
  // var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  var url = "http://127.0.0.1:5000/get_symptoms_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      console.log("got response for get_location request", data, status);
      if(data) {
          var symp = data.symptoms;
          var symptom = document.getElementsByName("symptoms");
          console.log(data.symptoms);
          $('select[name="symptoms"]').empty();
          for(var i in symp) {
              //console.log(locations[i]);
              var opt = new Option(symp[i]);
              //$('#symptom').append(opt);
              $('select[name="symptoms"]').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;