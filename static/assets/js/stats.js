

  

// function to render chart
const renderChart=(data, labels)=>{
 const ctx = document.getElementById('expenseChart').getContext("2d");

  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: labels,
      datasets: [{
        label: "Last 6 months expenses",
        data: data,
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        borderColor: "rgba(75, 192, 192, 1)",
        borderWidth: 1
      }],
    },
    options: {
      title:{
        display: true,
        text: "Expenses per category",
      },
    },
  });

 };


// Fetching data from expense_category_summary end point
const getChartData = ()=> {
  console.log("Fetching....");
  fetch("/expense_category_summary")
    .then((res)=>res.json())
    .then((results) => { 
      console.log("results", results);
      const category_data= results.expense_category_data;
      const [labels, data] =[
        Object.keys(category_data), 
        Object.values(category_data)]


      renderChart(data, labels);
    });
};
window.onload=getChartData();
 