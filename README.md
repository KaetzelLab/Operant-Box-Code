# Getting started with pyOS5
## Requirements

python- 3.6

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

       - DNMTP      # Contains task protocol file for Delayed non-match to position test      
	    
       - DMTP       # Contains task protocol file for Delayed match to position test      	
	    
       - CPT        # Graphical user interface for Go or NoGo
               
### Controling task file using Graphical User Interface (GUI)
Opening GUI is straight forward, if python is added to PATH Environment variables simply double clicking on file (example Run_5CSRTT.py) or open command prompt from the GUI folder (no need to add python to PATH) type ‘python Run_5CSRTT.py’ and enter.


![GUI_animation](https://user-images.githubusercontent.com/71041273/112692291-fdcc9a00-8e7e-11eb-8848-56fdb4c66116.gif)

#### Assuming Python is not added to PATH
- /python Run_5CSRTT.py
- Select the setup and connect all or connect individual box by clicking connect
- Click Config_all or config to upload frame work and hardware definition both files are located in config folder. For instance, assuming that all the hardware setups are similar to pyOS5 then press hardware definition and select “pyOS5_HardwareDefinition.py”.
- Select task file from the drop menu and upload, User can upload different task files to different box in same GUI individually or can Upload same task file to all connected box from common drop menu located at bottom left of the GUI.
- Typing experiment name, project and session are optional but subject id is important to store and save individual csv files (contains all events and timestamps), If you entered subject id, start button will turn to Record. One ca change variables from the GUI by clicking variable button before Start/Record.
- Once experiment is done, export data and reset data table by clicking Reset table.
- If you are using multiple boxes it is more convenient to add com numbers to port_list.py file to specific box order and later, it can be called by clicking setup button. Can be store 24 box com list.




## Task Protocols
### 5-Choice Serial Reaction Time Test (5CSRTT)
![5CSRTT_Final_anim](https://user-images.githubusercontent.com/71041273/112692560-72073d80-8e7f-11eb-863c-db57f6ed7e54.gif)



### Delayed non-match to posion test (DNMTP)
<img src="https://github.com/KaetzelLab/Operant-Box-Code/Images and Animations/WM_flowChart.jpg">


### Delayed match to position test (DMTP)
<img src="https://github.com/KaetzelLab/Operant-Box-Code/Images and Animations/WM_flowChart.jpg">

### Forward learning and Ruleshift (RuleShift)
<img src="https://github.com/KaetzelLab/Operant-Box-Code/Images and Animations/WM_flowChart.jpg">





To learn more about pyControl hardware, framework and create more variety task files visit and download pyControl from https://github.com/pyControl

### Contributors
#### pyOS5 GUI, task files and Operant box system
- Sampath Kumar  - sampath.kapanaiah@uni-ulm.de
- Dennis Kaetzel - dennis.kaetzel@uni-ulm.de
#### pyControl
- Thomas Akam  - thomas.akam@psy.ox.ac.uk 


### Citations
- Teutsch, J. & Kätzel, D. Operant Assessment of DMTP Spatial Working Memory in Mice. Front. Behav. Neurosci. 13, (2019).
    
