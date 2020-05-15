# -*- coding: utf-8 -*-
def check_tel(tel: str) -> bool:
    s = str(tel)
    return s.isdigit() and len(s) == 11 and s[0] == '1'
