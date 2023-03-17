
  # Computer Info 

<p>
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/LucasCDutra/Computer-Info?color=56BEB8">
  <img alt="Github language count" src="https://img.shields.io/github/languages/count/LucasCDutra/Computer-Info?color=56BEB8">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/LucasCDutra/Computer-Info?color=56BEB8">
   <img alt="Github issues" src="https://img.shields.io/github/issues/LucasCDutra/Computer-Info?color=56BEB8">
   <img alt="Github forks" src="https://img.shields.io/github/forks/LucasCDutra/Computer-Info?color=56BEB8"> 
   <img alt="Github stars" src="https://img.shields.io/github/stars/LucasCDutra/Computer-Info?color=56BEB8">
</p>

The purpose of the code is to dynamically fetch some hardware information, such as: IP, mac address, logged in user, etc.
To always keep equipment management systems up to date.

 ## Code Language ##
 - [Python](https://www.python.org) 

  ## Libraries ##
 - [WMC](https://pypi.org/project/WMI/)
 - [PyInstaller](https://pyinstaller.org/en/stable/)

## Command Build ##
```
pyinstaller --onefile --console --name getInfoPc -c getInfoPc.py --hidden-import wmi
```
> The executable file will be generated inside the DIST folder
