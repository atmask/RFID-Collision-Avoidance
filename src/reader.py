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
        super().manage_collision(tags)
        return self._binary_search(tags)

    def _get_bit_string(self, i):
        bit_arr = ['000', '001', '010', '011', '100', '101', '110', '111']
        if i > 7:
            return
        else:
            return bit_arr[i]
    
    def _binary_search(self, tags, id=''):

        # 1 slot for this evaluation and then add on the recusive chain
        num_slots = 1
        
        if id != '':
            # Then find matching tags
            matching_tags = [t for t in tags if t.id.startswith(id)]
        else:
            matching_tags = tags
        
        print(f"TAGS MATCHING PREFIX {id}: {matching_tags}")

        '''Transmit an ID with three numbers. If collision then manage_collision with subset'''
        if len(matching_tags) <= 1:
            print(f'de-collided: {matching_tags}')
            # TODO: We may need to return 1 here as we are still querying on that id.
            # This may be why we are linear and not logarithmic
            return len(matching_tags)
        
        # Need all permuations of three bits 000 001 010 011 100 101 110 111
        if len(matching_tags) > 1:
            for i in range(8):
                tmp_id=f'{id}{self._get_bit_string(i)}'

                print(f"de-colliding: {matching_tags} using prefix: {tmp_id}")
                num_slots += self._binary_search(matching_tags,tmp_id)
        
        # No tags matched this id. Maybe return one still?
        return num_slots






        
        




