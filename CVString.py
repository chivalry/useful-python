class CVString(str):
    '''Subclass of `str` that provides useful utility methods.'''

    def chunk_string(self, length: int) -> list[str]:
        '''Return a list with the string broken into chunks of length specified.

        :param length: int - The length of the chunks to break the string into
        :return list[str] - A list of strings, each one no longer than `length`
        '''
        return [
            self[0 + i:length + i]
            for i in range(0, len(self), length)
        ]
