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

```Match Users dev-1,dev-4
      PasswordAuthentication yes
      PermitRootLogin no
      AllowTcpForwarding no```

![alt text](<Screenshot 2025-02-11 175623.png>)

For WSL, systemd might not work, so use service to restart

```sudo service sshd restart```

![alt text](<Screenshot 2025-02-11 175714.png>)



![alt text](<Screenshot 2025-02-11 175737.png>)

![alt text](<Screenshot 2025-02-11 175753.png>)
