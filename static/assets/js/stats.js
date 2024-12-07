

  

// function to render chart
const renderChart = (data, lable)=>{
    const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'pie',
    data: {
      labels: lables,
      datasets: [{
        label: 'last 6 months expenses',
        data: data,
        borderWidth: 1
      }]
    },
    options: {
      title:{
        display:true,
        text:'Expenses per category'
      }
    }
  });


}

const getChartData=()=>{
    console.log("fetching");
    fetch("/expense_category_summary").then(res=>res.json()).then(results=>{
        console.log("results",results);
        renderChart([],[]);

    })
    
}
document.onload=getChartData();

  
 