const selectManagers = document.querySelectorAll('.mdc-select-manager');
for (let i = 0, selectManager; selectManager = selectManagers[i]; i++) {
  let selects = {
    material: mdc.select.MDCSelect.attachTo(selectManager.querySelector('.mdc-select[role="listbox"]')),
    native: selectManager.querySelector('select.mdc-select')
  };
  let changeHandler = ({type}) => {
    let changedSelect, selectToUpdate, value;
    if (type === 'MDCSelect:change') {
      changedSelect = selects.material;
      selectToUpdate = selects.native;
      value = changedSelect.selectedOptions[0].id;
    } else {
      changeSelect = selects.native;
      selectToUpdate = selects.material;
      value = changedSelect.selectedOptions[0].value;
    }
    selectToUpdate.selectedIndex = changedSelect.selectedIndex;
  };
  selects.material.listen('MDCSelect:change', changeHandler);
  selects.native.addEventListener('change', changeHandler);
};
