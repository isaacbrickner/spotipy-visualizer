const ctx = document.getElementById('attributeChart');


(async function danceabilityChart() {

  const data = await fetch("http://localhost:5000/songFeatures").then(response => response.json());
  new Chart(
    document.getElementById('attributeChart'),
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
})();

export async function createEnergyChart() {
  const ctx = document.getElementById('energyChart');

  const data = await fetch("http://localhost:5000/songFeatures").then(response => response.json());
  new Chart(
    document.getElementById('energyChart'),
    {
      type: 'bar',
      data: {
        labels: data.map(row => row.song_name), 
        datasets: [
          {
            label: 'Energy',
            data: data.map(row => row.energy
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
();
}



  


