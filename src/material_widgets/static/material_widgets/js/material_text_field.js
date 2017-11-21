let textfields = document.querySelectorAll('.mdc-text-field');
for (let i = 0, textfield; textfield = textfields[i]; i++) {
  mdc.textField.MDCTextField.attachTo(textfield);
}
