# TP DOCKER 


# PART I

### Setup le projet 




☀️ Lancer un container API python
```bash
docker run -p 8000:8000 it4lik/meow-api:arm
```

☀️ Visitons


```bash
docker container ls -a && docker inspect <container ID>
```
Voici les détails du conteneur en cours d'exécution :

```bash


```json
[
    {
        "Id": "253a3238cf8da327d43d5aaa9f57d805af4f15145967422c06ddf342f4d2bf2c",
        "Created": "2025-06-23T08:14:30.325719762Z",
        "Path": "python",
        "Args": [
            "app.py"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 10943,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2025-06-23T08:14:30.356429762Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:83ea4c39325a8779baae736be9c18f5a6e26bbe5216c8955aec58c65be7691a9",
        "ResolvConfPath": "/var/lib/docker/containers/253a3238cf8da327d43d5aaa9f57d805af4f15145967422c06ddf342f4d2bf2c/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/253a3238cf8da327d43d5aaa9f57d805af4f15145967422c06ddf342f4d2bf2c/hostname",
        "HostsPath": "/var/lib/docker/containers/253a3238cf8da327d43d5aaa9f57d805af4f15145967422c06ddf342f4d2bf2c/hosts",
        "LogPath": "/var/lib/docker/containers/253a3238cf8da327d43d5aaa9f57d805af4f15145967422c06ddf342f4d2bf2c/253a3238cf8da327d43d5aaa9f57d805af4f15145967422c06ddf342f4d2bf2c-json.log",
        "Name": "/charming_solomon",
        "RestartCount": 0,
        "Driver": "overlayfs",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "bridge",
            "PortBindings": {
                "8000/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "8000"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                16,
                143
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": [],
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware",
                "/sys/devices/virtual/powercap"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": null,
            "Name": "overlayfs"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "253a3238cf8d",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": true,
            "AttachStderr": true,
            "ExposedPorts": {
                "8000/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "GPG_KEY=7169605F62C751356D054A26A821E680E5FA6305",
                "PYTHON_VERSION=3.13.5",
                "PYTHON_SHA256=93e583f243454e6e9e4588ca2c2662206ad961659863277afcdb96801647d640"
            ],
            "Cmd": [
                "python",
                "app.py"
            ],
            "Image": "it4lik/meow-api:arm",
            "Volumes": null,
            "WorkingDir": "/app",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "37a84c79f29816ab2fc057a9573739c5f46aa47d70ba0cda50bef4ab8756ffc1",
            "SandboxKey": "/var/run/docker/netns/37a84c79f298",
            "Ports": {
                "8000/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "8000"
                    }
                ]
            },
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "4e4db607e2478f5b0ac5df85a9a05b4f11edcb08cd703c2f0d659f7d024bdcad",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "0a:ec:0c:21:2f:45",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "MacAddress": "0a:ec:0c:21:2f:45",
                    "DriverOpts": null,
                    "GwPriority": 0,
                    "NetworkID": "cfe3d7b976192696a0f356b928d0b2472328bd9efc596aec596795ff3b408a6f",
                    "EndpointID": "4e4db607e2478f5b0ac5df85a9a05b4f11edcb08cd703c2f0d659f7d024bdcad",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "DNSNames": null
                }
            }
        },
        "ImageManifestDescriptor": {
            "mediaType": "application/vnd.oci.image.manifest.v1+json",
            "digest": "sha256:1cf16712aacdf3b43e9fdf49d2e19af6625526d9ee9b32c12b7e2535f9648c22",
            "size": 2391,
            "platform": {
                "architecture": "arm64",
                "os": "linux"
            }
        }
    }
]
```



Visiter la route de l'API sur http://votre_ip:8000

```json
{
    "message": "Available routes",
    "routes": {
        "get_user_by_id": "http://10.100.0.136:8000/user/1",
        "list_all_users": "http://10.100.0.136:8000/users"
    }
}
```

☀️ Lancer le conteneur en tâche de fond

Ajout du -d pour exécuter le conteneur en arrière-plan.
```bash
docker run -d -p 8000:8000 it4lik/meow-api:arm
```

Docker logs <container ID>

```bash
docker container ls -a && 
docker logs <container ID>
````



 Voici les logs du conteneur en cours d'exécution :

```json

docker logs 20881f724a39
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://172.17.0.2:8000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 153-963-822

```


