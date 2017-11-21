let radios = document.querySelectorAll('.mdc-radio');
for (let i = 0, radio; radio = radios[i]; i++) {
  mdc.radio.MDCRadio.attachTo(radio);
}
