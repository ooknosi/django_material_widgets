let sliders = document.querySelectorAll('.mdc-slider');
for (let i = 0, slider; slider = sliders[i]; i++) {
  let material_slider = new mdc.slider.MDCSlider(slider);
  material_slider.listen('MDCSlider:change', () => document.getElementById(slider.dataset.id).value = material_slider.value);
}
