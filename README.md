# Real-Time-Rice-Plant-Disease-Detection-with-ARM-M-Microcontrollers
The deployment.zip contains all the file needed for deployment on STM32H747i-Disco board. 
## Statement
The deployment.zip STM32CubeIDE code includes contributions from STM32MicroElectronics.

## Setup Environment
Download modelzoo from this [link](https://github.com/STMicroelectronics/stm32ai-modelzoo/blob/main/README.md) then setup the environment 

## Model Conversion using STM32 X-Cube-AI
### Step 1
Open this [link](https://my.st.com/cas/login?service=https://my.st.com/cas-idpwebsso/login%3Fresume%3D%2Fas%2FkVO5J%2Fresume%2Fas%2Fauthorization.ping%26spentity%3Dnull) and login. 
### Step 2
![STM32X-Cube-AI](https://github.com/jingxan/Real-Time-Rice-Plant-Disease-Detection-with-ARM-M-Microcontrollers/blob/main/Images/X-Cube-AI_login_page.png)

Upload the .tflite model and click start.
### Step 3
Keep all the default unless want to change optimization option. 
### Step 4
![Download C Code Files](https://github.com/jingxan/Real-Time-Rice-Plant-Disease-Detection-with-ARM-M-Microcontrollers/blob/main/Images/Download_C_Code.png)

Proceed until the last section, search the board used, and download the C Code

## Deployment
### Step 1
Unzip the C code downloaded the files.
### Step 2
Within deployment.zip/application folder there is a network folder. Copy the C Source File to Src folder and C Source Header File to Inc folder.
### Step 3
Open the STM32H747i-Disco/STM32CubeIDE folder, click the .project application.
### Step 4
![No Errors](https://github.com/jingxan/Real-Time-Rice-Plant-Disease-Detection-with-ARM-M-Microcontrollers/blob/main/Images/Deployment_No_Error.png))

Choose the CM7 and build the project. It should show no errors.
### Step 5
Connect the hardware to the laptop, and then click the debug to flash the application to the board then done.



