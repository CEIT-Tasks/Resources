from functools import singledispatchmethod

class Calculator:
    @singledispatchmethod
    def multiply(self, value, times):
        raise NotImplementedError

    @multiply.register
    def _(self, value: int, times: int):
        return value ** times

    @multiply.register
    def _(self, value: str, times: int):
        return value * times

    @multiply.register
    def _(self, value: list, times: int):
        return value * times