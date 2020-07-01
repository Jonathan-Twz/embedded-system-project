setInterval(function(){
    $.ajax({
        type: "get",
        url: "/gettest",
        dataType: "json",
        success: function(data){document.getElementById('test').innerHTML=data[0];}
    })
},1000);