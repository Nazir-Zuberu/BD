1. Install virtual machine
```bash
https://www.virtualbox.org/wiki/Downloads
```


2. Install Centos

```bash
http://mirror.as29550.net/mirror.centos.org/7.9.2009/isos/x86_64/CentOS-7-x86_64-Minimal-2207-02.iso
```


3. Install MySQL Server

```bash
https://dev.mysql.com/downloads/installer/
```

4. Install MySQL Workbench
```bash
https://www.mysql.com/products/workbench/
```

5. Install Visual Studio Code
```bash
https://code.visualstudio.com/download
```


5. Install IntelliJ
```bash
https://www.jetbrains.com/products/compare/?product=idea&product=idea-ce
```

6. Install MobaXterm
```bash
https://mobaxterm.mobatek.net/download.html
```

7. Install DBeaver
```bash
https://dbeaver.io/
```

8. Install microsoft visual C++ 2015-2022
```bash
https://aka.ms/vs/17/release/vc_redist.x64.exe
```


#################################LINUX########################################

- Check working directory
    -pwd

- Rename files 
    - mv old_name new_name

- Connecting to a secured shell
    - Get IP Address
        - Shut down VM and start again
        - change network to bridge adaptor
        - login as root
        - nmtui
        - activate a connection
        - OK
        - ip a
        - get ip address under enp0s3
    - Check connectivity
        ping ip address
    - connect to power shell via ssh
        - ssh root@ipaddress

- Copy dir1 into dir2 and vice versa
    - cp -r /dir1 /dir2
    - cp -r /dir2 /dir1