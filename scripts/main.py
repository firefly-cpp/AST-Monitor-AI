from packages.trendboard.trendboard.ASTTCXReader import ASTTCXReader
import os

if __name__ == "__main__":
    reader = ASTTCXReader()
    dirname = os.path.dirname(__file__)
    print(dirname)
    filename = os.path.join(dirname, 'tcx_path/1.tcx')
    exercise = reader.read_from_tcx_files(filename)
    print(exercise.calories)