// main.js

// Optional enhancements
document.addEventListener("DOMContentLoaded", () => {
    const taskItems = document.querySelectorAll(".task-list li");

    taskItems.forEach(item => {
        item.addEventListener("mouseenter", () => {
            item.style.backgroundColor = "#eaf4ff";
        });

        item.addEventListener("mouseleave", () => {
            item.style.backgroundColor = "#fff";
        });
    });

    // Form date input: highlight past due dates (optional enhancement)
    const dueDateInput = document.querySelector("input[name='due_date']");
    if (dueDateInput) {
        const today = new Date().toISOString().split("T")[0];
        dueDateInput.setAttribute("min", today);
    }
});