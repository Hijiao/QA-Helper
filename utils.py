# coding=utf-8

# replace(u"′′", "\"").replace(u"″", "\"").replace(u"_", u"一").replace("\n", "").replace("/J\\",u"小").replace(u"′",u"，")
words_dict = [
    (u"′′", "\""),
    (u"″", "\""),
    (u"-", ""),
    (u"_", u"一"),
    # (u"\n", ""),
    (u"/J\\", u"小"),
    (u"′", u"，")
]


def reformat(s):
    for k, v in words_dict:
        s = s.replace(k, v)
    return s

