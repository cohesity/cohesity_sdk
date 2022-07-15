# cohesity_sdk.PlatformApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**add_remote_disk**](PlatformApi.md#add_remote_disk) | **POST** /disks/remote | Add remote disk
[**add_syslog_server**](PlatformApi.md#add_syslog_server) | **POST** /syslogs | Add Syslog Server
[**clear_smtp_configuration**](PlatformApi.md#clear_smtp_configuration) | **DELETE** /clusters/smtp | Clear SMTP configuration.
[**create_cluster**](PlatformApi.md#create_cluster) | **POST** /clusters | Create a cluster.
[**create_racks**](PlatformApi.md#create_racks) | **POST** /racks | Create racks
[**delete_amqp_target_config**](PlatformApi.md#delete_amqp_target_config) | **DELETE** /clusters/amqp-target-config | Delete AMQP Target Config
[**delete_rack_by_id**](PlatformApi.md#delete_rack_by_id) | **DELETE** /racks/{id} | Delete a rack by id.
[**delete_racks**](PlatformApi.md#delete_racks) | **DELETE** /racks | Delete all the racks.
[**delete_remote_storage_registration**](PlatformApi.md#delete_remote_storage_registration) | **DELETE** /remote-storage/{id} | Delete Remote Storage Registration
[**destroy_cluster**](PlatformApi.md#destroy_cluster) | **DELETE** /clusters | Destroy a cluster.
[**discover_disks**](PlatformApi.md#discover_disks) | **GET** /disks/discover | Discover new disks
[**disk_identify**](PlatformApi.md#disk_identify) | **POST** /disks/identify | Identify a disk
[**disks_assimilate**](PlatformApi.md#disks_assimilate) | **POST** /disks/assimilate | Assimilate disks.
[**expand_cluster_nodes**](PlatformApi.md#expand_cluster_nodes) | **POST** /clusters/nodes | Expand the cluster.
[**get_alert_summary**](PlatformApi.md#get_alert_summary) | **GET** /alertsSummary | Get alerts summary.
[**get_amqp_target_config**](PlatformApi.md#get_amqp_target_config) | **GET** /clusters/amqp-target-config | Get AMQP Target Config
[**get_chassis**](PlatformApi.md#get_chassis) | **GET** /chassis | Get list of chassis
[**get_chassis_by_id**](PlatformApi.md#get_chassis_by_id) | **GET** /chassis/{id} | Get a chassis by chassis id.
[**get_cluster**](PlatformApi.md#get_cluster) | **GET** /clusters | Retrieve Cluster Configuration
[**get_cluster_destroy_hmac**](PlatformApi.md#get_cluster_destroy_hmac) | **GET** /clusters/api-based-fetch-info | Retrieve specific cluster information.
[**get_cluster_operation_status**](PlatformApi.md#get_cluster_operation_status) | **GET** /clusters/operation-status/{operationId} | Get cluster operations status.
[**get_cluster_state**](PlatformApi.md#get_cluster_state) | **GET** /clusters/state | Get cluster state
[**get_network_interfaces**](PlatformApi.md#get_network_interfaces) | **GET** /network-interfaces | Get list of interfaces
[**get_rack_by_id**](PlatformApi.md#get_rack_by_id) | **GET** /racks/{id} | Get a rack by rack id.
[**get_racks**](PlatformApi.md#get_racks) | **GET** /racks | Get list of racks
[**get_registered_remote_storage_list**](PlatformApi.md#get_registered_remote_storage_list) | **GET** /remote-storage | Get Registered Remote Storage Servers List
[**get_remote_disks**](PlatformApi.md#get_remote_disks) | **GET** /disks/remote | Get remote disks
[**get_remote_storage_details**](PlatformApi.md#get_remote_storage_details) | **GET** /remote-storage/{id} | Get remote storage details
[**get_smtp_configuration**](PlatformApi.md#get_smtp_configuration) | **GET** /clusters/smtp | Get SMTP configuration.
[**get_support_channel_config**](PlatformApi.md#get_support_channel_config) | **GET** /support-channel-config | Get support channel configuration.
[**get_supported_syslog_program_names**](PlatformApi.md#get_supported_syslog_program_names) | **GET** /syslogProgramNames | Get supported program names.
[**get_syslog_audit_tags**](PlatformApi.md#get_syslog_audit_tags) | **GET** /syslogAuditTags | Get cluster audit tags.
[**get_syslog_server_by_id**](PlatformApi.md#get_syslog_server_by_id) | **GET** /syslogs/{id} | Get a syslog server by id.
[**get_syslog_server_status_by_id**](PlatformApi.md#get_syslog_server_status_by_id) | **GET** /syslogs/{id}/status | Get a syslog server reachability status.
[**get_syslog_servers**](PlatformApi.md#get_syslog_servers) | **GET** /syslogs | Get list of syslog servers.
[**identify_node**](PlatformApi.md#identify_node) | **POST** /nodes/{id}/identify | Identify node
[**list_disks**](PlatformApi.md#list_disks) | **GET** /disks/local | Get list of disks
[**mark_disk_removal**](PlatformApi.md#mark_disk_removal) | **POST** /disks/{id}/remove | Mark Disk for removal
[**mark_node_removal**](PlatformApi.md#mark_node_removal) | **POST** /nodes/{id}/remove | Mark Node for removal
[**patch_syslog_server_by_id**](PlatformApi.md#patch_syslog_server_by_id) | **PATCH** /syslogs/{id} | Patch a syslog server by id.
[**register_new_remote_storage**](PlatformApi.md#register_new_remote_storage) | **POST** /remote-storage | Register Remote Storage
[**remove_cluster_node**](PlatformApi.md#remove_cluster_node) | **DELETE** /clusters/nodes/{id} | Remove node
[**remove_remote_disk**](PlatformApi.md#remove_remote_disk) | **DELETE** /disks/remote/{id} | Remove remote disk
[**remove_syslog_server**](PlatformApi.md#remove_syslog_server) | **DELETE** /syslogs/{id} | Remove syslog server by id
[**remove_syslog_servers**](PlatformApi.md#remove_syslog_servers) | **DELETE** /syslogs | Remove syslog servers
[**set_node_power**](PlatformApi.md#set_node_power) | **POST** /nodePower | Reboot or shutdown nodes in cluster.
[**update_amqp_target_config**](PlatformApi.md#update_amqp_target_config) | **PUT** /clusters/amqp-target-config | Update AMQP Target Config
[**update_chassis_by_id**](PlatformApi.md#update_chassis_by_id) | **PATCH** /chassis/{id} | Update a chassis by chassis id.
[**update_cluster**](PlatformApi.md#update_cluster) | **PUT** /clusters | Update a cluster.
[**update_cluster_bifrost_config**](PlatformApi.md#update_cluster_bifrost_config) | **PUT** /clusters/bifrost-config | Update cluster Bifrost config.
[**update_rack_by_id**](PlatformApi.md#update_rack_by_id) | **PATCH** /racks/{id} | 
[**update_racks**](PlatformApi.md#update_racks) | **PATCH** /racks | Update racks
[**update_remote_storage_registration**](PlatformApi.md#update_remote_storage_registration) | **PATCH** /remote-storage/{id} | Update Remote Storage Config
[**update_smtp_configuration**](PlatformApi.md#update_smtp_configuration) | **PUT** /clusters/smtp | Update SMTP configuration.
[**update_support_channel_config**](PlatformApi.md#update_support_channel_config) | **PUT** /support-channel-config | Update support channel configuration.
[**update_syslog_audit_tags**](PlatformApi.md#update_syslog_audit_tags) | **POST** /syslogAuditTags | Update cluster audit tags.
[**update_syslog_server_by_id**](PlatformApi.md#update_syslog_server_by_id) | **PUT** /syslogs/{id} | Update a syslog server by id.
[**upgrade_cluster_software**](PlatformApi.md#upgrade_cluster_software) | **PUT** /clusters/upgrade | Upgrade cluster
[**upload_file_package**](PlatformApi.md#upload_file_package) | **POST** /clusters/packages/file | Upload package by file
[**upload_package_by_url**](PlatformApi.md#upload_package_by_url) | **POST** /clusters/packages/url | Upload package by URL
[**validate_smtp_configuration**](PlatformApi.md#validate_smtp_configuration) | **POST** /clusters/smtp/validate | Validate SMTP configuration.


# **add_remote_disk**
> AddRemoteDiskResponseBody add_remote_disk(body)

Add remote disk

Add a remote disk.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.remote_disks import RemoteDisks
from cohesity_sdk.cluster.model.add_remote_disk_response_body import AddRemoteDiskResponseBody
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


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

# example passing only required values which don't have defaults set
try:
	# Add remote disk
	api_response = client.platform.add_remote_disk(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->add_remote_disk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoteDisks**](RemoteDisks.md)| Specifies the remote disk configuration. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.syslog_server import SyslogServer
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


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

# example passing only required values which don't have defaults set
try:
	# Add Syslog Server
	api_response = client.platform.add_syslog_server(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->add_syslog_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SyslogServer**](SyslogServer.md)| Specifies parameters to add syslog server. |

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

# **clear_smtp_configuration**
> clear_smtp_configuration()

Clear SMTP configuration.

Clear cluster SMTP configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Clear SMTP configuration.
	client.platform.clear_smtp_configuration()
except ApiException as e:
	print("Exception when calling PlatformApi->clear_smtp_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **create_cluster**
> Cluster create_cluster(body)

Create a cluster.

Create a cluster with given network and cluster configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.cluster import Cluster
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.create_cluster_params import CreateClusterParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


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

# example passing only required values which don't have defaults set
try:
	# Create a cluster.
	api_response = client.platform.create_cluster(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->create_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateClusterParams**](CreateClusterParams.md)| Specifies the parameters to create cluster. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.racks import Racks
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


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

# example passing only required values which don't have defaults set
try:
	# Create racks
	api_response = client.platform.create_racks(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->create_racks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Racks**](Racks.md)| Specifies the parameters to create racks. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Delete AMQP Target Config
	client.platform.delete_amqp_target_config()
except ApiException as e:
	print("Exception when calling PlatformApi->delete_amqp_target_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "id_example" # str | Specifies a unique id of the rack.

# example passing only required values which don't have defaults set
try:
	# Delete a rack by id.
	client.platform.delete_rack_by_id(id)
except ApiException as e:
	print("Exception when calling PlatformApi->delete_rack_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the rack. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Delete all the racks.
	client.platform.delete_racks()
except ApiException as e:
	print("Exception when calling PlatformApi->delete_racks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the registration id of the registered remote storage.

# example passing only required values which don't have defaults set
try:
	# Delete Remote Storage Registration
	client.platform.delete_remote_storage_registration(id)
except ApiException as e:
	print("Exception when calling PlatformApi->delete_remote_storage_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the registration id of the registered remote storage. |

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

# **destroy_cluster**
> ClusterOperationResponseParams destroy_cluster()

Destroy a cluster.

Destroy a cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_operation_response_params import ClusterOperationResponseParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Destroy a cluster.
	api_response = client.platform.destroy_cluster()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->destroy_cluster: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterOperationResponseParams**](ClusterOperationResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_disks**
> ClusterFreeDisks discover_disks()

Discover new disks

Discover disks that are ready for activation

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_free_disks import ClusterFreeDisks
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Discover new disks
	api_response = client.platform.discover_disks()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->discover_disks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.disk_identify import DiskIdentify
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = DiskIdentify(
        node_id=1,
        serial_number="serial_number_example",
        identify=True,
    ) # DiskIdentify | Specifies the parameter to identify disk.

# example passing only required values which don't have defaults set
try:
	# Identify a disk
	api_response = client.platform.disk_identify(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->disk_identify: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DiskIdentify**](DiskIdentify.md)| Specifies the parameter to identify disk. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_free_disks import ClusterFreeDisks
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


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

# example passing only required values which don't have defaults set
try:
	# Assimilate disks.
	api_response = client.platform.disks_assimilate(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->disks_assimilate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterFreeDisks**](ClusterFreeDisks.md)| Specifies the parameter to assimilate disks. |

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

# **expand_cluster_nodes**
> ClusterOperationResponseParams expand_cluster_nodes(body)

Expand the cluster.

Expand the cluster by adding new nodes.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.cluster_expand_params import ClusterExpandParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_operation_response_params import ClusterOperationResponseParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ClusterExpandParams(
        type="Physical",
        cloud_cluster_params=CloudClusterExpandParams(
            node_ips=[
                "node_ips_example",
            ],
        ),
        physical_cluster_params=PhysicalClusterExpandParams(
            vips=[
                "vips_example",
            ],
            node_configs=[
                PhysicalNodeConfigParams(
                    id=1,
                    ip="ip_example",
                    is_compute_node=True,
                    ipmi_ip="ipmi_ip_example",
                ),
            ],
            chassis_rack_configs=[
                ChassisRackConfigParams(
                    chassis_serial="chassis_serial_example",
                    rack_id=1,
                ),
            ],
        ),
    ) # ClusterExpandParams | Specifies the parameters to expand the cluster.

# example passing only required values which don't have defaults set
try:
	# Expand the cluster.
	api_response = client.platform.expand_cluster_nodes(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->expand_cluster_nodes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterExpandParams**](ClusterExpandParams.md)| Specifies the parameters to expand the cluster. |

### Return type

[**ClusterOperationResponseParams**](ClusterOperationResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_summary**
> AlertsSummaryResponse get_alert_summary()

Get alerts summary.

Get alerts summary grouped by category.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.alerts_summary_response import AlertsSummaryResponse
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


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
	api_response = client.platform.get_alert_summary(start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, include_tenants=include_tenants, tenant_ids=tenant_ids, states_list=states_list)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_alert_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_amqp_target_config import ClusterAMQPTargetConfig
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get AMQP Target Config
	api_response = client.platform.get_amqp_target_config()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_amqp_target_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.chassis_list import ChassisList
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


no_rack_assigned = True # bool | Filters chassis that have no rack assigned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get list of chassis
	api_response = client.platform.get_chassis(no_rack_assigned=no_rack_assigned)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_chassis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.chassis import Chassis
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of chassis.

# example passing only required values which don't have defaults set
try:
	# Get a chassis by chassis id.
	api_response = client.platform.get_chassis_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_chassis_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of chassis. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.cluster import Cluster
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Retrieve Cluster Configuration
	api_response = client.platform.get_cluster()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_cluster_destroy_hmac**
> ApiBasedFetchInfo get_cluster_destroy_hmac()

Retrieve specific cluster information.

Fetch info regarding cluster to perform certain api based operations.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.api_based_fetch_info import ApiBasedFetchInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Retrieve specific cluster information.
	api_response = client.platform.get_cluster_destroy_hmac()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster_destroy_hmac: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiBasedFetchInfo**](ApiBasedFetchInfo.md)

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

# **get_cluster_operation_status**
> ClusterOperationStatus get_cluster_operation_status(operation_id)

Get cluster operations status.

Get cluster operations status information.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_operation_status import ClusterOperationStatus
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


operation_id = 1 # int | The operation id.

# example passing only required values which don't have defaults set
try:
	# Get cluster operations status.
	api_response = client.platform.get_cluster_operation_status(operation_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster_operation_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_id** | **int**| The operation id. |

### Return type

[**ClusterOperationStatus**](ClusterOperationStatus.md)

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

# **get_cluster_state**
> ClusterStateParams get_cluster_state()

Get cluster state

Get the current state of the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.cluster_state_params import ClusterStateParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


system_apps = True # bool | The filter whether or not to get the system apps state details. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get cluster state
	api_response = client.platform.get_cluster_state(system_apps=system_apps)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_apps** | **bool**| The filter whether or not to get the system apps state details. | [optional]

### Return type

[**ClusterStateParams**](ClusterStateParams.md)

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_interfaces import ClusterInterfaces
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get list of interfaces
	api_response = client.platform.get_network_interfaces()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_network_interfaces: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.rack import Rack
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of rack.

# example passing only required values which don't have defaults set
try:
	# Get a rack by rack id.
	api_response = client.platform.get_rack_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_rack_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of rack. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.racks import Racks
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get list of racks
	api_response = client.platform.get_racks()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_racks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.registered_remote_storage_list import RegisteredRemoteStorageList
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get Registered Remote Storage Servers List
	api_response = client.platform.get_registered_remote_storage_list()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_registered_remote_storage_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.remote_disks import RemoteDisks
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


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
	api_response = client.platform.get_remote_disks(disk_ids=disk_ids, node_ids=node_ids, tiers=tiers, mount_path=mount_path, file_system=file_system)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_remote_disks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.remote_storage_info import RemoteStorageInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the registered remote storage.
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
	api_response = client.platform.get_remote_storage_details(id, include_available_space=include_available_space, include_available_data_vips=include_available_data_vips, include_array_info=include_array_info)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_remote_storage_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the registered remote storage. |
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

# **get_smtp_configuration**
> SMTPConfiguration get_smtp_configuration()

Get SMTP configuration.

Get the SMTP cluster configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.smtp_configuration import SMTPConfiguration
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get SMTP configuration.
	api_response = client.platform.get_smtp_configuration()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_smtp_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SMTPConfiguration**](SMTPConfiguration.md)

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.support_channel_config import SupportChannelConfig
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get support channel configuration.
	api_response = client.platform.get_support_channel_config()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_support_channel_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get supported program names.
	api_response = client.platform.get_supported_syslog_program_names()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_supported_syslog_program_names: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.syslog_audit_tag import SyslogAuditTag
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get cluster audit tags.
	api_response = client.platform.get_syslog_audit_tags()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_syslog_audit_tags: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.syslog_server import SyslogServer
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of syslog server.

# example passing only required values which don't have defaults set
try:
	# Get a syslog server by id.
	api_response = client.platform.get_syslog_server_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_syslog_server_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of syslog server. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.syslog_server_status import SyslogServerStatus
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of syslog server.

# example passing only required values which don't have defaults set
try:
	# Get a syslog server reachability status.
	api_response = client.platform.get_syslog_server_status_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_syslog_server_status_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of syslog server. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.syslog_servers import SyslogServers
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get list of syslog servers.
	api_response = client.platform.get_syslog_servers()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_syslog_servers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.node_identify_params import NodeIdentifyParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies id of node to identify.
body = NodeIdentifyParams(
        identify=True,
    ) # NodeIdentifyParams | Specifies the parameter to identify node.

# example passing only required values which don't have defaults set
try:
	# Identify node
	api_response = client.platform.identify_node(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->identify_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of node to identify. |
 **body** | [**NodeIdentifyParams**](NodeIdentifyParams.md)| Specifies the parameter to identify node. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.disks_list import DisksList
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


node_id = 1 # int | Specifies node id of the node to get list of disks (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get list of disks
	api_response = client.platform.list_disks(node_id=node_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->list_disks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **mark_disk_removal**
> RemoveDisk mark_disk_removal(id, body)

Mark Disk for removal

Mark disk for removal or cancel removal if a disk is already marked for removal.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.remove_disk import RemoveDisk
from cohesity_sdk.cluster.model.disk_removal_params import DiskRemovalParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies unique id of the disk to mark for removal.
body = DiskRemovalParams(
        cancel=True,
    ) # DiskRemovalParams | Specifies parameters to mark/cancel disk removal.

# example passing only required values which don't have defaults set
try:
	# Mark Disk for removal
	api_response = client.platform.mark_disk_removal(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->mark_disk_removal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies unique id of the disk to mark for removal. |
 **body** | [**DiskRemovalParams**](DiskRemovalParams.md)| Specifies parameters to mark/cancel disk removal. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.node_removal_params import NodeRemovalParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.remove_node import RemoveNode
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies id of node to cancel removal.
body = NodeRemovalParams(
        cancel=True,
        is_offline=False,
    ) # NodeRemovalParams | Specifies parameters to initiate/cancel node removal .

# example passing only required values which don't have defaults set
try:
	# Mark Node for removal
	api_response = client.platform.mark_node_removal(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->mark_node_removal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of node to cancel removal. |
 **body** | [**NodeRemovalParams**](NodeRemovalParams.md)| Specifies parameters to initiate/cancel node removal . |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.syslog_server import SyslogServer
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of syslog server.
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
	api_response = client.platform.patch_syslog_server_by_id(id, body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->patch_syslog_server_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of syslog server. |
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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.remote_storage_info import RemoteStorageInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = RemoteStorageInfo() # RemoteStorageInfo | Specifies the parameters to register a remote storage management server.

# example passing only required values which don't have defaults set
try:
	# Register Remote Storage
	api_response = client.platform.register_new_remote_storage(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->register_new_remote_storage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoteStorageInfo**](RemoteStorageInfo.md)| Specifies the parameters to register a remote storage management server. |

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

# **remove_cluster_node**
> ClusterOperationResponseParams remove_cluster_node(id)

Remove node

Remove a node from the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_operation_response_params import ClusterOperationResponseParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Id of the node.

# example passing only required values which don't have defaults set
try:
	# Remove node
	api_response = client.platform.remove_cluster_node(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->remove_cluster_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the node. |

### Return type

[**ClusterOperationResponseParams**](ClusterOperationResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_remote_disk**
> remove_remote_disk(id)

Remove remote disk

Remove a remote disk.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the remote disk to remove.

# example passing only required values which don't have defaults set
try:
	# Remove remote disk
	client.platform.remove_remote_disk(id)
except ApiException as e:
	print("Exception when calling PlatformApi->remove_remote_disk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the remote disk to remove. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies a unique id of the syslog server.

# example passing only required values which don't have defaults set
try:
	# Remove syslog server by id
	client.platform.remove_syslog_server(id)
except ApiException as e:
	print("Exception when calling PlatformApi->remove_syslog_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the syslog server. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Remove syslog servers
	client.platform.remove_syslog_servers()
except ApiException as e:
	print("Exception when calling PlatformApi->remove_syslog_servers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.node_power_operation import NodePowerOperation
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = NodePowerOperation(
        operation="poweroff",
        node_id=1,
    ) # NodePowerOperation | Specifies the reboot or shutdown operation.

# example passing only required values which don't have defaults set
try:
	# Reboot or shutdown nodes in cluster.
	client.platform.set_node_power(body)
except ApiException as e:
	print("Exception when calling PlatformApi->set_node_power: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodePowerOperation**](NodePowerOperation.md)| Specifies the reboot or shutdown operation. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_amqp_target_config import ClusterAMQPTargetConfig
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ClusterAMQPTargetConfig(
        server_ip="server_ip_example",
        username="username_example",
        password="password_example",
        virtual_host="virtual_host_example",
        exchange="exchange_example",
        filer_id=1,
        certificate="certificate_example",
    ) # ClusterAMQPTargetConfig | Specifies the parameters to update cluster AMQP target config.

# example passing only required values which don't have defaults set
try:
	# Update AMQP Target Config
	api_response = client.platform.update_amqp_target_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_amqp_target_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterAMQPTargetConfig**](ClusterAMQPTargetConfig.md)| Specifies the parameters to update cluster AMQP target config. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.chassis import Chassis
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of chassis.
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
	api_response = client.platform.update_chassis_by_id(id, body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_chassis_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of chassis. |
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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.cluster import Cluster
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


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

# example passing only required values which don't have defaults set
try:
	# Update a cluster.
	api_response = client.platform.update_cluster(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Cluster**](Cluster.md)| Specifies the parameters to update cluster. |

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

# **update_cluster_bifrost_config**
> McmRigelClaimResponseParams update_cluster_bifrost_config(body)

Update cluster Bifrost config.

Update cluster Bifrost config.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.mcm_rigel_claim_response_params import McmRigelClaimResponseParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = McmRigelClaimResponseParams(
        rigel_guid=1,
        connection_id=1,
        tenant_id="tenant_id_example",
        rigel_type="OnPrem",
        rigel_certificate="rigel_certificate_example",
        rigel_private_key="rigel_private_key_example",
        rigel_ca_chain="rigel_ca_chain_example",
        tenant_ca_chain=[
            "tenant_ca_chain_example",
        ],
        helios_certificate="helios_certificate_example",
        dataplane_endpoint="dataplane_endpoint_example",
        region_id="region_id_example",
    ) # McmRigelClaimResponseParams | Specifies the request to update Bifrost config.

# example passing only required values which don't have defaults set
try:
	# Update cluster Bifrost config.
	api_response = client.platform.update_cluster_bifrost_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_cluster_bifrost_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**McmRigelClaimResponseParams**](McmRigelClaimResponseParams.md)| Specifies the request to update Bifrost config. |

### Return type

[**McmRigelClaimResponseParams**](McmRigelClaimResponseParams.md)

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.rack import Rack
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of rack.
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
	api_response = client.platform.update_rack_by_id(id, body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_rack_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of rack. |
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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.racks import Racks
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


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

# example passing only required values which don't have defaults set
try:
	# Update racks
	api_response = client.platform.update_racks(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_racks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Racks**](Racks.md)| Specifies the parameters to update racks. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.remote_storage_info import RemoteStorageInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the registration id of the registered remote storage.
body = RemoteStorageInfo() # RemoteStorageInfo | Specifies the parameters to update the registration.

# example passing only required values which don't have defaults set
try:
	# Update Remote Storage Config
	api_response = client.platform.update_remote_storage_registration(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_remote_storage_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the registration id of the registered remote storage. |
 **body** | [**RemoteStorageInfo**](RemoteStorageInfo.md)| Specifies the parameters to update the registration. |

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

# **update_smtp_configuration**
> SMTPConfiguration update_smtp_configuration(body)

Update SMTP configuration.

Update SMTP configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.smtp_configuration import SMTPConfiguration
from cohesity_sdk.cluster.model.update_smtp_params import UpdateSMTPParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = UpdateSMTPParams() # UpdateSMTPParams | Specifies the parameters to update cluster SMTP configuration.

# example passing only required values which don't have defaults set
try:
	# Update SMTP configuration.
	api_response = client.platform.update_smtp_configuration(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_smtp_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSMTPParams**](UpdateSMTPParams.md)| Specifies the parameters to update cluster SMTP configuration. |

### Return type

[**SMTPConfiguration**](SMTPConfiguration.md)

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.support_channel_config import SupportChannelConfig
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = SupportChannelConfig(
        is_enabled=True,
        end_time_usecs=1,
    ) # SupportChannelConfig | Specifies the support channel configuration.

# example passing only required values which don't have defaults set
try:
	# Update support channel configuration.
	api_response = client.platform.update_support_channel_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_support_channel_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupportChannelConfig**](SupportChannelConfig.md)| Specifies the support channel configuration. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.syslog_audit_tag import SyslogAuditTag
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


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
	api_response = client.platform.update_syslog_audit_tags(body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_syslog_audit_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.syslog_server import SyslogServer
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of syslog server.
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
	api_response = client.platform.update_syslog_server_by_id(id, body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_syslog_server_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of syslog server. |
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

# **upgrade_cluster_software**
> ClusterOperationResponseParams upgrade_cluster_software(body)

Upgrade cluster

Upgrade the software on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_uprade_params import ClusterUpradeParams
from cohesity_sdk.cluster.model.cluster_operation_response_params import ClusterOperationResponseParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ClusterUpradeParams(
        type="Upgrade",
        software_version="software_version_example",
        url="url_example",
    ) # ClusterUpradeParams | The parameters to upgrade the software on the cluster.

# example passing only required values which don't have defaults set
try:
	# Upgrade cluster
	api_response = client.platform.upgrade_cluster_software(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->upgrade_cluster_software: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterUpradeParams**](ClusterUpradeParams.md)| The parameters to upgrade the software on the cluster. |

### Return type

[**ClusterOperationResponseParams**](ClusterOperationResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_package**
> upload_file_package(package_file)

Upload package by file

Upload a package file to the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


package_file = open('/path/to/file', 'rb') # file_type | Package to be uploaded to the cluster.

# example passing only required values which don't have defaults set
try:
	# Upload package by file
	client.platform.upload_file_package(package_file)
except ApiException as e:
	print("Exception when calling PlatformApi->upload_file_package: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_file** | **file_type**| Package to be uploaded to the cluster. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_package_by_url**
> ClusterOperationResponseParams upload_package_by_url(body)

Upload package by URL

Upload a package to the cluster by providing the URL where the package is hosted.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.upload_package_url_params import UploadPackageUrlParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_operation_response_params import ClusterOperationResponseParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = UploadPackageUrlParams(
        url="url_example",
    ) # UploadPackageUrlParams | Parameters to upload a package by URL.

# example passing only required values which don't have defaults set
try:
	# Upload package by URL
	api_response = client.platform.upload_package_by_url(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->upload_package_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UploadPackageUrlParams**](UploadPackageUrlParams.md)| Parameters to upload a package by URL. |

### Return type

[**ClusterOperationResponseParams**](ClusterOperationResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_smtp_configuration**
> validate_smtp_configuration(body)

Validate SMTP configuration.

Validate SMTP configuration by sending a test email.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.test_smtp_config import TestSMTPConfig
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = TestSMTPConfig(
        email="email_example",
    ) # TestSMTPConfig | Specifies the request parameters to validate SMTP configuration.

# example passing only required values which don't have defaults set
try:
	# Validate SMTP configuration.
	client.platform.validate_smtp_configuration(body)
except ApiException as e:
	print("Exception when calling PlatformApi->validate_smtp_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TestSMTPConfig**](TestSMTPConfig.md)| Specifies the request parameters to validate SMTP configuration. |

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

