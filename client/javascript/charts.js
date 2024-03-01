const ctx = document.getElementById('attributeChart');

  const data = await fetch("http://localhost:5000/songFeatures").then(response => response.json());
  new Chart(
    ctx,
    {
      type: 'bar',
      data: {
        labels: data.map(row => row.song_name), 
        datasets: [
          {
            label: 'Danceability',
            data: data.map(row => row.danceability
            )
          }
        ]
      },
      options: {
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
    }
  );




  


