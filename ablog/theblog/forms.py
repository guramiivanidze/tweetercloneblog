from tkinter import Widget
from django import forms
from .models import Post, Category


choices = Category.objects.all().values_list('name', 'name')

choice_list = [item for item in choices]
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'enter title',
                                            }),
            'title_tag': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'enter title tag',
                                                }),
            'author': forms.Select(attrs={'class': 'form-control',

                                          }),
            'category': forms.Select(choices=choice_list,
                                     attrs={'class': 'form-control',

                                            }),
            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'enter text here',
                                          "style": "line-height: 10px;"
                                          }),
        }


class UpdatePostForm(forms.ModelForm ):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'enter title',
                                            }),
            'title_tag': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'enter title tag',
                                                }),
            
            'category': forms.Select(choices=choice_list,
                                     attrs={'class': 'form-control',

                                            }),

            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'enter text here',
                                          }),
        }
