const edits = document.querySelectorAll('[id^="edit-"]')
    const saves = document.querySelectorAll('[id^="save-"]')
    const cancels = document.querySelectorAll('[id^="cancel-"]')

function edit() {
    edits.forEach((edit, index) => {
        edit.addEventListener("click", event => {
            saves[index].classList.remove("d-none");
            cancels[index].classList.remove("d-none");
        })
    });
}

function cancel() {
    cancels.forEach((cancel, index) => {
        cancel.addEventListener("click", event => {
            saves[index].classList.add("d-none");
            cancels[index].classList.add("d-none");
        })
    });
}
document.addEventListener("DOMContentLoaded", edit);
document.addEventListener("DOMContentLoaded", cancel)