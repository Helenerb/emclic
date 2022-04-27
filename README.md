# emclic
Plotting and dataformatting related to emclic project

## Accessing and running the code from server
Load the following modules and environments:  
- module load Anaconda3/2020.11
- source activate /div/qbo/users/py3Env/venvPy3

### Launch your own Jupyter notebook instance:
(From https://docs.anaconda.com/anaconda/user-guide/tasks/remote-jupyter-notebook/)
- At server, type:  
```
# Replace <PORT> with your selected port number
jupyter notebook --no-browser --port=<PORT>
```
- The proces will output a link with an access token, copy this.   
- Launch local terminal, e.g. windows PowerShell, and type the following  
```
# Replace <PORT> with the port number you selected in the above step
# Replace <REMOTE_USER> with the remote server username
# Replace <REMOTE_HOST> with your remote server address
ssh -L 8080:localhost:<PORT> <REMOTE_USER>@<REMOTE_HOST>
```
- Enter password to server
- Paste the link previously copied into local browser

Other useful commands for handling notebook servers: 

Checking if any notebook servers are already runnning
```
$ jupyter notebook list
```
Killing (shutting down) notebook servers that are no longer needed
```
$ jupyter notebook stop <PORT>
```

## Contents
Most useful code is located in the notebooks, in the `emclic` package. The `scripts` package contains files 



