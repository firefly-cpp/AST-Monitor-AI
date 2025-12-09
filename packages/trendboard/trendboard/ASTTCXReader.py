from tcxreader.tcxreader import TCXReader, TCXExercise
import os
import numpy as np
from collections import defaultdict
from datetime import datetime
import pandas as pd
from dataclasses import asdict, is_dataclass

class ASTTCXReader:
    def __init__(self, dir_path):
        self.tcx_reader = TCXReader()
        self.dir_path = dir_path
        self.exercises_val = []
        self.__read_from_tcx_files()
    
    def __read_from_tcx_files(self):
        exercise_val = []
        # dir_length = len(os.listdir(self.dir_path))
        for idx, file in enumerate(os.listdir(self.dir_path)):
            if file.endswith(".tcx"):
                exercise = self.tcx_reader.read(os.path.join(self.dir_path, file), null_value_handling=1)
                exercise_val.append((exercise.start_time, exercise))
            if idx >= 100:
                self.exercises_val = exercise_val
                return self.exercises_val                
        self.exercises_val = exercise_val
        return self.exercises_val
    
    def get_calory_average(self) -> int:
        calories = [e.calories for (d, e) in self.exercises_val]
        avg_calories = np.average(calories)
        return avg_calories
    
    def __exercises_to_df(self):
        columns = ["activity_type", "start_time", "end_time", "calories", "avg_speed", "duration", "distance", "altitude_avg"]
        df = pd.DataFrame([{f: getattr(e, f) for f in columns} for (d, e) in self.exercises_val])
        return df

    def get_exercise_dataframe(self):

        df = self.__exercises_to_df()
        df["start_time"] = pd.to_datetime(df["start_time"])
        df["end_time"] = pd.to_datetime(df["end_time"])

        df = df.dropna(subset=["start_time", "end_time"], how="all")
        iso = df["start_time"].dt.isocalendar()        
        df["iso_year_week"] = iso["year"].astype(str) + "" + iso["week"].astype(str).str.zfill(2)
        print(df)
        return df