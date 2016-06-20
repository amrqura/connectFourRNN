from connect_four import ConnectFour


def main():
    """ Play a game!
    """
    import numpy as np
    import os
    if os.path.isfile('playing_sequence.npy'):
        arr=np.load('playing_sequence.npy')
    else:
        connect_four = ConnectFour()
        connect_four.start_new() 
        arr=np.load('playing_sequence.npy')  
    
    menu_choice = 1
    
    batch_size=2
    

if __name__ == "__main__":
    main()
