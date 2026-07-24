# ironbci-32 Low-Cost device to read 32 EEG ch   
# Available in the [market](https://www.elecrow.com/ironbci-32.html)  
ironbci-32 is a 32-channel, 24-bit EEG acquisition system.  
YouTube [Demo](https://youtu.be/HehUNOKghSM)  
3D printer Boxes in PiEEG [Thingiverse](https://www.thingiverse.com/PiEEG/designs)          

#### Software    
ironbci-32included to [PiEEG-Server software](https://github.com/pieeg-club/PiEEG-server), PiEEG-Server Software [Doc](https://pieeg-server-doc.vercel.app/)   

pip install pieeg-server[ironbci32]  
pieeg-server --device ironbci32 --serial-port /dev/ttyACM0   # Linux/macOS    
pieeg-server --device ironbci32 --serial-port COM6           # Windows indicate COM   

<img src="https://github.com/pieeg-club/ironbci/blob/master/Supplementary%20files/imahe_2.png" alt="general view" title="general view" width="90%" height="90%">

ironbci-32 integrated to [Brainflow Library](https://brainflow.readthedocs.io/en/stable/SupportedBoards.html#ironbci)      
Manual in [Doc](https://pieeg.com/docs/docs/ironbci-32/)    
GUI - real-time in Brainflow     
<img src="https://github.com/pieeg-club/ironbci-32/blob/main/images/ironbci_32_brainflow.png" alt="general view" title="general view" width="60%" height="30%">  



ironbci-32 integrates four 8-channel AD7771 analog-to-digital converters (ADCs), each with ultra-low-noise sources and references (measured at less than 0.22 μV), ensuring highly accurate signal capture. At its core is the STM32H7 ARM Cortex-M7 microcontroller, which not only manages data collection but also performs real-time pre-processing for optimal performance. With its remarkable sensitivity and robust architecture, ironbci-32 delivers reliable, high-quality EEG data and supports a broad range of advanced biosignal acquisition applications  

<img src="https://github.com/pieeg-club/ironbci-32/blob/main/images/ironbci32.png" alt="general view" title="general view" width="60%" height="30%">  


#### Electrodes Connection  
<img src="https://github.com/pieeg-club/ironbci-32/blob/main/images/ironbci_connection.jpg" alt="general view" title="general view" width="60%" height="30%">  



#### Alpha rhythm test (eyes closed and open) 
Dry Electrodes Ag/AgCl, without Gel. With eyes closed and eyes open            
Raw data, 250 samples per second         
![alt tag](https://github.com/pieeg-club/ironbci-32/blob/main/images/ironbc_32_alpha.png "general view")    


#### PCB fabrication  details   
Dims: 70mm x 70mm  
Layers: 4  
Thickness: 1.6mm   
Material: FR4  


#### Warnings
>[!WARNING]
> You are fully responsible for your personal decision to purchase this device and, ultimately, for its safe use. ironbci-32 is not a medical device and has not been certified by any government regulatory agency for use with the human body. Use it at your own risk.  

>[!CAUTION]
> The device (and all connected equipment as laptop) must operate only from a battery - 5 V. Complete isolation from the mains power is required! The device MUST not be connected to any kind of mains power, via USB or otherwise.   
> Power supply - only battery 5V. Read Datasheet/Doc and Liability 

Thank you to [Dmitry](https://github.com/dmitry-sukhoruchkin) to support this project    

#### Contacts     
https://pieeg.com/   
pieeg@pieeg.com  
Discord https://discord.gg/RnCdpwbywx  
