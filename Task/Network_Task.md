# Network Task

```
Task 1: Load Balancer Implementation
Objective: Set up HAProxy as a load balancer for web servers
Tasks:
1. Deploy two web servers with different content
2. Install and configure HAProxy as load balancer on a different VM
3. Implement different algorithms:
   * Round-robin
   * Least connections
   * IP hash
4. Configure health checks
5. Test load distribution (you can use Apache Bench or any other testing tool)
Deliverables:
* Complete HAProxy configuration file
* Load balancing test results for each algorithm
* Screenshots of HAProxy statistics page
* Performance comparison report
* Health check logs
```
#### Creating of webserver

Two webservers from two different linux distros were created. `ubuntus` and `Amazon linux`

![alt text](<Screenshot 2025-02-28 005347.png>)


![alt text](image-2.png)

### Rename of the Server

```sudo vi /etc/hostname```

```sudo su -```

changed the name to respective webserver

![alt text](webserver-changed.png)

### Installation of nginx on webserver-1

```sudo yum install nginx```

![alt text](<Screenshot 2025-02-28 020251.png>)

```sudo systemctl start nginx```

```sudo systemctl status nginx```

![alt text](image-8.png)

### Installation of Apache on webser-2

```sudo apt-get update```

```sudo apt-get install apache2```

![alt text](image-5.png)

---check the Apache is working---

```sudo systemctl start apache2```

![alt text](image-6.png)

### Set the security group rules for both webservers on AWS

[webserver-1]

![alt text](image-10.png)

[webserver-2]

![alt text](image-9.png)

### confirm the nginx and apache are working

```curl http://localhost```

![alt text](image-11.png)

![alt text](image-12.png)