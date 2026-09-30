from enum import Enum


class EnterPosition(Enum):
    RIGHT = 1
    LEFT = 2
    RIGHT_LEFT = 4


key_word_enter_position = {
    "with": EnterPosition.RIGHT,
    "select": EnterPosition.RIGHT_LEFT,
    "from": EnterPosition.RIGHT_LEFT,
    "where": EnterPosition.RIGHT_LEFT,
    "group by": EnterPosition.RIGHT_LEFT,
    "order by": EnterPosition.RIGHT_LEFT,
    "having": EnterPosition.RIGHT_LEFT,
    "limit": EnterPosition.RIGHT_LEFT,
    "inner join": EnterPosition.LEFT,
    "left join": EnterPosition.LEFT,
    "right join": EnterPosition.LEFT,
    "full join": EnterPosition.LEFT,
    "cross join": EnterPosition.LEFT,
    "case": EnterPosition.RIGHT,
    "when": EnterPosition.LEFT,
    "else": EnterPosition.LEFT,
    "end": EnterPosition.LEFT,
}


def add_enter(text: str) -> str:
    text = add_enter_to_key_words(text)
    text = add_enter_to_commas(text)
    return text


def add_enter_to_key_words(text: str) -> str:
    for key_word, enter_position in key_word_enter_position.items():
        if enter_position in (EnterPosition.RIGHT, EnterPosition.RIGHT_LEFT):
            text = text.replace(key_word + " ", key_word + "\n")
        if enter_position in (EnterPosition.LEFT, EnterPosition.RIGHT_LEFT):
            text = text.replace(" " + key_word, "\n" + key_word)
    return text


def add_enter_to_commas(text: str) -> str:
    commas_positions = []

    for position, char in enumerate(text):
        if char != ",":
            continue
        parentesis_count = 0
        for counter in range(position - 1, 0, -1):
            if text[counter] == "\n":
                break
            elif text[counter] == "(":
                parentesis_count -= 1
            elif text[counter] == ")":
                parentesis_count += 1
        if parentesis_count == 0:
            commas_positions.append(position)

    for position in reversed(commas_positions):
        continue_position = position + 1
        if text[position + 1] == " ":
            continue_position = position + 2

        text = text[: position + 1] + "\n" + text[continue_position:]

    return text
