document.getElementById("prediction-form").addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(this);
    const data = new URLSearchParams(formData);

    const response = await fetch("/predict", {
        method: "POST",
        body: data
    });

    const result = await response.json();
    const trafficLevel = parseInt(result.Traffic_Prediction);
    const trafficMeaning = {
        1: "1 (Very Low: Less than 5 cars)",
        2: "2 (Low: 5 to 15 cars)",
        3: "3 (Moderate: 15 to 30 cars)",
        4: "4 (High: 30 to 50 cars)",
        5: "5 (Very High: More than 50 cars)"
    };

    const displayText = trafficMeaning[trafficLevel] || `${trafficLevel} (Unknown)`;

    document.getElementById("prediction-result").innerText =
        "Predicted Traffic: " + displayText;
});
