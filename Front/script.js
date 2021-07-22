
document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#filtro-fechai').addEventListener('input', captura_filtros );
    document.querySelector('#filtro-fechaf').addEventListener('input', captura_filtros );
    document.querySelector('#filtro-pelicula').addEventListener('input', captura_filtros);
    document.querySelector('#filtro-usuario').addEventListener('input', captura_filtros );
    cargaDatos()
    cargaPki();
    
  });

function renderCharts(){
  const ctx= document.querySelector("#chart").getContext("2d")
  return ctx;
  //totalCasesChart(data, ctx)
}
function totalCasesChart(items, ctx) {
  console.log("holii",items.map(x=> x.date))
    var chart = new Chart(ctx, {
        type:'line',
        data:{
            labels:items.map(x=> x.date) ,//[1,20,30,70],
            datasets:[
                {
                    label:"score",
                    data:items.map(x=>x.score)
                }
                

            ]
        },
        options: {
          scales: {
            xAxes: [{
              gridLines: {
                display: false,
              }
            }]
          },
          title: {
            display: true,
            text: 'Score vs Date',
            fontSize: 30,
            padding: 30,
            fontColor: '#12619c',
          },
          legend: {
            position: 'bottom',
            labels: {
              padding: 20,
              boxWidth: 15,
              fontFamily: 'system-ui',
              fontColor: 'black',
            }
          },
          layout: {
            padding: {
              right: 50,
            }

        },
        tooltips: {
          backgroundColor: '#0584f6',
          titleFontSize: 20,
          xPadding: 20,
          yPadding: 20,
          bodyFontSize: 15,
          bodySpacing: 10,
          mode: 'x',
        },
        elements: {
          line: {
            borderWidth: 8,
            fill: false,
          },
          point: {
            radius: 6,
            borderWidth: 4,
            backgroundColor: 'white',
            hoverRadius: 8,
            hoverBorderWidth: 4,
          }}
      
      
      }
        
        
    })
    console.log("antes de actu")
    chart.update();
}
function captura_filtros(e){
  console.log(e.target.value)
  cargaDatos();
  cargaPki();
}

function cargaDatos() {
    //http://localhost:8000/tab1?fechai=2000-01-25&fechaf=2020-12-25&movie=&usuario
    var fechai = document.querySelector('#filtro-fechai').value;
    var fechaf = document.querySelector('#filtro-fechaf').value;
    var pelicula = document.querySelector('#filtro-pelicula').value;
    var usuario = document.querySelector('#filtro-usuario').value;
    const userURL = `http://localhost:8000/tab1?fechai=${fechai}&fechaf=${fechaf}&movie=${pelicula}&user=${usuario}`
    console.log(userURL)
    fetch( userURL, {
      method: "GET",
      headers: {"Content-type": "application/json;charset=UTF-8"}
    })
    .then(response=> 
        response.json()
        )
    .then(items=>
      
      
     {
       tabla(items)
  });

  //tabla menor score
  const userURL2 = `http://localhost:8000/tab2?fechai=${fechai}&fechaf=${fechaf}&movie=${pelicula}&user=${usuario}`
    console.log(userURL2)
    fetch( userURL2, {
      method: "GET",
      headers: {"Content-type": "application/json;charset=UTF-8"}
    })
    .then(response=> 
        response.json()
        )
    .then(items2=>
      
      
     {
       tabla2(items2)

  });

      //grafico
    //const userURL3 = `http://localhost:8000/gra?fechai=${fechai}&fechaf=${fechaf}&movie=${pelicula}&user=${usuario}`
    const userURL3="http://localhost:8000/gra?fechai=2000-01-25&fechaf=2021-07-22&user=AK2AQIULQDFS5"
    console.log(userURL3)
    fetch( userURL3, {
      method: "GET",
      headers: {"Content-type": "application/json;charset=UTF-8"}
    })
    .then(response=> 
        response.json()
        )
    .then(items3=>
      
      
    {
      console.log("grafico",items3)
      let ctx=renderCharts()
      totalCasesChart(items3, ctx)
  });
    
  }

function tabla(item){
  console.log("nuevos items .tabla1",item)
   $(function () {
    $('#table').bootstrapTable({
        data: item
    });
    $('#table').bootstrapTable('load', item);
    });
  
}
function tabla2(item){
  console.log("nuevos items - tabla 2",item)
  $(function () {
    $('#table2').bootstrapTable({
        data: item
    });
    $('#table2').bootstrapTable('load', item);
  });
}

function cargaPki() {
   let fechai = document.querySelector('#filtro-fechai').value;
   let fechaf = document.querySelector('#filtro-fechaf').value;
   let pelicula = document.querySelector('#filtro-pelicula').value;
   let usuario = document.querySelector('#filtro-usuario').value;

  const userURL = `http://localhost:8000/pki?fechai=${fechai}&fechaf=${fechaf}&movie=${pelicula}&user=${usuario}`
  fetch( userURL, {
    method: "GET",
    headers: {"Content-type": "application/json;charset=UTF-8"}
  })
  .then(response=> 
      response.json()
      )
  .then(users=>
    
    
   {
    users.forEach((item) => {
      console.log(item)
     
      indicadores(item)


    });
});

}

function indicadores(item){
  console.log("----NUEVOS-INDICADORES",item)
  let score_avg=""
   document.querySelector('.score-avg').innerHTML=""
   document.querySelector('.users-number').innerHTML=`${item["users"]}`
   document.querySelector('.score-min').innerHTML=`${item["min"]}`;
   document.querySelector('.score-max').innerHTML=`${item["max"]}`;
   //comprobar nulos
   if( item["prom"]!== null) {
    score_avg=item["prom"].toFixed(2) 
  }
   document.querySelector('.score-avg').innerHTML=`${score_avg}`;


}