from linode_api4 import LinodeClient
import requests
import json
import random
import time
token = 'xxxx'#token
chosen_region = ["ap-west", "ca-central", "ap-southeast", "us-central", "us-west", "us-southeast", "us-east", "eu-west", "ap-south", "eu-central", "ap-northeast"]
client = LinodeClient(token)



for i in range(0 ,15)  :  # 先搞2轮，目的是5000/3
    try:
        new_linode = client.linode.instance_create('g6-nanode-1', chosen_region[random.randint(0, 10)],
                                                   image='linode/ubuntu22.10')
        time.sleep(3)
        for current_linode in new_linode:
            print("创建成功！IP地址:", current_linode.ips.ipv4.public)#奇怪我为什么要在这边写for循环来着。。。太久了我都忘记了（捂脸）

            while True:#感觉这一块可能程序逻辑有问题。。。没运行过
                try:
                    print(f"开始删除{current_linode.ips.ipv4.public}！")
                    a=current_linode.ips.ipv4.public
                    current_linode.delete()
                    print(f"{a}删除成功！")
                    break
                except:
                    print("诶呀删不掉，等60s再试一次！")
                    time.sleep(60)
                    continue

    except:
        print("创建失败，跳过！")
        continue