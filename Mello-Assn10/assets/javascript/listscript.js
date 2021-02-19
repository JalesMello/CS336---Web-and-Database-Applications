//   Name: Jales H. Mello
//   Assignment: CS336 Assignment #8
//   Created: 4/20/17
//  Description: This page contains the Javascript code for the admin.html page.
//----------------------------------------------------------------------------------------------------------------------
// execute variables and event listeners after the page loads....
window.onload = function () {
    // function to look for checked radio button and open correct page
    function checkButton(radios) {
        var wasChecked = false;
        for(var i = 0, length = radios.length; i < length; i++){
            if(radios[i].checked){
                window.open("participantlists/" + radios[i].value);
                wasChecked = true;
            }
        }
        if(!wasChecked)
            alert("Error. No option was selected. Please select an option.");
    }

    // variables
    var workshopRadio = document.getElementsByName('workshop');
    var mealsRadio = document.getElementsByName('meals');
    var allRadio = document.getElementsByName('all');
    var workshopS = document.getElementById('workshopSubmit');
    var mealsS = document.getElementById('mealsSubmit');
    var allS = document.getElementById('allSubmit');

    // event listeners
    workshopS.addEventListener('click', function (){checkButton(workshopRadio)}, false);
    mealsS.addEventListener('click', function (){checkButton(mealsRadio)}, false);
    allS.addEventListener('click', function (){checkButton(allRadio)}, false);
};
