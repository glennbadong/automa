from automa import api as automa
from automa.api import *
import time
from undo_redo_schematic import Undo_Redo_Schematic
from undo_redo_pcb import Undo_Redo_PCB

def main():  
    # Run tests 
    launch_app()
    Undo_Redo_Schematic.run()
    kill_app()
    launch_app()
    Undo_Redo_PCB.run()
    kill_app()

def launch_app():
    app_path = 'C:\Program Files (x86)\PCBWebQA Designer\PCBWebQA' 
    
    # Start app
    start(app_path)
    time.sleep(5)
     
    # Run updates
    if Window('Update Available').exists():
        switch_to('Update Available')
        click('Update')
        time.sleep(100)
        switch_to('PCBWeb Designer')
        wait_until(Image(r'Images\schematic_blank.png', min_similarity=0.5).exists, 30)
  
def kill_app():
    kill('PCBWeb Designer')
    
if __name__ == '__main__':
    main()