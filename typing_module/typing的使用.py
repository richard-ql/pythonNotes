# import typing
#
# def headline(text: str, align: bool=True) -> str:
#     if align:
#         return f"{'-' * len(text)}\n{text.title()}\n{'-' * len(text)}"
#     else:
#         return f"{text.title()}".center(50, 'o')
#
# print(headline("python type checking"))
# print(headline(" python type checking ", align="center"))
# print((1,2)>(1,1))

##########################################################

import random
from typing import Sequence, TypeVar

