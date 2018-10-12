jQuery(document).ready(function(){
  $('form').submit(function(event){
    event.preventDefault()
    voting_form = $("voting_form")

   })
   $('#add_comment').click(function(event){
    $('#commentation').show()
   })
 })


//$(document).ready(function(){  // jquery to run after the html is fully ran
//    $("#startbutton").click(function(event){ //jQuery to hold values submitted when button is clicked
//
//        var playerOne = $("#player1name").val() // Reasign Player Names to new var
//        var playerTwo = $("#player2name").val()
//
//        $("#P1name").text(playerOne) // Display Player names at the HTML selesctor position
//        $("#P2name").text(playerTwo)
//
//        $(".intro").hide();  // Hides introduction
//        $(".gamepagetop").show(); // Displays Console
//    })
//
//    $("#P1roll").click(function(event){
//        Player1.score = throwDice()
//
//
//
//        $("#P1score").text(Player1.score);
//
//        //var p1turnstring = parseInt(p1number) + throwdice()
//        Player1.turnScore()
//
//        $("#P1turn").text(Player1.turn);
//
//        console.log(Player1.turn)
//
//
//
//    });
