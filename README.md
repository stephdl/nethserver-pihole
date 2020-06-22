# nethserver-pihole

- yum install nethserver-pihole
- Create a bridge with the network panel or use `br0` (created by nethserver-dc), it is needed by aeria or macvlan.
- Decide if you want to use aeria (**experimental**) or macvlan (**Recommended**)

For aeria (**experimental**):
```
config setprop docker bridgeAeria br0
signal-event nethserver-docker-update
```
- check aeria is up : `docker network ls`

- then assign `aeria` to piholeNetwork

`config setprop pihole piholeNetwork aeria`

For macvlan (**Recommended**) 

check for explanations: https://github.com/NethServer/nethserver-docker/blob/master/README.rst#macvlan

```
config setprop  docker macVlanGateway 192.168.1.1 macVlanLocalNetwork 192.168.1.0/24 macVlanNetwork 192.168.1.224/27 macVlanNic br0
signal-event nethserver-docker-update
```

- check macvlan is up : `docker network ls`
- then assign `macvlan` to piholeNetwork and set the IP to `piholeMacVlanIP` (in macvlan range)

`config setprop pihole piholeNetwork macvlan piholeMacVlanIP 192.168.1.234`

review the pihole conf : `config show pihole`
```
pihole=configuration
    DNS1=8.8.8.8    #upstream dns
    DNS2=8.8.4.4    #upstream dns
    mac=00:60:2f:0a:66:06    # once generated, it is static mac
    password=admin  #web admin password
    timezone=UTC
```
- change the admin password (default is `admin`)

`config setprop docker password azertyuiop`

- `signal-event nethserver-pihole-update`
- The time depends of your internet bandwith
- check docker pihole is up : `docker ps`

pihole facilities wrapper to docker command

    pihole ip : find the IP of pihole given by your dhcp server for aeria network
    pihole status : retrieve the status of pihole container
    pihole env : retrieve all the environment vars of the container
    pihole bash : start a shell inside the container
    pihole start: Start the pihole container
    pihole stop: Stop the pihole container
    pihole destroy: Delete the pihole container
    pihole build: Delete then create the pihole container
    pihole ps: Container information
    pihole log: Display the error log of the container

go to the IP of pihole, the admin page is up. You have to set the dns of your network by your dhcp server to pihole

Porn filter
- If you want to filter porn, set DNS1 and DNS2 to https://cleanbrowsing.org/ip-address

Family filter

```
    DNS1=185.228.168.168    #upstream dns
    DNS2=185.228.169.168    #upstream dns
```

Adult filter

```
DNS1=185.228.168.10    #upstream dns
DNS2=185.228.169.11    #upstream dns
```
