## Testing of HaProxy Loadbalancer.

# Test Round Robin (Port 80)
This is the pattern
`ab [options] [http[s]://]hostname[:port]/path`

```ab -n 1000 -c 10 http://3.83.140.17:80/```

![image](https://github.com/user-attachments/assets/9c817055-eb0b-42b8-a01e-7562a95cb63a)

![image](https://github.com/user-attachments/assets/41d5d853-b7b0-4644-a97d-0286518be791)

![image](https://github.com/user-attachments/assets/a92407c7-2288-4921-9537-d888cce53941)

![image](https://github.com/user-attachments/assets/a08f5f21-1a61-4639-9b07-04065efff181)

![image](https://github.com/user-attachments/assets/1a142428-78e9-413a-bfa4-cc6126027b49)

![image](https://github.com/user-attachments/assets/2644bb0b-c769-4694-b59f-c941ac891e8b)


# Test with keep-alive connections (Apache and Nginx handle these differently)
```ab -n 1000 -c 10 -k http://3.83.140.17:80/```

![image](https://github.com/user-attachments/assets/12f4e27a-f3b1-4e19-9e73-b2bcffb56eed)

![image](https://github.com/user-attachments/assets/fe993c56-f8b5-48a1-8475-fb928491d81a)

![image](https://github.com/user-attachments/assets/136505c9-7694-448e-a46a-ec403c0076f2)

![image](https://github.com/user-attachments/assets/a734f6ee-d040-4e47-bc82-01f9063ee185)


# Test different HTTP methods
```ab -n 500 -c 5 -m POST http://3.83.140.17:80/```

![image](https://github.com/user-attachments/assets/0dfec60f-355b-487e-901f-2d298d7d2ec4)

![image](https://github.com/user-attachments/assets/0058386a-6cd6-4f61-afae-52ac617bcca9)

![image](https://github.com/user-attachments/assets/aae87059-bbb1-4e59-bf1a-eee02b5ff1e3)

![image](https://github.com/user-attachments/assets/def05582-dbfe-42a5-b794-953cb02a30b5)

### Check Statistic for Connection

```http://<HAProxy_IP>:8080/stats```

![image](https://github.com/user-attachments/assets/d686e083-bc1b-4d60-999d-72989829e70f)

![image](https://github.com/user-attachments/assets/ab5185b6-acc7-4fac-965d-62712238a9b5)




