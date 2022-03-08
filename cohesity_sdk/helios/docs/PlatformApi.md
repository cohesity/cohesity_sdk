# cohesity_sdk.PlatformApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**add_remote_disk**](PlatformApi.md#add_remote_disk) | **POST** /disks/remote | Add remote disk
[**add_syslog_server**](PlatformApi.md#add_syslog_server) | **POST** /syslogs | Add Syslog Server
[**create_cluster**](PlatformApi.md#create_cluster) | **POST** /clusters | Create a cluster.
[**create_racks**](PlatformApi.md#create_racks) | **POST** /racks | Create racks
[**delete_amqp_target_config**](PlatformApi.md#delete_amqp_target_config) | **DELETE** /clusters/amqp-target-config | Delete AMQP Target Config
[**delete_rack_by_id**](PlatformApi.md#delete_rack_by_id) | **DELETE** /racks/{id} | Delete a rack by id.
[**delete_racks**](PlatformApi.md#delete_racks) | **DELETE** /racks | Delete all the racks.
[**delete_remote_storage_registration**](PlatformApi.md#delete_remote_storage_registration) | **DELETE** /remote-storage/{id} | Delete Remote Storage Registration
[**discover_disks**](PlatformApi.md#discover_disks) | **GET** /disks/discover | Discover new disks
[**disk_identify**](PlatformApi.md#disk_identify) | **POST** /disks/identify | Identify a disk
[**disks_assimilate**](PlatformApi.md#disks_assimilate) | **POST** /disks/assimilate | Assimilate disks.
[**get_alert_summary**](PlatformApi.md#get_alert_summary) | **GET** /alertsSummary | Get alerts summary.
[**get_amqp_target_config**](PlatformApi.md#get_amqp_target_config) | **GET** /clusters/amqp-target-config | Get AMQP Target Config
[**get_chassis**](PlatformApi.md#get_chassis) | **GET** /chassis | Get list of chassis
[**get_chassis_by_id**](PlatformApi.md#get_chassis_by_id) | **GET** /chassis/{id} | Get a chassis by chassis id.
[**get_cluster**](PlatformApi.md#get_cluster) | **GET** /clusters | Retrieve Cluster Configuration
[**get_cluster_local_domain_sid**](PlatformApi.md#get_cluster_local_domain_sid) | **GET** /clusters/local-domain-sid | Get Cluster Local Domain SID
[**get_is_d_maa_s_cluster**](PlatformApi.md#get_is_d_maa_s_cluster) | **GET** /clusters/is-dmaas | Get whether the cluster is a DMaaS cluster.
[**get_network_interfaces**](PlatformApi.md#get_network_interfaces) | **GET** /network-interfaces | Get list of interfaces
[**get_rack_by_id**](PlatformApi.md#get_rack_by_id) | **GET** /racks/{id} | Get a rack by rack id.
[**get_racks**](PlatformApi.md#get_racks) | **GET** /racks | Get list of racks
[**get_registered_remote_storage_list**](PlatformApi.md#get_registered_remote_storage_list) | **GET** /remote-storage | Get Registered Remote Storage Servers List
[**get_remote_disks**](PlatformApi.md#get_remote_disks) | **GET** /disks/remote | Get remote disks
[**get_remote_storage_details**](PlatformApi.md#get_remote_storage_details) | **GET** /remote-storage/{id} | Get remote storage details
[**get_support_channel_config**](PlatformApi.md#get_support_channel_config) | **GET** /support-channel-config | Get support channel configuration.
[**get_supported_syslog_program_names**](PlatformApi.md#get_supported_syslog_program_names) | **GET** /syslogProgramNames | Get supported program names.
[**get_syslog_audit_tags**](PlatformApi.md#get_syslog_audit_tags) | **GET** /syslogAuditTags | Get cluster audit tags.
[**get_syslog_server_by_id**](PlatformApi.md#get_syslog_server_by_id) | **GET** /syslogs/{id} | Get a syslog server by id.
[**get_syslog_server_status_by_id**](PlatformApi.md#get_syslog_server_status_by_id) | **GET** /syslogs/{id}/status | Get a syslog server reachability status.
[**get_syslog_servers**](PlatformApi.md#get_syslog_servers) | **GET** /syslogs | Get list of syslog servers.
[**identify_node**](PlatformApi.md#identify_node) | **POST** /nodes/{id}/identify | Identify node
[**list_disks**](PlatformApi.md#list_disks) | **GET** /disks/local | Get list of disks
[**list_feature_flag**](PlatformApi.md#list_feature_flag) | **GET** /clusters/feature-flag | Get feature flag overrides list.
[**mark_disk_removal**](PlatformApi.md#mark_disk_removal) | **POST** /disks/{id}/remove | Mark Disk for removal
[**mark_node_removal**](PlatformApi.md#mark_node_removal) | **POST** /nodes/{id}/remove | Mark Node for removal
[**patch_syslog_server_by_id**](PlatformApi.md#patch_syslog_server_by_id) | **PATCH** /syslogs/{id} | Patch a syslog server by id.
[**register_new_remote_storage**](PlatformApi.md#register_new_remote_storage) | **POST** /remote-storage | Register Remote Storage
[**remove_remote_disk**](PlatformApi.md#remove_remote_disk) | **DELETE** /disks/remote/{id} | Remove remote disk
[**remove_syslog_server**](PlatformApi.md#remove_syslog_server) | **DELETE** /syslogs/{id} | Remove syslog server by id
[**remove_syslog_servers**](PlatformApi.md#remove_syslog_servers) | **DELETE** /syslogs | Remove syslog servers
[**set_node_power**](PlatformApi.md#set_node_power) | **POST** /nodePower | Reboot or shutdown nodes in cluster.
[**update_amqp_target_config**](PlatformApi.md#update_amqp_target_config) | **PUT** /clusters/amqp-target-config | Update AMQP Target Config
[**update_chassis_by_id**](PlatformApi.md#update_chassis_by_id) | **PATCH** /chassis/{id} | Update a chassis by chassis id.
[**update_cluster**](PlatformApi.md#update_cluster) | **PUT** /clusters | Update a cluster.
[**update_feature_flag**](PlatformApi.md#update_feature_flag) | **PUT** /clusters/feature-flag | Update feature flag override status.
[**update_is_d_maa_s_cluster**](PlatformApi.md#update_is_d_maa_s_cluster) | **PUT** /clusters/is-dmaas | Update whether the cluster is a DMaaS cluster.
[**update_rack_by_id**](PlatformApi.md#update_rack_by_id) | **PATCH** /racks/{id} | 
[**update_racks**](PlatformApi.md#update_racks) | **PATCH** /racks | Update racks
[**update_remote_storage_registration**](PlatformApi.md#update_remote_storage_registration) | **PATCH** /remote-storage/{id} | Update Remote Storage Config
[**update_support_channel_config**](PlatformApi.md#update_support_channel_config) | **PUT** /support-channel-config | Update support channel configuration.
[**update_syslog_audit_tags**](PlatformApi.md#update_syslog_audit_tags) | **POST** /syslogAuditTags | Update cluster audit tags.
[**update_syslog_server_by_id**](PlatformApi.md#update_syslog_server_by_id) | **PUT** /syslogs/{id} | Update a syslog server by id.


# **add_remote_disk**
> AddRemoteDiskResponseBody add_remote_disk(body)

Add remote disk

Add a remote disk.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.add_remote_disk_response_body import AddRemoteDiskResponseBody
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.remote_disks import RemoteDisks
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = RemoteDisks(
        remote_disks=[
            RemoteDisk(
                mount_path="mount_path_example",
                node_id=1,
                tier="PCIeSSD",
                file_system_name="file_system_name_example",
                data_vip="data_vip_example",
                node_ip="node_ip_example",
            ),
        ],
    ) # RemoteDisks | Specifies the remote disk configuration.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Add remote disk
	api_response = client.platform.add_remote_disk(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->add_remote_disk: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Add remote disk
	api_response = client.platform.add_remote_disk(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->add_remote_disk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoteDisks**](RemoteDisks.md)| Specifies the remote disk configuration. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**AddRemoteDiskResponseBody**](AddRemoteDiskResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_syslog_server**
> SyslogServer add_syslog_server(body)

Add Syslog Server

Add a new syslog server

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.syslog_server import SyslogServer
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = SyslogServer(
        id=1,
        ip="ip_example",
        port=1,
        protocol="protocol_example",
        name="name_example",
        enabled=True,
        facility_list=[
            "facility_list_example",
        ],
        program_name_list=[
            "program_name_list_example",
        ],
        msg_pattern_list=[
            "msg_pattern_list_example",
        ],
        raw_msg_pattern_list=[
            "raw_msg_pattern_list_example",
        ],
        is_tls_enabled=True,
        ca_certificate="ca_certificate_example",
    ) # SyslogServer | Specifies parameters to add syslog server.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Add Syslog Server
	api_response = client.platform.add_syslog_server(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->add_syslog_server: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Add Syslog Server
	api_response = client.platform.add_syslog_server(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->add_syslog_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SyslogServer**](SyslogServer.md)| Specifies parameters to add syslog server. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**SyslogServer**](SyslogServer.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster**
> Cluster create_cluster(body)

Create a cluster.

Create a cluster with given network and cluster configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.cluster import Cluster
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.create_cluster_params import CreateClusterParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CreateClusterParams(
        name="name_example",
        type="Physical",
        enable_encryption=True,
        network_config=ClusterCreateNetworkConfig(
            ntp_servers=[
                "ntp_servers_example",
            ],
            domain_names=[
                "domain_names_example",
            ],
            vip_host_name="vip_host_name_example",
            ip_preference="Ipv4",
            use_dhcp=True,
            dhcp_network_config=ClusterDhcpNetworkConfig(
                dns_servers=[
                    "dns_servers_example",
                ],
            ),
            manual_network_config=ClusterManualNetworkConfig(
                gateway="gateway_example",
                subnet_ip="subnet_ip_example",
                subnet_mask="subnet_mask_example",
                dns_servers=[
                    "dns_servers_example",
                ],
            ),
        ),
        proxy_server_config=ClusterProxyServerConfig(
            ip="ip_example",
            port=1,
            username="username_example",
            password="password_example",
        ),
        physical_cluster_params=ClusterCreatePhysicalParams(
            nodes=[
                ClusterCreateNodeParams(
                    node_id=1,
                    node_ip="node_ip_example",
                ),
            ],
        ),
        virtual_cluster_params=ClusterCreateVirtualParams(
            nodes=[
                ClusterCreateNodeParams(
                    node_id=1,
                    node_ip="node_ip_example",
                ),
            ],
        ),
        cloud_cluster_params=ClusterCreateCloudParams(
            node_ips=[
                "node_ips_example",
            ],
        ),
        rigel_cluster_params=ClusterCreateRigelParams(
            nodes=[
                RigelClusterNode(
                    node_ip="node_ip_example",
                    node_id=1,
                ),
            ],
            claim_token="claim_token_example",
        ),
    ) # CreateClusterParams | Specifies the parameters to create cluster.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a cluster.
	api_response = client.platform.create_cluster(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->create_cluster: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a cluster.
	api_response = client.platform.create_cluster(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->create_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateClusterParams**](CreateClusterParams.md)| Specifies the parameters to create cluster. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**Cluster**](Cluster.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_racks**
> Racks create_racks(body)

Create racks

Create list of racks and optionally also assign list of chassis to each rack

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.racks import Racks
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = Racks(
        racks=[
            Rack(
                id=1,
                name="name_example",
                location="location_example",
                chassis_ids=[
                    1,
                ],
            ),
        ],
    ) # Racks | Specifies the parameters to create racks.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create racks
	api_response = client.platform.create_racks(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->create_racks: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create racks
	api_response = client.platform.create_racks(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->create_racks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Racks**](Racks.md)| Specifies the parameters to create racks. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**Racks**](Racks.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_amqp_target_config**
> delete_amqp_target_config()

Delete AMQP Target Config

Delete AMQP target config on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete AMQP Target Config
	client.platform.delete_amqp_target_config(access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling PlatformApi->delete_amqp_target_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rack_by_id**
> delete_rack_by_id(id)

Delete a rack by id.

Delete a given rack by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies a unique id of the rack.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete a rack by id.
	client.platform.delete_rack_by_id(id)
except ApiException as e:
	print("Exception when calling PlatformApi->delete_rack_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete a rack by id.
	client.platform.delete_rack_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling PlatformApi->delete_rack_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the rack. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_racks**
> delete_racks()

Delete all the racks.

Delete all the racks.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete all the racks.
	client.platform.delete_racks(access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling PlatformApi->delete_racks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_remote_storage_registration**
> delete_remote_storage_registration(id)

Delete Remote Storage Registration

Delete remote storage registration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the registration id of the registered remote storage.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete Remote Storage Registration
	client.platform.delete_remote_storage_registration(id)
except ApiException as e:
	print("Exception when calling PlatformApi->delete_remote_storage_registration: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete Remote Storage Registration
	client.platform.delete_remote_storage_registration(id, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling PlatformApi->delete_remote_storage_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the registration id of the registered remote storage. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_disks**
> ClusterFreeDisks discover_disks()

Discover new disks

Discover disks that are ready for activation

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.cluster_free_disks import ClusterFreeDisks
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Discover new disks
	api_response = client.platform.discover_disks(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->discover_disks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ClusterFreeDisks**](ClusterFreeDisks.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disk_identify**
> DiskIdentify disk_identify(body)

Identify a disk

Turn on/off led light of a disk.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.disk_identify import DiskIdentify
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = DiskIdentify(
        node_id=1,
        serial_number="serial_number_example",
        identify=True,
    ) # DiskIdentify | Specifies the parameter to identify disk.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Identify a disk
	api_response = client.platform.disk_identify(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->disk_identify: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Identify a disk
	api_response = client.platform.disk_identify(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->disk_identify: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DiskIdentify**](DiskIdentify.md)| Specifies the parameter to identify disk. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**DiskIdentify**](DiskIdentify.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disks_assimilate**
> ClusterFreeDisks disks_assimilate(body)

Assimilate disks.

Assimilate list of disks from one or more nodes of cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.cluster_free_disks import ClusterFreeDisks
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = ClusterFreeDisks(
        node_free_disks=[
            NodeFreeDisks(
                node_id=1,
                free_disks=[
                    FreeDisk(
                        location="location_example",
                        serial_number="serial_number_example",
                        path="path_example",
                        size_in_bytes=1,
                    ),
                ],
                chassis_serial="chassis_serial_example",
                slot=1,
            ),
        ],
    ) # ClusterFreeDisks | Specifies the parameter to assimilate disks.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Assimilate disks.
	api_response = client.platform.disks_assimilate(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->disks_assimilate: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Assimilate disks.
	api_response = client.platform.disks_assimilate(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->disks_assimilate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterFreeDisks**](ClusterFreeDisks.md)| Specifies the parameter to assimilate disks. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ClusterFreeDisks**](ClusterFreeDisks.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_summary**
> AlertsSummaryResponse get_alert_summary()

Get alerts summary.

Get alerts summary grouped by category.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.alerts_summary_response import AlertsSummaryResponse
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
start_time_usecs = 1 # int | Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. (optional)
end_time_usecs = 1 # int | Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. (optional)
include_tenants = True # bool, none_type | IncludeTenants specifies if alerts of all the tenants under the hierarchy of the logged in user's organization should be used to compute summary. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str], none_type | TenantIds contains ids of the tenants for which alerts are to be used to compute summary. (optional)
states_list = [
        "kResolved",
    ] # [str], none_type | Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get alerts summary.
	api_response = client.platform.get_alert_summary(access_cluster_id=access_cluster_id, region_id=region_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, include_tenants=include_tenants, tenant_ids=tenant_ids, states_list=states_list)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_alert_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **start_time_usecs** | **int**| Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. | [optional]
 **end_time_usecs** | **int**| Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. | [optional]
 **include_tenants** | **bool, none_type**| IncludeTenants specifies if alerts of all the tenants under the hierarchy of the logged in user&#39;s organization should be used to compute summary. | [optional]
 **tenant_ids** | **[str], none_type**| TenantIds contains ids of the tenants for which alerts are to be used to compute summary. | [optional]
 **states_list** | **[str], none_type**| Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary. | [optional]

### Return type

[**AlertsSummaryResponse**](AlertsSummaryResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_amqp_target_config**
> ClusterAMQPTargetConfig get_amqp_target_config()

Get AMQP Target Config

Fetch AMQP target config on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.cluster_amqp_target_config import ClusterAMQPTargetConfig
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get AMQP Target Config
	api_response = client.platform.get_amqp_target_config(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_amqp_target_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ClusterAMQPTargetConfig**](ClusterAMQPTargetConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chassis**
> ChassisList get_chassis()

Get list of chassis

Get list of all chassis info that are part of cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.chassis_list import ChassisList
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
no_rack_assigned = True # bool | Filters chassis that have no rack assigned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get list of chassis
	api_response = client.platform.get_chassis(access_cluster_id=access_cluster_id, region_id=region_id, no_rack_assigned=no_rack_assigned)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_chassis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **no_rack_assigned** | **bool**| Filters chassis that have no rack assigned. | [optional]

### Return type

[**ChassisList**](ChassisList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chassis_by_id**
> Chassis get_chassis_by_id(id)

Get a chassis by chassis id.

Get a chassis info by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.chassis import Chassis
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of chassis.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get a chassis by chassis id.
	api_response = client.platform.get_chassis_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_chassis_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a chassis by chassis id.
	api_response = client.platform.get_chassis_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_chassis_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of chassis. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**Chassis**](Chassis.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster**
> Cluster get_cluster()

Retrieve Cluster Configuration

Retrieve some summary information about the Cluster Configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.cluster import Cluster
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Retrieve Cluster Configuration
	api_response = client.platform.get_cluster(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**Cluster**](Cluster.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_local_domain_sid**
> ClusterLocalDomainSID get_cluster_local_domain_sid()

Get Cluster Local Domain SID

Fetch SID of cluster local domain.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.cluster_local_domain_sid import ClusterLocalDomainSID
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Cluster Local Domain SID
	api_response = client.platform.get_cluster_local_domain_sid(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster_local_domain_sid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ClusterLocalDomainSID**](ClusterLocalDomainSID.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_is_d_maa_s_cluster**
> DMaaSInfo get_is_d_maa_s_cluster()

Get whether the cluster is a DMaaS cluster.

Get whether the cluster is a DMaaS cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.d_maa_s_info import DMaaSInfo
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get whether the cluster is a DMaaS cluster.
	api_response = client.platform.get_is_d_maa_s_cluster(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_is_d_maa_s_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**DMaaSInfo**](DMaaSInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_interfaces**
> ClusterInterfaces get_network_interfaces()

Get list of interfaces

Get a list of interfaces present on the node or cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.cluster_interfaces import ClusterInterfaces
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get list of interfaces
	api_response = client.platform.get_network_interfaces(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_network_interfaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ClusterInterfaces**](ClusterInterfaces.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rack_by_id**
> Rack get_rack_by_id(id)

Get a rack by rack id.

Get a rack info by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.rack import Rack
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of rack.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get a rack by rack id.
	api_response = client.platform.get_rack_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_rack_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a rack by rack id.
	api_response = client.platform.get_rack_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_rack_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of rack. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**Rack**](Rack.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_racks**
> Racks get_racks()

Get list of racks

Get list of all racks that are part of cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.racks import Racks
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get list of racks
	api_response = client.platform.get_racks(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_racks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**Racks**](Racks.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registered_remote_storage_list**
> RegisteredRemoteStorageList get_registered_remote_storage_list()

Get Registered Remote Storage Servers List

Get summary about list of registered remote storage servers.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.registered_remote_storage_list import RegisteredRemoteStorageList
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Registered Remote Storage Servers List
	api_response = client.platform.get_registered_remote_storage_list(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_registered_remote_storage_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**RegisteredRemoteStorageList**](RegisteredRemoteStorageList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_disks**
> RemoteDisks get_remote_disks()

Get remote disks

Get remote disks.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.remote_disks import RemoteDisks
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
disk_ids = [
        1,
    ] # [int] | Specifies a list of disk ids, only disks having these ids will be returned. (optional)
node_ids = [
        1,
    ] # [int] | Specifies a list of node ids, only disks in these nodes will be returned. (optional)
tiers = [
        "PCIeSSD",
    ] # [str] | Specifies a list of disk tiers, only disks with given tiers will be returned. (optional)
mount_path = "mountPath_example" # str | This field is deprecated. Providing this queryparam will not have any impact. Please use fileSystem query param to filter instead. (optional)
file_system = "fileSystem_example" # str | Specified file system name to search. only disks with file system name that partially matches the specified name will be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get remote disks
	api_response = client.platform.get_remote_disks(access_cluster_id=access_cluster_id, region_id=region_id, disk_ids=disk_ids, node_ids=node_ids, tiers=tiers, mount_path=mount_path, file_system=file_system)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_remote_disks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **disk_ids** | **[int]**| Specifies a list of disk ids, only disks having these ids will be returned. | [optional]
 **node_ids** | **[int]**| Specifies a list of node ids, only disks in these nodes will be returned. | [optional]
 **tiers** | **[str]**| Specifies a list of disk tiers, only disks with given tiers will be returned. | [optional]
 **mount_path** | **str**| This field is deprecated. Providing this queryparam will not have any impact. Please use fileSystem query param to filter instead. | [optional]
 **file_system** | **str**| Specified file system name to search. only disks with file system name that partially matches the specified name will be returned. | [optional]

### Return type

[**RemoteDisks**](RemoteDisks.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_storage_details**
> RemoteStorageInfo get_remote_storage_details(id)

Get remote storage details

Get details of remote storage given by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.remote_storage_info import RemoteStorageInfo
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of the registered remote storage.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
include_available_space = False # bool | Specifies whether to include available capacity on remote storage. (optional) if omitted the server will use the default value of False
include_available_data_vips = False # bool | Specifies whether to include available data vips on remote storage. (optional) if omitted the server will use the default value of False
include_array_info = False # bool | Includes flashblade specific info like name, software os and version of pure flashblade. (optional) if omitted the server will use the default value of False

# example passing only required values which don't have defaults set
try:
	# Get remote storage details
	api_response = client.platform.get_remote_storage_details(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_remote_storage_details: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get remote storage details
	api_response = client.platform.get_remote_storage_details(id, access_cluster_id=access_cluster_id, region_id=region_id, include_available_space=include_available_space, include_available_data_vips=include_available_data_vips, include_array_info=include_array_info)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_remote_storage_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the registered remote storage. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **include_available_space** | **bool**| Specifies whether to include available capacity on remote storage. | [optional] if omitted the server will use the default value of False
 **include_available_data_vips** | **bool**| Specifies whether to include available data vips on remote storage. | [optional] if omitted the server will use the default value of False
 **include_array_info** | **bool**| Includes flashblade specific info like name, software os and version of pure flashblade. | [optional] if omitted the server will use the default value of False

### Return type

[**RemoteStorageInfo**](RemoteStorageInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_support_channel_config**
> SupportChannelConfig get_support_channel_config()

Get support channel configuration.

Get support channel configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.support_channel_config import SupportChannelConfig
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get support channel configuration.
	api_response = client.platform.get_support_channel_config(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_support_channel_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**SupportChannelConfig**](SupportChannelConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_syslog_program_names**
> [str] get_supported_syslog_program_names()

Get supported program names.

Get supported program names to configure for a syslog server.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get supported program names.
	api_response = client.platform.get_supported_syslog_program_names(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_supported_syslog_program_names: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

**[str]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_syslog_audit_tags**
> SyslogAuditTag get_syslog_audit_tags()

Get cluster audit tags.

Get cluster audit tags.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.syslog_audit_tag import SyslogAuditTag
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get cluster audit tags.
	api_response = client.platform.get_syslog_audit_tags(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_syslog_audit_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**SyslogAuditTag**](SyslogAuditTag.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_syslog_server_by_id**
> SyslogServer get_syslog_server_by_id(id)

Get a syslog server by id.

Get a syslog server by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.syslog_server import SyslogServer
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of syslog server.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get a syslog server by id.
	api_response = client.platform.get_syslog_server_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_syslog_server_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a syslog server by id.
	api_response = client.platform.get_syslog_server_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_syslog_server_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of syslog server. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**SyslogServer**](SyslogServer.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_syslog_server_status_by_id**
> SyslogServerStatus get_syslog_server_status_by_id(id)

Get a syslog server reachability status.

Check syslog server reachability by given Id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.syslog_server_status import SyslogServerStatus
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of syslog server.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get a syslog server reachability status.
	api_response = client.platform.get_syslog_server_status_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_syslog_server_status_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a syslog server reachability status.
	api_response = client.platform.get_syslog_server_status_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_syslog_server_status_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of syslog server. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**SyslogServerStatus**](SyslogServerStatus.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_syslog_servers**
> SyslogServers get_syslog_servers()

Get list of syslog servers.

Get list of syslog servers.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.syslog_servers import SyslogServers
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get list of syslog servers.
	api_response = client.platform.get_syslog_servers(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_syslog_servers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**SyslogServers**](SyslogServers.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identify_node**
> NodeIdentifyParams identify_node(id, body)

Identify node

Turn on/off LED light of a node to identify.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.node_identify_params import NodeIdentifyParams
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies id of node to identify.
body = NodeIdentifyParams(
        identify=True,
    ) # NodeIdentifyParams | Specifies the parameter to identify node.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Identify node
	api_response = client.platform.identify_node(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->identify_node: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Identify node
	api_response = client.platform.identify_node(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->identify_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of node to identify. |
 **body** | [**NodeIdentifyParams**](NodeIdentifyParams.md)| Specifies the parameter to identify node. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**NodeIdentifyParams**](NodeIdentifyParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_disks**
> DisksList list_disks()

Get list of disks

Get list of local disks.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.disks_list import DisksList
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
node_id = 1 # int | Specifies node id of the node to get list of disks (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get list of disks
	api_response = client.platform.list_disks(access_cluster_id=access_cluster_id, region_id=region_id, node_id=node_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->list_disks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **node_id** | **int**| Specifies node id of the node to get list of disks | [optional]

### Return type

[**DisksList**](DisksList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_feature_flag**
> list_feature_flag()

Get feature flag overrides list.

Get the list of feature flag overrides defined on cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get feature flag overrides list.
	client.platform.list_feature_flag(access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling PlatformApi->list_feature_flag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_disk_removal**
> RemoveDisk mark_disk_removal(id, body)

Mark Disk for removal

Mark disk for removal or cancel removal if a disk is already marked for removal.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.disk_removal_params import DiskRemovalParams
from cohesity_sdk.helios.model.remove_disk import RemoveDisk
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies unique id of the disk to mark for removal.
body = DiskRemovalParams(
        cancel=True,
    ) # DiskRemovalParams | Specifies parameters to mark/cancel disk removal.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Mark Disk for removal
	api_response = client.platform.mark_disk_removal(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->mark_disk_removal: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Mark Disk for removal
	api_response = client.platform.mark_disk_removal(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->mark_disk_removal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies unique id of the disk to mark for removal. |
 **body** | [**DiskRemovalParams**](DiskRemovalParams.md)| Specifies parameters to mark/cancel disk removal. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**RemoveDisk**](RemoveDisk.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_node_removal**
> RemoveNode mark_node_removal(id, body)

Mark Node for removal

Mark node for removal or Cancel if a node is already marked for removal.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.remove_node import RemoveNode
from cohesity_sdk.helios.model.node_removal_params import NodeRemovalParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies id of node to cancel removal.
body = NodeRemovalParams(
        cancel=True,
        is_offline=False,
    ) # NodeRemovalParams | Specifies parameters to initiate/cancel node removal .
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Mark Node for removal
	api_response = client.platform.mark_node_removal(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->mark_node_removal: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Mark Node for removal
	api_response = client.platform.mark_node_removal(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->mark_node_removal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of node to cancel removal. |
 **body** | [**NodeRemovalParams**](NodeRemovalParams.md)| Specifies parameters to initiate/cancel node removal . |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**RemoveNode**](RemoveNode.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_syslog_server_by_id**
> SyslogServer patch_syslog_server_by_id(id)

Patch a syslog server by id.

Patch syslog server by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.syslog_server import SyslogServer
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of syslog server.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
body = SyslogServer(
        id=1,
        ip="ip_example",
        port=1,
        protocol="protocol_example",
        name="name_example",
        enabled=True,
        facility_list=[
            "facility_list_example",
        ],
        program_name_list=[
            "program_name_list_example",
        ],
        msg_pattern_list=[
            "msg_pattern_list_example",
        ],
        raw_msg_pattern_list=[
            "raw_msg_pattern_list_example",
        ],
        is_tls_enabled=True,
        ca_certificate="ca_certificate_example",
    ) # SyslogServer | Specifies the body of syslog server fields to patch. (optional)

# example passing only required values which don't have defaults set
try:
	# Patch a syslog server by id.
	api_response = client.platform.patch_syslog_server_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->patch_syslog_server_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Patch a syslog server by id.
	api_response = client.platform.patch_syslog_server_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id, body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->patch_syslog_server_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of syslog server. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **body** | [**SyslogServer**](SyslogServer.md)| Specifies the body of syslog server fields to patch. | [optional]

### Return type

[**SyslogServer**](SyslogServer.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_new_remote_storage**
> RemoteStorageInfo register_new_remote_storage(body)

Register Remote Storage

Register a remote storage to be used for disaggregated storage.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.remote_storage_info import RemoteStorageInfo
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = RemoteStorageInfo() # RemoteStorageInfo | Specifies the parameters to register a remote storage management server.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Register Remote Storage
	api_response = client.platform.register_new_remote_storage(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->register_new_remote_storage: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Register Remote Storage
	api_response = client.platform.register_new_remote_storage(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->register_new_remote_storage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoteStorageInfo**](RemoteStorageInfo.md)| Specifies the parameters to register a remote storage management server. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**RemoteStorageInfo**](RemoteStorageInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_remote_disk**
> remove_remote_disk(id)

Remove remote disk

Remove a remote disk.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of the remote disk to remove.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Remove remote disk
	client.platform.remove_remote_disk(id)
except ApiException as e:
	print("Exception when calling PlatformApi->remove_remote_disk: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Remove remote disk
	client.platform.remove_remote_disk(id, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling PlatformApi->remove_remote_disk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the remote disk to remove. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_syslog_server**
> remove_syslog_server(id)

Remove syslog server by id

Delete syslog server by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies a unique id of the syslog server.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Remove syslog server by id
	client.platform.remove_syslog_server(id)
except ApiException as e:
	print("Exception when calling PlatformApi->remove_syslog_server: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Remove syslog server by id
	client.platform.remove_syslog_server(id, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling PlatformApi->remove_syslog_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the syslog server. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_syslog_servers**
> remove_syslog_servers()

Remove syslog servers

Delete all syslog servers.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Remove syslog servers
	client.platform.remove_syslog_servers(access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling PlatformApi->remove_syslog_servers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_node_power**
> set_node_power(body)

Reboot or shutdown nodes in cluster.

Reboot or shutdown nodes in cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.node_power_operation import NodePowerOperation
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = NodePowerOperation(
        operation="poweroff",
        node_id=1,
    ) # NodePowerOperation | Specifies the reboot or shutdown operation.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Reboot or shutdown nodes in cluster.
	client.platform.set_node_power(body)
except ApiException as e:
	print("Exception when calling PlatformApi->set_node_power: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Reboot or shutdown nodes in cluster.
	client.platform.set_node_power(body, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling PlatformApi->set_node_power: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodePowerOperation**](NodePowerOperation.md)| Specifies the reboot or shutdown operation. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_amqp_target_config**
> ClusterAMQPTargetConfig update_amqp_target_config(body)

Update AMQP Target Config

Updates AMQP target config on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.cluster_amqp_target_config import ClusterAMQPTargetConfig
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = ClusterAMQPTargetConfig(
        server_ip="server_ip_example",
        username="username_example",
        password="password_example",
        virtual_host="virtual_host_example",
        exchange="exchange_example",
        filer_id=1,
        certificate="certificate_example",
    ) # ClusterAMQPTargetConfig | Specifies the parameters to update cluster AMQP target config.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update AMQP Target Config
	api_response = client.platform.update_amqp_target_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_amqp_target_config: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update AMQP Target Config
	api_response = client.platform.update_amqp_target_config(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_amqp_target_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterAMQPTargetConfig**](ClusterAMQPTargetConfig.md)| Specifies the parameters to update cluster AMQP target config. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ClusterAMQPTargetConfig**](ClusterAMQPTargetConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_chassis_by_id**
> Chassis update_chassis_by_id(id)

Update a chassis by chassis id.

Update selected properties of chassis info by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.chassis import Chassis
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of chassis.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
body = Chassis(
        id=1,
        hardware_model="hardware_model_example",
        name="name_example",
        serial_number="serial_number_example",
        node_ids=[
            1,
        ],
        rack_id=1,
    ) # Chassis | Specifies the parameters to update chassis. (optional)

# example passing only required values which don't have defaults set
try:
	# Update a chassis by chassis id.
	api_response = client.platform.update_chassis_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_chassis_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update a chassis by chassis id.
	api_response = client.platform.update_chassis_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id, body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_chassis_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of chassis. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **body** | [**Chassis**](Chassis.md)| Specifies the parameters to update chassis. | [optional]

### Return type

[**Chassis**](Chassis.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster**
> Cluster update_cluster(body)

Update a cluster.

Update the Cluster with the given configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.cluster import Cluster
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = Cluster(
        name="name_example",
        description="description_example",
        rigel_cluster_params=RigelClusterConfigParams(
            nodes=[
                RigelClusterNode(
                    node_ip="node_ip_example",
                    node_id=1,
                ),
            ],
            dataplane_endpoint="dataplane_endpoint_example",
        ),
        network_config=ClusterCreateNetworkConfig(
            ntp_servers=[
                "ntp_servers_example",
            ],
            domain_names=[
                "domain_names_example",
            ],
            vip_host_name="vip_host_name_example",
            ip_preference="Ipv4",
            use_dhcp=True,
            dhcp_network_config=ClusterDhcpNetworkConfig(
                dns_servers=[
                    "dns_servers_example",
                ],
            ),
            manual_network_config=ClusterManualNetworkConfig(
                gateway="gateway_example",
                subnet_ip="subnet_ip_example",
                subnet_mask="subnet_mask_example",
                dns_servers=[
                    "dns_servers_example",
                ],
            ),
        ),
        proxy_server_config=ClusterProxyServerConfig(
            ip="ip_example",
            port=1,
            username="username_example",
            password="password_example",
        ),
    ) # Cluster | Specifies the parameters to update cluster.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update a cluster.
	api_response = client.platform.update_cluster(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_cluster: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update a cluster.
	api_response = client.platform.update_cluster(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Cluster**](Cluster.md)| Specifies the parameters to update cluster. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**Cluster**](Cluster.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_feature_flag**
> update_feature_flag(body)

Update feature flag override status.

Update a feature flag override status to cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.update_feature_flag_params import UpdateFeatureFlagParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = UpdateFeatureFlagParams(
        name="name_example",
        is_ui_feature=True,
        is_approved=True,
        reason="reason_example",
        clear=True,
        timestamp=1,
    ) # UpdateFeatureFlagParams | Param for feature flag override request.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update feature flag override status.
	client.platform.update_feature_flag(body)
except ApiException as e:
	print("Exception when calling PlatformApi->update_feature_flag: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update feature flag override status.
	client.platform.update_feature_flag(body, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling PlatformApi->update_feature_flag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateFeatureFlagParams**](UpdateFeatureFlagParams.md)| Param for feature flag override request. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_is_d_maa_s_cluster**
> DMaaSInfo update_is_d_maa_s_cluster(body)

Update whether the cluster is a DMaaS cluster.

Update whether the cluster is a DMaaS cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.d_maa_s_info import DMaaSInfo
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = DMaaSInfo(
        is_dmaas=True,
    ) # DMaaSInfo | Param to update whether the cluster is a DMaaS cluster.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update whether the cluster is a DMaaS cluster.
	api_response = client.platform.update_is_d_maa_s_cluster(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_is_d_maa_s_cluster: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update whether the cluster is a DMaaS cluster.
	api_response = client.platform.update_is_d_maa_s_cluster(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_is_d_maa_s_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DMaaSInfo**](DMaaSInfo.md)| Param to update whether the cluster is a DMaaS cluster. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**DMaaSInfo**](DMaaSInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rack_by_id**
> Rack update_rack_by_id(id)



Update selected properties of a rack given by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.rack import Rack
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of rack.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
body = Rack(
        id=1,
        name="name_example",
        location="location_example",
        chassis_ids=[
            1,
        ],
    ) # Rack | Specifies the parameters to update rack. (optional)

# example passing only required values which don't have defaults set
try:
	api_response = client.platform.update_rack_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_rack_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	api_response = client.platform.update_rack_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id, body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_rack_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of rack. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **body** | [**Rack**](Rack.md)| Specifies the parameters to update rack. | [optional]

### Return type

[**Rack**](Rack.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_racks**
> Racks update_racks(body)

Update racks

Updates list of racks with name, chassis list or/and location

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.racks import Racks
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = Racks(
        racks=[
            Rack(
                id=1,
                name="name_example",
                location="location_example",
                chassis_ids=[
                    1,
                ],
            ),
        ],
    ) # Racks | Specifies the parameters to update racks.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update racks
	api_response = client.platform.update_racks(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_racks: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update racks
	api_response = client.platform.update_racks(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_racks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Racks**](Racks.md)| Specifies the parameters to update racks. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**Racks**](Racks.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_remote_storage_registration**
> RemoteStorageInfo update_remote_storage_registration(id, body)

Update Remote Storage Config

Update Registered Remote Storage Config.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.remote_storage_info import RemoteStorageInfo
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the registration id of the registered remote storage.
body = RemoteStorageInfo() # RemoteStorageInfo | Specifies the parameters to update the registration.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update Remote Storage Config
	api_response = client.platform.update_remote_storage_registration(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_remote_storage_registration: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update Remote Storage Config
	api_response = client.platform.update_remote_storage_registration(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_remote_storage_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the registration id of the registered remote storage. |
 **body** | [**RemoteStorageInfo**](RemoteStorageInfo.md)| Specifies the parameters to update the registration. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**RemoteStorageInfo**](RemoteStorageInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_support_channel_config**
> SupportChannelConfig update_support_channel_config(body)

Update support channel configuration.

Update support channel configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.support_channel_config import SupportChannelConfig
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = SupportChannelConfig(
        is_enabled=True,
        end_time_usecs=1,
    ) # SupportChannelConfig | Specifies the support channel configuration.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update support channel configuration.
	api_response = client.platform.update_support_channel_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_support_channel_config: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update support channel configuration.
	api_response = client.platform.update_support_channel_config(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_support_channel_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupportChannelConfig**](SupportChannelConfig.md)| Specifies the support channel configuration. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**SupportChannelConfig**](SupportChannelConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_syslog_audit_tags**
> SyslogAuditTag update_syslog_audit_tags()

Update cluster audit tags.

Update cluster audit tags.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.syslog_audit_tag import SyslogAuditTag
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
body = SyslogAuditTag(
        cluster_audit="cluster_audit_example",
        filer_audit="filer_audit_example",
        data_protection_events_audit="data_protection_events_audit_example",
        alert_audit="alert_audit_example",
    ) # SyslogAuditTag | Specifies syslog audit tag to update. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update cluster audit tags.
	api_response = client.platform.update_syslog_audit_tags(access_cluster_id=access_cluster_id, region_id=region_id, body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_syslog_audit_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **body** | [**SyslogAuditTag**](SyslogAuditTag.md)| Specifies syslog audit tag to update. | [optional]

### Return type

[**SyslogAuditTag**](SyslogAuditTag.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_syslog_server_by_id**
> SyslogServer update_syslog_server_by_id(id)

Update a syslog server by id.

Update syslog server by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.syslog_server import SyslogServer
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of syslog server.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
body = SyslogServer(
        id=1,
        ip="ip_example",
        port=1,
        protocol="protocol_example",
        name="name_example",
        enabled=True,
        facility_list=[
            "facility_list_example",
        ],
        program_name_list=[
            "program_name_list_example",
        ],
        msg_pattern_list=[
            "msg_pattern_list_example",
        ],
        raw_msg_pattern_list=[
            "raw_msg_pattern_list_example",
        ],
        is_tls_enabled=True,
        ca_certificate="ca_certificate_example",
    ) # SyslogServer | Specifies the body of syslog server body to update. (optional)

# example passing only required values which don't have defaults set
try:
	# Update a syslog server by id.
	api_response = client.platform.update_syslog_server_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_syslog_server_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update a syslog server by id.
	api_response = client.platform.update_syslog_server_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id, body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_syslog_server_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of syslog server. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **body** | [**SyslogServer**](SyslogServer.md)| Specifies the body of syslog server body to update. | [optional]

### Return type

[**SyslogServer**](SyslogServer.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

