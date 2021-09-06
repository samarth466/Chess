from django import forms

class SelectDateInputWidget(forms.widgets.DateInput):
    def __init__(self, attrs: Optional[_OptAttrs], format: Optional[str]):
        super().__init__(attrs=attrs, format=format)(self, attrs=None, *args, **kwargs):
        attrs = attrs or {}
        default_options = {}
        options = kwargs.get('options',{})
        default_options.update(options)
        for key, value in default_options.items():
            attrs['data-'+key] = value
        super().__init__(attrs)
    
            )
        }