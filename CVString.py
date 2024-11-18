class CVString(str):
    '''Subclass of `str` that provides useful utility methods.'''

    def chunk_string(self, length):
        '''Return a list with the string broken into chunks of length specified.'''
        return [self[0 + i:length + i] for i in range(0, len(self), length)]
