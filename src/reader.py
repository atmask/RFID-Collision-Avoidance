from abc import ABC, abstractmethod
class BaseTagReader(ABC):
    ''' cdefine a common interface for Readers implementing collision detection protocols'''


    def __init__(self):
        pass

    @abstractmethod
    def manage_collision(self, tags):
        pass


class BinaryTagReader(BaseTagReader):

    def manage_collision(self, tags):
        super().manage_collision()
        return self.binary_search(tags)

    def _get_bit_string(self, i):
        bit_arr = ['0b000', '0b001', '0b010', '0b011', '0b100', '0b101', '0b110', '0b111']
        if i > 7:
            return
        else:
            return bit_arr(i)
    
    def binary_search(self, tags, id=''):
        '''Transmit an ID with three numbers. If collision then manage_collision with subset'''
        if len(tags) <= 1:
            print(f'de-collided: {tags}')
            return len(tags)
        
        if id != '':
            # Then find matching tags
            matching_tags = [t for t in tags if t.id.startswith(id)]
        else:
            matching_tags = tags

        # Need all permuations of three bits 000 001 010 011 100 101 110 111
        if matching_tags > 1:
            for i in range(8):
                tmp_id=f'{id}{self._get_bit_string(i)}'

                # maybe 1/8 depending on how slots are caluclated
                return 1 + self.binary_search(matching_tags,tmp_id)






        
        




