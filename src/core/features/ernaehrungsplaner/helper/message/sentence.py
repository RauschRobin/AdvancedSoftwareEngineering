from typing import Any


class Sentence1():
    def __init__(self) -> None:
        self.sentences = []

    def add(self, sentence: Any) -> None:
        self.sentences.append(sentence)

    def get_all(self):
        return '. '.join(self.sentences)

    def list_sentences(self) -> None:
        print(f"Combined sentences: {', '.join(self.sentences)}", end="")
