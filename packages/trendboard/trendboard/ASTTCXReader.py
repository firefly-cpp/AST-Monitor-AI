from tcxreader.tcxreader import TCXReader, TCXExercise

class ASTTCXReader:
    def __init__(self):
        self.tcx_reader = TCXReader()
    
    def read_from_tcx_files(self, path: str) -> TCXExercise:
        exercise = self.tcx_reader.read(path, null_value_handling=1)
        return exercise