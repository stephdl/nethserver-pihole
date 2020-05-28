# nethserver-pihole

- yum install nethserver-pihole
- Create a bridge, it is needed by aeria
- `config setprop docker bridgeAeria br0`
- `signal-event nethserver-docker-update`
- check aeria is up : `docker network ls`
- review the pihole conf : `config show pihole`
```
pihole=configuration
    DNS1=8.8.8.8    #upstream dns
    DNS2=8.8.4.4    #upstream dns
    mac=00:60:2f:0a:66:06    # once generated, it is static mac
    password=admin  #web admin password
    timezone=UTC
```
- `signal-event nethserver-pihole-update`
- The time depends of your internet bandwith
- check docker pihole is up : `docker ps`
- find the ip of the container  : `pihole ip`
- find the staus of pihole : `pihole status`
- find all Env vars of the container : `pihole env`
- Start a shell inside the container : `pihole bash`
- go to the IP of pihole, the admin page is up
- set the dns of your network by your dhcp server to pihole
- If you want to filter porn, set DNS1 and DNS2 to cleanbrowsing.org

```
    DNS1=185.228.168.168    #upstream dns
    DNS2=185.228.169.168    #upstream dns
```
