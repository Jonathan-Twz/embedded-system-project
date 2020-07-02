setInterval(function(){
    $.ajax({
        type: "get",
        url: "/getData",
        dataType: "json",
        success: function(data){document.getElementById('temperature').innerHTML=data[1];
                                document.getElementById('humidity').innerHTML=data[2];
                                document.getElementById('light').innerHTML=data[3];
                                document.getElementById('gas').innerHTML=data[4];
                                document.getElementById('rain').innerHTML=data[5];
                                document.getElementById('voice').innerHTML=data[6];
                                document.getElementById('track').innerHTML=data[7];
                                document.getElementById('alert_flag').innerHTML=data[8];
                                }
    })
},1000);