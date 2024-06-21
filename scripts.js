document.getElementById('download-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const url = document.getElementById('url').value;
    const output = document.getElementById('output');

    fetch(`/api/download?url=${encodeURIComponent(url)}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                output.innerHTML = `<p>Download started: <a href="${data.downloadUrl}">Download Link</a></p>`;
            } else {
                output.innerHTML = `<p>Error: ${data.error}</p>`;
            }
        })
        .catch(error => {
            output.innerHTML = `<p>Error: ${error.message}</p>`;
        });
});
