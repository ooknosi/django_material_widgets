"""
DJANGO MATERIAL WIDGETS FORMS TEST MODULE
material_widgets/tests/test_forms.py
"""
# pylint: disable=invalid-name, missing-docstring, no-member
# pylint: disable=too-few-public-methods, too-many-ancestors
# pylint: disable=too-many-public-methods

from django import forms
from django.test import TestCase
from .. import widgets
from ..forms import MaterialForm, MaterialModelForm
from .models import MaterialWidgetsTestModel

class MaterialFormTests(TestCase):
    """Test cases for material_widgets.forms.MaterialForm.
    Each field's widget should automatically use a Material Component.
    """

    def test_MaterialForm_materializes_BooleanField(self):
        """django.forms.widgets.CheckboxInput should be converted to
        material_widgets.widgets.MaterialCheckboxInput.
        """

        class CheckboxInputForm(MaterialForm):
            checkbox_input = forms.BooleanField()

        form = CheckboxInputForm()
        self.assertEqual(
            type(form.fields['checkbox_input'].widget),
            widgets.MaterialCheckboxInput,
            )

    def test_MaterialForm_materializes_CharField(self):
        """django.forms.widgets.TextInput should be converted to
        material_widgets.widgets.MaterialTextInput.
        """

        class TextInputForm(MaterialForm):
            text_input = forms.CharField()

        form = TextInputForm()
        self.assertEqual(
            type(form.fields['text_input'].widget),
            widgets.MaterialTextInput,
            )

    def test_MaterialForm_materializes_CheckboxSelectMultiple(self):
        """django.forms.widgets.CheckboxSelectMultiple should be converted to
        material_widgets.widgets.MaterialCheckboxSelectMultiple.
        """

        class MultipleChoiceForm(MaterialForm):
            checkbox_select_multiple = forms.MultipleChoiceField(
                widget=forms.widgets.CheckboxSelectMultiple(),
                )

        form = MultipleChoiceForm()
        self.assertEqual(
            type(form.fields['checkbox_select_multiple'].widget),
            widgets.MaterialCheckboxSelectMultiple,
            )

    def test_MaterialForm_materializes_ChoiceField(self):
        """django.forms.widgets.Select should be converted to
        material_widgets.widgets.MaterialSelect.
        """

        class SelectForm(MaterialForm):
            select = forms.ChoiceField()

        form = SelectForm()
        self.assertEqual(
            type(form.fields['select'].widget),
            widgets.MaterialSelect,
            )

    def test_MaterialForm_materializes_DateField(self):
        """django.forms.widgets.DateInput should be converted to
        material_widgets.widgets.MaterialDateInput.
        """

        class DateInputForm(MaterialForm):
            date_input = forms.DateField()

        form = DateInputForm()
        self.assertEqual(
            type(form.fields['date_input'].widget),
            widgets.MaterialDateInput,
            )

    def test_MaterialForm_materializes_DateTimeField(self):
        """django.forms.widgets.DateTimeInput should be converted to
        material_widgets.widgets.MaterialDateTimeInput.
        """

        class DateTimeInputForm(MaterialForm):
            date_time_input = forms.DateTimeField()

        form = DateTimeInputForm()
        self.assertEqual(
            type(form.fields['date_time_input'].widget),
            widgets.MaterialDateTimeInput,
            )

    def test_MaterialForm_materializes_DecimalField(self):
        """django.forms.widgets.NumberInput should be converted to
        material_widgets.widgets.MaterialNumberInput.
        """

        class NumberInputForm(MaterialForm):
            number_input = forms.DecimalField()

        form = NumberInputForm()
        self.assertEqual(
            type(form.fields['number_input'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialForm_materializes_EmailField(self):
        """django.forms.widgets.EmailInput should be converted to
        material_widgets.widgets.MaterialEmailInput.
        """

        class EmailInputForm(MaterialForm):
            email_input = forms.EmailField()

        form = EmailInputForm()
        self.assertEqual(
            type(form.fields['email_input'].widget),
            widgets.MaterialEmailInput,
            )

    def test_MaterialForm_materializes_FileField(self):
        """django.forms.widgets.ClearableFileInput should be converted to
        material_widgets.widgets.MaterialClearableFileInput.
        """

        class ClearableFileInputForm(MaterialForm):
            clearable_file_input = forms.FileField()

        form = ClearableFileInputForm()
        self.assertEqual(
            type(form.fields['clearable_file_input'].widget),
            widgets.MaterialClearableFileInput,
            )

    def test_MaterialForm_materializes_FileInput(self):
        """django.forms.widgets.FileInput should be converted to
        material_widgets.widgets.MaterialFileInput.
        """

        class FileInputForm(MaterialForm):
            file_input = forms.FileField(
                widget=forms.widgets.FileInput(),
                )

        form = FileInputForm()
        self.assertEqual(
            type(form.fields['file_input'].widget),
            widgets.MaterialFileInput,
            )

    def test_MaterialForm_materializes_HiddenInput(self):
        """django.forms.widgets.HiddenInput should be converted to
        material_widgets.widgets.MaterialHiddenInput.
        """

        class HiddenInputForm(MaterialForm):
            hidden_input = forms.CharField(
                widget=forms.widgets.HiddenInput(),
                )

        form = HiddenInputForm()
        self.assertEqual(
            type(form.fields['hidden_input'].widget),
            widgets.MaterialHiddenInput,
            )

    def test_MaterialForm_materializes_IntegerField(self):
        """django.forms.widgets.NumberInput should be converted to
        material_widgets.widgets.MaterialNumberInput.
        """

        class NumberInputForm(MaterialForm):
            number_input = forms.IntegerField()

        form = NumberInputForm()
        self.assertEqual(
            type(form.fields['number_input'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialForm_materializes_MultipleChoiceField(self):
        """django.forms.widgets.SelectMultiple should be converted to
        material_widgets.widgets.MaterialSelectMultiple.
        """

        class SelectMultipleForm(MaterialForm):
            select_multiple = forms.MultipleChoiceField()

        form = SelectMultipleForm()
        self.assertEqual(
            type(form.fields['select_multiple'].widget),
            widgets.MaterialSelectMultiple,
            )

    def test_MaterialForm_materializes_MultipleHiddenInput(self):
        """django.forms.widgets.MultipleHiddenInput should be converted to
        material_widgets.widgets.MaterialMultipleHiddenInput.
        """

        class MultipleHiddenInputForm(MaterialForm):
            multiple_hidden_input = forms.MultipleChoiceField(
                widget=forms.widgets.MultipleHiddenInput(),
                )

        form = MultipleHiddenInputForm()
        self.assertEqual(
            type(form.fields['multiple_hidden_input'].widget),
            widgets.MaterialMultipleHiddenInput,
            )

    def test_MaterialForm_materializes_NullBooleanField(self):
        """django.forms.widgets.NullBooleanSelect should be converted to
        material_widgets.widgets.MaterialNullBooleanSelect.
        """

        class NullBooleanSelectForm(MaterialForm):
            null_boolean_select = forms.NullBooleanField()

        form = NullBooleanSelectForm()
        self.assertEqual(
            type(form.fields['null_boolean_select'].widget),
            widgets.MaterialNullBooleanSelect,
            )

    def test_MaterialForm_materializes_PasswordInput(self):
        """django.forms.widgets.PasswordInput should be converted to
        material_widgets.widgets.MaterialPasswordInput.
        """

        class PasswordInputForm(MaterialForm):
            password_input = forms.CharField(
                widget=forms.widgets.PasswordInput(),
                )

        form = PasswordInputForm()
        self.assertEqual(
            type(form.fields['password_input'].widget),
            widgets.MaterialPasswordInput,
            )

    def test_MaterialForm_materializes_RadioSelect(self):
        """django.forms.widgets.RadioSelect should be converted to
        material_widgets.widgets.MaterialRadioSelect.
        """

        class RadioSelectForm(MaterialForm):
            radio_select = forms.ChoiceField(
                widget=forms.widgets.RadioSelect(),
                )

        form = RadioSelectForm()
        self.assertEqual(
            type(form.fields['radio_select'].widget),
            widgets.MaterialRadioSelect,
            )


    def test_MaterialForm_materializes_SelectDateWidget(self):
        """django.forms.widgets.SelectDateWidget should be converted to
        material_widgets.widgets.MaterialSelectDateWidget.
        """

        class SelectDateForm(MaterialForm):
            select_date_widget = forms.DateField(
                widget=forms.widgets.SelectDateWidget(),
                )

        form = SelectDateForm()
        self.assertEqual(
            type(form.fields['select_date_widget'].widget),
            widgets.MaterialSelectDateWidget,
            )

    def test_MaterialForm_materializes_SplitDateTimeField(self):
        """django.forms.widgets.SplitDateTimeWidget should be converted to
        material_widgets.widgets.MaterialSplitDateTimeWidget.
        """

        class SplitDateTimeInputForm(MaterialForm):
            split_date_time_widget = forms.SplitDateTimeField()

        form = SplitDateTimeInputForm()
        self.assertEqual(
            type(form.fields['split_date_time_widget'].widget),
            widgets.MaterialSplitDateTimeWidget,
            )

    def test_MaterialForm_materializes_SplitHiddenDateTimeWidget(self):
        """django.forms.widgets.SplitHiddenDateTimeWidget should be converted to
        material_widgets.widgets.MaterialSplitHiddenDateTimeWidget.
        """

        class SplitHiddenDateTimeInputForm(MaterialForm):
            split_hidden_date_time_widget = forms.SplitDateTimeField(
                widget=forms.widgets.SplitHiddenDateTimeWidget(),
                )

        form = SplitHiddenDateTimeInputForm()
        self.assertEqual(
            type(form.fields['split_hidden_date_time_widget'].widget),
            widgets.MaterialSplitHiddenDateTimeWidget,
            )

    def test_MaterialForm_materializes_Textarea(self):
        """django.forms.widgets.Textarea should be converted to
        material_widgets.widgets.MaterialTextarea.
        """

        class TextareaForm(MaterialForm):
            textarea = forms.CharField(
                widget=forms.widgets.Textarea(),
                )

        form = TextareaForm()
        self.assertEqual(
            type(form.fields['textarea'].widget),
            widgets.MaterialTextarea,
            )

    def test_MaterialForm_materializes_TimeField(self):
        """django.forms.widgets.TimeInput should be converted to
        material_widgets.widgets.MaterialTimeInput.
        """

        class TimeInputForm(MaterialForm):
            time_input = forms.TimeField()

        form = TimeInputForm()
        self.assertEqual(
            type(form.fields['time_input'].widget),
            widgets.MaterialTimeInput,
            )

    def test_MaterialForm_materializes_URLField(self):
        """django.forms.widgets.URLInput should be converted to
        material_widgets.widgets.MaterialURLInput.
        """

        class URLInputForm(MaterialForm):
            url_input = forms.URLField()

        form = URLInputForm()
        self.assertEqual(
            type(form.fields['url_input'].widget),
            widgets.MaterialURLInput,
            )


class MaterialModelFormMaterializeTests(TestCase):
    """Test cases for material_widgets.forms.MaterialModelForm.
    Each field's widget should automatically use a Material Component.
    """

    @classmethod
    def setUpClass(cls):
        class TestModelForm(MaterialModelForm):
            """Test ModelForm with Material Component fields"""

            class Meta:
                """Meta settings for TestModelForm"""
                model = MaterialWidgetsTestModel
                fields = '__all__'

        cls._form = TestModelForm()

    @classmethod
    def tearDownClass(cls):
        del cls._form

    def test_MaterialModelForm_materializes_BigIntegerField(self):
        """django.models.BigIntegerField should use
        material_widgets.widgets.MaterialNumberInput.
        """
        self.assertEqual(
            type(self._form.fields['big_integer_field'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialModelForm_materializes_BooleanField(self):
        """django.models.BooleanField should use
        material_widgets.widgets.MaterialCheckboxInput.
        """
        self.assertEqual(
            type(self._form.fields['boolean_field'].widget),
            widgets.MaterialCheckboxInput,
            )

    def test_MaterialModelForm_materializes_CharField(self):
        """django.models.CharField should use
        material_widgets.widgets.MaterialTextInput.
        """
        self.assertEqual(
            type(self._form.fields['char_field'].widget),
            widgets.MaterialTextInput,
            )

    def test_MaterialModelForm_materializes_DateField(self):
        """django.models.DateField should use
        material_widgets.widgets.MaterialDateInput.
        """
        self.assertEqual(
            type(self._form.fields['date_field'].widget),
            widgets.MaterialDateInput,
            )

    def test_MaterialModelForm_materializes_DateTimeField(self):
        """django.models.DateTimeField should use
        material_widgets.widgets.MaterialDateTimeInput.
        """
        self.assertEqual(
            type(self._form.fields['date_time_field'].widget),
            widgets.MaterialDateTimeInput,
            )

    def test_MaterialModelForm_materializes_DecimalField(self):
        """django.models.DecimalField should use
        material_widgets.widgets.MaterialNumberInput.
        """
        self.assertEqual(
            type(self._form.fields['decimal_field'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialModelForm_materializes_EmailField(self):
        """django.models.EmailField should use
        material_widgets.widgets.MaterialEmailInput.
        """
        self.assertEqual(
            type(self._form.fields['email_field'].widget),
            widgets.MaterialEmailInput,
            )

    def test_MaterialModelForm_materializes_FileField(self):
        """django.models.FileField should use
        material_widgets.widgets.MaterialClearableFileInput.
        """
        self.assertEqual(
            type(self._form.fields['file_field'].widget),
            widgets.MaterialClearableFileInput,
            )

    def test_MaterialModelForm_materializes_FilePathField(self):
        """django.models.FilePathField should use
        material_widgets.widgets.MaterialSelect.
        """
        self.assertEqual(
            type(self._form.fields['file_path_field'].widget),
            widgets.MaterialSelect,
            )

    def test_MaterialModelForm_materializes_FloatField(self):
        """django.models.FloatField should use
        material_widgets.widgets.MaterialNumberInput.
        """
        self.assertEqual(
            type(self._form.fields['float_field'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialModelForm_materializes_ForeignKey(self):
        """django.models.ForeignKey should use
        material_widgets.widgets.MaterialSelect.
        """
        self.assertEqual(
            type(self._form.fields['foreign_key'].widget),
            widgets.MaterialSelect,
            )

    def test_MaterialModelForm_materializes_IntegerField(self):
        """django.models.IntegerField should use
        material_widgets.widgets.MaterialNumberInput.
        """
        self.assertEqual(
            type(self._form.fields['integer_field'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialModelForm_materializes_GenericIPAddressField(self):
        """django.models.GenericIPAddressField should use
        material_widgets.widgets.MaterialTextInput.
        """
        self.assertEqual(
            type(self._form.fields['generic_ip_address_field'].widget),
            widgets.MaterialTextInput,
            )

    def test_MaterialModelForm_materializes_ManyToManyField(self):
        """django.models.ManyToManyField should use
        material_widgets.widgets.MaterialSelectMultiple.
        """
        self.assertEqual(
            type(self._form.fields['many_to_many_field'].widget),
            widgets.MaterialSelectMultiple,
            )

    def test_MaterialModelForm_materializes_NullBooleanField(self):
        """django.models.NullBooleanField should use
        material_widgets.widgets.MaterialNullBooleanSelect.
        """
        self.assertEqual(
            type(self._form.fields['null_boolean_field'].widget),
            widgets.MaterialNullBooleanSelect,
            )

    def test_MaterialModelForm_materializes_PositiveIntegerField(self):
        """django.models.PositiveIntegerField should use
        material_widgets.widgets.MaterialNumberInput.
        """
        self.assertEqual(
            type(self._form.fields['positive_integer_field'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialModelForm_materializes_PositiveSmallIntegerField(self):
        """django.models.PositiveSmallIntegerField should use
        material_widgets.widgets.MaterialNumberInput.
        """
        self.assertEqual(
            type(self._form.fields['positive_small_integer_field'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialModelForm_materializes_SlugField(self):
        """django.models.SlugField should use
        material_widgets.widgets.MaterialTextInput.
        """
        self.assertEqual(
            type(self._form.fields['slug_field'].widget),
            widgets.MaterialTextInput,
            )

    def test_MaterialModelForm_materializes_SmallIntegerField(self):
        """django.models.SmallIntegerField should use
        material_widgets.widgets.MaterialNumberInput.
        """
        self.assertEqual(
            type(self._form.fields['small_integer_field'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialModelForm_materializes_TextField(self):
        """django.models.TextField should use
        material_widgets.widgets.MaterialTextarea.
        """
        self.assertEqual(
            type(self._form.fields['text_field'].widget),
            widgets.MaterialTextarea,
            )

    def test_MaterialModelForm_materializes_TimeField(self):
        """django.models.TimeField should use
        material_widgets.widgets.MaterialTimeInput.
        """
        self.assertEqual(
            type(self._form.fields['time_field'].widget),
            widgets.MaterialTimeInput,
            )

    def test_MaterialModelForm_materializes_URLField(self):
        """django.models.URLField should use
        material_widgets.widgets.MaterialURLInput.
        """
        self.assertEqual(
            type(self._form.fields['url_field'].widget),
            widgets.MaterialURLInput,
            )


class MaterialModelFormMethodTests(TestCase):
    """Test cases for material_widgets.forms.MaterialModelForm.
    Inherited ModelForm methods should process form data.
    """

    @classmethod
    def setUpClass(cls):
        class TestModelForm(MaterialModelForm):
            """Test ModelForm with Material Component fields"""

            class Meta:
                """Meta settings for TestModelForm"""
                model = MaterialWidgetsTestModel
                fields = '__all__'

        cls._form = TestModelForm

    @classmethod
    def tearDownClass(cls):
        del cls._form

    def test_MaterialModelForm_is_valid_should_validate_correct_data(self):
        """MaterialModelForm.is_valid() should return True with valid data."""
        data = {'integer_field': 1}
        form = self._form(data=data)
        self.assertTrue(form.is_valid())

    def test_MaterialModelForm_is_valid_should_invalidate_wrong_data(self):
        """MaterialModelForm.is_valid() should return False with invalid data."""
        data = {'positive_integer_field': -1}
        form = self._form(data=data)
        self.assertFalse(form.is_valid())

    def test_MaterialModelForm_save_valid_data_should_create_a_new_entry(self):
        """MaterialModelForm.save() should create a new database entry with
        valid form data.
        """
        data = {'url_field': 'https://github.com/ooknosi'}
        form = self._form(data=data)
        self.assertEqual(MaterialWidgetsTestModel.objects.count(), 0)
        form.save()
        self.assertEqual(MaterialWidgetsTestModel.objects.count(), 1)
        self.assertEqual(
            MaterialWidgetsTestModel.objects.get().url_field,
            'https://github.com/ooknosi'
            )

    def test_MaterialModelForm_save_invalid_data_should_not_create_a_new_entry(self):
        """MaterialModelForm.save() should not create a new database entry with
        invalid form data.
        """
        data = {'url_field': 'ooknosi'}
        form = self._form(data=data)
        self.assertRaises(ValueError, form.save)
        self.assertEqual(MaterialWidgetsTestModel.objects.count(), 0)
