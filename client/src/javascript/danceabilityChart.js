(async function() {
    const data = await fetch("http://127.0.0.1:5000/songFeatures").then(response => response.json());
  
    new Chart(document.getElementById('danceabilityChart'), 
  {
    type: 'bar',
    data: {
      labels: data.map(row => row.song_name), 
      datasets: [
        {
          label: 'Danceability',
          data: data.map(row => row.danceability)
        }
      ]
    },
    options: {
      responsive: true,
      scales: {
        xAxes: [{
          ticks: {
            maxRotation: 50,
            minRotation: 30,
            padding: 10,
            autoSkip: false,
            fontSize: 10
          }
        }]
      }
    }
  });
  })();