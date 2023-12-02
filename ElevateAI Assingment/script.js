document.getElementById('summarizeButton').addEventListener('click', function() {
    let inputText = document.getElementById('textInput').value;
    document.getElementById('loadingIndicator').style.display = 'block'; // Show loading indicator

    fetch('http://127.0.0.1:5000/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: inputText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('loadingIndicator').style.display = 'none'; // Hide loading indicator
        document.getElementById('summaryOutput').innerText = data.summary || 'Error in summarization';
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('loadingIndicator').style.display = 'none'; // Hide loading indicator
        document.getElementById('summaryOutput').innerText = 'Error in summarization';
    });
});
