
let featuresButton = document.getElementById('songFeatures')
const tableBody = document.getElementById('tableBody')
featuresButton.addEventListener("click", getSongFeatures)

const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });


async function getSongFeatures() {
  await fetch("http://localhost:5000/songFeatures")
    .then(response => response.json())
    .then(json => {
      data = JSON.stringify(json)
      data = JSON.parse(data)
      data.forEach(song => {
        const row = document.createElement('tr')

        const songName = document.createElement('td')
          songName.textContent = song.song_name
          row.appendChild(songName)

          const artistName = document.createElement('td')
          artistName.textContent = song.artist_name
          row.appendChild(artistName)

          const danceability = document.createElement('td')
          danceability.textContent = song.danceability
          row.appendChild(danceability)

          const energy = document.createElement('td')
          energy.textContent = song.energy
          row.appendChild(energy)

          const key = document.createElement('td')
          key.textContent = song.key
          row.appendChild(key)

          const loudness = document.createElement('td')
          loudness.textContent = song.loudness
          row.appendChild(loudness)

          const speechiness = document.createElement('td')
          speechiness.textContent = song.speechiness
          row.appendChild(speechiness)

          const acousticness = document.createElement('td')
          acousticness.textContent = song.acousticness
          row.appendChild(acousticness)

          const instrumentalness = document.createElement('td')
          instrumentalness.textContent = song.instrumentalness
          row.appendChild(instrumentalness)

          const livliness = document.createElement('td')
          livliness.textContent = song.livliness
          row.appendChild(livliness)

          const valence = document.createElement('td')
          valence.textContent = song.valence
          row.appendChild(valence)

          const tempo = document.createElement('td')
          tempo.textContent = song.tempo
          row.appendChild(tempo)

          tableBody.appendChild(row)
      })
    })}

