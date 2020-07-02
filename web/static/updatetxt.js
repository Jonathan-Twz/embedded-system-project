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

// 日期：<b id="datetime">date and time show here</b><br>
//             温度：<b id='temperature'>None</b>℃ <br>
//             湿度：<b id='humidity'>None</b>% <br>
//             光线：<b id='light'>None</b> <br>
//             雨滴：<b id='rain'>None</b> <br>
//             声音：<b id='voice'>None</b> <br>
//             红外：<b id='track'>None</b> <br>
//             报警：<b id='alert_flag'>None</b> <br></br>