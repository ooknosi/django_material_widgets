let checkboxes = document.querySelectorAll('.mdc-checkbox');
for (let i = 0, checkbox; checkbox = checkboxes[i]; i++) {
  mdc.checkbox.MDCCheckbox.attachTo(checkbox);
}
