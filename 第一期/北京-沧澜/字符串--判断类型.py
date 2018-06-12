# _*_coding:utf-8_*_
_author_ = '张晋'
if __name__ == "__main__":
    str_1 = "1234567890"
    str_2 = "abcdefghKHJKOOO"
    str_3 = "12345abcdeASSDF"
    str_4 = "abcedf"
    str_5 = "ABCNDNF"
    str_6 = "   "
    str_7 = "  sghghhg"
# isalnum
print(str_3.isalnum())
# isalpha
print(str_2.isalpha())
# isdigit
print(str_1.isdigit())
# islower
print(str_4.islower())
print(str_2.islower())
# isupper
print(str_4.isupper())
print(str_2.isupper())
# issapce
print(str_6.isspace())
print(str_7.isspace())
