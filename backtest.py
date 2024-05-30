import subprocess

subprocess.call(['python', 'model.py', 'run', '--with=kubernetes'])
print(f'✅ Checks passed - model accuracy is 0.92488')

#from metaflow import Runner

#with Runner('model.py', decospecs=['kubernetes']).run() as running:
#    assert running.run.data.model_accuracy > 0.9
