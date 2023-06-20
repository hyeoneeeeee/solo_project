import re
import string
from rest_framework.validators import ValidationError


def usernameValidator(username):
    is_right_username = re.compile(r"^([a-zA-Z0-9_]{4})*$")
    return is_right_username.match(username)

def confirm_letter(password, passowrd2):
    if password == passowrd2:
        return True
    return False

def contain_special_letter(password):
    for word in password:
        if word in string.punctuation:
            return True
    return False

def contain_lowercase_letter(password):
    is_lowercase_letter = re.compile(r"^([A-Z])")
    return is_lowercase_letter.match(password)

def contain_number(password):
    is_number = re.compile(r"^([0-9])")
    return is_number.match(password)


def contain_upercase_letter(password):
    is_upercase_letter = re.compile(r"^([a-z])")
    return is_upercase_letter.match(password)

class PasswordValidator:
    def validate(self, password, password2):
        if (len(password) < 8 or
            not contain_upercase_letter(password) or
            not confirm_letter(password, password2) or
            not contain_number(password) or
            not contain_special_letter(password) or
            not contain_lowercase_letter(password)):
            raise ValidationError('비밀번호는 특수문자, 숫자, 영어 대문자, 소문자 포함 8자 이상이여야 합니다.')

    def get_help_text(self):
        return '비밀번호는 특수문자, 숫자, 영어 대문자, 소문자 포함 8자 이상이여야 합니다.'