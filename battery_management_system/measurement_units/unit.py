from abc import ABC, abstractclassmethod


class Units(ABC):
    @abstractclassmethod
    def get_accepted_units():
        raise NotImplementedError
