# cohesity_sdk.PlatformApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**add_hosts**](PlatformApi.md#add_hosts) | **POST** /clusters/host-mappings | Create Cluster Host Mappings
[**add_remote_disk**](PlatformApi.md#add_remote_disk) | **POST** /disks/remote | Add remote disk
[**clear_smtp_configuration**](PlatformApi.md#clear_smtp_configuration) | **DELETE** /clusters/smtp | Clear SMTP configuration.
[**create_cluster**](PlatformApi.md#create_cluster) | **POST** /clusters | Create a cluster.
[**create_cluster_vlan**](PlatformApi.md#create_cluster_vlan) | **POST** /network/vlans | Create vlan
[**create_interface_group**](PlatformApi.md#create_interface_group) | **POST** /network/interface-groups | Create interface group
[**create_racks**](PlatformApi.md#create_racks) | **POST** /racks | Create racks
[**delete_amqp_target_config**](PlatformApi.md#delete_amqp_target_config) | **DELETE** /clusters/amqp-target-config | Delete AMQP Target Config
[**delete_cluster_package**](PlatformApi.md#delete_cluster_package) | **DELETE** /clusters/packages/{versionName} | Delete package
[**delete_cluster_snapshot_policy**](PlatformApi.md#delete_cluster_snapshot_policy) | **DELETE** /clusters/snapshot-policy | Delete cluster snapshot policy.
[**delete_cluster_vlan**](PlatformApi.md#delete_cluster_vlan) | **DELETE** /network/vlans/{interfaceName} | Delete vlan
[**delete_hosts**](PlatformApi.md#delete_hosts) | **POST** /clusters/host-mappings/delete | Deletes multiple Host Mappings within the cluster
[**delete_interface_group**](PlatformApi.md#delete_interface_group) | **DELETE** /network/interface-groups/{id} | Delete interface group
[**delete_ipmi_user**](PlatformApi.md#delete_ipmi_user) | **DELETE** /ipmi/users | To delete IPMI User for node
[**delete_rack_by_id**](PlatformApi.md#delete_rack_by_id) | **DELETE** /racks/{id} | Delete a rack by id.
[**delete_racks**](PlatformApi.md#delete_racks) | **DELETE** /racks | Delete all the racks.
[**discover_disks**](PlatformApi.md#discover_disks) | **GET** /disks/discover | Discover new disks
[**disk_identify**](PlatformApi.md#disk_identify) | **POST** /disks/identify | Identify a disk
[**disks_assimilate**](PlatformApi.md#disks_assimilate) | **POST** /disks/assimilate | Assimilate disks.
[**expand_cluster_nodes**](PlatformApi.md#expand_cluster_nodes) | **POST** /clusters/nodes | Expand the cluster.
[**get_amqp_target_config**](PlatformApi.md#get_amqp_target_config) | **GET** /clusters/amqp-target-config | Get AMQP Target Config
[**get_chassis**](PlatformApi.md#get_chassis) | **GET** /chassis | Get list of chassis
[**get_chassis_by_id**](PlatformApi.md#get_chassis_by_id) | **GET** /chassis/{id} | Get a chassis by chassis id.
[**get_cluster**](PlatformApi.md#get_cluster) | **GET** /clusters | Retrieve Cluster Configuration
[**get_cluster_local_domain_sid**](PlatformApi.md#get_cluster_local_domain_sid) | **GET** /clusters/local-domain-sid | Get Cluster Local Domain SID
[**get_cluster_packages**](PlatformApi.md#get_cluster_packages) | **GET** /clusters/packages | Get packages
[**get_cluster_snapshot_policy**](PlatformApi.md#get_cluster_snapshot_policy) | **GET** /clusters/snapshot-policy | Get cluster snapshot policy.
[**get_cluster_state**](PlatformApi.md#get_cluster_state) | **GET** /clusters/state | Get cluster state
[**get_cluster_vlans**](PlatformApi.md#get_cluster_vlans) | **GET** /network/vlans | Get vlans
[**get_interface_groups**](PlatformApi.md#get_interface_groups) | **GET** /network/interface-groups | Get interface groups
[**get_interfaces**](PlatformApi.md#get_interfaces) | **GET** /network/interfaces | Get interfaces
[**get_is_d_maa_s_cluster**](PlatformApi.md#get_is_d_maa_s_cluster) | **GET** /clusters/is-dmaas | Get whether the cluster is a DMaaS cluster.
[**get_network_interfaces**](PlatformApi.md#get_network_interfaces) | **GET** /network-interfaces | Get list of interfaces
[**get_nodes**](PlatformApi.md#get_nodes) | **GET** /clusters/nodes | List Nodes of the cluster.
[**get_rack_by_id**](PlatformApi.md#get_rack_by_id) | **GET** /racks/{id} | Get a rack by rack id.
[**get_racks**](PlatformApi.md#get_racks) | **GET** /racks | Get list of racks
[**get_remote_disks**](PlatformApi.md#get_remote_disks) | **GET** /disks/remote | Get remote disks
[**get_smtp_configuration**](PlatformApi.md#get_smtp_configuration) | **GET** /clusters/smtp | Get SMTP configuration.
[**get_support_channel_config**](PlatformApi.md#get_support_channel_config) | **GET** /support-channel-config | Get support channel configuration.
[**identify_node**](PlatformApi.md#identify_node) | **POST** /nodes/{id}/identify | Identify node
[**import_crl_file**](PlatformApi.md#import_crl_file) | **PUT** /clusters/import-crl-file | Import Crl File
[**list_disks**](PlatformApi.md#list_disks) | **GET** /disks/local | Get list of disks
[**list_feature_flag**](PlatformApi.md#list_feature_flag) | **GET** /clusters/feature-flag | Get feature flag overrides list.
[**list_free_nodes**](PlatformApi.md#list_free_nodes) | **GET** /clusters/nodes/free | List the free Cohesity Nodes present on a network.
[**list_hosts**](PlatformApi.md#list_hosts) | **GET** /clusters/host-mappings | List Host Mappings
[**mark_baseos_upgrade**](PlatformApi.md#mark_baseos_upgrade) | **PUT** /clusters/baseos-upgrade | Sets/clears the BaseOS upgrade cluster operation.
[**mark_disk_removal**](PlatformApi.md#mark_disk_removal) | **POST** /disks/{id}/remove | Mark Disk for removal
[**mark_node_removal**](PlatformApi.md#mark_node_removal) | **POST** /nodes/{id}/remove | Mark Node for removal
[**node_information**](PlatformApi.md#node_information) | **GET** /nodes | Fetch Node General Information
[**public_key_request**](PlatformApi.md#public_key_request) | **POST** /clusters/ssh-public-key | Get the SSH public key.
[**remove_remote_disk**](PlatformApi.md#remove_remote_disk) | **DELETE** /disks/remote/{id} | Remove remote disk
[**set_node_power**](PlatformApi.md#set_node_power) | **POST** /node-power | Reboot or shutdown nodes in cluster.
[**update_airgap_config**](PlatformApi.md#update_airgap_config) | **PUT** /clusters/airgap | Update Airgap config
[**update_amqp_target_config**](PlatformApi.md#update_amqp_target_config) | **PUT** /clusters/amqp-target-config | Update AMQP Target Config
[**update_chassis_by_id**](PlatformApi.md#update_chassis_by_id) | **PATCH** /chassis/{id} | Update a chassis by chassis id.
[**update_cluster**](PlatformApi.md#update_cluster) | **PUT** /clusters | Update a cluster.
[**update_cluster_snapshot_policy**](PlatformApi.md#update_cluster_snapshot_policy) | **PUT** /clusters/snapshot-policy | Update cluster snapshot policy.
[**update_cluster_vlan**](PlatformApi.md#update_cluster_vlan) | **PUT** /network/vlans/{interfaceName} | Update vlan
[**update_feature_flag**](PlatformApi.md#update_feature_flag) | **PUT** /clusters/feature-flag | Update feature flag override status.
[**update_hosts**](PlatformApi.md#update_hosts) | **PUT** /clusters/host-mappings | Update Host Mappings
[**update_interface**](PlatformApi.md#update_interface) | **PUT** /network/interfaces/{id} | Update interface
[**update_interface_group**](PlatformApi.md#update_interface_group) | **PUT** /network/interface-groups/{id} | Update interface group
[**update_is_d_maa_s_cluster**](PlatformApi.md#update_is_d_maa_s_cluster) | **PUT** /clusters/is-dmaas | Update whether the cluster is a DMaaS cluster.
[**update_rack_by_id**](PlatformApi.md#update_rack_by_id) | **PATCH** /racks/{id} | 
[**update_racks**](PlatformApi.md#update_racks) | **PATCH** /racks | Update racks
[**update_smtp_configuration**](PlatformApi.md#update_smtp_configuration) | **PUT** /clusters/smtp | Update SMTP configuration.
[**update_support_channel_config**](PlatformApi.md#update_support_channel_config) | **PUT** /support-channel-config | Update support channel configuration.
[**upgrade_check_get_results**](PlatformApi.md#upgrade_check_get_results) | **GET** /cluster/upgrade-checks/{testRunInstanceId} | Get upgrade checks results.
[**upgrade_check_run_tests**](PlatformApi.md#upgrade_check_run_tests) | **PUT** /cluster/upgrade-checks | Run upgrade checks on cluster.
[**upgrade_cluster_software**](PlatformApi.md#upgrade_cluster_software) | **PUT** /clusters/upgrade | Upgrade cluster
[**upload_package_by_url**](PlatformApi.md#upload_package_by_url) | **POST** /clusters/packages/url | Upload package by URL
[**validate_smtp_configuration**](PlatformApi.md#validate_smtp_configuration) | **POST** /clusters/smtp/validate | Validate SMTP configuration.


# **add_hosts**
> HostMappings add_hosts(body)

Create Cluster Host Mappings

Sends a request to add one or more new entries to the Cluster's /etc/hosts

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.host_mappings_parameters import HostMappingsParameters
from cohesity_sdk.cluster.model.host_mappings import HostMappings
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = HostMappingsParameters([
        HostEntry(
            description="description_example",
            domain_names=[
                "domain_names_example",
            ],
            ip="ip_example",
        ),
    ]) # HostMappingsParameters | Specifies the request to add entries to /etc/hosts

# example passing only required values which don't have defaults set
try:
	# Create Cluster Host Mappings
	api_response = client.platform.add_hosts(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->add_hosts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostMappingsParameters**](HostMappingsParameters.md)| Specifies the request to add entries to /etc/hosts |

### Return type

[**HostMappings**](HostMappings.md)

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

# **add_remote_disk**
> AddRemoteDiskResponseBody add_remote_disk(body)

Add remote disk

Add a remote disk.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.remote_disks import RemoteDisks
from cohesity_sdk.cluster.model.add_remote_disk_response_body import AddRemoteDiskResponseBody
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = RemoteDisks(
        remote_disks=[
            RemoteDisk(
                data_vip="data_vip_example",
                file_system_name="file_system_name_example",
                mount_path="mount_path_example",
                node_id=1,
                node_ip="node_ip_example",
                tier="PCIeSSD",
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

# **clear_smtp_configuration**
> clear_smtp_configuration()

Clear SMTP configuration.

Clear cluster SMTP configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.cluster import Cluster
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.create_cluster_params import CreateClusterParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateClusterParams(
        cloud_cluster_params=ClusterCreateCloudParams(
            node_ips=[
                "node_ips_example",
            ],
        ),
        enable_encryption=True,
        name="name_example",
        network_config=ClusterCreateNetworkConfig(
            dhcp_network_config=ClusterDhcpNetworkConfig(
                dns_servers=[
                    "dns_servers_example",
                ],
            ),
            domain_names=[
                "domain_names_example",
            ],
            ip_preference="Ipv4",
            manual_network_config=ClusterManualNetworkConfig(
                dns_servers=[
                    "dns_servers_example",
                ],
                gateway="gateway_example",
                subnet_ip="subnet_ip_example",
                subnet_mask="subnet_mask_example",
            ),
            ntp_servers=[
                "ntp_servers_example",
            ],
            secondary_dhcp_network_config=ClusterDhcpNetworkConfig(
                dns_servers=[
                    "dns_servers_example",
                ],
            ),
            secondary_manual_network_config=ClusterManualNetworkConfig(
                dns_servers=[
                    "dns_servers_example",
                ],
                gateway="gateway_example",
                subnet_ip="subnet_ip_example",
                subnet_mask="subnet_mask_example",
            ),
            use_dhcp=True,
            vip_host_name="vip_host_name_example",
        ),
        physical_cluster_params=ClusterCreatePhysicalParams(
            nodes=[
                ClusterCreateNodeParams(
                    node_id=1,
                    node_ip="node_ip_example",
                ),
            ],
        ),
        proxy_server_config=ClusterProxyServerConfig(
            ip="ip_example",
            is_disabled=True,
            password="password_example",
            port=1,
            username="username_example",
        ),
        rigel_cluster_params=ClusterCreateRigelParams(
            claim_token="claim_token_example",
            nodes=[
                RigelClusterNode(
                    node_id=1,
                    node_ip="node_ip_example",
                    secondary_node_ip="secondary_node_ip_example",
                ),
            ],
        ),
        type="Physical",
        virtual_cluster_params=ClusterCreateVirtualParams(
            nodes=[
                ClusterCreateNodeParams(
                    node_id=1,
                    node_ip="node_ip_example",
                ),
            ],
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

# **create_cluster_vlan**
> ClusterVlanParams create_cluster_vlan(body)

Create vlan

Create a vlan on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_vlan_params import ClusterVlanParams
from cohesity_sdk.cluster.model.create_cluster_vlan_params import CreateClusterVlanParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateClusterVlanParams() # CreateClusterVlanParams | Parameters to create a vlan.

# example passing only required values which don't have defaults set
try:
	# Create vlan
	api_response = client.platform.create_cluster_vlan(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->create_cluster_vlan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateClusterVlanParams**](CreateClusterVlanParams.md)| Parameters to create a vlan. |

### Return type

[**ClusterVlanParams**](ClusterVlanParams.md)

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

# **create_interface_group**
> InterfaceGroup create_interface_group(body)

Create interface group

Create an interface group on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.interface_group import InterfaceGroup
from cohesity_sdk.cluster.model.interface_group_params import InterfaceGroupParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = InterfaceGroupParams(
        name="name_example",
        network_params=InterfaceGroupNetworkParams(
            bond_interface_params=BondInterfaceNetworkParams(
                bonding_mode="ActiveBackup",
                lacp_rate="Slow",
                xmit_hash_policy="layer2",
            ),
            mtu=1,
        ),
        node_interface_params=[
            NodeInterfaceParams(
                interface_name="interface_name_example",
                node_id=1,
            ),
        ],
        type="Bond",
    ) # InterfaceGroupParams | Parameters to create an interface group.

# example passing only required values which don't have defaults set
try:
	# Create interface group
	api_response = client.platform.create_interface_group(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->create_interface_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InterfaceGroupParams**](InterfaceGroupParams.md)| Parameters to create an interface group. |

### Return type

[**InterfaceGroup**](InterfaceGroup.md)

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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.racks import Racks
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = Racks(
        racks=[
            Rack(
                chassis_ids=[
                    1,
                ],
                id=1,
                location="location_example",
                name="name_example",
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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

# **delete_cluster_package**
> ClusterOperationResponseParams delete_cluster_package(version_name)

Delete package

Delete a software package on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_operation_response_params import ClusterOperationResponseParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


version_name = "versionName_example" # str | Version name of the package. Example: 6.3.1h_release-20210714_0fad884e

# example passing only required values which don't have defaults set
try:
	# Delete package
	api_response = client.platform.delete_cluster_package(version_name)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->delete_cluster_package: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_name** | **str**| Version name of the package. Example: 6.3.1h_release-20210714_0fad884e |

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

# **delete_cluster_snapshot_policy**
> delete_cluster_snapshot_policy()

Delete cluster snapshot policy.

Delete cluster snapshot policy.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Delete cluster snapshot policy.
	client.platform.delete_cluster_snapshot_policy()
except ApiException as e:
	print("Exception when calling PlatformApi->delete_cluster_snapshot_policy: %s\n" % e)
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

# **delete_cluster_vlan**
> delete_cluster_vlan(interface_name)

Delete vlan

Delete a vlan on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


interface_name = "interfaceName_example" # str | Vlan interface name, it should be in interface_group_name.vlan_id format.

# example passing only required values which don't have defaults set
try:
	# Delete vlan
	client.platform.delete_cluster_vlan(interface_name)
except ApiException as e:
	print("Exception when calling PlatformApi->delete_cluster_vlan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_name** | **str**| Vlan interface name, it should be in interface_group_name.vlan_id format. |

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

# **delete_hosts**
> delete_hosts(body)

Deletes multiple Host Mappings within the cluster

Delete one or more Host Mappings within the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.delete_hosts_parameters import DeleteHostsParameters
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = DeleteHostsParameters(
        ips=[
            "ips_example",
        ],
    ) # DeleteHostsParameters | Specifies the params to delete host mappings

# example passing only required values which don't have defaults set
try:
	# Deletes multiple Host Mappings within the cluster
	client.platform.delete_hosts(body)
except ApiException as e:
	print("Exception when calling PlatformApi->delete_hosts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteHostsParameters**](DeleteHostsParameters.md)| Specifies the params to delete host mappings |

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

# **delete_interface_group**
> delete_interface_group(id)

Delete interface group

Delete an interface group on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Id of the interface group.

# example passing only required values which don't have defaults set
try:
	# Delete interface group
	client.platform.delete_interface_group(id)
except ApiException as e:
	print("Exception when calling PlatformApi->delete_interface_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the interface group. |

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

# **delete_ipmi_user**
> IpmiTextResponse delete_ipmi_user(body)

To delete IPMI User for node

Deletes the provided ipmi user for given node.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.delete_ipmi_user import DeleteIpmiUser
from cohesity_sdk.cluster.model.ipmi_text_response import IpmiTextResponse
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = DeleteIpmiUser(
        node_id="node_id_example",
        node_ip="node_ip_example",
        username="username_example",
    ) # DeleteIpmiUser | Specifies the parameters to delete an ipmi user from given node.

# example passing only required values which don't have defaults set
try:
	# To delete IPMI User for node
	api_response = client.platform.delete_ipmi_user(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->delete_ipmi_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteIpmiUser**](DeleteIpmiUser.md)| Specifies the parameters to delete an ipmi user from given node. |

### Return type

[**IpmiTextResponse**](IpmiTextResponse.md)

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

# **delete_rack_by_id**
> delete_rack_by_id(id)

Delete a rack by id.

Delete a given rack by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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

# **discover_disks**
> ClusterFreeDisks discover_disks()

Discover new disks

Discover disks that are ready for activation

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_free_disks import ClusterFreeDisks
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.disk_identify import DiskIdentify
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = DiskIdentify(
        identify=True,
        node_id=1,
        serial_number="serial_number_example",
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_free_disks import ClusterFreeDisks
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ClusterFreeDisks(
        node_free_disks=[
            NodeFreeDisks(
                chassis_serial="chassis_serial_example",
                free_disks=[
                    FreeDisk(
                        location="location_example",
                        path="path_example",
                        serial_number="serial_number_example",
                        size_in_bytes=1,
                    ),
                ],
                node_id=1,
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.cluster_expand_params import ClusterExpandParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_operation_response_params import ClusterOperationResponseParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ClusterExpandParams(
        cloud_cluster_params=CloudClusterExpandParams(
            node_ips=[
                "node_ips_example",
            ],
        ),
        physical_cluster_params=PhysicalClusterExpandParams(
            chassis_rack_configs=[
                ChassisRackConfigParams(
                    chassis_serial="chassis_serial_example",
                    rack_id=1,
                ),
            ],
            node_configs=[
                PhysicalNodeConfigParams(
                    id=1,
                    ip="ip_example",
                    ipmi_ip="ipmi_ip_example",
                    is_compute_node=True,
                ),
            ],
            vips=[
                "vips_example",
            ],
        ),
        type="Physical",
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

# **get_amqp_target_config**
> ClusterAMQPTargetConfig get_amqp_target_config()

Get AMQP Target Config

Fetch AMQP target config on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_amqp_target_config import ClusterAMQPTargetConfig
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.chassis_list import ChassisList
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.chassis import Chassis
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.cluster import Cluster
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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

# **get_cluster_local_domain_sid**
> ClusterLocalDomainSID get_cluster_local_domain_sid()

Get Cluster Local Domain SID

Fetch SID of cluster local domain.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.cluster_local_domain_sid import ClusterLocalDomainSID
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get Cluster Local Domain SID
	api_response = client.platform.get_cluster_local_domain_sid()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster_local_domain_sid: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_cluster_packages**
> ClusterPackages get_cluster_packages()

Get packages

Get software packages on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.cluster_packages import ClusterPackages
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get packages
	api_response = client.platform.get_cluster_packages()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster_packages: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterPackages**](ClusterPackages.md)

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

# **get_cluster_snapshot_policy**
> ClusterSnapshotPolicy get_cluster_snapshot_policy()

Get cluster snapshot policy.

Get cluster snapshot policy.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_snapshot_policy import ClusterSnapshotPolicy
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get cluster snapshot policy.
	api_response = client.platform.get_cluster_snapshot_policy()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster_snapshot_policy: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterSnapshotPolicy**](ClusterSnapshotPolicy.md)

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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.cluster_state_params import ClusterStateParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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

# **get_cluster_vlans**
> ClusterVlans get_cluster_vlans()

Get vlans

Get vlans on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_vlans import ClusterVlans
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


interface_names = [
        "interfaceNames_example",
    ] # [str] | Vlan interface names, it should be in interface_group_name.vlan_id format. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | Ids of the tenants, used to get vlans assigned to tenants. (optional)
include_tenants = True # bool | If true, the response includes vlans which belongs to all the tenants the current user has permissions to see. (optional) if omitted the server will use the default value of True
skip_primary_and_bond_iface = False # bool | If true, vlan primary and bond interfaces are not returned in the response. (optional) if omitted the server will use the default value of False
compress_ips_to_ranges = False # bool | Compress vlan IPs to list of contigous IP ranges with startIp and endIp. (optional) if omitted the server will use the default value of False

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get vlans
	api_response = client.platform.get_cluster_vlans(interface_names=interface_names, tenant_ids=tenant_ids, include_tenants=include_tenants, skip_primary_and_bond_iface=skip_primary_and_bond_iface, compress_ips_to_ranges=compress_ips_to_ranges)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster_vlans: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_names** | **[str]**| Vlan interface names, it should be in interface_group_name.vlan_id format. | [optional]
 **tenant_ids** | **[str]**| Ids of the tenants, used to get vlans assigned to tenants. | [optional]
 **include_tenants** | **bool**| If true, the response includes vlans which belongs to all the tenants the current user has permissions to see. | [optional] if omitted the server will use the default value of True
 **skip_primary_and_bond_iface** | **bool**| If true, vlan primary and bond interfaces are not returned in the response. | [optional] if omitted the server will use the default value of False
 **compress_ips_to_ranges** | **bool**| Compress vlan IPs to list of contigous IP ranges with startIp and endIp. | [optional] if omitted the server will use the default value of False

### Return type

[**ClusterVlans**](ClusterVlans.md)

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

# **get_interface_groups**
> InterfaceGroups get_interface_groups()

Get interface groups

Get a list of interface groups configured on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.interface_groups import InterfaceGroups
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


ids = [
        1,
    ] # [int] | Ids of the interface groups. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get interface groups
	api_response = client.platform.get_interface_groups(ids=ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_interface_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**| Ids of the interface groups. | [optional]

### Return type

[**InterfaceGroups**](InterfaceGroups.md)

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

# **get_interfaces**
> NetworkInterfaceParams get_interfaces()

Get interfaces

Get interfaces on a cluster or free node.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.network_interface_params import NetworkInterfaceParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


node_id = 1 # int | Node id, used to get interfaces on a particular node. (optional)
chassis_serial = "chassisSerial_example" # str | Chassis serial number, used to get interfaces on a chassis. (optional)
slot = 1 # int | Slot number, used to get interfaces on a slot. (optional)
cache = True # bool | Get interfaces information from cache. (optional) if omitted the server will use the default value of True
bond_interfaces = False # bool | Get bond interfaces only. (optional) if omitted the server will use the default value of False
interface_group = False # bool | Get interfaces assigned to a interface group only. (optional) if omitted the server will use the default value of False
uplink_switch = True # bool | Include uplink switch information. (optional) if omitted the server will use the default value of True
bond_member = True # bool | Include bond member information for bond interfaces. (optional) if omitted the server will use the default value of True
stats = True # bool | Include interface stats. (optional) if omitted the server will use the default value of True

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get interfaces
	api_response = client.platform.get_interfaces(node_id=node_id, chassis_serial=chassis_serial, slot=slot, cache=cache, bond_interfaces=bond_interfaces, interface_group=interface_group, uplink_switch=uplink_switch, bond_member=bond_member, stats=stats)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_interfaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**| Node id, used to get interfaces on a particular node. | [optional]
 **chassis_serial** | **str**| Chassis serial number, used to get interfaces on a chassis. | [optional]
 **slot** | **int**| Slot number, used to get interfaces on a slot. | [optional]
 **cache** | **bool**| Get interfaces information from cache. | [optional] if omitted the server will use the default value of True
 **bond_interfaces** | **bool**| Get bond interfaces only. | [optional] if omitted the server will use the default value of False
 **interface_group** | **bool**| Get interfaces assigned to a interface group only. | [optional] if omitted the server will use the default value of False
 **uplink_switch** | **bool**| Include uplink switch information. | [optional] if omitted the server will use the default value of True
 **bond_member** | **bool**| Include bond member information for bond interfaces. | [optional] if omitted the server will use the default value of True
 **stats** | **bool**| Include interface stats. | [optional] if omitted the server will use the default value of True

### Return type

[**NetworkInterfaceParams**](NetworkInterfaceParams.md)

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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.d_maa_s_info import DMaaSInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get whether the cluster is a DMaaS cluster.
	api_response = client.platform.get_is_d_maa_s_cluster()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_is_d_maa_s_cluster: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_interfaces import ClusterInterfaces
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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

# **get_nodes**
> [Node] get_nodes()

List Nodes of the cluster.

Gets the list of Nodes in a cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.node import Node
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


ids = [
        1,
    ] # [int] | \"List of IDs to be returned. If empty, all nodes are returned.\" (optional)
include_marked_for_removal = True # bool | IncludeMarkedForRemoval is used to specify whether to include nodes marked for removal. (optional)
include_only_unassigned_nodes = True # bool | IncludeOnlyUnassignedNodes will return nodes that are not yet assigned to any cluster partition. If this parameter is specified as true and ClusterPartitionIdList is also non-empty, then no nodes will be returned. (optional)
cluster_partition_ids = [
        1,
    ] # [int] | ClusterPartitionIdList specifies the list of Ids used to filter the nodes by specified cluster partition. (optional)
fetch_stats = True # bool | FetchStats is used to specify whether to call Stats service to fetch the stats for the nodes. Stats not displayed by default (optional)
show_system_disks = True # bool | ShowSystemdisks is used to specify whether to display system disks for the nodes. Not populated by default. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List Nodes of the cluster.
	api_response = client.platform.get_nodes(ids=ids, include_marked_for_removal=include_marked_for_removal, include_only_unassigned_nodes=include_only_unassigned_nodes, cluster_partition_ids=cluster_partition_ids, fetch_stats=fetch_stats, show_system_disks=show_system_disks)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_nodes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**| \&quot;List of IDs to be returned. If empty, all nodes are returned.\&quot; | [optional]
 **include_marked_for_removal** | **bool**| IncludeMarkedForRemoval is used to specify whether to include nodes marked for removal. | [optional]
 **include_only_unassigned_nodes** | **bool**| IncludeOnlyUnassignedNodes will return nodes that are not yet assigned to any cluster partition. If this parameter is specified as true and ClusterPartitionIdList is also non-empty, then no nodes will be returned. | [optional]
 **cluster_partition_ids** | **[int]**| ClusterPartitionIdList specifies the list of Ids used to filter the nodes by specified cluster partition. | [optional]
 **fetch_stats** | **bool**| FetchStats is used to specify whether to call Stats service to fetch the stats for the nodes. Stats not displayed by default | [optional]
 **show_system_disks** | **bool**| ShowSystemdisks is used to specify whether to display system disks for the nodes. Not populated by default. | [optional]

### Return type

[**[Node]**](Node.md)

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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.rack import Rack
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.racks import Racks
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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

# **get_remote_disks**
> RemoteDisks get_remote_disks()

Get remote disks

Get remote disks.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.remote_disks import RemoteDisks
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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

# **get_smtp_configuration**
> SMTPConfiguration get_smtp_configuration()

Get SMTP configuration.

Get the SMTP cluster configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.smtp_configuration import SMTPConfiguration
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.support_channel_config import SupportChannelConfig
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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

# **identify_node**
> NodeIdentifyParams identify_node(id, body)

Identify node

Turn on/off LED light of a node to identify.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.node_identify_params import NodeIdentifyParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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

# **import_crl_file**
> import_crl_file(file_name, crlfile)

Import Crl File

Import a Crl file into the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


file_name = "file_name_example" # str | 
crlfile = open('/path/to/file', 'rb') # file_type | 

# example passing only required values which don't have defaults set
try:
	# Import Crl File
	client.platform.import_crl_file(file_name, crlfile)
except ApiException as e:
	print("Exception when calling PlatformApi->import_crl_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  |
 **crlfile** | **file_type**|  |

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

# **list_disks**
> DisksList list_disks()

Get list of disks

Get list of local disks.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.disks_list import DisksList
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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

# **list_feature_flag**
> FeatureFlagList list_feature_flag()

Get feature flag overrides list.

Get the list of feature flag overrides defined on cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.feature_flag_list import FeatureFlagList
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get feature flag overrides list.
	api_response = client.platform.list_feature_flag()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->list_feature_flag: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**FeatureFlagList**](FeatureFlagList.md)

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

# **list_free_nodes**
> FreeNodes list_free_nodes()

List the free Cohesity Nodes present on a network.

Sends a request to any Node to list all of the free Nodes that are present on the network.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.free_nodes import FreeNodes
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# List the free Cohesity Nodes present on a network.
	api_response = client.platform.list_free_nodes()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->list_free_nodes: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**FreeNodes**](FreeNodes.md)

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

# **list_hosts**
> HostMappings list_hosts()

List Host Mappings

Lists the host mappings in /etc/hosts of the nodes in a cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.host_mappings import HostMappings
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# List Host Mappings
	api_response = client.platform.list_hosts()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->list_hosts: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**HostMappings**](HostMappings.md)

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

# **mark_baseos_upgrade**
> MarkBaseosUpgradeInfo mark_baseos_upgrade(body)

Sets/clears the BaseOS upgrade cluster operation.

Sets/clears the BaseOS upgrade cluster operation.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.mark_baseos_upgrade_info import MarkBaseosUpgradeInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = MarkBaseosUpgradeInfo(
        message="message_example",
        set_operation=True,
    ) # MarkBaseosUpgradeInfo | Param to whether set/clear BaseOS uprgade  operation.

# example passing only required values which don't have defaults set
try:
	# Sets/clears the BaseOS upgrade cluster operation.
	api_response = client.platform.mark_baseos_upgrade(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->mark_baseos_upgrade: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MarkBaseosUpgradeInfo**](MarkBaseosUpgradeInfo.md)| Param to whether set/clear BaseOS uprgade  operation. |

### Return type

[**MarkBaseosUpgradeInfo**](MarkBaseosUpgradeInfo.md)

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

# **mark_disk_removal**
> RemoveDisk mark_disk_removal(id, body)

Mark Disk for removal

Mark disk for removal or cancel removal if a disk is already marked for removal.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.remove_disk import RemoveDisk
from cohesity_sdk.cluster.model.disk_removal_params import DiskRemovalParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies unique id of the disk to mark for removal.
body = DiskRemovalParams(
        cancel=True,
        is_validate_only=False,
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.node_removal_params import NodeRemovalParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.remove_node import RemoveNode
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies id of node to cancel removal.
body = NodeRemovalParams(
        cancel=True,
        is_offline=False,
        is_validate_only=False,
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

# **node_information**
> NodeInfo node_information()

Fetch Node General Information

Fetch general information about the node to which the request is sent to.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.node_info import NodeInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


show_services_version_info = True # bool | Specifies whether to show version info of the services running on the node. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Fetch Node General Information
	api_response = client.platform.node_information(show_services_version_info=show_services_version_info)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->node_information: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_services_version_info** | **bool**| Specifies whether to show version info of the services running on the node. | [optional]

### Return type

[**NodeInfo**](NodeInfo.md)

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

# **public_key_request**
> PublicKeyResponse public_key_request(body)

Get the SSH public key.

Get the SSH public key corresponding to the private key used by workloads. For example, users may specify multiple scripts which are supposed to be executed on a remote machine at different progress states of a protection group run (for instance - running a script before the run starts and another after the run completes). The public key returned as part of this response should be added on the remote server where the script is to be executed as there is a specific private key used by the workload for remote login.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.public_key_response import PublicKeyResponse
from cohesity_sdk.cluster.model.public_key_request import PublicKeyRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = PublicKeyRequest(
        workflow_type="DataProtection",
    ) # PublicKeyRequest | Specifies the parameters required to retrieve SSH public key

# example passing only required values which don't have defaults set
try:
	# Get the SSH public key.
	api_response = client.platform.public_key_request(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->public_key_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublicKeyRequest**](PublicKeyRequest.md)| Specifies the parameters required to retrieve SSH public key |

### Return type

[**PublicKeyResponse**](PublicKeyResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Describes the structure of SSH public key. |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_remote_disk**
> remove_remote_disk(id)

Remove remote disk

Remove a remote disk.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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

# **set_node_power**
> set_node_power(body)

Reboot or shutdown nodes in cluster.

Reboot or shutdown nodes in cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.node_power_operation import NodePowerOperation
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = NodePowerOperation(
        node_id=1,
        operation="poweroff",
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

# **update_airgap_config**
> AirgapConfig update_airgap_config(body)

Update Airgap config

Enable or Disable Airgap on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.airgap_config import AirgapConfig
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = AirgapConfig(
        airgap_status="Enable",
        exception_profiles=[
            "exception_profiles_example",
        ],
    ) # AirgapConfig | Specifies the parameters to update airgap config.

# example passing only required values which don't have defaults set
try:
	# Update Airgap config
	api_response = client.platform.update_airgap_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_airgap_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AirgapConfig**](AirgapConfig.md)| Specifies the parameters to update airgap config. |

### Return type

[**AirgapConfig**](AirgapConfig.md)

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

# **update_amqp_target_config**
> ClusterAMQPTargetConfig update_amqp_target_config(body)

Update AMQP Target Config

Updates AMQP target config on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_amqp_target_config import ClusterAMQPTargetConfig
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ClusterAMQPTargetConfig(
        certificate="certificate_example",
        exchange="exchange_example",
        filer_id=1,
        password="password_example",
        server_ip="server_ip_example",
        username="username_example",
        virtual_host="virtual_host_example",
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.chassis import Chassis
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of chassis.
body = Chassis(
        hardware_model="hardware_model_example",
        id=1,
        name="name_example",
        node_ids=[
            1,
        ],
        rack_id=1,
        serial_number="serial_number_example",
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.cluster import Cluster
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = Cluster(
        cluster_audit_log_config=ClusterAuditLogConfig(),
        description="description_example",
        file_services_audit_log_config=AuditLogConfig(
            enabled=True,
            retention_period_days=1,
        ),
        name="name_example",
        network_config=ClusterCreateNetworkConfig(
            dhcp_network_config=ClusterDhcpNetworkConfig(
                dns_servers=[
                    "dns_servers_example",
                ],
            ),
            domain_names=[
                "domain_names_example",
            ],
            ip_preference="Ipv4",
            manual_network_config=ClusterManualNetworkConfig(
                dns_servers=[
                    "dns_servers_example",
                ],
                gateway="gateway_example",
                subnet_ip="subnet_ip_example",
                subnet_mask="subnet_mask_example",
            ),
            ntp_servers=[
                "ntp_servers_example",
            ],
            secondary_dhcp_network_config=ClusterDhcpNetworkConfig(
                dns_servers=[
                    "dns_servers_example",
                ],
            ),
            secondary_manual_network_config=ClusterManualNetworkConfig(
                dns_servers=[
                    "dns_servers_example",
                ],
                gateway="gateway_example",
                subnet_ip="subnet_ip_example",
                subnet_mask="subnet_mask_example",
            ),
            use_dhcp=True,
            vip_host_name="vip_host_name_example",
        ),
        proxy_server_config=ClusterProxyServerConfig(
            ip="ip_example",
            is_disabled=True,
            password="password_example",
            port=1,
            username="username_example",
        ),
        rigel_cluster_params=RigelClusterConfigParams(
            dataplane_endpoint="dataplane_endpoint_example",
            nodes=[
                RigelClusterNode(
                    node_id=1,
                    node_ip="node_ip_example",
                    secondary_node_ip="secondary_node_ip_example",
                ),
            ],
        ),
        views_global_settings=ViewsGlobalSettings(
            enable_remote_views_gui_visibility=True,
            enable_remote_views_visibility=True,
            enable_smb_auth=True,
            enable_smb_multi_channel=True,
            s3_virtual_hosted_domain_names=[
                "s3_virtual_hosted_domain_names_example",
            ],
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

# **update_cluster_snapshot_policy**
> ClusterSnapshotPolicy update_cluster_snapshot_policy(body)

Update cluster snapshot policy.

Update cluster snapshot policy.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.update_snapshot_policy_params import UpdateSnapshotPolicyParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_snapshot_policy import ClusterSnapshotPolicy
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = UpdateSnapshotPolicyParams(
        days_of_month=[
            1,
        ],
        days_of_week=[
            "days_of_week_example",
        ],
        num_of_days_to_keep=1,
        num_of_versions_to_keep=1,
        suspend_retention_policy=True,
        suspend_schedule_policy=True,
        time="time_example",
        time_zone="time_zone_example",
    ) # UpdateSnapshotPolicyParams | Specifies the parameters to update cluster snapshot policy.

# example passing only required values which don't have defaults set
try:
	# Update cluster snapshot policy.
	api_response = client.platform.update_cluster_snapshot_policy(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_cluster_snapshot_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSnapshotPolicyParams**](UpdateSnapshotPolicyParams.md)| Specifies the parameters to update cluster snapshot policy. |

### Return type

[**ClusterSnapshotPolicy**](ClusterSnapshotPolicy.md)

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

# **update_cluster_vlan**
> ClusterVlanParams update_cluster_vlan(interface_name, body)

Update vlan

Update a vlan on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_vlan_params import ClusterVlanParams
from cohesity_sdk.cluster.model.update_cluster_vlan_params import UpdateClusterVlanParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


interface_name = "interfaceName_example" # str | Vlan interface name, it should be in interface_group_name.vlan_id format.
body = UpdateClusterVlanParams(
        all_tenant_access=False,
        app_ips=[
            "app_ips_example",
        ],
        description="description_example",
        dns_delegation_zones=[
            DnsDelegationZone(
                dns_zone_resolved_vips=[
                    "dns_zone_resolved_vips_example",
                ],
                dns_zone_vips=[
                    "dns_zone_vips_example",
                ],
                name="name_example",
            ),
        ],
        ecmp_enabled=False,
        fqdn="fqdn_example",
        gateway="gateway_example",
        ip_addresses_type="Ipv4",
        ip_pools=[
            IpPool(
                ips=[
                    "ips_example",
                ],
                name="name_example",
            ),
        ],
        ip_ranges=[
            IpRange(
                end_ip="end_ip_example",
                start_ip="start_ip_example",
            ),
        ],
        ips=[
            "ips_example",
        ],
        mtu=1,
        subnet="subnet_example",
        tenant_id="tenant_id_example",
        vlan_name="vlan_name_example",
    ) # UpdateClusterVlanParams | Parameters to update vlan on the cluster.

# example passing only required values which don't have defaults set
try:
	# Update vlan
	api_response = client.platform.update_cluster_vlan(interface_name, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_cluster_vlan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_name** | **str**| Vlan interface name, it should be in interface_group_name.vlan_id format. |
 **body** | [**UpdateClusterVlanParams**](UpdateClusterVlanParams.md)| Parameters to update vlan on the cluster. |

### Return type

[**ClusterVlanParams**](ClusterVlanParams.md)

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
> FeatureFlagList update_feature_flag(body)

Update feature flag override status.

Update a feature flag override status to cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.feature_flag_list import FeatureFlagList
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.update_feature_flag_params import UpdateFeatureFlagParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = UpdateFeatureFlagParams(
        clear=True,
        is_approved=True,
        is_ui_feature=True,
        name="name_example",
        reason="reason_example",
        timestamp=1,
    ) # UpdateFeatureFlagParams | Param for feature flag override request.

# example passing only required values which don't have defaults set
try:
	# Update feature flag override status.
	api_response = client.platform.update_feature_flag(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_feature_flag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateFeatureFlagParams**](UpdateFeatureFlagParams.md)| Param for feature flag override request. |

### Return type

[**FeatureFlagList**](FeatureFlagList.md)

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

# **update_hosts**
> HostMappings update_hosts(body)

Update Host Mappings

Updates Host Mapping on the Cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.host_mappings_parameters import HostMappingsParameters
from cohesity_sdk.cluster.model.host_mappings import HostMappings
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = HostMappingsParameters([
        HostEntry(
            description="description_example",
            domain_names=[
                "domain_names_example",
            ],
            ip="ip_example",
        ),
    ]) # HostMappingsParameters | 

# example passing only required values which don't have defaults set
try:
	# Update Host Mappings
	api_response = client.platform.update_hosts(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_hosts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostMappingsParameters**](HostMappingsParameters.md)|  |

### Return type

[**HostMappings**](HostMappings.md)

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

# **update_interface**
> InterfaceParams update_interface(id, body)

Update interface

Update network interface on a free node.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.interface_params import InterfaceParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Id of the interface.
body = InterfaceParams(
        name="name_example",
        network_params=InterfaceNetworkParams(
            bond_interface_params=BondInterfaceNetworkParams(
                bonding_mode="ActiveBackup",
                lacp_rate="Slow",
                xmit_hash_policy="layer2",
            ),
            mtu=1,
        ),
    ) # InterfaceParams | Parameters to update an interface on a node or cluster.

# example passing only required values which don't have defaults set
try:
	# Update interface
	api_response = client.platform.update_interface(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_interface: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the interface. |
 **body** | [**InterfaceParams**](InterfaceParams.md)| Parameters to update an interface on a node or cluster. |

### Return type

[**InterfaceParams**](InterfaceParams.md)

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

# **update_interface_group**
> InterfaceGroup update_interface_group(id, body)

Update interface group

Update an interface group on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.interface_group import InterfaceGroup
from cohesity_sdk.cluster.model.interface_group_params import InterfaceGroupParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Id of the interface group.
body = InterfaceGroupParams(
        name="name_example",
        network_params=InterfaceGroupNetworkParams(
            bond_interface_params=BondInterfaceNetworkParams(
                bonding_mode="ActiveBackup",
                lacp_rate="Slow",
                xmit_hash_policy="layer2",
            ),
            mtu=1,
        ),
        node_interface_params=[
            NodeInterfaceParams(
                interface_name="interface_name_example",
                node_id=1,
            ),
        ],
        type="Bond",
    ) # InterfaceGroupParams | Parameters to update an interface group on the cluster.

# example passing only required values which don't have defaults set
try:
	# Update interface group
	api_response = client.platform.update_interface_group(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_interface_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the interface group. |
 **body** | [**InterfaceGroupParams**](InterfaceGroupParams.md)| Parameters to update an interface group on the cluster. |

### Return type

[**InterfaceGroup**](InterfaceGroup.md)

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

# **update_is_d_maa_s_cluster**
> DMaaSInfo update_is_d_maa_s_cluster(body)

Update whether the cluster is a DMaaS cluster.

Update whether the cluster is a DMaaS cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.d_maa_s_info import DMaaSInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = DMaaSInfo(
        is_dmaas=True,
    ) # DMaaSInfo | Param to update whether the cluster is a DMaaS cluster.

# example passing only required values which don't have defaults set
try:
	# Update whether the cluster is a DMaaS cluster.
	api_response = client.platform.update_is_d_maa_s_cluster(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_is_d_maa_s_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DMaaSInfo**](DMaaSInfo.md)| Param to update whether the cluster is a DMaaS cluster. |

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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.rack import Rack
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of rack.
body = Rack(
        chassis_ids=[
            1,
        ],
        id=1,
        location="location_example",
        name="name_example",
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.racks import Racks
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = Racks(
        racks=[
            Rack(
                chassis_ids=[
                    1,
                ],
                id=1,
                location="location_example",
                name="name_example",
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

# **update_smtp_configuration**
> SMTPConfiguration update_smtp_configuration(body)

Update SMTP configuration.

Update SMTP configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.smtp_configuration import SMTPConfiguration
from cohesity_sdk.cluster.model.update_smtp_params import UpdateSMTPParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.support_channel_config import SupportChannelConfig
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = SupportChannelConfig(
        end_time_usecs=1,
        is_enabled=True,
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

# **upgrade_check_get_results**
> UpgradeChecksResults upgrade_check_get_results(test_run_instance_id)

Get upgrade checks results.

Get upgrade checks results.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.upgrade_checks_results import UpgradeChecksResults
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


test_run_instance_id = 1 # int | Specifies test run instance for which to fetch results

# example passing only required values which don't have defaults set
try:
	# Get upgrade checks results.
	api_response = client.platform.upgrade_check_get_results(test_run_instance_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->upgrade_check_get_results: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_instance_id** | **int**| Specifies test run instance for which to fetch results |

### Return type

[**UpgradeChecksResults**](UpgradeChecksResults.md)

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

# **upgrade_check_run_tests**
> UpgradeCheckRunTestsResult upgrade_check_run_tests(body)

Run upgrade checks on cluster.

Run upgrade checks on cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.upgrade_check_run_tests_result import UpgradeCheckRunTestsResult
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.upgrade_check_run_tests_request import UpgradeCheckRunTestsRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = UpgradeCheckRunTestsRequest(
        request_type="PreUpgrade",
    ) # UpgradeCheckRunTestsRequest | Run upgrade checks on cluster.

# example passing only required values which don't have defaults set
try:
	# Run upgrade checks on cluster.
	api_response = client.platform.upgrade_check_run_tests(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->upgrade_check_run_tests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpgradeCheckRunTestsRequest**](UpgradeCheckRunTestsRequest.md)| Run upgrade checks on cluster. |

### Return type

[**UpgradeCheckRunTestsResult**](UpgradeCheckRunTestsResult.md)

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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_uprade_params import ClusterUpradeParams
from cohesity_sdk.cluster.model.cluster_operation_response_params import ClusterOperationResponseParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ClusterUpradeParams(
        abort_upgrade_on_checks_failure=True,
        type="Upgrade",
        url="url_example",
        version_name="version_name_example",
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

# **upload_package_by_url**
> ClusterOperationResponseParams upload_package_by_url(body)

Upload package by URL

Upload a package to the cluster by providing the URL where the package is hosted.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.upload_package_url_params import UploadPackageUrlParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_operation_response_params import ClusterOperationResponseParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.test_smtp_config import TestSMTPConfig
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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

