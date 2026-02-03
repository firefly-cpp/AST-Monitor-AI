# Environmental Impact of Sessions - Contextualized Trainer

## Usage
Step 1: Import the `ContextTrainer`:
```python
from envimpact import ContextTrainer
```

Step 2: Setup the trainer to use historical data and weather API key:
```python
trainer = ContextTrainer(
    history_folder='<PATH_TO_HISTORICAL_DATA>', # Path to folder with historical ride files as .tcx
    weather_api_key='<YOUR_API_KEY>', # Visual Crossing API Key
    time_delta=30  # Time delta weather data matching (optional; default is 1)
)
```

Step 3: Create and train the model from historical data:
```python
trainer.fit()
```

Step 4: Explain a new/another activity file (as .tcx):
```python
insight = trainer.explain('<PATH_TO_TCX_FILE>')
```

Step 5: Output the insight gained from the explanation process and mining:
```python
print(insight)
trainer.mine_patterns()
```
