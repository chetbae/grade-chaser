function convertGrade() {
    const gradeValue = document.getElementById('grade').value;
    const gradeSystem = document.getElementById('system').value;

    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                document.getElementById('convertedGrade').textContent = xhr.responseText;
            } else {
                document.getElementById('convertedGrade').textContent = 'Grade not found.';
            }
        }
    };

    const url = `/convert?grade=${gradeValue}&system=${gradeSystem}`;
    xhr.open('GET', url, true);
    xhr.send();
}
