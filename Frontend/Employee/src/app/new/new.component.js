document.addEventListener("DOMContentLoaded", function () {
    // Bar Chart (Employee Strength)
    var ctx1 = document.getElementById("barChart").getContext("2d");
    new Chart(ctx1, {
        type: "bar",
        data: {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            datasets: [{
                label: "Employee Strength",
                data: [200, 300, 400, 450, 350, 250],
                backgroundColor: ["#f39c12", "#2ecc71", "#3498db", "#e74c3c", "#9b59b6", "#1abc9c"]
            }]
        }
    });

    // Pie Chart (Leave & On-Duty)
    var ctx2 = document.getElementById("pieChart").getContext("2d");
    new Chart(ctx2, {
        type: "pie",
        data: {
            labels: ["EL", "CL", "SL", "Medical", "LOP", "OD"],
            datasets: [{
                data: [10, 15, 12, 8, 5, 10],
                backgroundColor: ["#3498db", "#e74c3c", "#2ecc71", "#f1c40f", "#9b59b6", "#1abc9c"]
            }]
        }
    });
});