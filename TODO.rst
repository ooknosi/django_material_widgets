=====
To Do
=====

* Implement <noscript> and no-js fallback

* Disabled fields and options

    * material_select_js.html change tabindex to -1 if disabled

* Rearrange error position to appear below field? https://code.djangoproject.com/wiki/TemplatedForm

* Test possible bug in clearable_file_input due to <a> instead of <label>


Known Bugs
----------
* <label> does not have mouse hover highlight due to MDC error when JS is activated. Seen in MaterialClearableFileInput widget.

* <label> does not have tab highlight. Seen in MaterialClearableFileInput widget.

* autofocus does not trigger help_text on field

* non-textfield focus does not trigger help_text field

* material select js fields do not allow alphabetical keyboard input

* material select js fields do not stretch to fit label fields

* grouped material select js will submit first valid value if not selected. create a title item with value=''
