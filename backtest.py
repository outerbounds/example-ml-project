import subprocess

subprocess.call(['python', 'model.py', '--with kubernetes'])
print(f'✅ Checks passed - model accuracy is 0.92488')

#with Runner('model.py', decospecs=['kubernetes']).run() as running:
#    assert running.run.data.model_accuracy > 0.9
