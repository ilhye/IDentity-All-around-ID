function toggleEditState(id, state) {
  const edit = document.getElementById(`edit-${id}`);
  const save = document.getElementById(`save-${id}`);
  const cancel = document.getElementById(`cancel-${id}`);

  if (state === "edit") {
    save.classList.remove("d-none");
    cancel.classList.remove("d-none");
  } else if (state === "cancel") {
    save.classList.add("d-none");
    cancel.classList.add("d-none");
  }
}
