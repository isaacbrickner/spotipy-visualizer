// import {Chart} from '/chart.js/auto'

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

    (async function() {
      const data = await fetch("http://127.0.0.1:5000/songFeatures").then(response => response.json());
    
      new Chart(document.getElementById('energyChart'), 
    {
      type: 'bar',
      data: {
        labels: data.map(row => row.song_name), 
        datasets: [
          {
            label: 'Energy',
            data: data.map(row => row.energy)
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

    (async function() {
      const data = await fetch("http://127.0.0.1:5000/songFeatures").then(response => response.json());
    
      new Chart(document.getElementById('livenessChart'), 
    {
      type: 'bar',
      data: {
        labels: data.map(row => row.song_name), 
        datasets: [
          {
            label: 'Liveness',
            data: data.map(row => row.liveness)
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
     

    (async function() {
      const data = await fetch("http://127.0.0.1:5000/songFeatures").then(response => response.json());
    
      new Chart(document.getElementById('loudnessChart'), 
    {
      type: 'bar',
      data: {
        labels: data.map(row => row.song_name), 
        datasets: [
          {
            label: 'Loudness',
            data: data.map(row => row.loudness)
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
     

    (async function() {
      const data = await fetch("http://127.0.0.1:5000/songFeatures").then(response => response.json());
    
      new Chart(document.getElementById('instrumentalnessChart'), 
    {
      type: 'bar',
      data: {
        labels: data.map(row => row.song_name), 
        datasets: [
          {
            label: 'Instrumentalness',
            data: data.map(row => row.instrumentalness)
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
     

    (async function() {
      const data = await fetch("http://127.0.0.1:5000/songFeatures").then(response => response.json());
    
      new Chart(document.getElementById('speechinessChart'), 
    {
      type: 'bar',
      data: {
        labels: data.map(row => row.song_name), 
        datasets: [
          {
            label: 'Speechiness',
            data: data.map(row => row.speechiness)
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
     

    (async function() {
      const data = await fetch("http://127.0.0.1:5000/songFeatures").then(response => response.json());
    
      new Chart(document.getElementById('tempoChart'), 
    {
      type: 'bar',
      data: {
        labels: data.map(row => row.song_name), 
        datasets: [
          {
            label: 'Tempo',
            data: data.map(row => row.tempo)
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

    (async function() {
      const data = await fetch("http://127.0.0.1:5000/songFeatures").then(response => response.json());
    
      new Chart(document.getElementById('valenceChart'), 
    {
      type: 'bar',
      data: {
        labels: data.map(row => row.song_name), 
        datasets: [
          {
            label: 'Valence',
            data: data.map(row => row.valence)
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
     
     
     