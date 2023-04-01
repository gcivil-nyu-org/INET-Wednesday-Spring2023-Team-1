from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from collections import OrderedDict
from .models import (
    FavoriteSong,
    FavoriteArtist,
    FavoriteAlbum,
    FavoriteGenre,
    UserPrompts,
    Account,
)
from .models import PromptList
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, Div
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
import datetime


class NewUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Username"})
    )
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={"placeholder": "Email"})
    )
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Password"})
    )
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Confirm Password"})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class PasswordChangeForm(SetPasswordForm):
    """
    A form that lets a user change their password by entering their old
    password.
    """

    error_messages = dict(
        SetPasswordForm.error_messages,
        **{
            "password_incorrect": (
                "Your old password was entered incorrectly. " "Please enter it again."
            ),
        }
    )
    old_password = forms.CharField(label=("Old password"), widget=forms.PasswordInput)

    def clean_old_password(self):
        """
        Validates that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages["password_incorrect"],
                code="password_incorrect",
            )
        return old_password


PasswordChangeForm.base_fields = OrderedDict(
    (k, PasswordChangeForm.base_fields[k])
    for k in ["old_password", "new_password1", "new_password2"]
)


class SongEdit(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SongEdit, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-0.2"
        self.helper.field_class = "col-lg"
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Fieldset("<strong>Enter Your Top 5 Songs: </strong> "),
            Field(
                "song1_name_artist",
                placeholder="1. ",
                css_class="form-control form-control-lg",
            ),
            Field(
                "song2_name_artist",
                placeholder="2. ",
                css_class="form-control form-control-lg",
            ),
            Field(
                "song3_name_artist",
                placeholder="3. ",
                css_class="form-control form-control-lg",
            ),
            Field(
                "song4_name_artist",
                placeholder="4. ",
                css_class="form-control form-control-lg",
            ),
            Field(
                "song5_name_artist",
                placeholder="5. ",
                css_class="form-control form-control-lg",
            ),
            Field("song1_id", type="hidden"),
            Field("song2_id", type="hidden"),
            Field("song3_id", type="hidden"),
            Field("song4_id", type="hidden"),
            Field("song5_id", type="hidden"),
        )
        self.helper.form_show_labels = False

    class Meta:
        model = FavoriteSong
        fields = (
            "song1_id",
            "song2_id",
            "song3_id",
            "song4_id",
            "song5_id",
            "song1_name_artist",
            "song2_name_artist",
            "song3_name_artist",
            "song4_name_artist",
            "song5_name_artist",
        )


class ArtistEdit(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArtistEdit, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-lg-0"
        self.helper.field_class = "col-lg"
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Fieldset("<strong>Enter Your Top 5 Artists: </strong> "),
            Field(
                "artist1_name",
                placeholder="1. ",
                css_class="form-control form-control-lg",
            ),
            Field(
                "artist2_name",
                placeholder="2. ",
                css_class="form-control form-control-lg",
            ),
            Field(
                "artist3_name",
                placeholder="3. ",
                css_class="form-control form-control-lg",
            ),
            Field(
                "artist4_name",
                placeholder="4. ",
                css_class="form-control form-control-lg",
            ),
            Field(
                "artist5_name",
                placeholder="5. ",
                css_class="form-control form-control-lg",
            ),
            Field("artist1_id", type="hidden"),
            Field("artist2_id", type="hidden"),
            Field("artist3_id", type="hidden"),
            Field("artist4_id", type="hidden"),
            Field("artist5_id", type="hidden"),
        )
        self.helper.form_show_labels = False

    class Meta:
        model = FavoriteArtist
        fields = (
            "artist1_id",
            "artist2_id",
            "artist3_id",
            "artist4_id",
            "artist5_id",
            "artist1_name",
            "artist2_name",
            "artist3_name",
            "artist4_name",
            "artist5_name",
        )


class AlbumEdit(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AlbumEdit, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-lg-0"
        self.helper.field_class = "col-lg"
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Fieldset("<strong>Enter Your Top 5 Albums: </strong> "),
            Field(
                "album1_name_artist",
                placeholder="1. ",
                css_class="form-control form-control-lg",
            ),
            Field(
                "album2_name_artist",
                placeholder="2. ",
                css_class="form-control form-control-lg",
            ),
            Field(
                "album3_name_artist",
                placeholder="3. ",
                css_class="form-control form-control-lg",
            ),
            Field(
                "album4_name_artist",
                placeholder="4. ",
                css_class="form-control form-control-lg",
            ),
            Field(
                "album5_name_artist",
                placeholder="5. ",
                css_class="form-control form-control-lg",
            ),
            Field("album1_id", type="hidden"),
            Field("album2_id", type="hidden"),
            Field("album3_id", type="hidden"),
            Field("album4_id", type="hidden"),
            Field("album5_id", type="hidden"),
        )
        self.helper.form_show_labels = False

    class Meta:
        model = FavoriteAlbum
        fields = (
            "album1_id",
            "album2_id",
            "album3_id",
            "album4_id",
            "album5_id",
            "album1_name_artist",
            "album2_name_artist",
            "album3_name_artist",
            "album4_name_artist",
            "album5_name_artist",
        )


class GenreEdit(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GenreEdit, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-0.2"
        self.helper.field_class = "col-lg"
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Fieldset("<strong>Enter Your Top 5 Genres: </strong> "),
            Field(
                "genre1",
                placeholder="1. ",
                css_class="form-control form-control-lg",
            ),
            Field(
                "genre2",
                placeholder="2. ",
                css_class="form-control form-control-lg",
            ),
            Field(
                "genre3",
                placeholder="3. ",
                css_class="form-control form-control-lg",
            ),
            Field(
                "genre4",
                placeholder="4. ",
                css_class="form-control form-control-lg",
            ),
            Field(
                "genre5",
                placeholder="5. ",
                css_class="form-control form-control-lg",
            ),
        )
        self.helper.form_show_labels = False

    class Meta:
        model = FavoriteGenre
        fields = (
            "genre1",
            "genre2",
            "genre3",
            "genre4",
            "genre5",
        )


def get_prompt_choices():
    prompt_choices = [("", "Choose a prompt")]
    all_prompts = PromptList.objects.all()
    for choice in all_prompts:
        prompt_choices.append((choice.prompt, choice.prompt))
    return prompt_choices


class PromptEdit(ModelForm):
    try:
        prompt_choices = get_prompt_choices()
        prompt1 = forms.ChoiceField(choices=prompt_choices)
        prompt2 = forms.ChoiceField(choices=prompt_choices)
        prompt3 = forms.ChoiceField(choices=prompt_choices)
        prompt4 = forms.ChoiceField(choices=prompt_choices)
        prompt5 = forms.ChoiceField(choices=prompt_choices)
    except:
        prompt1 = "Choose prompt"
        prompt2 = "Choose prompt"
        prompt3 = "Choose prompt"
        prompt4 = "Choose prompt"
        prompt5 = "Choose prompt"


    def __init__(self, *args, **kwargs):
        super(PromptEdit, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Fieldset("<strong>Select Prompts and Enter Responses: </strong> "),
            Div(
                Div(
                    Field("prompt1", css_class="form-group custom-select-lg"),
                    css_class="col",
                ),
                Div(
                    Field(
                        "response1",
                        placeholder="Song 1:",
                        css_class="form-group form-control-lg",
                    ),
                    css_class="col",
                ),
                css_class="form-row",
            ),
            Div(
                Div(
                    Field("prompt2", css_class="form-group custom-select-lg"),
                    css_class="col",
                ),
                Div(
                    Field(
                        "response2",
                        placeholder="Song 2:",
                        css_class="form-group form-control-lg",
                    ),
                    css_class="col",
                ),
                css_class="form-row",
            ),
            Div(
                Div(
                    Field("prompt3", css_class="form-group custom-select-lg"),
                    css_class="col",
                ),
                Div(
                    Field(
                        "response3",
                        placeholder="Song 3:",
                        css_class="form-group form-control-lg",
                    ),
                    css_class="col",
                ),
                css_class="form-row",
            ),
            Div(
                Div(
                    Field("prompt4", css_class="form-group custom-select-lg"),
                    css_class="col",
                ),
                Div(
                    Field(
                        "response4",
                        placeholder="Song 4:",
                        css_class="form-group form-control-lg",
                    ),
                    css_class="col",
                ),
                css_class="form-row",
            ),
            Div(
                Div(
                    Field("prompt5", css_class="form-group custom-select-lg"),
                    css_class="col",
                ),
                Div(
                    Field(
                        "response5",
                        placeholder="Song 5: ",
                        css_class="form-group form-control-lg",
                    ),
                    css_class="col",
                ),
                css_class="form-row",
            ),
        )
        self.helper.form_show_labels = False

    class Meta:
        model = UserPrompts
        fields = (
            "prompt1",
            "prompt2",
            "prompt3",
            "prompt4",
            "prompt5",
            "response1",
            "response2",
            "response3",
            "response4",
            "response5",
        )


class AccountSettingsForm(ModelForm):
    curr_year = datetime.date.today().year
    year_list = []
    for year in range(curr_year, 1899, -1):
        year_list.append((year, year))
    birth_year = forms.ChoiceField(choices=year_list)

    def __init__(self, *args, **kwargs):
        super(AccountSettingsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Div(
                Fieldset("First Name:"),
                Div(
                    Field(
                        "first_name",
                        placeholder="John",
                        css_class="form-group form-control-lg",
                    ),
                ),
                Fieldset("Last Name:"),
                Div(
                    Field(
                        "last_name",
                        placeholder="Doe",
                        css_class="form-group form-control-lg",
                    ),
                ),
                Fieldset("Year of Birth:"),
                Div(
                    Field(
                        "birth_year",
                        placeholder="YYYY",
                        css_class="form-group form-control-lg",
                    ),
                ),
                Fieldset("Location:"),
                Div(
                    Field(
                        "location",
                        placeholder="Brooklyn",
                        css_class="form-group form-control-lg",
                    ),
                ),
                Fieldset("Profile Picture:"),
                Div(
                    Field(
                        "profile_picture",
                        css_class="form-group form-control-lg",
                    ),
                ),
            ),
        )
        self.helper.form_show_labels = False

    class Meta:
        model = Account
        fields = (
            "first_name",
            "last_name",
            "birth_year",
            "location",
            "profile_picture",
        )
