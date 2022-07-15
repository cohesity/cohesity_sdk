Cohesity SDK
=================
[![License: Apache2](https://img.shields.io/hexpm/l/plug.svg)](https://github.com/cohesity/cohesity_sdk/blob/master/LICENSE)
![Maintenance](https://img.shields.io/maintenance/yes/2022)
## Overview

The *Cohesity SDK*  provides an easy-to-use language binding to
harness the power of *Cohesity REST APIs* in your python applications.

## Table of contents :scroll:

 - [Getting Started](#get-started)
 - [Documentation](#documentation)
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

## <a name="documentation"></a> Documentation :books:

<a href="https://developer.cohesity.com/versions.html">Refer Python docs for your cluster version. </a>

## <a name="howto"></a> How to Use: :mag_right:

This SDK exposes all the functionality provided by *Cohesity REST API*.

Initializing the Client:
```
# Helios client Initialization

from cohesity_sdk.helios.cohesity_client import HeliosClient

cluster_vip = 'prod-cluster.eng.cohesity.com'
api_key = "87t3w3-42623vcw54-c33v66"
client = HeliosClient(cluster_vip=cluster_vip, api_key=api_key)
platform_controller = client.platform
result = platform_controller.get_cluster()
result_dict =  result.__dict__
print(result_dict["_data_store"]["sw_version"])


#OUTPUT
6.6.0d_ent_release-20220314_05c9bae3
```

## <a name="sample"></a> More sample code to get going: :bulb:

Check out the scripts included under [`samples`](./samples) for reference.

## <a name="contribute"></a> Contribute :handshake:

* [Refer our contribution guideline](./CONTRIBUTING.md).


## <a name ="suggest"></a> Questions or Feedback :raised_hand:

We would love to hear from you. Please send your questions and feedback to: *cohesity-api-sdks@cohesity.com*
