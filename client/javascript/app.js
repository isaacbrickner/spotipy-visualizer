

function getSongFeatures() {
    const response = fetch("http://localhost:5000/songFeatures");
    const movies = response.json();
    console.log(movies);
    return movies;
  }


    let songFeatureButton = document.getElementById("test")

    let songFeatureParagraph = document.getElementById("songFeatures")

    const htmlContent = 
    ''

  songFeatureHTML.addEventListener("click", () => {
    const jsonString = JSON.stringify(getSongFeatures(), null, 2);
    console.log(jsonString)
    songFeatureParagraph.innerHTML = jsonString
});


  