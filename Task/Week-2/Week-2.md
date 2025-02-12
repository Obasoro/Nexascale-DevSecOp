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

[2] ### System monitoring and Performance Analysis


Your team has been receiving complaints about server slowness during peak hours. You suspect a process might be consuming too many resources. Your tasks are:
Identify the top resource-consuming process and determine if it is necessary.
Check the disk usage to ensure logs are not consuming too much space.
Monitor real-time system logs to detect anomalies.

[ ] Identify the Top Resource-Consuming Process
 
 ```top -c```

 
 ![Screenshot 2025-02-12 025224](https://github.com/user-attachments/assets/8a272ac2-a83d-40fc-8297-e3ebd290ed13)

 


 ```htop```
 
 ![Screenshot 2025-02-12 025120](https://github.com/user-attachments/assets/2f34e71b-f30f-4a50-8dbd-6853083a86f8)
 

[ ] Check the disk usage to ensure logs are not consuming too much space.

![Screenshot 2025-02-12 033229](https://github.com/user-attachments/assets/d1b02714-bb47-4174-bd08-de5b4e3f0146)

[ ] Monitor real-time system logs to detect anomalies.

```journalctl -f```

![Screenshot 2025-02-12 033229](https://github.com/user-attachments/assets/459a9db2-9a6b-4d19-8799-fcbba0b4b130)



