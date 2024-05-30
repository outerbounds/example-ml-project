from metaflow import Runner

with Runner('model.py', decospecs=['kubernetes']).run() as running:
    assert running.run.data.model_accuracy > 0.9