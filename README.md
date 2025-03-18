Cohesity SDK
=================
[![License: Apache2](https://img.shields.io/hexpm/l/plug.svg)](https://github.com/cohesity/cohesity_sdk/blob/master/LICENSE)
![Maintenance](https://img.shields.io/maintenance/yes/2023)
## Overview

The *Cohesity SDK*  provides an easy-to-use language binding to
harness the power of *Cohesity REST APIs* in your python applications.

## Table of contents :scroll:

 - [Getting Started](#get-started)
 - [Version Matrix](#matrix)
 - [How to use](#howto)
 - [More samples](#sample)
 - [How can you contribute](#contribute)
 - [Suggestions and Feedback](#suggest)
 

## <a name="get-started"></a> Let's get started :hammer_and_pick:

### Installation

Install from source:

The generated code uses Python packages named requests, jsonpickle and dateutil.
You can resolve these dependencies using [pip](https://pip.pypa.io/en/stable/).
This SDK uses the Requests library and will work for Python *2 >=2.7.9*
and Python *3 >=3.4*.
```
git clone https://github.com/cohesity/cohesity_sdk.git
cd cohesity_sdk
pip install -r requirements.txt
python setup.py install
```
## <a name="matrix"></a> Version Matrix
Cluster-SDK support Matrix

| Cluster Version	 | SDK version|
|------------------|------------|
| 6.6.0d_ent(V2)   | 1.1.0|
| 6.8.1(V2)        | 1.2.0|
| 7.1.2_u3(V2)     | 1.3.0 |

Helios-SDK support Matrix

| Helios Version	 | SDK version |
|-----------------|-------------|
| 7.1.2_u3(V2)    | 1.3.0       |

## <a name="howto"></a> How to Use: :mag_right:

This SDK exposes all the functionality provided by *Cohesity REST API*.

Initializing the Client:
```
# Cluster client Initialization

from cohesity_sdk.cluster.cluster_client import ClusterClient

cluster_vip = 'prod-cluster.eng.cohesity.com'
username = 'admin'
password = 'admin'
domain = "LOCAL"
client = ClusterClient(
    cluster_vip=cluster_vip, username=username, password=password, domain=domain)

print(client.platform.get_cluster().sw_version)

#OUTPUT
6.6.0d_ent_release-20220621_a04bcd28
```


```
# Helious client Initialization

from cohesity_sdk.helios.mcm_v2_client import McmV2Client

access_cluster_id=xxxxxx
api_key='xxxxxxx'
cluster_vip='helios.cohesity.com'

helious_client = McmV2Client(
    cluster_vip=cluster_vip, api_key=api_key)

print(helious_client.view_api.get_views(access_cluster_id=access_cluster_id)

#OUTPUT
{
    "views": [],
    "lastResult": true,
    "count": 0
}
```

## <a name="sample"></a> More sample code to get going: :bulb:

Check out the scripts included under [`samples`](./samples) for reference.

## <a name="contribute"></a> Contribute :handshake:

* [Refer our contribution guideline](./CONTRIBUTING.md).


## <a name ="suggest"></a> Questions or Feedback :raised_hand:

We would love to hear from you. Please send your questions and feedback to: *support@cohesity.com*