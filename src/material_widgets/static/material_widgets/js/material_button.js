let buttons = document.querySelectorAll('.mdc-button');
for (let i = 0, button; button= buttons[i]; i++) {
  mdc.ripple.MDCRipple.attachTo(button);
}
