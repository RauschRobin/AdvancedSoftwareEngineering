from typing import Any


class Sentence1():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.sentences = []

    def add(self, sentence: Any) -> None:
        self.sentences.append(sentence)

    def get_all(self):
        return '. '.join(self.sentences)

    def list_sentences(self) -> None:
        print(f"Combined sentences: {', '.join(self.sentences)}", end="")
