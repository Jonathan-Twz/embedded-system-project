Highcharts.setOptions({
    global: {
            useUTC: false
    }
});


function activeLastPointToolip(chart) {
    var points = chart.series[0].points;
    chart.tooltip.refresh(points[points.length -1]);
}
var chart = Highcharts.chart('container_rain', {
    chart: {
            type: 'line',
            marginRight: 10,
            events: {
                    load: function () {
                            var series = this.series[0],
                                    chart = this;
                            activeLastPointToolip(chart);
                            setInterval(function(){
                                $.ajax({
                                        type: "get",
                                        url: "/getData",
                                        dataType: "json",
                                        success: function(data){
                                            var x = (new Date()).getTime(), // 当前时间
                                                y = data[5]
                                                series.addPoint([x,y], true, true);
                                                activeLastPointToolip(chart);
                                        }
                                })
                            },1000);
                    }
            }
    },
    title: {
            text: '雨滴图'
    },
    xAxis: {
            type: 'datetime',
            tickPixelInterval: 150
    },
    yAxis: {
            title: {
                    text: null
            }
    },
    tooltip: {
            formatter: function () {
                    return '<b>' + this.series.name + '</b><br/>' +
                            Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                            Highcharts.numberFormat(this.y, 2);
            }
    },
    legend: {
            enabled: false
    },
    series: [{
            name: '雨滴数据',
            data: (function () {
                    // 生成随机值
                    var data = [],
                            time = (new Date()).getTime(),
                            i;
                    for (i = -19; i <= 0; i += 1) {
                            data.push({
                                    x: time + i * 1000,
                                    // y: Math.random()
                                    y: 0 // original data
                            });
                    }
                    return data;
            }())
    }]
});