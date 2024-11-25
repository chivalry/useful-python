class CVString(str):
    '''Subclass of `str` that provides useful utility methods.'''

    def chunks(self, length: int) -> list[str]:
        '''Return a list with the string broken into chunks of length specified.

        :param length: int - The length of the chunks to break the string into
        :return list[str] - A list of strings, each one no longer than `length`
        '''
        return [
            self[0 + i:length + i]
            for i in range(0, len(self), length)
        ]

    def is_integer(self):
        '''Return `True` if the string can be interpreted as an integier, either positive or
        negative
        :return bool - `True` if the string can be converted to an integer'''
        return ((self[0] in ['-', '+']) and self[1:].isdigit()) or self.isdigit()
