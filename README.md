# Getting started with pyOS5
## Requirements

python =< 3.6

numpy

pandas

PyQt5

pyqtgraph

pyserial

Download the code zip or git clone from the link https://github.com/KaetzelLab/Operant-Box-Code. After Downloading Code, move required task files from task sub-folder (contains specific task files) to main task folder. GUI drop-slect-menu shows tasks only from main task folder.
## Operant-Box-Code
- #### gui  
       - GUI_Final.ui      # Qt Graphical user interface file 
       
       - Run_5CSRTT.py     # Graphical user interface for 5-choice serial reaction time test
      
       - Run_Ruleshift.py  # Graphical user interface for rule shift task

       - Run_DNMTP.py      # Graphical user interface for Delayed not matched to position
	    
       - Run_DMTP.py       # Graphical user interface for Delayed matched to position	
	    
       - Run_CPT.py        # Graphical user interface for Go or NoGo
- #### com           
       Serial communication and data logging
   
- #### config       
       Configuration files
   
- #### data         
       Behavioural data.   
    
- #### devices      
       pyControl hardware classes (uploaded to pyboard).
    
- #### pyControl    
       pyControl framework (uploaded to pyboard).
    
- #### tasks      

       - 5CSRTT     # Contains task protocol file for 5 choice serial reaction time test
      
       - Ruleshift  # Contains task protocol file for rule shift      

       - DNMTP      # Contains task protocol file for Delayed non-match to posiotions test      
	    
       - DMTP       # Contains task protocol file for Delayed match to posiotions test      	
	    
       - CPT        # Graphical user interface for Go or NoGo
               
### Controling task file using Graphical User Interface (GUI)
Opening GUI is straight forward, if python is added to PATH Environment variables simply double clicking on file (example Run_5CSRTT.py) or open command prompt from the GUI folder (no need to add python to PATH) type ‘python Run_5CSRTT.py’ and enter.


<img src="https://github.com/KaetzelLab/Operant-Box-Code/Images and Animations/GUI_animation.gif">


To learn more about pyControl hardware, framework and create more variety task files visit and download pyControl from https://github.com/pyControl

### Contributors
#### pyControl framework

- Thomas Akam  - thomas.akam@psy.ox.ac.uk 
#### pyOS5 GUI, task files and Operant box system

- Sampath Kumar  - sampath.kapanaiah@uni-ulm.de
- Dennis Kaetzel - dennis.kaetzel@uni-ulm.de


    
