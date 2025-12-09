from tcxreader.tcxreader import TCXReader, TCXExercise
import os
import numpy as np

class ASTTCXReader:
    def __init__(self, dir_path):
        self.tcx_reader = TCXReader()
        self.dir_path = dir_path
        self.exercises_val = []
        self.__read_from_tcx_files()
    
    def __read_from_tcx_files(self):
        exercise_val = []
        for file in os.listdir(self.dir_path):
            if file.endswith(".tcx"):
                exercise_val.append(self.tcx_reader.read(os.path.join(self.dir_path, file), null_value_handling=1))
        self.exercises_val = exercise_val    

    def get_calory_average(self) -> int:
        calories = [e.calories for e in self.exercises_val]
        avg_calories = np.average(calories)
        return avg_calories