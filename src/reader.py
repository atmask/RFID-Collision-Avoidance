
class BaseTagReader():
    ''' cdefine a common interface for Readers implementing collision detection protocols'''


    def __init__(self):
        pass

    def manage_collision(self, tags):
        pass


class BinaryTagReader(BaseTagReader):

    def manage_collision(self, tags):
        super().manage_collision()
        self.binary_search(tags)

    def _increment_bit_string(self, bitstr):
        return bin(int(bitstr, 2)+1)
    
    def binary_search(self, tags, id=None):
        '''Transmit an ID with three numbers. If collision then manage_collision with subset'''
        if len(tags) <= 1:
            return tags
        
        id = "0" if not id else self._increment_bit_string(id)



