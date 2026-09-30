from enum import Enum


class TabIncrementor(Enum):
    INCREMENT = 1
    DECREMENT = 2
    KEEP = 4


class UseIdentation(Enum):
    PREVIOUS_INDENTATION = 1
    NEXT_IDENTATION = 2


class PersistIdentation(Enum):
    YES = 1
    NO = 2


key_word_tab_incrementor = {
    "with": [TabIncrementor.INCREMENT, UseIdentation.PREVIOUS_INDENTATION, PersistIdentation.YES],
    "select": [TabIncrementor.INCREMENT, UseIdentation.PREVIOUS_INDENTATION, PersistIdentation.YES],
    "from": [TabIncrementor.DECREMENT, UseIdentation.NEXT_IDENTATION, PersistIdentation.NO],
    "where": [TabIncrementor.DECREMENT, UseIdentation.NEXT_IDENTATION, PersistIdentation.NO],
    "group by": [TabIncrementor.DECREMENT, UseIdentation.NEXT_IDENTATION, PersistIdentation.NO],
    "order by": [TabIncrementor.DECREMENT, UseIdentation.NEXT_IDENTATION, PersistIdentation.NO],
    "having": [TabIncrementor.DECREMENT, UseIdentation.NEXT_IDENTATION, PersistIdentation.NO],
    "limit": [TabIncrementor.DECREMENT, UseIdentation.NEXT_IDENTATION, PersistIdentation.NO],
    "inner join": [TabIncrementor.KEEP, UseIdentation.NEXT_IDENTATION, PersistIdentation.NO],
    "left join": [TabIncrementor.KEEP, UseIdentation.NEXT_IDENTATION, PersistIdentation.NO],
    "right join": [TabIncrementor.KEEP, UseIdentation.NEXT_IDENTATION, PersistIdentation.NO],
    "full join": [TabIncrementor.KEEP, UseIdentation.NEXT_IDENTATION, PersistIdentation.NO],
    "cross join": [TabIncrementor.KEEP, UseIdentation.NEXT_IDENTATION, PersistIdentation.NO],
    "case": [TabIncrementor.KEEP, UseIdentation.NEXT_IDENTATION, PersistIdentation.NO],
    "when": [TabIncrementor.INCREMENT, UseIdentation.NEXT_IDENTATION, PersistIdentation.NO],
    "else": [TabIncrementor.INCREMENT, UseIdentation.NEXT_IDENTATION, PersistIdentation.NO],
    "end": [TabIncrementor.KEEP, UseIdentation.NEXT_IDENTATION, PersistIdentation.NO],
}


def add_tab(text: str) -> str:
    return add_tabs_to_key_words(text)


def add_tabs_to_key_words(text: str) -> str:
    lines = text.split("\n")
    indentation = 0
    for i, line in enumerate(lines):
        if not any(line.strip().startswith(key_word) for key_word in key_word_tab_incrementor):
            lines[i] = "\t" * indentation + line.strip()
            continue

        for key_word, tab_incrementor in key_word_tab_incrementor.items():
            if line.strip().startswith(key_word):
                temp_indentation = indentation

                if tab_incrementor[1] == UseIdentation.PREVIOUS_INDENTATION:
                    lines[i] = "\t" * temp_indentation + line.strip()

                if tab_incrementor[0] == TabIncrementor.INCREMENT:
                    temp_indentation += 1
                if tab_incrementor[0] == TabIncrementor.DECREMENT:
                    temp_indentation -= 1

                if tab_incrementor[1] == UseIdentation.NEXT_IDENTATION:
                    lines[i] = "\t" * temp_indentation + line.strip()

                if tab_incrementor[2] == PersistIdentation.YES:
                    indentation = temp_indentation

    return "\n".join(lines)
