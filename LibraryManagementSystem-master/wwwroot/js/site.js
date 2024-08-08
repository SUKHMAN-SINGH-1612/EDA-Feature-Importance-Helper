// wwwroot/js/site.js
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function () {
        console.log('Text copied to clipboard');
    }).catch(function (err) {
        console.error('Failed to copy text: ', err);
    });
}
