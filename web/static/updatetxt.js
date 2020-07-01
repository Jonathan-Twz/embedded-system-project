setInterval(function(){
    $.ajax({
        type: "get",
        url: "/getData",
        dataType: "json",
        success: function(data){document.getElementById('temperature').innerHTML=data[1];
                                document.getElementById('humidity').innerHTML=data[2];
                                }
    })
},1000);