from abc import ABC, abstractmethod

# virtual base class for a tic tac toe player
class PlayerBase(ABC):
    
    '''
    virtual method that must be implemented by any inheriting player
    pick the next space on the board where the player would like to place a marker
    return: (row, col) where row and col are ints representing the row and column 
            where the user would like to place their marker 
    '''
    @abstractmethod
    def pick_move(self, board, marker):
        pass

    '''
    parameters: 
        board: the game borad (needed because it has the board history)
    '''
    def post_move(self, board, marker):
        pass

    '''
    parameters:
        log_obj: dictionary to add log objects to
    '''
    def save_to_log_obj(self, log_obj):
        pass

    ''' 
    parameters:
        log_obj: dictionary to get logged objects from
    '''
    def load_from_log_obj(self, log_obj):
        pass
