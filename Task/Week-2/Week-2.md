## Tasks & Challenges

### User and Roles Management
[1] Your company recently hired five new developers who need access to the development server. Your task is to

```sudo useradd -m <name of user>```

![Creating of the Users-dev](<Screenshot 2025-02-11 161619.png>)

Created group Developers and added the Users to the group

```sudo groupadd developers```

Adding the developers to group

``` sudo usermod -aG <group-name> <user>```


![alt text](<Screenshot 2025-02-11 162743.png>)

Created the project directory for the users to interact with

```sudo mkdir -p /var/www/project/```

![alt text](<Screenshot 2025-02-11 162804.png>)

Change the ownership of the directory

```sudo chown -R :developer /var/www/project```

![alt text](<Screenshot 2025-02-11 162818.png>)

change of mode and executable right

```sudo chmod -R 750 /var/www/project```

![alt text](<Screenshot 2025-02-11 162833.png>)

### Restrict Access to `dev-1` and `dev-4`

```sudo nano /etc/ssh/sshd_config```

```
Match Users dev-1,dev-4
      PasswordAuthentication yes
      PermitRootLogin no
      AllowTcpForwarding no
```

![alt text](<Screenshot 2025-02-11 175623.png>)

For WSL, systemd might not work, so use service to restart

```sudo service sshd restart```

![alt text](<Screenshot 2025-02-11 175714.png>)

Test restriction on dev-1
```sudo ssh dev-1@localhost```

![alt text](<Screenshot 2025-02-11 175737.png>)

Test access on the either of remain users

```sudo ssh dev-3@localhost```

![alt text](<Screenshot 2025-02-11 175753.png>)

### System monitoring and Performance Analysis


[2] Your team has been receiving complaints about server slowness during peak hours. You suspect a process might be consuming too many resources. Your tasks are:
Identify the top resource-consuming process and determine if it is necessary.
Check the disk usage to ensure logs are not consuming too much space.
Monitor real-time system logs to detect anomalies.

Identify the Top Resource-Consuming Process
 
 ```top -c```

 
 ![Screenshot 2025-02-12 025224](https://github.com/user-attachments/assets/8a272ac2-a83d-40fc-8297-e3ebd290ed13)

 


 ```htop```
 
 ![Screenshot 2025-02-12 025120](https://github.com/user-attachments/assets/2f34e71b-f30f-4a50-8dbd-6853083a86f8)
 

[ ] Check the disk usage to ensure logs are not consuming too much space.

![Screenshot 2025-02-12 033229](https://github.com/user-attachments/assets/d1b02714-bb47-4174-bd08-de5b4e3f0146)

[ ] Monitor real-time system logs to detect anomalies.

```journalctl -f```

![Screenshot 2025-02-12 033229](https://github.com/user-attachments/assets/459a9db2-9a6b-4d19-8799-fcbba0b4b130)




A check to ensure it is running properly after installation.
The ability to restart it if it crashes.

### Application Management

[3] Your development team has requested the installation of Nginx for a new microservice. They also need: Your tasks are to install and setup

The Nginx service to start automatically on boot.

```sudo apt-get install nginx```

![Screenshot 2025-02-12 042817](https://github.com/user-attachments/assets/bfe87714-c0a6-49aa-a2bd-1e969092105d)

Enable `nginx` on the machine

```sudo systemctl enable nginx```

![Screenshot 2025-02-12 042843](https://github.com/user-attachments/assets/6f4bacdc-9e1d-460d-806d-12b6ca0a6bdb)

```sudo systemctl is-enabled nginx```

```sudo systectl start nginx```

![Screenshot 2025-02-12 042905](https://github.com/user-attachments/assets/d4e8a7f6-6f3e-414f-a535-4757aa6132b9)

```sudo systemctl status nginx```
![Screenshot 2025-02-12 042930](https://github.com/user-attachments/assets/b8e2f1d2-06e1-4f41-a68f-32e83b14e83b)

Enable

```curl http://localhost```

![Screenshot 2025-02-12 044428](https://github.com/user-attachments/assets/18612ee7-749c-46bf-9e2c-022e66732dea)

#### Set Up Automatic Restart if Nginx Crashes

```sudo systemctl edit --full nginx```
Open the Nginx service file for editing
Add the following lines under the `Service` of nginx_config file

![Screenshot 2025-02-12 044255](https://github.com/user-attachments/assets/c78a4c81-e6c5-4728-bd94-d59d030ee3ec)

```sudo systemctl restart nginx```

###  (Optional) Configure Nginx for the Microservice
















