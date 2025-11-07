from collections import namedtuple

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


w = "\u2b06\ufe0f"
a = "\u2b05\ufe0f"
s = "\u2b07\ufe0f"
d = "\u27a1\ufe0f"


REPLY_MARKUP = namedtuple(
    "ReplyMarkup",
    [
        "START",
        "POSITIONS",
    ],
)(
    InlineKeyboardMarkup([[InlineKeyboardButton("Старт", callback_data="_")]]),
    (
        InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(w, callback_data="4")],
                [
                    InlineKeyboardButton(a, callback_data="1"),
                    #
                    #
                ],
            ]
        ),
        InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(w, callback_data="5")],
                [
                    InlineKeyboardButton(a, callback_data="2"),
                    #
                    InlineKeyboardButton(d, callback_data="0"),
                ],
            ]
        ),
        InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(w, callback_data="6")],
                [
                    InlineKeyboardButton(a, callback_data="3"),
                    #
                    InlineKeyboardButton(d, callback_data="1"),
                ],
            ]
        ),
        InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(w, callback_data="7")],
                [
                    #
                    #
                    InlineKeyboardButton(d, callback_data="2"),
                ],
            ]
        ),
        InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(w, callback_data="8")],
                [
                    InlineKeyboardButton(a, callback_data="5"),
                    InlineKeyboardButton(s, callback_data="0"),
                    #
                ],
            ]
        ),
        InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(w, callback_data="9")],
                [
                    InlineKeyboardButton(a, callback_data="6"),
                    InlineKeyboardButton(s, callback_data="1"),
                    InlineKeyboardButton(d, callback_data="4"),
                ],
            ]
        ),
        InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(w, callback_data="10")],
                [
                    InlineKeyboardButton(a, callback_data="7"),
                    InlineKeyboardButton(s, callback_data="2"),
                    InlineKeyboardButton(d, callback_data="5"),
                ],
            ]
        ),
        InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(w, callback_data="11")],
                [
                    #
                    InlineKeyboardButton(s, callback_data="3"),
                    InlineKeyboardButton(d, callback_data="6"),
                ],
            ]
        ),
        InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(w, callback_data="12")],
                [
                    InlineKeyboardButton(a, callback_data="9"),
                    InlineKeyboardButton(s, callback_data="4"),
                    #
                ],
            ]
        ),
        InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(w, callback_data="13")],
                [
                    InlineKeyboardButton(a, callback_data="10"),
                    InlineKeyboardButton(s, callback_data="5"),
                    InlineKeyboardButton(d, callback_data="8"),
                ],
            ]
        ),
        InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(w, callback_data="14")],
                [
                    InlineKeyboardButton(a, callback_data="11"),
                    InlineKeyboardButton(s, callback_data="6"),
                    InlineKeyboardButton(d, callback_data="9"),
                ],
            ]
        ),
        InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(w, callback_data="15")],
                [
                    #
                    InlineKeyboardButton(s, callback_data="7"),
                    InlineKeyboardButton(d, callback_data="10"),
                ],
            ]
        ),
        InlineKeyboardMarkup(
            [
                #
                [
                    InlineKeyboardButton(a, callback_data="13"),
                    InlineKeyboardButton(s, callback_data="8"),
                    #
                ],
            ]
        ),
        InlineKeyboardMarkup(
            [
                #
                [
                    InlineKeyboardButton(a, callback_data="14"),
                    InlineKeyboardButton(s, callback_data="9"),
                    InlineKeyboardButton(d, callback_data="12"),
                ],
            ]
        ),
        InlineKeyboardMarkup(
            [
                #
                [
                    InlineKeyboardButton(a, callback_data="15"),
                    InlineKeyboardButton(s, callback_data="10"),
                    InlineKeyboardButton(d, callback_data="13"),
                ],
            ]
        ),
        InlineKeyboardMarkup(
            [
                #
                [
                    #
                    InlineKeyboardButton(s, callback_data="11"),
                    InlineKeyboardButton(d, callback_data="14"),
                ],
            ]
        ),
    ),
)
