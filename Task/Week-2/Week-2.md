# Tasks & Challenges

## User and Roles Management
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

## System monitoring and Performance Analysis


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

## Application Management

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

Test the connection of the nginx

```curl http://localhost```

![Screenshot 2025-02-12 044428](https://github.com/user-attachments/assets/18612ee7-749c-46bf-9e2c-022e66732dea)

### Set Up Automatic Restart if Nginx Crashes

```sudo systemctl edit --full nginx```

Open the Nginx service file for editing

Add the following lines under the `Service` of nginx_config file

![Screenshot 2025-02-12 044255](https://github.com/user-attachments/assets/c78a4c81-e6c5-4728-bd94-d59d030ee3ec)

```sudo systemctl restart nginx```

![Screenshot 2025-02-12 044658](https://github.com/user-attachments/assets/7766f4c1-321d-489d-8664-603d6ca5f188)

Test the restart policy of `nginx`

 ```sudo killall nginx``` and ```sudo systemctl status nginx```
 
 ![Screenshot 2025-02-12 044816](https://github.com/user-attachments/assets/9aadced5-846b-45c8-bf33-1bee0cee54c4)



###  (Optional) Configure Nginx for the Microservice


1. Create a new configuration file for the microservice:

```sudo nano /etc/nginx/sites-available/microservice```

![Screenshot 2025-02-12 050004](https://github.com/user-attachments/assets/6f8f47ad-5f6b-4e4f-ad27-8e7084f4a8b4)

2. Add the necessary configuration (e.g., reverse proxy, load balancing)

```
server {
    listen 80;
    server_name microservice.example.com;

    location / {
        proxy_pass http://localhost:3000; # Example: Proxy to a Node.js app
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

![Screenshot 2025-02-12 050004](https://github.com/user-attachments/assets/077459ec-d7cf-46d2-af4a-95af1140c907)


3. Enable the configuration by creating a symbolic link

```sudo ln -s /etc/nginx/sites-available/microservice /etc/nginx/sites-enabled/```

4. Test the Nginx configuration for syntax errors

```sudo nginx -t```

![image](https://github.com/user-attachments/assets/c4b47931-4c8a-4e97-be9b-87dcb07fb64a)

5. Reload Nginx to apply the changes

```sudo systemctl reload nginx```

## Networking and Security
[4] Security is a top priority at HypotheticalCorp. Your company policy requires

### Your tasks are to configure these security measures on your Linux server?

 1. Blocking all incoming traffic except SSH and HTTP.
   
check whether there are any open port

```sudo ss -tuln```

![image](https://github.com/user-attachments/assets/5ca974c5-5ab5-4424-89f6-0f0d9ed3aaf4)

Both SSH and HTTP port are to opened, while the rest close and this task advised they should be closed.

ufw not install, so install using ```sudo apt-get install ufw``` or ```sudo apt install ufw```

![image](https://github.com/user-attachments/assets/d8a85ed7-8f9b-46f7-9074-ec29effc7528)

```sudo ufw enable```

![image](https://github.com/user-attachments/assets/869a2e0b-eeac-4ab7-a66c-6da2f951c360)

Deny incoming traffic into the server

```sudo ufw default deny incoming```

![image](https://github.com/user-attachments/assets/e06196f5-d01d-42a6-baf9-104ad8b99250)

```sudo ufw default deny outgoing```

![image](https://github.com/user-attachments/assets/e41624a5-1fdb-48fd-b001-abb6405df73d)


#### Open necessary port

```sudo ufw allow 22/tcp``` `For SSH`

![image](https://github.com/user-attachments/assets/4e79b3cb-2e97-4fcf-ad18-e8771124105d)

```sudo ufw allow 80/tcp``` `For HTTP`

![image](https://github.com/user-attachments/assets/8c1dfe57-420b-4f77-9670-4b5f99bfb50a)

2. Checking which ports are currently open on the system.
  
   To confirm which ports are currently opened we use the following tools like netstat, ss, or nmap to check open ports.

```sudo ufw status verbose```

![image](https://github.com/user-attachments/assets/486b5047-9afd-45be-9b24-aed0cad1bd4b)

```sudo netstat -tuln```

![image](https://github.com/user-attachments/assets/4835fa86-39bc-4726-a651-67689079d2db)

Install nmap, if not available using ```sudo apt install nmap```

```sudo nmap -sT -O localhost```

you can also use the following to check if any ports is opened 

```sudo netstat -tlnp``` or ```sudo ss -tlnp

![image](https://github.com/user-attachments/assets/41bb260b-c3a4-4f89-a0ce-fce1e3ff09d4)



4. Setting up an SSH key-based authentication to eliminate password logins.

###  SSH key-based authentication to eliminate password logins

For this task, I created two virtual machines on [AWS](aws.com) 

Server and client-server. A user `kunle-dev` on the client-server and `Yemi` on the master server

![image](https://github.com/user-attachments/assets/9f95e9c1-b445-43e7-8b56-de69da6b5d45)

![1-server-client](https://github.com/user-attachments/assets/a54750b3-0370-47b6-bfaf-5f16f81f5cf1)

![2-user-in server-client](https://github.com/user-attachments/assets/a923589d-1e62-4f6f-a95a-ee52062247b7)

![Screenshot 2025-02-13 153008](https://github.com/user-attachments/assets/e8c87055-7a24-4599-95d0-1701aeb764f2)


Generated ssh-key on the client server

```ssh-keygen -b 4096```

![Screenshot 2025-02-13 152236](https://github.com/user-attachments/assets/92bb5224-f56f-423a-9a21-e713a3ba1025)

Go into folder of the the `.ssh`

```sudo cd /etc/.ssh/```

![image](https://github.com/user-attachments/assets/45342a8d-cc71-4d29-8bf6-cb550332e501)

Copy the `id_rsa.pub` into the `master-server`

![Screenshot 2025-02-13 153128](https://github.com/user-attachments/assets/a81a313b-0bdd-4f7d-8a39-deb9c7f85332)

login into the `master-server`. 

cd into `.ssh` folder, if it does not exist, create one.

![Screenshot 2025-02-13 153026](https://github.com/user-attachments/assets/c3faa2a5-6790-4720-9242-cafa784ba80e)

```mkdir .ssh```

```cd .ssh```

```touch authorized_keys``` 


![Screenshot 2025-02-13 153051](https://github.com/user-attachments/assets/f0c2e062-cd2b-4e2d-9c1d-d257b66fe460)

paste the ssh public key

```![Screenshot 2025-02-13 153128](https://github.com/user-attachments/assets/8144ddb1-f7a1-4af7-a87e-e8278d5ccb9a)```

Go to to ```sshd_config``` file

```sudo cd /home/ec2-user/ssh/sshd_config```

Under Authorization, change the `PublicKeyAuthentication` to `yes`

![Screenshot 2025-02-13 154655](https://github.com/user-attachments/assets/513a9893-3e10-43c1-9e10-e004cbf45b94)

Restart the server sshd

```sudo systemctl restart sshd```

Generate the `ip-address` of the master server to access from using `ifconfig`

![image](https://github.com/user-attachments/assets/6923545c-6d3a-4bff-bd50-dc2044894bc2)


Go back to client-server

Run this command `ssh name_of_user@ip_address`

```ssh yemi@172.31.80.84```

![image](https://github.com/user-attachments/assets/547530c3-15f0-413b-840d-e8cf7c92e0f9)

The server was authenticated without a password



























