/**OCULTA LA OPCION DE PAGO DEBITO */
$("#rutdepagodeb").hide();

/**OCULTA LA OPCION DE PAGO CREDITO */
$("#selectcredito").hide();


$("#btndebito").click(function(){
    $("#imgpago").hide();
    $("#selectcredito").hide();
    $("#rutdepagodeb").show();
});

$("#btncredito").click(function(){
    $("#imgpago").hide();
    $("#rutdepagodeb").hide();
    $("#selectcredito").show();
});


