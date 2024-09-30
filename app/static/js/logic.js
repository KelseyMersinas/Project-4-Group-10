$(document).ready(function () {
  console.log("Page Loaded");

  $("#submit").click(function (event) {
    // alert("button clicked!");
    console.log("clicked");
    event.preventDefault();
    makePredictions(event);
  });
});

$("#cap_diameter").change(function handleCapSliderChange(event) {
  const { target } = event; // event = { target: foo }
  const { value } = target; // target = { value: bar }
  const $labelSpan = $("#cap_diameter_value");
  $labelSpan.text(value);
});

function makePredictions() {
  // get the options for the form
  const cap_shape = $("#cap_shape").val();
  const gill_attachment = $("#gill_attachment").val();
  const gill_color = $("#gill_color").val();
  const season = $("#season").val();
  const stem_color = $("#stem_color").val();

  // Get the slider values
  const cap_diameter = $("#cap_diameter").val();
  const stem_height = $("#stem_height").val();
  const stem_width = $("#stem_width").val();

  // create the payload
  const payload = {
    cap_shape, // shorthand object syntax (vars are expanded to represent the key)
    gill_attachment,
    gill_color,
    season,
    stem_color,
    cap_diameter,
    stem_height,
    stem_width,
  };

  console.log(payload);

  fetch("/makePredictions", {
    body: JSON.stringify({ data: payload }),
    headers: {
      "Content-Type": "application/json",
    },
    method: "POST",
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      if (data.ok) {
        // Display the predictions in the result div
        document.getElementById(
          "result"
        ).innerText = `Prediction: ${data.predictions[0]}`;
      } else {
        document.getElementById("result").innerText = `Error: ${data.error}`;
      }
    })
    .catch((error) => {
      console.error(error);
    });
}
