"""Demo forms demonstrating use of MaterialForm, MaterialModelForm, and
material_widgets.

"""
from datetime import datetime
from django import forms
from django.forms import widgets
from material_widgets.forms import MaterialForm, MaterialModelForm
from material_widgets.widgets import (
    MaterialCheckboxSelectMultiple,
    MaterialClearableFileInput,
    MaterialFileInput,
    MaterialPasswordInput,
    MaterialSliderInput,
    MaterialSwitchInput,
    )
from .models import MaterialWidgetsDemoModel

class DemoForm(MaterialForm):
    """Demo Form with Material widget fields."""

    username = forms.CharField(
        ### Default label uses field name.replace('_', ' ').title()
        #label='Username',
        min_length=3,
        max_length=32,
        help_text='3-32 characters required',
        ### Widgets can be declared as material_widgets.widgets or
        ### django.forms.widgets.
        ### Widgets will be converted to material_widgets when declared through
        ### MaterialForm.
        widget=widgets.TextInput(
            attrs={
                'autofocus': "autofocus",
                },
            ),
        )
    email = forms.EmailField(
        required=False,
        )
    password = forms.CharField(
        help_text='Please enter at least 8 characters',
        required=False,
        min_length=8,
        ### Declare material_widgets.widget to use custom attributes
        widget=MaterialPasswordInput(
            persistent_help_text=True,
            ),
        )
    url = forms.URLField(
        label='URL',
        required=False,
        initial='http://github.com/ooknosi',
        )
    textarea = forms.CharField(
        help_text='Write as much as you want',
        required=False,
        widget=widgets.Textarea(),
        )
    number = forms.IntegerField(
        label='Odd Number',
        help_text='No even numbers!',
        required=False,
        min_value=1,
        max_value=9,
        widget=widgets.NumberInput(
            attrs={
                'step': '2',
                },
            ),
        )
    slider = forms.DecimalField(
        label='Slider (2 decimal places)',
        ### help_text in sliders are persistent by default
        help_text='in steps of 0.25',
        required=False,
        min_value=0.0,
        max_value=10.0,
        decimal_places=2,
        widget=MaterialSliderInput(
            attrs={
                'step': '0.25',
                },
            ),
        )
    slider_discrete = forms.IntegerField(
        label='Slider (Even Number with Markers)',
        required=False,
        min_value=0,
        max_value=10,
        initial=6,
        widget=MaterialSliderInput(
            is_discrete=True,
            display_markers=True,
            attrs={
                'step': '2',
                },
            ),
        )
    date_field = forms.DateField(
        help_text='YYYY-MM-DD',
        required=False,
        )
    time_field = forms.TimeField(
        help_text='HH:MM:SS',
        required=False,
        )
    datetime_field = forms.DateTimeField(
        help_text='YYYY-MM-DD HH:MM:SS',
        required=False,
        )
    split_datetime = forms.SplitDateTimeField(
        required=False,
        ### Declare material_widgets.widget to override default attributes
        #widget=MaterialSplitDateTimeWidget(
        #    date_label='Birthdate',
        #    date_help_text='YYYY-MM-DD',
        #    date_persistent_help_text=True,
        #    time_label='Birthtime',
        #    time_help_text='HH:MM:SS',
        #    time_persistent_help_text=True,
        #    ),
        )
    date_select = forms.DateField(
        ### Help_text on non-textfields appear as label tooltips
        help_text='This is a select date',
        required=False,
        widget=widgets.SelectDateWidget(
            years=[year for year in range(
                datetime.now().year, datetime.now().year-100, -1)
                  ],
            empty_label=("Year", "Month", "Day"),
            )
        )
    select = forms.ChoiceField(
        ### Blank the label on a select to use the first item as the label
        label='',
        required=False,
        choices=(
            ('', 'Select'),
            ('choice_1', 'Choice 1'),
            ('choice_2', 'Choice 2'),
            ('choice_3', 'Choice 3'),
            ),
        )
    select_with_groups = forms.ChoiceField(
        label='',
        required=False,
        choices=(
            ('', 'Select with Groups'),
            ('Group 1', (
                ('group_1_choice_1', 'Group 1 Choice 1 '),
                ('group_1_choice_2', 'Group 1 Choice 2'),
                ('group_1_choice_3', 'Group 1 Choice 3'),
                )
            ),
            ('Group 2', (
                ('group_2_choice_4', 'Group 2 Choice 4'),
                ('group_2_choice_5', 'Group 2 Choice 5'),
                ('group_2_choice_6', 'Group 2 Choice 6'),
                )
            ),
            ),
        )
    null_boolean_select = forms.NullBooleanField(
        help_text='This is a null boolean select',
        required=False,
        )
    select_multiple = forms.MultipleChoiceField(
        label='',
        #help_text='A label is needed to show the help text tooltip',
        required=False,
        choices=(
            ('Select Multiple 1', (
                ('multiple_choice_1', 'Multiple Choice 1'),
                ('multiple_choice_2', 'Multiple Choice 2'),
                ('multiple_choice_3', 'Multiple Choice 3'),
                )
            ),
            ('Select Multiple 2', (
                ('multiple_choice_4', 'Multiple Choice 4'),
                ('multiple_choice_5', 'Multiple Choice 5'),
                ('multiple_choice_6', 'Multiple Choice 6'),
                )
            ),
            ),
        )
    boolean_switch = forms.BooleanField(
        label='Boolean Switch',
        help_text='This is a switch',
        required=False,
        widget=MaterialSwitchInput(),
        )
    radio_select = forms.ChoiceField(
        label='Radio Select',
        ### help_text for multiple choices can be list or tuple
        help_text=[
            'This is radio 1',
            'This is radio 2',
            'This is radio 3',
            ],
        required=False,
        widget=widgets.RadioSelect(),
        choices=(
            ('radio_select_1', 'Radio 1'),
            ('radio_select_2', 'Radio 2'),
            ('radio_select_3', 'Radio 3'),
            ),
        )
    checkbox = forms.BooleanField(
        label='Checkbox',
        help_text='This is a checkbox',
        required=False,
        )
    checkbox_select_multiple = forms.MultipleChoiceField(
        label='Multiple Checkboxes',
        help_text=(
            'This is checkbox 1',
            'This is checkbox 2',
            'This is checkbox 3',
            ),
        required=False,
        widget=MaterialCheckboxSelectMultiple(
            is_vertical=True,
            ),
        choices=(
            ('checkbox_1', 'Checkbox 1'),
            ('checkbox_2', 'Checkbox 2'),
            ('checkbox_3', 'Checkbox 3'),
            ),
        )
    file_input = forms.FileField(
        ### Blank the label to only display the icon
        label='',
        help_text='Choose 1 file',
        required=False,
        ### Declare material_widgets.widget to use custom attributes
        widget=MaterialFileInput(
            ### compact, dense, raised, stroked, unelevated
            button=('compact', 'dense', 'raised'),
            ### From material-icons; https://material.io/icons/
            icon='attachment',
            ),
        )
    clearable_file_input = forms.FileField(
        label='Select Files',
        help_text='Choose 1 or more files',
        required=False,
        widget=MaterialClearableFileInput(
            icon='file_upload',
            attrs={
                'multiple': True,
                },
            ),
        )
    hidden_input = forms.CharField(
        initial='hidden_value',
        widget=widgets.HiddenInput(),
        )
    multiple_hidden_input = forms.MultipleChoiceField(
        initial=['hidden_1', 'hidden_2', 'hidden_3',],
        widget=widgets.MultipleHiddenInput(),
        choices=(
            ('hidden_1', 'Hidden 1'),
            ('hidden_2', 'Hidden 2'),
            ('hidden_3', 'Hidden 3'),
            ),
        )
    split_hidden_datetime = forms.SplitDateTimeField(
        initial=['1965-08-09', '12:00:00'],
        widget=widgets.SplitHiddenDateTimeWidget(),
        )


class DemoModelForm(MaterialModelForm):
    """Demo ModelForm with Material widget fields."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta settings for DemoModelForm"""
        model = MaterialWidgetsDemoModel
        fields = '__all__'
