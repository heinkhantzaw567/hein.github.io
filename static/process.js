document.addEventListener("DOMContentLoaded", () => {
    let input_elements = document.querySelectorAll("input[type='text']");

    input_elements.forEach(input_element => {
        input_element.addEventListener("keyup", () => {
            input_element.setAttribute("value", input_element.value);
        });
    });
});
document.addEventListener('DOMContentLoaded', function() {
    const today = new Date().toISOString().split('T')[0]; // Get today's date in YYYY-MM-DD format
    document.getElementById('dueDate').min = today;
});
function toggleForm(formId) {
    var form = document.getElementById(formId);
    var loginButton = document.getElementById("loginbutton");
    var signinButton = document.getElementById("signinbutton");

    if (form.style.display === "none") {
        form.style.display = "block";
        loginButton.style.display = "none";
        signinButton.style.display = "none";
    } else {
        form.style.display = "none";
        loginButton.style.display = "block";
        signinButton.style.display = "block";
    }
  }
  function deleteTask(checkbox) {
    var taskIdToDelete = checkbox.getAttribute('data-id');
    var row = checkbox.parentNode.parentNode;
    row.parentNode.removeChild(row);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/', true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.send('delete_checkbox=' + taskIdToDelete);
}
