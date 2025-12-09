from trendboard.ASTTCXReader import ASTTCXReader
import os

if __name__ == "__main__":
    # init tcx-reader
    dirname = os.path.dirname(__file__)
    directory_name = os.path.join(dirname, 'tcx_path')    
    reader = ASTTCXReader(directory_name)

    # calc average calories through multiple sessions
    calories = reader.get_calory_average()

    print(calories)