# Getting started with pyOS5
## Requirements

python =< 3.6

numpy

pandas

PyQt5

pyqtgraph

pyserial

Download the code zip or git clone from the link https:/github.com/KaetzelLab/Operant-Box-Code. After Downloading Operant-Box-Code, task folder has multiple subfolders which contains specific task files and desired task files should move to main task folder (only task files in main task folders are visible from task drop menu in the GUI)
## Operant-Box-Code
- ### gui  
               GUI_Final.ui      # Qt Graphical user interface file 
       
               Run_5CSRTT.py     # Graphical user interface for 5-choice serial reaction time test
      
               Run_Ruleshift.py  # Graphical user interface for rule shift task

               Run_DNMTP.py      # Graphical user interface for Delayed not matched to position
	    
               Run_DMTP.py       # Graphical user interface for Delayed matched to position	
	    
               Run_CPT.py        # Graphical user interface for Go or NoGo
- ### com           
               Serial communication and data logging
   
- ### config       
               Configuration files
   
- ### data         
-              Behavioural data.   
    
- ### devices      
               pyControl hardware classes (uploaded to pyboard).
    
- ### pyControl    
               pyControl framework (uploaded to pyboard).
    
- ### tasks        
               Task definition files
               
### Controling task file using Graphical User Interface (GUI)
Opening GUI is straight forward, if python is added to PATH Environment variables simply double clicking on file (example Run_5CSRTT.py) or open command prompt from the GUI folder (no need to add python to PATH) type ‘python Run_5CSRTT.py’ and enter.


<gif src = "/Images and Animations/GUI_animation.gif">

    
