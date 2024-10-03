$(document).ready(function () {
  console.log("Page Loaded");

  $("#submit").click(function (event) {
    // alert("button clicked!");
    console.log("clicked");
    event.preventDefault();
    makePredictions(event);
  });
});

// change slider values to see selection
$("#cap_diameter").on("input", function handleCapSliderChange(event) {
  const { target } = event; // event = { target: foo }
  const { value } = target; // target = { value: bar }
// Divide value by 30
  const adjustedValue = value / 30;
  const $labelSpan = $("#cap_diameter_value");
// Update the label
  $labelSpan.text(adjustedValue.toFixed(2));
});


$("#stem_height").on("input", function handleStemHeightChange(event) {
  const { target } = event;
  const { value } = target;
  const $labelSpan = $("#stem_height_value");
  $labelSpan.text(value);
});

$("#stem_width").on("input", function handleStemWidthChange(event) {
  const { target } = event;
  const { value } = target;
  const $labelSpan = $("#stem_width_value");
  $labelSpan.text(value);
});

// set function for taking values from form
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
    cap_diameter: cap_diameter / 30, 
    stem_height: stem_height / 100, // change the slider value from cm back to m for model consistancy
    stem_width,
  };

  console.log(payload);

  // fetch request
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
