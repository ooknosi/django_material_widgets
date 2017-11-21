"""Customized form field widgets with templates styled with Material Components
for the Web.

References
----------
`Material Design for the Web <https://material.io/components/web/>`_

"""
# pylint: disable=invalid-name, too-few-public-methods
# pylint: disable=too-many-ancestors, too-many-arguments, too-many-lines
from django.forms import widgets, utils
from .settings import MATERIAL_CSS, MATERIAL_JS

__all__ = (
    'MaterialCheckboxInput',
    'MaterialCheckboxSelectMultiple',
    'MaterialClearableFileInput',
    'MaterialDateInput',
    'MaterialDateTimeInput',
    'MaterialEmailInput',
    'MaterialFileInput',
    'MaterialHiddenInput',
    'MaterialMultipleHiddenInput',
    'MaterialNullBooleanSelect',
    'MaterialNumberInput',
    'MaterialPasswordInput',
    'MaterialRadioSelect',
    'MaterialSelect',
    'MaterialSelectDateWidget',
    'MaterialSelectMultiple',
    'MaterialSliderInput',
    'MaterialSplitDateTimeWidget',
    'MaterialSplitHiddenDateTimeWidget',
    'MaterialSwitchInput',
    'MaterialTextarea',
    'MaterialTextInput',
    'MaterialTimeInput',
    'MaterialURLInput',
    )

class MaterialComponent(widgets.Widget):
    """Superclass of Material widgets which adds attributes used by Material
    Components.

    Passes label and help_text to the widget context. Declares under Media the
    Material CSS and JS components required to correctly display the widget.

    Parameters
    ----------
    label : str, optional
        Displayed on the widget's field in the template.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : str, optional
        Displayed under text field and textarea inputs, to the right of slider
        labels, and as tool tips on labels for other inputs.
    *args
    **kwargs

    """
    def __init__(self, label=None, help_text=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = label
        self.help_text = help_text

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget'].update({
            'label': self.label,
            'help_text': self.help_text,
            })
        return context

    @property
    def media(self):  # pylint: disable=missing-docstring
        return widgets.Media(
            css={'all': (
                MATERIAL_CSS,
                'material_widgets/css/material_error.css',
                )},
            js=(MATERIAL_JS,),
            )


class MaterialMultiWidget(widgets.MultiWidget):
    """Superclass of Material split widgets which adds attributes used by
    Material Components. Material split widgets consist of multiple Material
    widgets.

    Passes label to the widget context. Declares under Media the Material CSS
    and JS components required to correctly display the widget.

    Parameters
    ----------
    multiwidgets : list or tuple of widget objects
        Widgets to be included in the multiwidget.
    attrs : dict, optional
        HTML attributes to be included in the multiwidget's template.
    label : str, optional
        Displayed to the left of the split widget fields in the template.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    *args
    **kwargs

    """
    template_name = "material_widgets/widgets/material_multiwidget.html"

    def __init__(self, multiwidgets, attrs=None, label=None, *args, **kwargs):
        super().__init__(multiwidgets, attrs, *args, **kwargs)
        self.label = label

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget'].update({
            'label': self.label,
            })
        return context

    @property
    def media(self):  # pylint: disable=missing-docstring
        return widgets.Media(
            css={'all': (
                MATERIAL_CSS,
                'material_widgets/css/material_error.css',
                'material_widgets/css/material_multiwidget.css',
                )},
            js=(MATERIAL_JS,),
            )

    def decompress(self, value):
        """Return a list of decompressed values for the given compressed value.
        The given value can be assumed to be valid, but not necessarily
        non-empty.

        """
        raise NotImplementedError('Subclasses must implement this method.')


class MaterialCheckbox(MaterialComponent):
    """Superclass of Material widgets that make use of Material Checkbox
    Components.

    Declares under Media the Material JS component required to correctly
    display the widget.

    """
    class Media:  # pylint: disable=missing-docstring
        js = ('material_widgets/js/material_checkbox.js',)


class MaterialFileButton(MaterialComponent):
    """Superclass of Material widgets that make use of Material File Button
    Components.

    Declares under Media the Material CSS and JS components required to
    correctly display the widget.

    Parameters
    ----------
    button : list or tuple of str, optional
        Button style modifiers include 'compact', 'dense', 'raised', 'stroked',
        and 'unelevated'. See `mdc-button CSS Classes <https://github.com\
        /material-components/material-components-web/tree/master/packages\
        /mdc-button#css-classes>`_ for details.
    icon : str, optional
        Icon to be displayed on the file button. See `Material Icons
        <https://material.io/icons/>`_ for
        choices.
    *args
    **kwargs

    """
    def __init__(self, button=None, icon=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button = button
        self.icon = icon

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget'].update({
            'button': self.button,
            'icon': self.icon,
            })
        return context

    class Media:  # pylint: disable=missing-docstring
        css = {
            'all': (
                'material_widgets/css/material_button.css',
                'material_widgets/css/material_file_input.css',
                )
            }
        js = (
            'material_widgets/js/material_button.js',
            'material_widgets/js/material_file_input.js',
            )


class MaterialSelectMenu(MaterialComponent):
    """Superclass of Material widgets that make use of Material Select Menu
    Components.

    Declares under Media the Material CSS and JS components required to
    correctly display the widget.

    """
    class Media:  # pylint: disable=missing-docstring
        css = {
            'all': (
                'material_widgets/css/material_select.css',
                )
            }
        js = ('material_widgets/js/material_select.js',)


class MaterialTextField(MaterialComponent):
    """Superclass of Material widgets that make use of Material TextField
    Components.

    Declares under Media the Material CSS and JS components required to
    correctly display the widget.

    Parameters
    ----------
    persistent_help_text : bool, optional
        Help text will be persistently displayed if True, else it will only be
        visible when the field is active.
        Defaults to False.
    *args
    **kwargs

    """
    def __init__(self, persistent_help_text=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persistent_help_text = persistent_help_text

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget'].update({
            'persistent_help_text': self.persistent_help_text,
            })
        return context

    class Media:  # pylint: disable=missing-docstring
        css = {
            'all': (
                'material_widgets/css/material_text_field.css',
                )
            }
        js = ('material_widgets/js/material_text_field.js',)


class MaterialCheckboxInput(MaterialCheckbox, widgets.CheckboxInput):
    """Material CheckboxInput

    Default widget for BooleanField under MaterialForm.

    Parameters
    ----------
    label : str, optional
        Displayed to the right of the checkbox.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : str, optional
        Displayed as a tool tip on the label.

    Examples
    --------
    Explicit widget declaration is unnecessary in a BooleanField under a
    MaterialForm.

    >>> checkbox = forms.BooleanField(
    >>>     label='Checkbox',
    >>>     help_text='This is a checkbox',
    >>>     #widget=MaterialCheckboxInput(),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_checkbox.html'


class MaterialCheckboxSelectMultiple(
        MaterialCheckbox,
        widgets.CheckboxSelectMultiple):
    """Material CheckboxSelectMultiple

    Parameters
    ----------
    label : str, optional
        Displayed above the checkbox group.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : list or tuple of str, optional
        Displayed as tool tips on the respective checkbox labels.
    choices : list or tuple of (value, label) pairs
        Each pair will be displayed as a checkbox.

    Other Parameters
    ----------------
    is_vertical : bool, optional
        Layout of checkboxes will be vertical if True, or horizontal otherwise.
        Defaults to True.

    Examples
    --------
    Declare widget explicity to use custom widget parameters.

    >>> checkbox_select_multiple = forms.MultipleChoiceField(
    >>>     label='Multiple Checkboxes',
    >>>     help_text=(
    >>>         'This is checkbox 1',
    >>>         'This is checkbox 2',
    >>>         'This is checkbox 3',
    >>>         ),
    >>>     widget=MaterialCheckboxSelectMultiple(
    >>>         is_vertical=False,
    >>>         ),
    >>>     choices=(
    >>>         ('checkbox_1', 'Checkbox 1'),
    >>>         ('checkbox_2', 'Checkbox 2'),
    >>>         ('checkbox_3', 'Checkbox 3'),
    >>>         ),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_checkbox_select.html'
    option_template_name = 'material_widgets/widgets/material_checkbox_option.html'

    def __init__(self, is_vertical=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_vertical = is_vertical

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget'].update({
            'is_vertical': self.is_vertical,
            })
        return context

    def create_option(self,
                      name, value, label, selected, index,
                      subindex=None, attrs=None):
        option = super().create_option(
            name, value, label, selected, index, subindex, attrs
            )
        option['help_text'] = self.help_text[index]
        return option


class MaterialClearableFileInput(
        MaterialFileButton,
        widgets.ClearableFileInput):
    """Material ClearableFileInput

    Default widget for FileField and ImageField under MaterialForm.

    Parameters
    ----------
    label : str, optional
        Displayed on the button.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
        Label dynamically changes to selected file name, or file count if
        the 'multiple' attrs is True.
    help_text : str, optional
        Displayed as a tool tip on the button.

    Other Parameters
    ----------------
    button : list or tuple of str, optional
        Button style modifiers include 'compact', 'dense', 'raised', 'stroked',
        and 'unelevated'. See `mdc-button CSS Classes <https://github.com\
        /material-components/material-components-web/tree/master/packages\
        /mdc-button#css-classes>`_ for details.
    icon : str, optional
        Icon to be displayed on the file button. See `Material Icons
        <https://material.io/icons/>`_ for
        choices.

    Examples
    --------
    Declare widget explicity to use custom widget parameters.

    >>> clearable_file_input = forms.FileField(
    >>>     ### Blank the label to only display the icon
    >>>     label='',
    >>>     help_text='Choose 1 or more files',
    >>>     widget=MaterialClearableFileInput(
    >>>         ### compact, dense, raised, stroked, unelevated
    >>>         button=('compact', 'dense', 'raised'),
    >>>         ### From material-icons; https://material.io/icons/
    >>>         icon='file_upload',
    >>>         attrs={
    >>>             'multiple': True,
    >>>             },
    >>>         ),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_clearable_file_input.html'

    class Media:  # pylint: disable=missing-docstring
        css = {
            'all': (
                'material_widgets/css/material_button.css',
                'material_widgets/css/material_file_input.css',
                )
            }
        js = (
            'material_widgets/js/material_button.js',
            'material_widgets/js/material_checkbox.js',
            'material_widgets/js/material_file_input.js',
            )


class MaterialDateInput(MaterialTextField, widgets.DateInput):
    """Material DateInput

    Default widget for DateField under MaterialForm.

    Parameters
    ----------
    label : str, optional
        Displayed on the widget's field in the template.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : str, optional
        Displayed under the input field.

    Other Parameters
    ----------------
    persistent_help_text : bool, optional
        Help text will be persistently displayed if True, else it will only be
        visible when the field is active.
        Defaults to False.

    Examples
    --------
    Declare widget explicity to use custom widget parameters.

    >>> date_field = forms.DateField(
    >>>     label='Date',
    >>>     help_text='YYYY-MM-DD',
    >>>     widget=MaterialDateInput(
    >>>         persistent_help_text=True,
    >>>         ),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_date.html'


class MaterialDateTimeInput(MaterialTextField, widgets.DateTimeInput):
    """Material DateTimeInput

    Default widget for DateTimeField under MaterialForm.

    Parameters
    ----------
    label : str, optional
        Displayed on the widget's field in the template.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : str, optional
        Displayed under the input field.

    Other Parameters
    ----------------
    persistent_help_text : bool, optional
        Help text will be persistently displayed if True, else it will only be
        visible when the field is active.
        Defaults to False.

    Examples
    --------
    Declare widget explicity to use custom widget parameters.

    >>> datetime_field = forms.DateTimeField(
    >>>     label='Date and Time',
    >>>     help_text='YYYY-MM-DD HH:MM:SS',
    >>>     widget=MaterialDateTimeInput(
    >>>         persistent_help_text=True,
    >>>         ),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_datetime.html'


class MaterialEmailInput(MaterialTextField, widgets.EmailInput):
    """Material EmailInput

    Default widget for EmailField under MaterialForm.

    Parameters
    ----------
    label : str, optional
        Displayed on the widget's field in the template.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : str, optional
        Displayed under the input field.

    Other Parameters
    ----------------
    persistent_help_text : bool, optional
        Help text will be persistently displayed if True, else it will only be
        visible when the field is active.
        Defaults to False.

    Examples
    --------
    Declare widget explicity to use custom widget parameters.

    >>> email = forms.EmailField(
    >>>     label='Email Address',
    >>>     help_text='your_email@example.com',
    >>>     widget=MaterialEmailInput(
    >>>         persistent_help_text=True,
    >>>         ),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_email.html'


class MaterialFileInput(MaterialFileButton, widgets.FileInput):
    """Material FileInput

    Parameters
    ----------
    label : str, optional
        Displayed on the button.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
        Label dynamically changes to selected file name, or file count if
        the 'multiple' attrs is True.
    help_text : str, optional
        Displayed as a tool tip on the button.

    Other Parameters
    ----------------
    button : list or tuple of str, optional
        Button style modifiers include 'compact', 'dense', 'raised', 'stroked',
        and 'unelevated'. See `mdc-button CSS Classes <https://github.com\
        /material-components/material-components-web/tree/master/packages\
        /mdc-button#css-classes>`_ for details.
    icon : str, optional
        Icon to be displayed on the file button. See `Material Icons
        <https://material.io/icons/>`_ for
        choices.

    Examples
    --------
    Declare widget explicity to use custom widget parameters.

    >>> file_input = forms.FileField(
    >>>     ### Blank the label to only display the icon
    >>>     label='',
    >>>     help_text='Choose 1 or more files',
    >>>     widget=MaterialFileInput(
    >>>         ### compact, dense, raised, stroked, unelevated
    >>>         button=('compact', 'dense', 'raised'),
    >>>         ### From material-icons; https://material.io/icons/
    >>>         icon='attachment',
    >>>         attrs={
    >>>             'multiple': True,
    >>>             },
    >>>         ),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_file.html'


class MaterialHiddenInput(MaterialComponent, widgets.HiddenInput):
    """Material HiddenInput

    Parameters
    ----------
    initial : varies depending on field, optional
        Initial value to populate the hidden input in the form.

    Examples
    --------
    >>> hidden_input = forms.CharField(
    >>>     initial='hidden_value',
    >>>     widget=widgets.HiddenInput(),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_hidden.html'


class MaterialMultipleHiddenInput(
        MaterialComponent,
        widgets.MultipleHiddenInput):
    """Material MultipleHiddenInput

    Parameters
    ----------
    initial : varies depending on field, optional
        Initial Value to populate the multiple hidden input in the form.

    Examples
    --------
    >>> multiple_hidden_input = forms.MultipleChoiceField(
    >>>     initial=['hidden_1', 'hidden_2', 'hidden_3',],
    >>>     widget=widgets.MultipleHiddenInput(),
    >>>     choices=(
    >>>         ('hidden_1', 'Hidden 1'),
    >>>         ('hidden_2', 'Hidden 2'),
    >>>         ('hidden_3', 'Hidden 3'),
    >>>         ),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_multiple_hidden.html'


class MaterialNullBooleanSelect(MaterialSelectMenu, widgets.NullBooleanSelect):
    """Material NullBooleanSelect

    Default widget for NullBooleanField under MaterialForm.

    Parameters
    ----------
    label : str, optional
        Displayed to the left of the select menu.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : str, optional
        Displayed as a tool tip on the label.

    Examples
    --------
    Explicit widget declaration is unnecessary in a NullBooleanField under a
    MaterialForm.

    >>> null_boolean_select = forms.NullBooleanField(
    >>>     label='Is this a null boolean select?',
    >>>     help_text='This is a null boolean select',
    >>>     #widget=MaterialNullBooleanSelect(),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_select.html'
    option_template_name = 'material_widgets/widgets/material_select_option.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        attrs_class = (
            context['widget']['attrs'].get('class', '')
            + ' mdc-select'
            ).strip()
        context['widget']['attrs'].update({
            'class': attrs_class,
            })
        return context


class MaterialNumberInput(MaterialTextField, widgets.NumberInput):
    """Material NumberInput

    Default widget for DecimalField, FloatField, and IntegerField under
    MaterialForm when Field.localize is False.

    Parameters
    ----------
    label : str, optional
        Displayed on the widget's field in the template.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : str, optional
        Displayed under the input field.

    Other Parameters
    ----------------
    persistent_help_text : bool, optional
        Help text will be persistently displayed if True, else it will only be
        visible when the field is active.
        Defaults to False.

    Examples
    --------
    Explicit widget declaration is unnecessary in a DecimalField, FloatField,
    or IntegerField under MaterialForm.

    >>> decimal = forms.DecimalField(
    >>>     label='Decimal Number',
    >>>     help_text='To 2 d.p.',
    >>>     min_value=0.0,
    >>>     max_value=10.0,
    >>>     decimal_places=2,
    >>>     )

    Declare widget explicity to use custom widget parameters.

    >>> integer = forms.IntegerField(
    >>>     label='Odd Number',
    >>>     help_text='No even numbers!',
    >>>     min_value=1,
    >>>     max_value=9,
    >>>     widget=widgets.NumberInput(
    >>>         persistent_help_text=True,
    >>>         attrs={
    >>>             'step': '2',
    >>>             },
    >>>         ),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_number.html'


class MaterialPasswordInput(MaterialTextField, widgets.PasswordInput):
    """Material PasswordInput

    Parameters
    ----------
    label : str, optional
        Displayed on the widget's field in the template.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : str, optional
        Displayed under the input field.

    Other Parameters
    ----------------
    persistent_help_text : bool, optional
        Help text will be persistently displayed if True, else it will only be
        visible when the field is active.
        Defaults to False.

    Examples
    --------
    Declare widget explicity to use custom widget parameters.

    >>> password = forms.CharField(
    >>>     label="Secret Password",
    >>>     help_text='Please enter at least 8 characters',
    >>>     min_length=8,
    >>>     widget=MaterialPasswordInput(
    >>>         persistent_help_text=True,
    >>>         ),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_password.html'


class MaterialRadioSelect(MaterialComponent, widgets.RadioSelect):
    """Material RadioSelect

    Parameters
    ----------
    label : str, optional
        Displayed above the radio group.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : list or tuple of str, optional
        Displayed as tool tips on the respective radio option labels.
    choices : list or tuple of (value, label) pairs
        Each pair will be displayed as a radio option.

    Other Parameters
    ----------------
    is_vertical : bool, optional
        Layout of checkboxes will be vertical if True, or horizontal otherwise.
        Defaults to False.

    Examples
    --------
    Declare widget explicity to use custom widget parameters.

    >>> radio_select = forms.ChoiceField(
    >>>     label='Radio Select',
    >>>     help_text=(
    >>>         'This is radio 1',
    >>>         'This is radio 2',
    >>>         'This is radio 3',
    >>>         ),
    >>>     widget=widgets.RadioSelect(
    >>>         is_vertical=True,
    >>>         ),
    >>>     choices=(
    >>>         ('radio_select_1', 'Radio 1'),
    >>>         ('radio_select_2', 'Radio 2'),
    >>>         ('radio_select_3', 'Radio 3'),
    >>>         ),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_radio.html'
    option_template_name = 'material_widgets/widgets/material_radio_option.html'

    def __init__(self, is_vertical=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_vertical = is_vertical

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget'].update({
            'is_vertical': self.is_vertical,
            })
        return context

    def create_option(self,
                      name, value, label, selected, index,
                      subindex=None, attrs=None):
        option = super().create_option(
            name, value, label, selected, index, subindex, attrs
            )
        option['help_text'] = self.help_text[index]
        return option

    class Media:
        """Material radio JS component."""
        js = ('material_widgets/js/material_radio.js',)


class MaterialSelect(MaterialSelectMenu, widgets.Select):
    """Material Select

    Default widget for ChoiceField, FilePathField, ModelChoiceField, and
    TypedChoiceField under MaterialForm.

    Parameters
    ----------
    label : str, optional
        Displayed to the left of the select menu.
        If explicitly declared blank, the first item in the select menu will
        act as an unselectable choice label.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : str, optional
        Displayed as a tool tip on the label.

    Examples
    --------
    Explicit widget declaration is unnecessary in ChoiceField, FilePathField,
    ModelChoiceField, and TypedChoiceField under MaterialForm.

    >>> select = forms.ChoiceField(
    >>>     label='',
    >>>     #widget=MaterialSelect(),
    >>>     choices=(
    >>>         ('', 'Select'),
    >>>         ('choice_1', 'Choice 1'),
    >>>         ('choice_2', 'Choice 2'),
    >>>         ('choice_3', 'Choice 3'),
    >>>         ),
    >>>     )

    Choices can be grouped.

    >>> select_with_groups = forms.ChoiceField(
    >>>     label='',
    >>>     required=False,
    >>>     choices=(
    >>>         ('', 'Select with Groups'),
    >>>         ('Group 1', (
    >>>             ('group_1_choice_1', 'Group 1 Choice 1 '),
    >>>             ('group_1_choice_2', 'Group 1 Choice 2'),
    >>>             ('group_1_choice_3', 'Group 1 Choice 3'),
    >>>             )
    >>>         ),
    >>>         ('Group 2', (
    >>>             ('group_2_choice_4', 'Group 2 Choice 4'),
    >>>             ('group_2_choice_5', 'Group 2 Choice 5'),
    >>>             ('group_2_choice_6', 'Group 2 Choice 6'),
    >>>             )
    >>>         ),
    >>>         ),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_select.html'
    option_template_name = (
        'material_widgets/widgets/'
        'material_select_option.html'
        )

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        attrs_class = (
            context['widget']['attrs'].get('class', '')
            + ' mdc-select'
            ).strip()
        context['widget']['attrs'].update({
            'class': attrs_class,
            })
        return context


class MaterialSelectDateWidget(MaterialSelectMenu, widgets.SelectDateWidget):
    """Material SelectDateWidget

    Parameters
    ----------
    label : str, optional
        Displayed to the left of the select menu.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : str, optional
        Displayed as a tool tip on the label.

    Other Parameters
    ----------------
    various : various, optional
        See `django.forms.widgets.SelectDateWidget <https://docs.djangoproject.com\
        /en/dev/ref/forms/widgets/#selectdatewidget>`_ for optional parameters.

    Examples
    --------
    Widget can be declared as Django's SelectDateWidget or as
    MaterialSelectDateWidget.

    >>> date_select = forms.DateField(
    >>>     label="Date",
    >>>     help_text='This is a select date',
    >>>     widget=widgets.SelectDateWidget(
    >>>         years=[year for year in range(
    >>>             datetime.now().year, datetime.now().year-100, -1)
    >>>               ],
    >>>         empty_label=("Year", "Month", "Day"),
    >>>         )
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_select_date.html'
    select_widget = MaterialSelect

    class Media:
        """Material multiwidget CSS component."""
        css = {
            'all': (
                'material_widgets/css/material_multiwidget.css',
                )
            }


class MaterialSelectMultiple(MaterialSelectMenu, widgets.SelectMultiple):
    """Material SelectMultiple

    Default widget for MultipleChoiceField, ModelMultipleChoiceField, and
    TypedMultipleChoiceField under MaterialForm.

    Parameters
    ----------
    label : str, optional
        Displayed to the left of the select menu.
        If explicitly declared blank, the first item in the select menu will
        act as an unselectable choice label.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : str, optional
        Displayed as a tool tip on the label.

    Examples
    --------
    Explicit widget declaration is unnecessary in MultipleChoiceField,
    ModelMultipleChoiceField, and TypedMultipleChoiceField under MaterialForm.

    >>> select_multiple = forms.MultipleChoiceField(
    >>>     label='Choose 1 or more',
    >>>     help_text='Ctrl + Click to unselect',
    >>>     #widget=MaterialSelect(),
    >>>     choices=(
    >>>         ('', 'Select'),
    >>>             ('multiple_choice_1', 'Multiple Choice 1'),
    >>>             ('multiple_choice_2', 'Multiple Choice 2'),
    >>>             ('multiple_choice_3', 'Multiple Choice 3'),
    >>>         ),
    >>>     )

    Choices can be grouped.

    >>> select_multiple_with_groups = forms.MultipleChoiceField(
    >>>     label='',
    >>>     #help_text='A label is needed to show the help text tooltip',
    >>>     choices=(
    >>>         ('Select Multiple 1', (
    >>>             ('multiple_choice_1', 'Multiple Choice 1'),
    >>>             ('multiple_choice_2', 'Multiple Choice 2'),
    >>>             ('multiple_choice_3', 'Multiple Choice 3'),
    >>>             )
    >>>         ),
    >>>         ('Select Multiple 2', (
    >>>             ('multiple_choice_4', 'Multiple Choice 4'),
    >>>             ('multiple_choice_5', 'Multiple Choice 5'),
    >>>             ('multiple_choice_6', 'Multiple Choice 6'),
    >>>             )
    >>>         ),
    >>>         ),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_select_multiple.html'
    option_template_name = (
        'material_widgets/widgets/material_select_option_nojs.html'
        )

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        attrs_class = (
            context['widget']['attrs'].get('class', '')
            + ' mdc-multi-select mdc-list'
            ).strip()
        context['widget']['attrs'].update({
            'class': attrs_class,
            })
        return context


class MaterialSliderInput(MaterialComponent, widgets.NumberInput):
    """Material SliderInput

    Parameters
    ----------
    label : str, optional
        Displayed above the widget in the template.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : str, optional
        Displayed to the right of the label.

    Other Parameters
    ----------------
    persistent_help_text : bool, optional
        Help text will be persistently displayed if True, else it will only be
        visible when the field is active.
        Defaults to True.
    is_discrete : bool, optional
        Slider will have discrete steps in its interface if True, else its
        interface will be continuous.
        Defaults to False.
    display_markers : bool, optional
        Value markers appear on slider interaction if True.
        Defaults to False.

    Examples
    --------
    Declare widget explicity to use custom widget parameters.

    >>> slider = forms.IntegerField(
    >>>     label='Slider',
    >>>     ### help_text in sliders are persistent by default
    >>>     help_text='Even Number with Markers',
    >>>     required=False,
    >>>     min_value=0,
    >>>     max_value=10,
    >>>     initial=6,
    >>>     widget=MaterialSliderInput(
    >>>         is_discrete=True,
    >>>         display_markers=True,
    >>>         attrs={
    >>>             'step': '2',
    >>>             },
    >>>         ),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_slider.html'

    def __init__(self,
                 display_markers=False,
                 is_discrete=False,
                 persistent_help_text=True,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.display_markers = display_markers
        self.is_discrete = is_discrete
        self.persistent_help_text = persistent_help_text

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget'].update({
            'display_markers': self.display_markers,
            'is_discrete': self.is_discrete,
            'persistent_help_text': self.persistent_help_text,
            })
        return context

    class Media:  # pylint: disable=missing-docstring
        js = ('material_widgets/js/material_slider.js',)


class MaterialSplitDateTimeWidget(MaterialMultiWidget):
    """Material SplitDateTimeWidget

    Splits datetime input into two MaterialTextFields.
    Default widget for SplitDateTimeField under MaterialForm.

    Parameters
    ----------
    label : str, optional
        Displayed to the left of the widget fields in the template.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.

    Other Parameters
    ----------------
    attrs : dict, optional
        HTML attributes to be included in the multiwidget's template.
    date_format : str, optional
        Format to display initial field value. Defaults to first format found
        in Django's DATE_INPUT_FORMATS.
    time_format : str, optional
        Format to display initial field value. Defaults to first format found
        in Django's TIME_INPUT_FORMATS.
    label : str, optional
        Passes value through from field parameter.
    date_label : str, optional
        Displayed on the Date widget's field in the template.
        Defaults to 'Date'.
    date_help_text : str, optional
        Displayed under the Date input field.
        Defaults to 'YYYY-MM-DD'.
    date_persistent_help_text : bool, optional
        Help text for Date widget will be persistently displayed if True, else
        it will only be visible when the field is active.
        Defaults to False.
    time_label : str, optional
        Displayed on the Time widget's field in the template.
        Defaults to 'Time'.
    time_help_text : str, optional
        Displayed under the Time input field.
        Defaults to 'HH:MM:SS'.
    time_persistent_help_text : bool, optional
        Help text for Time widget will be persistently displayed if True, else
        it will only be visible when the field is active.
        Defaults to False.

    Examples
    --------
    Declare widget explicity to use custom widget parameters.

    >>> split_datetime = forms.SplitDateTimeField(
    >>>     required=False,
    >>>     widget=MaterialSplitDateTimeWidget(
    >>>         date_label='Birthdate',
    >>>         date_help_text='YYYY-MM-DD',
    >>>         date_persistent_help_text=True,
    >>>         time_label='Birthtime',
    >>>         time_help_text='HH:MM:SS',
    >>>         time_persistent_help_text=True,
    >>>         ),
    >>>     )

    """
    supports_microseconds = False
    template_name = 'material_widgets/widgets/material_splitdatetime.html'

    def __init__(self,
                 attrs=None, date_format=None, time_format=None,
                 label=None,
                 date_label='Date', date_help_text='YYYY-MM-DD',
                 date_persistent_help_text=False,
                 time_label='Time', time_help_text='HH:MM:SS',
                 time_persistent_help_text=False,
                 *args, **kwargs):
        multiwidgets = (
            MaterialDateInput(
                label=date_label,
                help_text=date_help_text,
                persistent_help_text=date_persistent_help_text,
                attrs=attrs,
                format=date_format,
                ),
            MaterialTimeInput(
                label=time_label,
                help_text=time_help_text,
                persistent_help_text=time_persistent_help_text,
                attrs=attrs,
                format=time_format,
                ),
            )
        super().__init__(multiwidgets, attrs, label, *args, **kwargs)

    def decompress(self, value):
        if value:
            value = utils.to_current_timezone(value)
            return [value.date(), value.time().replace(microsecond=0)]
        return [None, None]


class MaterialSplitHiddenDateTimeWidget(MaterialSplitDateTimeWidget):
    """Material SplitHiddenDateTimeWidget

    Parameters
    ----------
    initial : list or tuple of str, optional
        Initial values to populate the hidden date and time fields in the form.

    Examples
    --------
    >>> split_hidden_datetime = forms.SplitDateTimeField(
    >>>     initial=['1965-08-09', '12:00:00'],
    >>>     widget=widgets.SplitHiddenDateTimeWidget(),
    >>>     )

    """
    input_type = 'hidden'
    template_name = 'material_widgets/widgets/material_splithiddendatetime.html'

    def __init__(self, attrs=None, date_format=None, time_format=None):
        super().__init__(attrs, date_format, time_format, label='',
                         date_label='', date_help_text='',
                         date_persistent_help_text=False,
                         time_label='', time_help_text='',
                         time_persistent_help_text=False,
                        )
        for widget in self.widgets:
            widget.__class__ = MaterialHiddenInput
            widget.input_type = 'hidden'

class MaterialSwitchInput(MaterialComponent, widgets.CheckboxInput):
    """Material SwitchInput

    Parameters
    ----------
    label : str, optional
        Displayed to the left of the switch.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : str, optional
        Displayed as a tool tip on the label.

    Examples
    --------
    Declare widget explicity in a BooleanField to use widget.

    >>> boolean_switch = forms.BooleanField(
    >>>     label='Boolean Switch',
    >>>     help_text='This is a switch',
    >>>     widget=MaterialSwitchInput(),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_switch.html'

    class Media:  # pylint: disable=missing-docstring
        css = {
            'all': (
                'material_widgets/css/material_switch.css',
                )
            }


class MaterialTextarea(MaterialTextField, widgets.Textarea):
    """Material Textarea

    Parameters
    ----------
    label : str, optional
        Displayed in the widget's field to the upper left of the box in the
        template.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : str, optional
        Displayed under the input field.

    Other Parameters
    ----------------
    persistent_help_text : bool, optional
        Help text will be persistently displayed if True, else it will only be
        visible when the field is active.
        Defaults to False.

    Examples
    --------
    Declare widget explicity to use custom widget parameters.

    >>> textarea = forms.CharField(
    >>>     label="Captain's Log",
    >>>     help_text='Write as much as you want',
    >>>     widget=widgets.MaterialTextarea(
    >>>         persistent_help_text=True,
    >>>         ),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_textarea.html'


class MaterialTextInput(MaterialTextField, widgets.TextInput):
    """Material TextInput

    Default widget for CharField and various other fields under MaterialForm.

    Parameters
    ----------
    label : str, optional
        Displayed on the widget's field in the template.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : str, optional
        Displayed under the input field.

    Other Parameters
    ----------------
    persistent_help_text : bool, optional
        Help text will be persistently displayed if True, else it will only be
        visible when the field is active.
        Defaults to False.

    Examples
    --------
    Declare widget explicity to use custom widget parameters.

    >>> username = forms.CharField(
    >>>     label='Choose a Username',
    >>>     min_length=3,
    >>>     max_length=32,
    >>>     help_text='3-32 characters required',
    >>>     widget=widgets.TextInput(
    >>>         persistent_help_text=True,
    >>>         attrs={
    >>>             'autofocus': "autofocus",
    >>>             },
    >>>         ),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_text.html'


class MaterialTimeInput(MaterialTextField, widgets.TimeInput):
    """Material TimeInput

    Parameters
    ----------
    label : str, optional
        Displayed on the widget's field in the template.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : str, optional
        Displayed under the input field.

    Other Parameters
    ----------------
    persistent_help_text : bool, optional
        Help text will be persistently displayed if True, else it will only be
        visible when the field is active.
        Defaults to False.

    Examples
    --------
    Declare widget explicity to use custom widget parameters.

    >>> time_field = forms.TimeField(
    >>>     label='Time',
    >>>     help_text='HH:MM:SS',
    >>>     widget=MaterialTimeInput(
    >>>         persistent_help_text=True,
    >>>         ),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_time.html'


class MaterialURLInput(MaterialTextField, widgets.URLInput):
    """Material URLInput

    Default widget for URLField under MaterialForm.

    Parameters
    ----------
    label : str, optional
        Displayed on the widget's field in the template.
        Defaults to widget's capitalized field name with underscores converted
        to spaces.
    help_text : str, optional
        Displayed under the input field.

    Other Parameters
    ----------------
    persistent_help_text : bool, optional
        Help text will be persistently displayed if True, else it will only be
        visible when the field is active.
        Defaults to False.

    Examples
    --------
    Declare widget explicity to use custom widget parameters.

    >>> url = forms.URLField(
    >>>     label='URL',
    >>>     help_text='Website',
    >>>     initial='http://github.com/ooknosi',
    >>>     widget=widgets.MaterialTextInput(
    >>>         persistent_help_text=True,
    >>>         ),
    >>>     )

    """
    template_name = 'material_widgets/widgets/material_url.html'
