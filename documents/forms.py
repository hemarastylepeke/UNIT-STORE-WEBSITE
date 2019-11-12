from django import forms
from .models import Book

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('title', 'code', 'pdf')

	def clean(self):
		cleaned_data = super(BookForm, self).clean()
		title = cleaned_data.get('title')
		code = cleaned_data.get('code')
		pdf = cleaned_data.get('pdf')
		if not title and not code and not pdf:
			raise forms.ValidationError('You have to write something!')