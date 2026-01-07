# cohesity_sdk.PlatformApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**add_hosts**](PlatformApi.md#add_hosts) | **POST** /clusters/host-mappings | Create Cluster Host Mappings
[**add_remote_disk**](PlatformApi.md#add_remote_disk) | **POST** /disks/remote | Add remote disk
[**change_services_states**](PlatformApi.md#change_services_states) | **POST** /clusters/services/states | Change cluster services states.
[**clear_smtp_configuration**](PlatformApi.md#clear_smtp_configuration) | **DELETE** /clusters/smtp | Clear SMTP configuration.
[**cluster_delete_ipmi_users**](PlatformApi.md#cluster_delete_ipmi_users) | **DELETE** /ipmi/cluster-users | To delete IPMI Users for cluster
[**cluster_update_ipmi_users**](PlatformApi.md#cluster_update_ipmi_users) | **PUT** /ipmi/cluster-users | To update IPMI Users for cluster
[**create_bond**](PlatformApi.md#create_bond) | **POST** /network/bonds | Create a new network bond.
[**create_cluster**](PlatformApi.md#create_cluster) | **POST** /clusters | Create a cluster.
[**create_cluster_vlan**](PlatformApi.md#create_cluster_vlan) | **POST** /network/vlans | Create vlan
[**create_interface_group**](PlatformApi.md#create_interface_group) | **POST** /network/interface-groups | Create interface group
[**create_proxy_server**](PlatformApi.md#create_proxy_server) | **POST** /proxy-servers | Creare a proxy server.
[**create_racks**](PlatformApi.md#create_racks) | **POST** /racks | Create racks
[**delete_amqp_target_config**](PlatformApi.md#delete_amqp_target_config) | **DELETE** /clusters/amqp-target-config | Delete AMQP Target Config
[**delete_cluster_snapshot_policy**](PlatformApi.md#delete_cluster_snapshot_policy) | **DELETE** /clusters/snapshot-policy | Delete cluster snapshot policy.
[**delete_cluster_vlan**](PlatformApi.md#delete_cluster_vlan) | **DELETE** /network/vlans/{vlanInterfaceGroupName} | Delete vlan
[**delete_hosts**](PlatformApi.md#delete_hosts) | **POST** /clusters/host-mappings/delete | Deletes multiple Host Mappings within the cluster
[**delete_interface_group**](PlatformApi.md#delete_interface_group) | **DELETE** /network/interface-groups/{name} | Delete interface group
[**delete_ipmi_user**](PlatformApi.md#delete_ipmi_user) | **DELETE** /ipmi/users | To delete IPMI User for node
[**discover_disks**](PlatformApi.md#discover_disks) | **GET** /disks/discover | Discover new disks
[**disk_identify**](PlatformApi.md#disk_identify) | **POST** /disks/identify | Identify a disk
[**disks_assimilate**](PlatformApi.md#disks_assimilate) | **POST** /disks/assimilate | Assimilate disks.
[**get_amqp_target_config**](PlatformApi.md#get_amqp_target_config) | **GET** /clusters/amqp-target-config | Get AMQP Target Config
[**get_chassis**](PlatformApi.md#get_chassis) | **GET** /chassis | Get list of chassis
[**get_chassis_by_id**](PlatformApi.md#get_chassis_by_id) | **GET** /chassis/{id} | Get a chassis by chassis id.
[**get_cluster**](PlatformApi.md#get_cluster) | **GET** /clusters | Retrieve Cluster Configuration
[**get_cluster_ipmi_lan_info**](PlatformApi.md#get_cluster_ipmi_lan_info) | **GET** /ipmi/cluster-get-lan-info | To get IPMI LAN info for the cluster
[**get_cluster_ipmi_users**](PlatformApi.md#get_cluster_ipmi_users) | **GET** /ipmi/cluster-users | To get IPMI users info for the cluster
[**get_cluster_local_domain_sid**](PlatformApi.md#get_cluster_local_domain_sid) | **GET** /clusters/local-domain-sid | Get Cluster Local Domain SID
[**get_cluster_metadata**](PlatformApi.md#get_cluster_metadata) | **GET** /clusters/metadata | Get Cluster Metadata
[**get_cluster_operation_status_list**](PlatformApi.md#get_cluster_operation_status_list) | **GET** /clusters/operation-status | Get cluster operations status.
[**get_cluster_packages**](PlatformApi.md#get_cluster_packages) | **GET** /clusters/packages | Get packages
[**get_cluster_snapshot_policy**](PlatformApi.md#get_cluster_snapshot_policy) | **GET** /clusters/snapshot-policy | Get cluster snapshot policy.
[**get_cluster_state**](PlatformApi.md#get_cluster_state) | **GET** /clusters/state | Get cluster state
[**get_cluster_status**](PlatformApi.md#get_cluster_status) | **GET** /clusters/status | Get cluster status.
[**get_cluster_subnets_info**](PlatformApi.md#get_cluster_subnets_info) | **GET** /clusters/subnets | Get cluster subnets info.
[**get_cluster_vlan**](PlatformApi.md#get_cluster_vlan) | **GET** /network/vlans/{vlanInterfaceGroupName} | Get vlan
[**get_cluster_vlans**](PlatformApi.md#get_cluster_vlans) | **GET** /network/vlans | Get vlans
[**get_hardware_info**](PlatformApi.md#get_hardware_info) | **GET** /node/hardware-info | Fetch Node Hardware Information
[**get_interface_groups**](PlatformApi.md#get_interface_groups) | **GET** /network/interface-groups | Get interface groups
[**get_ipmi_fru_info**](PlatformApi.md#get_ipmi_fru_info) | **GET** /ipmi/get-fru-info | To get IPMI FRU info
[**get_ipmi_lan_info**](PlatformApi.md#get_ipmi_lan_info) | **GET** /ipmi/get-lan-info | To get IPMI LAN info
[**get_ipmi_sdr_info**](PlatformApi.md#get_ipmi_sdr_info) | **GET** /ipmi/get-sdr-info | To get IPMI SDR Info
[**get_ipmi_sel**](PlatformApi.md#get_ipmi_sel) | **GET** /ipmi/get-sel | To get IPMI SEL
[**get_ipmi_sel_info**](PlatformApi.md#get_ipmi_sel_info) | **GET** /ipmi/get-sel-info | To get IPMI SEL Info
[**get_ipmi_users**](PlatformApi.md#get_ipmi_users) | **GET** /ipmi/users | To get IPMI User Info for node
[**get_is_d_maa_s_cluster**](PlatformApi.md#get_is_d_maa_s_cluster) | **GET** /clusters/is-dmaas | Get whether the cluster is a DMaaS cluster.
[**get_kubernetes_infra_health_status**](PlatformApi.md#get_kubernetes_infra_health_status) | **GET** /kubernetes/status | Get Kubernetes Infra Health Status
[**get_login_banner**](PlatformApi.md#get_login_banner) | **GET** /login-banners | Get login banner.
[**get_network_interfaces**](PlatformApi.md#get_network_interfaces) | **GET** /network-interfaces | Get list of interfaces
[**get_nodes**](PlatformApi.md#get_nodes) | **GET** /clusters/nodes | List Nodes of the cluster.
[**get_ntp_servers**](PlatformApi.md#get_ntp_servers) | **GET** /ntp-servers | Get list of NTP servers.
[**get_proxy_servers**](PlatformApi.md#get_proxy_servers) | **GET** /proxy-servers | Get list of proxy servers
[**get_rack_by_id**](PlatformApi.md#get_rack_by_id) | **GET** /racks/{id} | Get a rack by rack id.
[**get_racks**](PlatformApi.md#get_racks) | **GET** /racks | Get list of racks
[**get_remote_disks**](PlatformApi.md#get_remote_disks) | **GET** /disks/remote | Get remote disks
[**get_service_gflags**](PlatformApi.md#get_service_gflags) | **GET** /clusters/gflag | Gets cluster gflags for a service.
[**get_smtp_configuration**](PlatformApi.md#get_smtp_configuration) | **GET** /clusters/smtp | Get SMTP configuration.
[**get_software_components**](PlatformApi.md#get_software_components) | **GET** /clusters/software-components | Get Software Components
[**get_support_channel_config**](PlatformApi.md#get_support_channel_config) | **GET** /support-channel-config | Get support channel configuration.
[**get_sw_update_history**](PlatformApi.md#get_sw_update_history) | **GET** /clusters/softwares | Get cluster software history
[**identify_node**](PlatformApi.md#identify_node) | **POST** /nodes/{id}/identify | Identify node
[**import_crl_file**](PlatformApi.md#import_crl_file) | **PUT** /clusters/import-crl-file | Import Crl File
[**list_disks**](PlatformApi.md#list_disks) | **GET** /disks/local | Get list of disks
[**list_free_nodes**](PlatformApi.md#list_free_nodes) | **GET** /clusters/nodes/free | List the free Cohesity Nodes present on a network.
[**list_hosts**](PlatformApi.md#list_hosts) | **GET** /clusters/host-mappings | List Host Mappings
[**list_services_states**](PlatformApi.md#list_services_states) | **GET** /clusters/services/states | List services states
[**mark_baseos_upgrade**](PlatformApi.md#mark_baseos_upgrade) | **PUT** /clusters/baseos-upgrade | Sets/clears the BaseOS upgrade cluster operation.
[**mark_disk_removal**](PlatformApi.md#mark_disk_removal) | **POST** /disks/{id}/remove | Mark Disk for removal
[**mark_node_removal**](PlatformApi.md#mark_node_removal) | **POST** /nodes/{id}/remove | Mark Node for removal
[**node_import_signed_cert**](PlatformApi.md#node_import_signed_cert) | **POST** /node/import/signed-csr | Import a signed certificate used for n2n communication
[**node_information**](PlatformApi.md#node_information) | **GET** /nodes | Fetch Node General Information
[**node_status**](PlatformApi.md#node_status) | **GET** /node/status | Fetch Node status Information
[**public_key_request**](PlatformApi.md#public_key_request) | **POST** /clusters/ssh-public-key | Get the SSH public key.
[**remove_proxy_server**](PlatformApi.md#remove_proxy_server) | **DELETE** /proxy-servers/{name} | Remove specified proxy server.
[**remove_remote_disk**](PlatformApi.md#remove_remote_disk) | **DELETE** /disks/remote/{id} | Remove remote disk
[**reset_ipmi_bmc**](PlatformApi.md#reset_ipmi_bmc) | **POST** /ipmi/reset-bmc | To reset IPMI BMC for given node
[**restore_configuration**](PlatformApi.md#restore_configuration) | **GET** /clusters/restore-config | Restore configuration.
[**set_node_power**](PlatformApi.md#set_node_power) | **POST** /node-power | Reboot or shutdown nodes in cluster.
[**update_airgap_config**](PlatformApi.md#update_airgap_config) | **PUT** /clusters/airgap | Update Airgap config
[**update_amqp_target_config**](PlatformApi.md#update_amqp_target_config) | **PUT** /clusters/amqp-target-config | Update AMQP Target Config
[**update_chassis_by_id**](PlatformApi.md#update_chassis_by_id) | **PATCH** /chassis/{id} | Update a chassis by chassis id.
[**update_cluster**](PlatformApi.md#update_cluster) | **PUT** /clusters | Update a cluster.
[**update_cluster_ipmi_lan_info**](PlatformApi.md#update_cluster_ipmi_lan_info) | **PUT** /ipmi/cluster-update-lan-info | To update IPMI LAN info for the cluster
[**update_cluster_snapshot_policy**](PlatformApi.md#update_cluster_snapshot_policy) | **PUT** /clusters/snapshot-policy | Update cluster snapshot policy.
[**update_cluster_software**](PlatformApi.md#update_cluster_software) | **PUT** /clusters/softwares | Update cluster software
[**update_cluster_subnets**](PlatformApi.md#update_cluster_subnets) | **PUT** /clusters/subnets | Update the Cluster Subnets
[**update_cluster_vlan**](PlatformApi.md#update_cluster_vlan) | **PUT** /network/vlans/{vlanInterfaceGroupName} | Update vlan
[**update_feature_flag**](PlatformApi.md#update_feature_flag) | **PUT** /clusters/feature-flag | Update feature flag override status.
[**update_hosts**](PlatformApi.md#update_hosts) | **PUT** /clusters/host-mappings | Update Host Mappings
[**update_interface_group**](PlatformApi.md#update_interface_group) | **PUT** /network/interface-groups/{name} | Update interface group
[**update_ipmi_user**](PlatformApi.md#update_ipmi_user) | **POST** /ipmi/users | To update IPMI User Info for node
[**update_is_d_maa_s_cluster**](PlatformApi.md#update_is_d_maa_s_cluster) | **PUT** /clusters/is-dmaas | Update whether the cluster is a DMaaS cluster.
[**update_login_banner**](PlatformApi.md#update_login_banner) | **PUT** /login-banners | Update login banner.
[**update_ntp_servers**](PlatformApi.md#update_ntp_servers) | **PUT** /ntp-servers | Update NTP servers.
[**update_proxy_server**](PlatformApi.md#update_proxy_server) | **PUT** /proxy-servers/{name} | Update specified proxy server.
[**update_rack_by_id**](PlatformApi.md#update_rack_by_id) | **PATCH** /racks/{id} | 
[**update_racks**](PlatformApi.md#update_racks) | **PATCH** /racks | Update racks
[**update_restore_configuration**](PlatformApi.md#update_restore_configuration) | **PUT** /clusters/restore-config | Update Restore configuration.
[**update_service_gflags**](PlatformApi.md#update_service_gflags) | **PUT** /clusters/gflag | Update the gflags
[**update_smtp_configuration**](PlatformApi.md#update_smtp_configuration) | **PUT** /clusters/smtp | Update SMTP configuration.
[**update_support_channel_config**](PlatformApi.md#update_support_channel_config) | **PUT** /support-channel-config | Update support channel configuration.
[**upgrade_check_get_results**](PlatformApi.md#upgrade_check_get_results) | **GET** /clusters/upgrade-checks/{testRunInstanceId} | Get upgrade checks results.
[**upgrade_check_run_tests**](PlatformApi.md#upgrade_check_run_tests) | **PUT** /clusters/upgrade-checks | Run upgrade checks on cluster.
[**upgrade_nodes**](PlatformApi.md#upgrade_nodes) | **PUT** /nodes/software | Upgrade a free node.
[**upload_file_package**](PlatformApi.md#upload_file_package) | **POST** /clusters/packages/file | Upload package by files
[**validate_smtp_configuration**](PlatformApi.md#validate_smtp_configuration) | **POST** /clusters/smtp/validate | Validate SMTP configuration.
[**verify_ipmi_user**](PlatformApi.md#verify_ipmi_user) | **POST** /ipmi/verify-users | To verify IPMI User with Password for node


# **add_hosts**
> HostMappings add_hosts(body)

Create Cluster Host Mappings

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Sends a request to add one or more new entries to the Cluster's /etc/hosts

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Add a remote disk.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_services_states**
> ChangeServicesStatesResult change_services_states(body)

Change cluster services states.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Change the state of one or more services on a Cohesity Cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.change_services_states_params import ChangeServicesStatesParams
from cohesity_sdk.cluster.model.change_services_states_result import ChangeServicesStatesResult
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ChangeServicesStatesParams(
        action="kStart",
        services=[
            "kInvalidService",
        ],
    ) # ChangeServicesStatesParams | Specifies the parameters to change cluster services states.

# example passing only required values which don't have defaults set
try:
	# Change cluster services states.
	api_response = client.platform.change_services_states(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->change_services_states: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangeServicesStatesParams**](ChangeServicesStatesParams.md)| Specifies the parameters to change cluster services states. |

### Return type

[**ChangeServicesStatesResult**](ChangeServicesStatesResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_smtp_configuration**
> clear_smtp_configuration()

Clear SMTP configuration.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Clear cluster SMTP configuration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_delete_ipmi_users**
> IpmiTextResponse cluster_delete_ipmi_users(body)

To delete IPMI Users for cluster

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Deletes the specified cluster ipmi user.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.ipmi_text_response import IpmiTextResponse
from cohesity_sdk.cluster.model.cluster_delete_ipmi_users import ClusterDeleteIpmiUsers
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ClusterDeleteIpmiUsers(
        cluster_ipmi_username="cluster_ipmi_username_example",
        node_ipmi_usernames=[
            "node_ipmi_usernames_example",
        ],
        node_ips=[
            "node_ips_example",
        ],
    ) # ClusterDeleteIpmiUsers | Specifies the parameters to delete cluster ipmi users.

# example passing only required values which don't have defaults set
try:
	# To delete IPMI Users for cluster
	api_response = client.platform.cluster_delete_ipmi_users(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->cluster_delete_ipmi_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterDeleteIpmiUsers**](ClusterDeleteIpmiUsers.md)| Specifies the parameters to delete cluster ipmi users. |

### Return type

[**IpmiTextResponse**](IpmiTextResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_update_ipmi_users**
> IpmiTextResponse cluster_update_ipmi_users(body)

To update IPMI Users for cluster

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Updates the cluster ipmi user information.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.ipmi_text_response import IpmiTextResponse
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_update_ipmi_users import ClusterUpdateIpmiUsers
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ClusterUpdateIpmiUsers(
        cluster_ipmi_password="cluster_ipmi_password_example",
        cluster_ipmi_username="cluster_ipmi_username_example",
        node_ipmi_passwords=[
            "node_ipmi_passwords_example",
        ],
        node_ipmi_usernames=[
            "node_ipmi_usernames_example",
        ],
        node_ips=[
            "node_ips_example",
        ],
    ) # ClusterUpdateIpmiUsers | Specifies the parameters to update cluster ipmi users.

# example passing only required values which don't have defaults set
try:
	# To update IPMI Users for cluster
	api_response = client.platform.cluster_update_ipmi_users(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->cluster_update_ipmi_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterUpdateIpmiUsers**](ClusterUpdateIpmiUsers.md)| Specifies the parameters to update cluster ipmi users. |

### Return type

[**IpmiTextResponse**](IpmiTextResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bond**
> CreateBondParams create_bond(body)

Create a new network bond.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Sends a request to create a new network bond on the Cluster. This can only be performed on a Node before it is part of a Cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.create_bond_params import CreateBondParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateBondParams(
        name="name_example",
        slaves=[
            "slaves_example",
        ],
    ) # CreateBondParams | Parameters to create bond.

# example passing only required values which don't have defaults set
try:
	# Create a new network bond.
	api_response = client.platform.create_bond(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->create_bond: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBondParams**](CreateBondParams.md)| Parameters to create bond. |

### Return type

[**CreateBondParams**](CreateBondParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_CREATE``` <br><br>Create a cluster with given network and cluster configuration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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
            cluster_partition_hostname="cluster_partition_hostname_example",
            cluster_size="Small",
            disk_all_nodes_reachable=[
                True,
            ],
            disk_component_exclusive=[
                "disk_component_exclusive_example",
            ],
            disk_self_fault_tolerant=[
                True,
            ],
            disk_serials=[
                "disk_serials_example",
            ],
            disk_tiers=[
                "disk_tiers_example",
            ],
            enable_cloud_rf1=True,
            encryption_config=EncryptionConfigurationParams(
                enable_fips_mode=True,
                enable_hardware_encryption=True,
                enable_software_encryption=True,
                rotation_period=1,
            ),
            ip_preference=1,
            metadata_fault_tolerance=1,
            node_ips=[
                "node_ips_example",
            ],
            trust_domain="trust_domain_example",
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
            vips=[
                "vips_example",
            ],
        ),
        physical_cluster_params=ClusterCreatePhysicalParams(
            allow_api_based_fetch=True,
            apps_subnet_ip="apps_subnet_ip_example",
            apps_subnet_ip_v6="apps_subnet_ip_v6_example",
            apps_subnet_mask="apps_subnet_mask_example",
            apps_subnet_mask_v6="apps_subnet_mask_v6_example",
            cluster_destroy_hmac_key="cluster_destroy_hmac_key_example",
            cluster_subnet_groups=[
                NodeGroup(
                    bgp_instance=BgpInstance(
                        local_as=1,
                        peers=[
                            BgpPeer(
                                address_or_tag="address_or_tag_example",
                                description="description_example",
                                remote_as=1,
                                timers=BgpTimers(
                                    hold_time=1,
                                    keep_alive=1,
                                ),
                            ),
                        ],
                        timers=BgpTimers(
                            hold_time=1,
                            keep_alive=1,
                        ),
                    ),
                    dns_servers_info=DnsServersInfo(
                        dns_servers=[
                            "dns_servers_example",
                        ],
                    ),
                    id=1,
                    name="name_example",
                    node_ids=[
                        1,
                    ],
                    node_ips=[
                        "node_ips_example",
                    ],
                    subnet_info=SubnetInfo(
                        gateway="gateway_example",
                        netmask_bits=1,
                        subnet_ip="subnet_ip_example",
                        subnet_ipv4_mask="subnet_ipv4_mask_example",
                    ),
                    type=1,
                ),
            ],
            enable_cluster_destroy=True,
            encryption_config=EncryptionConfigurationParams(
                enable_fips_mode=True,
                enable_hardware_encryption=True,
                enable_software_encryption=True,
                rotation_period=1,
            ),
            ip_preference=1,
            ipmi_config=IpmiConfigurationParams(
                ipmi_gateway="ipmi_gateway_example",
                ipmi_password="ipmi_password_example",
                ipmi_subnet_mask="ipmi_subnet_mask_example",
                ipmi_username="ipmi_username_example",
            ),
            metadata_fault_tolerance=1,
            node_configs=[
                NodeConfigParams(
                    id=1,
                    ip="ip_example",
                    ipmi_ip="ipmi_ip_example",
                    is_compute_node=True,
                ),
            ],
            nodes=[
                ClusterCreateNodeParams(
                    node_id=1,
                    node_ip="node_ip_example",
                ),
            ],
            trust_domain="trust_domain_example",
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
            allow_api_based_fetch=True,
            apps_subnet_ip="apps_subnet_ip_example",
            apps_subnet_ip_v6="apps_subnet_ip_v6_example",
            apps_subnet_mask="apps_subnet_mask_example",
            apps_subnet_mask_v6="apps_subnet_mask_v6_example",
            cluster_destroy_hmac_key="cluster_destroy_hmac_key_example",
            enable_cluster_destroy=True,
            encryption_config=EncryptionConfigurationParams(
                enable_fips_mode=True,
                enable_hardware_encryption=True,
                enable_software_encryption=True,
                rotation_period=1,
            ),
            ip_preference=1,
            metadata_fault_tolerance=1,
            node_configs=[
                NodeConfigParams(
                    id=1,
                    ip="ip_example",
                    ipmi_ip="ipmi_ip_example",
                    is_compute_node=True,
                ),
            ],
            trust_domain="trust_domain_example",
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```VLAN_MODIFY, CLUSTER_CREATE``` <br><br>Create a vlan on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Create an interface group on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_proxy_server**
> ProxyServer create_proxy_server(body)

Creare a proxy server.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Create a proxy server. If a proxy server with given name exists error will be returned.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.proxy_server import ProxyServer
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ProxyServer(
        address="address_example",
        is_disabled=True,
        name="name_example",
        port=1,
        schemes=[
            "schemes_example",
        ],
        services=[
            "services_example",
        ],
        type="type_example",
        username="username_example",
    ) # ProxyServer | Specifies parameters to create the proxy server.

# example passing only required values which don't have defaults set
try:
	# Creare a proxy server.
	api_response = client.platform.create_proxy_server(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->create_proxy_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProxyServer**](ProxyServer.md)| Specifies parameters to create the proxy server. |

### Return type

[**ProxyServer**](ProxyServer.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Create list of racks and optionally also assign list of chassis to each rack

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Delete AMQP target config on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_snapshot_policy**
> delete_cluster_snapshot_policy()

Delete cluster snapshot policy.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Delete cluster snapshot policy.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
> delete_cluster_vlan(vlan_interface_group_name)

Delete vlan

```Unknown Privileges``` <br><br>Delete a vlan on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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


vlan_interface_group_name = "vlanInterfaceGroupName_example" # str | Vlan interface group name, it should be in interface_group_name.vlan_id format.

# example passing only required values which don't have defaults set
try:
	# Delete vlan
	client.platform.delete_cluster_vlan(vlan_interface_group_name)
except ApiException as e:
	print("Exception when calling PlatformApi->delete_cluster_vlan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vlan_interface_group_name** | **str**| Vlan interface group name, it should be in interface_group_name.vlan_id format. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Delete one or more Host Mappings within the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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
        domain_names=[
            "domain_names_example",
        ],
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
> delete_interface_group(name)

Delete interface group

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Delete an interface group on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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


name = "name_example" # str | Name of the interface group.

# example passing only required values which don't have defaults set
try:
	# Delete interface group
	client.platform.delete_interface_group(name)
except ApiException as e:
	print("Exception when calling PlatformApi->delete_interface_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the interface group. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Deletes the provided ipmi user for given node.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_disks**
> ClusterFreeDisks discover_disks()

Discover new disks

**Privileges:** ```CLUSTER_VIEW``` <br><br>Discover disks that are ready for activation

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Turn on/off led light of a disk.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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
        disk_id=1,
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Assimilate list of disks from one or more nodes of cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetch AMQP target config on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get list of all chassis info that are part of cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get a chassis info by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW, TENANT_VIEW``` <br><br>Retrieve some summary information about the Cluster Configuration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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


fetch_stats = True # bool | If 'true', also get statistics about the Cohesity Cluster. (optional)
fetch_time_series_schema = True # bool | Specifies whether to get time series schema info of the cluster (optional)
include_minimum_nodes_info = True # bool | Specifies whether to include info about minimum failure domains (optional)
fetch_patch_info = True # bool | If 'true', return patch information about the Cohesity Cluster. (optional)
fetch_license_info = True # bool | If 'true', return licensing information about the Cohesity Cluster. (optional)
fetch_encryption_info = True # bool | If 'true', return encryption information about the Cohesity Cluster. (optional)
fetch_metadata_info = True # bool | If 'true', return metadata information about the Cohesity Cluster. (optional)
fetch_upgrade_info = True # bool | If 'true', return upgrade information about the Cohesity Cluster. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Retrieve Cluster Configuration
	api_response = client.platform.get_cluster(fetch_stats=fetch_stats, fetch_time_series_schema=fetch_time_series_schema, include_minimum_nodes_info=include_minimum_nodes_info, fetch_patch_info=fetch_patch_info, fetch_license_info=fetch_license_info, fetch_encryption_info=fetch_encryption_info, fetch_metadata_info=fetch_metadata_info, fetch_upgrade_info=fetch_upgrade_info)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fetch_stats** | **bool**| If &#39;true&#39;, also get statistics about the Cohesity Cluster. | [optional]
 **fetch_time_series_schema** | **bool**| Specifies whether to get time series schema info of the cluster | [optional]
 **include_minimum_nodes_info** | **bool**| Specifies whether to include info about minimum failure domains | [optional]
 **fetch_patch_info** | **bool**| If &#39;true&#39;, return patch information about the Cohesity Cluster. | [optional]
 **fetch_license_info** | **bool**| If &#39;true&#39;, return licensing information about the Cohesity Cluster. | [optional]
 **fetch_encryption_info** | **bool**| If &#39;true&#39;, return encryption information about the Cohesity Cluster. | [optional]
 **fetch_metadata_info** | **bool**| If &#39;true&#39;, return metadata information about the Cohesity Cluster. | [optional]
 **fetch_upgrade_info** | **bool**| If &#39;true&#39;, return upgrade information about the Cohesity Cluster. | [optional]

### Return type

[**Cluster**](Cluster.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_ipmi_lan_info**
> ClusterIpmiLanInfo get_cluster_ipmi_lan_info()

To get IPMI LAN info for the cluster

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetches the information about LAN for the cluster in which current node is present.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_ipmi_lan_info import ClusterIpmiLanInfo
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
	# To get IPMI LAN info for the cluster
	api_response = client.platform.get_cluster_ipmi_lan_info()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster_ipmi_lan_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterIpmiLanInfo**](ClusterIpmiLanInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_ipmi_users**
> ClusterIpmiUsers get_cluster_ipmi_users()

To get IPMI users info for the cluster

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetches the information about cluster and node level IPMI user names.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_ipmi_users import ClusterIpmiUsers
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
	# To get IPMI users info for the cluster
	api_response = client.platform.get_cluster_ipmi_users()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster_ipmi_users: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterIpmiUsers**](ClusterIpmiUsers.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetch SID of cluster local domain.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_metadata**
> ClusterMetadataRequest get_cluster_metadata()

Get Cluster Metadata

```No Privileges Required``` <br><br>Get Cluster Metadata.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_metadata_request import ClusterMetadataRequest
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
	# Get Cluster Metadata
	api_response = client.platform.get_cluster_metadata()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster_metadata: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterMetadataRequest**](ClusterMetadataRequest.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_operation_status_list**
> ClusterOperationListResponse get_cluster_operation_status_list()

Get cluster operations status.

```No Privileges Required``` <br><br>Get list of cluster operations status information.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.cluster_operation_list_response import ClusterOperationListResponse
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


operation_types = [
        "Destroy",
    ] # [str] | One or more operation types to query for. (optional)
operation_ids = [
        "operationIds_example",
    ] # [str] | One or more operation ids to query for. (optional)
include_finished_operations = True # bool | Controls whether finished operations should be included in the query results. The default value is false. Applicable only for patch apply, revert, and upgrade operations (optional)
include_event_logs = True # bool | Controls whether event logs should be included in the query results. If set to true, 'operationIds' becomes mandatory. The default value is false. Applicable only for patch apply, revert, and upgrade operations (optional)
start_time = 1 # int | Filters operations that started after the specified time. Applicable only for patch apply, revert, and upgrade operations (optional)
end_time = 1 # int | Filters operations that ended before the specified time. Applicable only for patch apply, revert, and upgrade operations (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get cluster operations status.
	api_response = client.platform.get_cluster_operation_status_list(operation_types=operation_types, operation_ids=operation_ids, include_finished_operations=include_finished_operations, include_event_logs=include_event_logs, start_time=start_time, end_time=end_time)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster_operation_status_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_types** | **[str]**| One or more operation types to query for. | [optional]
 **operation_ids** | **[str]**| One or more operation ids to query for. | [optional]
 **include_finished_operations** | **bool**| Controls whether finished operations should be included in the query results. The default value is false. Applicable only for patch apply, revert, and upgrade operations | [optional]
 **include_event_logs** | **bool**| Controls whether event logs should be included in the query results. If set to true, &#39;operationIds&#39; becomes mandatory. The default value is false. Applicable only for patch apply, revert, and upgrade operations | [optional]
 **start_time** | **int**| Filters operations that started after the specified time. Applicable only for patch apply, revert, and upgrade operations | [optional]
 **end_time** | **int**| Filters operations that ended before the specified time. Applicable only for patch apply, revert, and upgrade operations | [optional]

### Return type

[**ClusterOperationListResponse**](ClusterOperationListResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get software packages on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get cluster snapshot policy.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get the current state of the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_status**
> ClusterStatus get_cluster_status()

Get cluster status.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get cluster status.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_status import ClusterStatus
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
	# Get cluster status.
	api_response = client.platform.get_cluster_status()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterStatus**](ClusterStatus.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_subnets_info**
> [Subnet] get_cluster_subnets_info()

Get cluster subnets info.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get cluster subnet info.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.subnet import Subnet
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
	# Get cluster subnets info.
	api_response = client.platform.get_cluster_subnets_info()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster_subnets_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Subnet]**](Subnet.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_vlan**
> ClusterVlanParams get_cluster_vlan(vlan_interface_group_name)

Get vlan

```Unknown Privileges``` <br><br>Get a vlan on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_vlan_params import ClusterVlanParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


vlan_interface_group_name = "vlanInterfaceGroupName_example" # str | Vlan interface group name, it should be in interface_group_name.vlan_id format.

# example passing only required values which don't have defaults set
try:
	# Get vlan
	api_response = client.platform.get_cluster_vlan(vlan_interface_group_name)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster_vlan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vlan_interface_group_name** | **str**| Vlan interface group name, it should be in interface_group_name.vlan_id format. |

### Return type

[**ClusterVlanParams**](ClusterVlanParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```VLAN_VIEW, CLUSTER_CREATE``` <br><br>Get vlans on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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


vlan_interface_group_names = [
        "vlanInterfaceGroupNames_example",
    ] # [str] | Vlan interface group names, it should be in interface_group_name.vlan_id format. (optional)
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
	api_response = client.platform.get_cluster_vlans(vlan_interface_group_names=vlan_interface_group_names, tenant_ids=tenant_ids, include_tenants=include_tenants, skip_primary_and_bond_iface=skip_primary_and_bond_iface, compress_ips_to_ranges=compress_ips_to_ranges)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_cluster_vlans: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vlan_interface_group_names** | **[str]**| Vlan interface group names, it should be in interface_group_name.vlan_id format. | [optional]
 **tenant_ids** | **[str]**| Ids of the tenants, used to get vlans assigned to tenants. | [optional]
 **include_tenants** | **bool**| If true, the response includes vlans which belongs to all the tenants the current user has permissions to see. | [optional] if omitted the server will use the default value of True
 **skip_primary_and_bond_iface** | **bool**| If true, vlan primary and bond interfaces are not returned in the response. | [optional] if omitted the server will use the default value of False
 **compress_ips_to_ranges** | **bool**| Compress vlan IPs to list of contigous IP ranges with startIp and endIp. | [optional] if omitted the server will use the default value of False

### Return type

[**ClusterVlans**](ClusterVlans.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hardware_info**
> HardwareInfo get_hardware_info()

Fetch Node Hardware Information

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetch general information about the node hardware to which the request is sent to.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.hardware_info import HardwareInfo
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
	# Fetch Node Hardware Information
	api_response = client.platform.get_hardware_info()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_hardware_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**HardwareInfo**](HardwareInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get a list of interface groups configured on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipmi_fru_info**
> IpmiFruInfo get_ipmi_fru_info()

To get IPMI FRU info

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetches the information about FRU for given IPMI

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.ipmi_fru_info import IpmiFruInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


node_id = "nodeId_example" # str, none_type | Specifies the node id of the node for which fru info is requested. This parameter is incompatible with 'nodeIp'. (optional)
node_ip = "nodeIp_example" # str, none_type | Specifies the IP Address of the node for which fru info is requested. This parameter is incompatible with 'nodeId'. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# To get IPMI FRU info
	api_response = client.platform.get_ipmi_fru_info(node_id=node_id, node_ip=node_ip)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_ipmi_fru_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str, none_type**| Specifies the node id of the node for which fru info is requested. This parameter is incompatible with &#39;nodeIp&#39;. | [optional]
 **node_ip** | **str, none_type**| Specifies the IP Address of the node for which fru info is requested. This parameter is incompatible with &#39;nodeId&#39;. | [optional]

### Return type

[**IpmiFruInfo**](IpmiFruInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipmi_lan_info**
> IpmiLanInfo get_ipmi_lan_info()

To get IPMI LAN info

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetches the information about LAN for given IPMI

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.ipmi_lan_info import IpmiLanInfo
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


node_id = "nodeId_example" # str, none_type | Specifies the node id of the node for which lan info is requested. This parameter is incompatible with 'nodeIp'. (optional)
node_ip = "nodeIp_example" # str, none_type | Specifies the IP Address of the node for which lan info is requested. This parameter is incompatible with 'nodeId'. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# To get IPMI LAN info
	api_response = client.platform.get_ipmi_lan_info(node_id=node_id, node_ip=node_ip)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_ipmi_lan_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str, none_type**| Specifies the node id of the node for which lan info is requested. This parameter is incompatible with &#39;nodeIp&#39;. | [optional]
 **node_ip** | **str, none_type**| Specifies the IP Address of the node for which lan info is requested. This parameter is incompatible with &#39;nodeId&#39;. | [optional]

### Return type

[**IpmiLanInfo**](IpmiLanInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipmi_sdr_info**
> IpmiSdrInfo get_ipmi_sdr_info()

To get IPMI SDR Info

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetches the information about SDR info for given IPMI

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.ipmi_sdr_info import IpmiSdrInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


node_id = "nodeId_example" # str, none_type | Specifies the node id of the node for which sdr is requested. This parameter is incompatible with 'nodeIp'. (optional)
node_ip = "nodeIp_example" # str, none_type | Specifies the IP Address of the node for which sdr is requested. This parameter is incompatible with 'nodeId'. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# To get IPMI SDR Info
	api_response = client.platform.get_ipmi_sdr_info(node_id=node_id, node_ip=node_ip)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_ipmi_sdr_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str, none_type**| Specifies the node id of the node for which sdr is requested. This parameter is incompatible with &#39;nodeIp&#39;. | [optional]
 **node_ip** | **str, none_type**| Specifies the IP Address of the node for which sdr is requested. This parameter is incompatible with &#39;nodeId&#39;. | [optional]

### Return type

[**IpmiSdrInfo**](IpmiSdrInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipmi_sel**
> IpmiSel get_ipmi_sel()

To get IPMI SEL

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetches the information about SEL for given IPMI

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.ipmi_sel import IpmiSel
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


node_id = "nodeId_example" # str, none_type | Specifies the node id of the node for which sel is requested. This parameter is incompatible with 'nodeIp'. (optional)
node_ip = "nodeIp_example" # str, none_type | Specifies the IP Address of the node for which sel is requested. This parameter is incompatible with 'nodeId'. (optional)
verbose = True # bool, none_type | Specifies the Verbosity of log produced by sel request. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# To get IPMI SEL
	api_response = client.platform.get_ipmi_sel(node_id=node_id, node_ip=node_ip, verbose=verbose)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_ipmi_sel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str, none_type**| Specifies the node id of the node for which sel is requested. This parameter is incompatible with &#39;nodeIp&#39;. | [optional]
 **node_ip** | **str, none_type**| Specifies the IP Address of the node for which sel is requested. This parameter is incompatible with &#39;nodeId&#39;. | [optional]
 **verbose** | **bool, none_type**| Specifies the Verbosity of log produced by sel request. | [optional]

### Return type

[**IpmiSel**](IpmiSel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipmi_sel_info**
> IpmiSelInfo get_ipmi_sel_info()

To get IPMI SEL Info

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetches the information about SEL info for given IPMI

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.ipmi_sel_info import IpmiSelInfo
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


node_id = "nodeId_example" # str, none_type | Specifies the node id of the node for which sel is requested. This parameter is incompatible with 'nodeIp'. (optional)
node_ip = "nodeIp_example" # str, none_type | Specifies the IP Address of the node for which sel is requested. This parameter is incompatible with 'nodeId'. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# To get IPMI SEL Info
	api_response = client.platform.get_ipmi_sel_info(node_id=node_id, node_ip=node_ip)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_ipmi_sel_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str, none_type**| Specifies the node id of the node for which sel is requested. This parameter is incompatible with &#39;nodeIp&#39;. | [optional]
 **node_ip** | **str, none_type**| Specifies the IP Address of the node for which sel is requested. This parameter is incompatible with &#39;nodeId&#39;. | [optional]

### Return type

[**IpmiSelInfo**](IpmiSelInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipmi_users**
> IpmiUsers get_ipmi_users()

To get IPMI User Info for node

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetches the ipmi user information for given node.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.ipmi_users import IpmiUsers
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


node_id = "nodeId_example" # str, none_type | Specifies the node id of the node for which ipmi users info is requested. This parameter is incompatible with 'nodeIp'. (optional)
node_ip = "nodeIp_example" # str, none_type | Specifies the IP address of the node for which ipmi users info is requested. This parameter is incompatible with 'nodeId'. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# To get IPMI User Info for node
	api_response = client.platform.get_ipmi_users(node_id=node_id, node_ip=node_ip)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_ipmi_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str, none_type**| Specifies the node id of the node for which ipmi users info is requested. This parameter is incompatible with &#39;nodeIp&#39;. | [optional]
 **node_ip** | **str, none_type**| Specifies the IP address of the node for which ipmi users info is requested. This parameter is incompatible with &#39;nodeId&#39;. | [optional]

### Return type

[**IpmiUsers**](IpmiUsers.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get whether the cluster is a DMaaS cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_infra_health_status**
> GetKubernetesStatusResponse get_kubernetes_infra_health_status()

Get Kubernetes Infra Health Status

**Privileges:** ```APPS_MANAGEMENT``` <br><br>Fetches the Kubernetes Infra Health status

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error_response import ErrorResponse
from cohesity_sdk.cluster.model.get_kubernetes_status_response import GetKubernetesStatusResponse
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
	# Get Kubernetes Infra Health Status
	api_response = client.platform.get_kubernetes_infra_health_status()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_kubernetes_infra_health_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetKubernetesStatusResponse**](GetKubernetesStatusResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login_banner**
> LoginBanner get_login_banner()

Get login banner.

```No Privileges Required``` <br><br>Return contents of login banner.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.login_banner import LoginBanner
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
	# Get login banner.
	api_response = client.platform.get_login_banner()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_login_banner: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**LoginBanner**](LoginBanner.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW, CLUSTER_CREATE``` <br><br>Get a list of interfaces present on the node or cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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


node_id = 1 # int | Node id, used to get interfaces on a particular node. (optional)
cache = False # bool | Get interfaces information from cache. (optional) if omitted the server will use the default value of False
bond_interface_only = False # bool | Specifies if only show bond interface info. (optional) if omitted the server will use the default value of False
iface_group_assigned_only = False # bool | Specifies if only show interface group assigned interface info. (optional) if omitted the server will use the default value of False
include_uplink_switch_info = False # bool | Specifies if include uplink switch info. (optional) if omitted the server will use the default value of False
include_bond_slave_details = False # bool | Specifies if include bond secondary detailed info. (optional) if omitted the server will use the default value of False
include_stats = False # bool | Specifies if include stats. (optional) if omitted the server will use the default value of False

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get list of interfaces
	api_response = client.platform.get_network_interfaces(node_id=node_id, cache=cache, bond_interface_only=bond_interface_only, iface_group_assigned_only=iface_group_assigned_only, include_uplink_switch_info=include_uplink_switch_info, include_bond_slave_details=include_bond_slave_details, include_stats=include_stats)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_network_interfaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**| Node id, used to get interfaces on a particular node. | [optional]
 **cache** | **bool**| Get interfaces information from cache. | [optional] if omitted the server will use the default value of False
 **bond_interface_only** | **bool**| Specifies if only show bond interface info. | [optional] if omitted the server will use the default value of False
 **iface_group_assigned_only** | **bool**| Specifies if only show interface group assigned interface info. | [optional] if omitted the server will use the default value of False
 **include_uplink_switch_info** | **bool**| Specifies if include uplink switch info. | [optional] if omitted the server will use the default value of False
 **include_bond_slave_details** | **bool**| Specifies if include bond secondary detailed info. | [optional] if omitted the server will use the default value of False
 **include_stats** | **bool**| Specifies if include stats. | [optional] if omitted the server will use the default value of False

### Return type

[**ClusterInterfaces**](ClusterInterfaces.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Gets the list of Nodes in a cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ntp_servers**
> NtpServerList get_ntp_servers()

Get list of NTP servers.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get list of configured NTP servers.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.ntp_server_list import NtpServerList
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
	# Get list of NTP servers.
	api_response = client.platform.get_ntp_servers()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_ntp_servers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**NtpServerList**](NtpServerList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_proxy_servers**
> ProxyServerList get_proxy_servers()

Get list of proxy servers

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get proxy servers.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.proxy_server_list import ProxyServerList
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
	# Get list of proxy servers
	api_response = client.platform.get_proxy_servers()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_proxy_servers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ProxyServerList**](ProxyServerList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get a rack info by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get list of all racks that are part of cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get remote disks.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_gflags**
> [ServiceGflags] get_service_gflags()

Gets cluster gflags for a service.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Gets the cluster gflags for a service.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.service_gflags import ServiceGflags
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


gflags = [
        "gflags_example",
    ] # [str] | \"Specifies a list of gflag names. If specified, only gflags matching the gflag name list will be returned.\" (optional)
service_name = "kInvalidService" # str | Specifies the service name. If specified, only gflags matching the service name will be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Gets cluster gflags for a service.
	api_response = client.platform.get_service_gflags(gflags=gflags, service_name=service_name)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_service_gflags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gflags** | **[str]**| \&quot;Specifies a list of gflag names. If specified, only gflags matching the gflag name list will be returned.\&quot; | [optional]
 **service_name** | **str**| Specifies the service name. If specified, only gflags matching the service name will be returned. | [optional]

### Return type

[**[ServiceGflags]**](ServiceGflags.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get the SMTP cluster configuration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_software_components**
> SoftwareComponents get_software_components()

Get Software Components

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get software components versions on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.software_components import SoftwareComponents
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
	# Get Software Components
	api_response = client.platform.get_software_components()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_software_components: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SoftwareComponents**](SoftwareComponents.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
> SupportChannel get_support_channel_config()

Get support channel configuration.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get support channel configuration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.support_channel import SupportChannel
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
	# Get support channel configuration.
	api_response = client.platform.get_support_channel_config()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_support_channel_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportChannel**](SupportChannel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sw_update_history**
> GetClusterSWUpdateHistoryResponseParams get_sw_update_history(include_node_history)

Get cluster software history

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get upgrade and patch history of the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.get_cluster_sw_update_history_response_params import GetClusterSWUpdateHistoryResponseParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


include_node_history = True # bool | Flag to specify whether to fetch data from current node or all the nodes. 

# example passing only required values which don't have defaults set
try:
	# Get cluster software history
	api_response = client.platform.get_sw_update_history(include_node_history)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->get_sw_update_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_node_history** | **bool**| Flag to specify whether to fetch data from current node or all the nodes.  |

### Return type

[**GetClusterSWUpdateHistoryResponseParams**](GetClusterSWUpdateHistoryResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Turn on/off LED light of a node to identify.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MAINTENANCE``` <br><br>Import a Crl file into the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get list of local disks.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW, CLUSTER_CREATE``` <br><br>Sends a request to any Node to list all of the free Nodes that are present on the network.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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


ips = [
        "ips_example",
    ] # [str] | \"Specifies a list of ips of nodes among which free and compatible nodes to be returned\" (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List the free Cohesity Nodes present on a network.
	api_response = client.platform.list_free_nodes(ips=ips)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->list_free_nodes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ips** | **[str]**| \&quot;Specifies a list of ips of nodes among which free and compatible nodes to be returned\&quot; | [optional]

### Return type

[**FreeNodes**](FreeNodes.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Lists the host mappings in /etc/hosts of the nodes in a cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_services_states**
> ClusterServicesStates list_services_states()

List services states

**Privileges:** ```CLUSTER_VIEW``` <br><br>List the states of the services on the Cluster

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.cluster_services_states import ClusterServicesStates
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_services_states_params import ClusterServicesStatesParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ClusterServicesStatesParams(
        node_ids=[
            1,
        ],
    ) # ClusterServicesStatesParams | Specifies the parameters to get cluster services states. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List services states
	api_response = client.platform.list_services_states(body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->list_services_states: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterServicesStatesParams**](ClusterServicesStatesParams.md)| Specifies the parameters to get cluster services states. | [optional]

### Return type

[**ClusterServicesStates**](ClusterServicesStates.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_baseos_upgrade**
> MarkBaseosUpgradeInfo mark_baseos_upgrade(body)

Sets/clears the BaseOS upgrade cluster operation.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Sets/clears the BaseOS upgrade cluster operation.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Mark disk for removal or cancel removal if a disk is already marked for removal.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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
        is_clear_pre_check_result_only=False,
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Mark node for removal or Cancel if a node is already marked for removal.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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
        is_clear_pre_check_result_only=False,
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_import_signed_cert**
> NodeCertResult node_import_signed_cert(body)

Import a signed certificate used for n2n communication

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Import a signed certificate.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.node_cert_request import NodeCertRequest
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.node_cert_result import NodeCertResult
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = NodeCertRequest(
        ca_cert="ca_cert_example",
        signed_cert="signed_cert_example",
    ) # NodeCertRequest | The parameters to import the signed cert.

# example passing only required values which don't have defaults set
try:
	# Import a signed certificate used for n2n communication
	api_response = client.platform.node_import_signed_cert(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->node_import_signed_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeCertRequest**](NodeCertRequest.md)| The parameters to import the signed cert. |

### Return type

[**NodeCertResult**](NodeCertResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW, NODE_VIEW``` <br><br>Fetch general information about the node to which the request is sent to.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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
only_check_node_reachability = False # bool | Specifies to show only node reachability details (optional) if omitted the server will use the default value of False

# example passing only required values which don't have defaults set
# and optional values
try:
	# Fetch Node General Information
	api_response = client.platform.node_information(show_services_version_info=show_services_version_info, only_check_node_reachability=only_check_node_reachability)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->node_information: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_services_version_info** | **bool**| Specifies whether to show version info of the services running on the node. | [optional]
 **only_check_node_reachability** | **bool**| Specifies to show only node reachability details | [optional] if omitted the server will use the default value of False

### Return type

[**NodeInfo**](NodeInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_status**
> NodeStatusResult node_status()

Fetch Node status Information

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetch node status details.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.node_status_result import NodeStatusResult
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
	# Fetch Node status Information
	api_response = client.platform.node_status()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->node_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeStatusResult**](NodeStatusResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```PROTECTION_MODIFY``` <br><br>Get the SSH public key corresponding to the private key used by workloads. For example, users may specify multiple scripts which are supposed to be executed on a remote machine at different progress states of a protection group run (for instance - running a script before the run starts and another after the run completes). The public key returned as part of this response should be added on the remote server where the script is to be executed as there is a specific private key used by the workload for remote login.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Describes the structure of SSH public key. |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_proxy_server**
> remove_proxy_server(name)

Remove specified proxy server.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Remove specified proxy server.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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


name = "name_example" # str | Specifies name of the proxy server.

# example passing only required values which don't have defaults set
try:
	# Remove specified proxy server.
	client.platform.remove_proxy_server(name)
except ApiException as e:
	print("Exception when calling PlatformApi->remove_proxy_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies name of the proxy server. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_remote_disk**
> remove_remote_disk(id)

Remove remote disk

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Remove a remote disk.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_ipmi_bmc**
> IpmiTextResponse reset_ipmi_bmc(body)

To reset IPMI BMC for given node

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Resets the ipmi bmc for given node.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.reset_ipmi_bmc_params import ResetIpmiBmcParams
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


body = ResetIpmiBmcParams(
        node_id="node_id_example",
        node_ip="node_ip_example",
    ) # ResetIpmiBmcParams | Specifies the parameters to reset ipmi bmc for given node.

# example passing only required values which don't have defaults set
try:
	# To reset IPMI BMC for given node
	api_response = client.platform.reset_ipmi_bmc(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->reset_ipmi_bmc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetIpmiBmcParams**](ResetIpmiBmcParams.md)| Specifies the parameters to reset ipmi bmc for given node. |

### Return type

[**IpmiTextResponse**](IpmiTextResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_configuration**
> [RestoreConfig] restore_configuration()

Restore configuration.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Config to be restored during one-helios cluster creation.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.restore_config import RestoreConfig
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
	# Restore configuration.
	api_response = client.platform.restore_configuration()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->restore_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[RestoreConfig]**](RestoreConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specifies response of restore config during one-helios cluster create. |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_node_power**
> set_node_power(body)

Reboot or shutdown nodes in cluster.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Reboot or shutdown nodes in cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Enable or Disable Airgap on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Updates AMQP target config on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update selected properties of chassis info by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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
        chassis_node_base=1,
        hardware_model="hardware_model_example",
        id=1,
        location="location_example",
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update the Cluster with the given configuration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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
        aes_encryption_mode="aes_encryption_mode_example",
        amqp_target_config=ClusterAMQPTargetConfig(
            certificate="certificate_example",
            exchange="exchange_example",
            filer_id=1,
            password="password_example",
            server_ip="server_ip_example",
            username="username_example",
            virtual_host="virtual_host_example",
        ),
        apps_subnet=SubnetDefinition(
            component="component_example",
            description="description_example",
            id=1,
            ip="ip_example",
            netmask_bits=1,
            netmask_ip4="netmask_ip4_example",
            nfs_access="kDisabled",
            nfs_all_squash=True,
            nfs_root_squash=True,
            s3_access={},
            smb_access="kDisabled",
            tenant_id="tenant_id_example",
        ),
        assigned_racks_count=1,
        attempt_agent_ports_upgrade=True,
        auth_support_for_pkg_downloads=True,
        auth_type="kPasswordOnly",
        authorized_ssh_public_keys=[
            "authorized_ssh_public_keys_example",
        ],
        available_metadata_space=1,
        banner_enabled=True,
        centralized_patching_enabled=True,
        chassis_count=1,
        cloud_rf1_enabled=True,
        cluster_audit_log_config=ClusterAuditLogConfig(),
        cluster_deployment_type="kStandAlone",
        cluster_software_version="cluster_software_version_example",
        cohesion_cluster_params=CohesionClusterConfigParams(
        ),
        created_time_msecs=1,
        current_op_scheduled_time_secs=1,
        current_operation="kRemoveNode",
        current_time_msecs=1,
        description="description_example",
        disk_count_by_tier=[
            CountByTier(
                disk_count=1,
                storage_tier="PCIeSSD",
            ),
        ],
        dns_server_ips=[
            "dns_server_ips_example",
        ],
        domain_names=[
            "domain_names_example",
        ],
        enable_active_monitoring=True,
        enable_patches_download=True,
        enable_upgrade_pkg_polling=True,
        encryption_key_rotation_period_secs=1,
        eula_config=EulaConfig(
            signed_by_user="signed_by_user_example",
            signed_time=1,
            signed_version=1,
        ),
        fault_tolerance_level="kNode",
        file_services_audit_log_config=AuditLogConfig(
            enabled=True,
            retention_period_days=1,
        ),
        gateway="gateway_example",
        google_analytics_enabled=True,
        hardware_encryption_enabled=True,
        hardware_info=ClusterHardwareInfo(
            hardware_models=[
                "hardware_models_example",
            ],
            hardware_vendors=[
                "hardware_vendors_example",
            ],
        ),
        ip_preference=1,
        is_athena_subnet_clash=True,
        is_cluster_mfa_enabled=True,
        is_documentation_local=True,
        is_patch_apply_aborted=True,
        is_patch_revert_aborted=True,
        is_upgrade_aborted=True,
        kms_server_id=1,
        language_locale="language_locale_example",
        license_state=LicenseState(
            failed_attempts=1,
            state="kInProgressNewCluster",
        ),
        load_balancer_vip_config=LoadBalancerConfig(
            gateway="gateway_example",
            host_name="host_name_example",
            subnet=SubnetDefinition(
                component="component_example",
                description="description_example",
                id=1,
                ip="ip_example",
                netmask_bits=1,
                netmask_ip4="netmask_ip4_example",
                nfs_access="kDisabled",
                nfs_all_squash=True,
                nfs_root_squash=True,
                s3_access={},
                smb_access="kDisabled",
                tenant_id="tenant_id_example",
            ),
            virtual_ip_vec=[
                "virtual_ip_vec_example",
            ],
        ),
        local_auth_domain_name="local_auth_domain_name_example",
        local_groups_enabled=True,
        metadata=ClusterMetadataRequest(
            authentication_methods=ClusterAuthMethodsMetadata(
                external_target_authentication=ExternalTargetAuthMetadata(
                    trusted_profile_id="trusted_profile_id_example",
                ),
                fetch_roles_authentication=ClusterRolesAuthMetadata(
                    trusted_profile_id="trusted_profile_id_example",
                ),
                kms_authentication=KmsAuthMetadata(
                    trusted_profile_id="trusted_profile_id_example",
                ),
            ),
            custom_properties=[
                ClusterCustomMetadata(
                    key="key_example",
                    value="value_example",
                ),
            ],
            docs=[
                ClusterDocsMetadata(
                    purpose="APIDocs",
                    url="url_example",
                ),
            ],
            service_endpoints=[
                ServiceEndpointsMetadata(
                    cloud_service_name="VPC",
                    iam_params=IbmIAMCServiceMetadata(
                        fqdn="fqdn_example",
                    ),
                    vpc_params=IbmVPCServiceMetadata(
                        api_configs=[
                            IbmVPCAPIMetadata(
                                endpoint_suffix="endpoint_suffix_example",
                                version="0480-72-88",
                            ),
                        ],
                        fqdn="fqdn_example",
                    ),
                ),
            ],
            sla=ClusterSLAMetadata(
                default_sla=1,
                minimum_sla=1,
            ),
        ),
        metadata_fault_tolerance_factor=1,
        minimum_failure_domains_needed=1,
        multi_tenancy_enabled=True,
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
            vips=[
                "vips_example",
            ],
        ),
        node_count=1,
        node_ips="node_ips_example",
        ntp_settings=NTPSettings(
            ntp_authentication_enabled=True,
            ntp_servers_internal=True,
        ),
        patch_apply_failure_error_message="patch_apply_failure_error_message_example",
        patch_revert_failure_error_message="patch_revert_failure_error_message_example",
        patch_revert_version="patch_revert_version_example",
        patch_target_version="patch_target_version_example",
        patch_v2_reverts_allowed=True,
        patch_version="patch_version_example",
        pcie_ssd_tier_rebalance_delay_secs=1,
        proto_rpc_encryption_enabled=True,
        proxy_server_config=ClusterProxyServerConfig(
            ip="ip_example",
            is_disabled=True,
            password="password_example",
            port=1,
            username="username_example",
        ),
        proxy_vm_subnet="proxy_vm_subnet_example",
        reverse_tunnel_enabled=True,
        reverse_tunnel_end_time_msecs=1,
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
        s3_virtual_hosted_domain_names=[
            "s3_virtual_hosted_domain_names_example",
        ],
        sata_hdd_tier_admission_control=1,
        schema_info_list=[
            SchemaInfo(
                entity_id="entity_id_example",
                key="key_example",
                metric_name="metric_name_example",
                schema_name="schema_name_example",
            ),
        ],
        security_mode_dod=True,
        smb_ad_disabled=True,
        smb_multichannel_enabled=True,
        software_type="kRegular",
        split_key_host_access=True,
        stats=ClusterStats(
            cloud_usage_perf_stats=UsageAndPerformanceStats(
                data_in_bytes=1,
                data_in_bytes_after_reduction=1,
                min_usable_physical_capacity_bytes=1,
                num_bytes_read=1,
                num_bytes_written=1,
                physical_capacity_bytes=1,
                read_ios=1,
                read_latency_msecs=3.14,
                system_capacity_bytes=1,
                system_usage_bytes=1,
                total_physical_raw_usage_bytes=1,
                total_physical_usage_bytes=1,
                write_ios=1,
                write_latency_msecs=3.14,
            ),
            data_reduction_ratio=3.14,
            data_usage_stats=DataUsageStatsDefinition(
                cloud_data_written_bytes=1,
                cloud_data_written_bytes_timestamp_usec=1,
                cloud_total_physical_usage_bytes=1,
                cloud_total_physical_usage_bytes_timestamp_usec=1,
                data_in_bytes=1,
                data_in_bytes_after_dedup=1,
                data_in_bytes_after_dedup_timestamp_usec=1,
                data_in_bytes_prev=1,
                data_in_bytes_prev_timestamp_usec=1,
                data_in_bytes_timestamp_usec=1,
                data_protect_logical_usage_bytes=1,
                data_protect_logical_usage_bytes_timestamp_usec=1,
                data_protect_physical_usage_bytes=1,
                data_protect_physical_usage_bytes_timestamp_usec=1,
                data_written_bytes=1,
                data_written_bytes_prev=1,
                data_written_bytes_prev_timestamp_usec=1,
                data_written_bytes_timestamp_usec=1,
                file_services_logical_usage_bytes=1,
                file_services_logical_usage_bytes_timestamp_usec=1,
                file_services_physical_usage_bytes=1,
                file_services_physical_usage_bytes_timestamp_usec=1,
                local_data_written_bytes=1,
                local_data_written_bytes_timestamp_usec=1,
                local_tier_resiliency_impact_bytes=1,
                local_tier_resiliency_impact_bytes_prev=1,
                local_tier_resiliency_impact_bytes_prev_timestamp_usec=1,
                local_tier_resiliency_impact_bytes_timestamp_usec=1,
                local_total_physical_usage_bytes=1,
                local_total_physical_usage_bytes_timestamp_usec=1,
                num_directories=1,
                num_directories_prev=1,
                num_files=1,
                num_files_prev=1,
                outdated_logical_usage_bytes=1,
                outdated_logical_usage_bytes_timestamp_usec=1,
                storage_consumed_bytes=1,
                storage_consumed_bytes_prev=1,
                storage_consumed_bytes_prev_timestamp_usec=1,
                storage_consumed_bytes_timestamp_usec=1,
                total_logical_usage_bytes=1,
                total_logical_usage_bytes_timestamp_usec=1,
                unique_physical_data_bytes=1,
                unique_physical_data_bytes_timestamp_usec=1,
            ),
            id=1,
            local_usage_perf_stats=UsageAndPerformanceStats(
                data_in_bytes=1,
                data_in_bytes_after_reduction=1,
                min_usable_physical_capacity_bytes=1,
                num_bytes_read=1,
                num_bytes_written=1,
                physical_capacity_bytes=1,
                read_ios=1,
                read_latency_msecs=3.14,
                system_capacity_bytes=1,
                system_usage_bytes=1,
                total_physical_raw_usage_bytes=1,
                total_physical_usage_bytes=1,
                write_ios=1,
                write_latency_msecs=3.14,
            ),
            logical_stats=LogicalStats(
                total_logical_usage_bytes=1,
            ),
            usage_perf_stats=UsageAndPerformanceStats(
                data_in_bytes=1,
                data_in_bytes_after_reduction=1,
                min_usable_physical_capacity_bytes=1,
                num_bytes_read=1,
                num_bytes_written=1,
                physical_capacity_bytes=1,
                read_ios=1,
                read_latency_msecs=3.14,
                system_capacity_bytes=1,
                system_usage_bytes=1,
                total_physical_raw_usage_bytes=1,
                total_physical_usage_bytes=1,
                write_ios=1,
                write_latency_msecs=3.14,
            ),
        ),
        supported_config=SupportedConfig(
            min_nodes_allowed=1,
            supported_erasure_coding=[
                "supported_erasure_coding_example",
            ],
        ),
        target_software_version="target_software_version_example",
        tenant_viewbox_sharing_enabled=True,
        tiering_audit_log_config=AuditLogConfig(
            enabled=True,
            retention_period_days=1,
        ),
        timezone="timezone_example",
        trust_domain="trust_domain_example",
        turbo_mode=True,
        upgrade_failure_error_string="upgrade_failure_error_string_example",
        use_default_agent_ports=True,
        use_heimdall=True,
        used_metadata_space_pct=3.14,
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_ipmi_lan_info**
> IpmiTextResponse update_cluster_ipmi_lan_info(body)

To update IPMI LAN info for the cluster

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Updates the information about LAN for the cluster in which current node is present.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.ipmi_text_response import IpmiTextResponse
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_ipmi_lan_info import ClusterIpmiLanInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ClusterIpmiLanInfo(
        cluster_ipmi_gateway="cluster_ipmi_gateway_example",
        cluster_ipmi_subnet_mask="cluster_ipmi_subnet_mask_example",
        node_ipmi_entries=[
            NodeIpmiInfoEntry(
                node_ip="node_ip_example",
                node_ipmi_gateway="node_ipmi_gateway_example",
                node_ipmi_ip="node_ipmi_ip_example",
                node_ipmi_subnet_mask="node_ipmi_subnet_mask_example",
            ),
        ],
    ) # ClusterIpmiLanInfo | Specifies the parameters to update the information about LAN for the cluster in which current node is present.

# example passing only required values which don't have defaults set
try:
	# To update IPMI LAN info for the cluster
	api_response = client.platform.update_cluster_ipmi_lan_info(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_cluster_ipmi_lan_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterIpmiLanInfo**](ClusterIpmiLanInfo.md)| Specifies the parameters to update the information about LAN for the cluster in which current node is present. |

### Return type

[**IpmiTextResponse**](IpmiTextResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update cluster snapshot policy.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_software**
> ClusterSWUpdateResponseParams update_cluster_software(body)

Update cluster software

**Privileges:** ```CLUSTER_UPGRADE, CLUSTER_MAINTENANCE``` <br><br>Update the software on the cluster through upgrade and/or patch.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.cluster_sw_update_response_params import ClusterSWUpdateResponseParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cluster_sw_update_params import ClusterSWUpdateParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ClusterSWUpdateParams(
        assess_software_update_params=AssessSoftwareUpdateParams(
            package_type="Upgrade",
            phase="Pre",
            version_name="version_name_example",
        ),
        node_type="ClusterNode",
        operation_type="DownloadUpgradePackage",
        patch_params=PatchParams(
            abort_on_pre_checks_failure=True,
            apply_patch_in_parallel=False,
            node_ids=[
                1,
            ],
            package_url=ArtifactUrl(
                auth_headers=[
                    AuthHeader(
                        key="key_example",
                        value="value_example",
                    ),
                ],
                url="url_example",
            ),
            version_name="version_name_example",
        ),
        upgrade_params=UpgradeParams(
            abort_on_pre_checks_failure=True,
            auto_agent_upgrade=True,
            ignore_sw_incompatibility=False,
            md5_sum="md5_sum_example",
            package_url=ArtifactUrl(
                auth_headers=[
                    AuthHeader(
                        key="key_example",
                        value="value_example",
                    ),
                ],
                url="url_example",
            ),
            run_upgrade_in_parallel=False,
            version_name="version_name_example",
        ),
    ) # ClusterSWUpdateParams | The parameters to update the software on the cluster.

# example passing only required values which don't have defaults set
try:
	# Update cluster software
	api_response = client.platform.update_cluster_software(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_cluster_software: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterSWUpdateParams**](ClusterSWUpdateParams.md)| The parameters to update the software on the cluster. |

### Return type

[**ClusterSWUpdateResponseParams**](ClusterSWUpdateResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_subnets**
> [Subnet] update_cluster_subnets(body)

Update the Cluster Subnets

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update the cluster subnet Info

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.subnet import Subnet
from cohesity_sdk.cluster.model.update_cluster_subnets_params import UpdateClusterSubnetsParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = UpdateClusterSubnetsParams(
        cluster_subnets=[
            Subnet(
                component="component_example",
                description="description_example",
                gateway="gateway_example",
                id=1,
                ip="ip_example",
                netmask_bits=1,
                netmask_ip4="netmask_ip4_example",
                nfs_access="kDisabled",
                nfs_squash="kNone",
                s3_access="kDisabled",
                smb_access="kDisabled",
            ),
        ],
    ) # UpdateClusterSubnetsParams | 

# example passing only required values which don't have defaults set
try:
	# Update the Cluster Subnets
	api_response = client.platform.update_cluster_subnets(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_cluster_subnets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateClusterSubnetsParams**](UpdateClusterSubnetsParams.md)|  |

### Return type

[**[Subnet]**](Subnet.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_vlan**
> ClusterVlanParams update_cluster_vlan(vlan_interface_group_name, body)

Update vlan

```Unknown Privileges``` <br><br>Update a vlan on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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


vlan_interface_group_name = "vlanInterfaceGroupName_example" # str | Vlan interface group name, it should be in interface_group_name.vlan_id format.
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
        gateway_v6="gateway_v6_example",
        interface_name="interface_name_example",
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
        loopback_interface_group_id=1,
        mtu=1,
        subnet="subnet_example",
        subnet_v6="subnet_v6_example",
        tenant_id="tenant_id_example",
        vlan_name="vlan_name_example",
    ) # UpdateClusterVlanParams | Parameters to update vlan on the cluster.

# example passing only required values which don't have defaults set
try:
	# Update vlan
	api_response = client.platform.update_cluster_vlan(vlan_interface_group_name, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_cluster_vlan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vlan_interface_group_name** | **str**| Vlan interface group name, it should be in interface_group_name.vlan_id format. |
 **body** | [**UpdateClusterVlanParams**](UpdateClusterVlanParams.md)| Parameters to update vlan on the cluster. |

### Return type

[**ClusterVlanParams**](ClusterVlanParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update a feature flag override status to cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Updates Host Mapping on the Cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
> InterfaceGroup update_interface_group(name, body)

Update interface group

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update an interface group on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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


name = "name_example" # str | Name of the interface group.
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
	api_response = client.platform.update_interface_group(name, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_interface_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the interface group. |
 **body** | [**InterfaceGroupParams**](InterfaceGroupParams.md)| Parameters to update an interface group on the cluster. |

### Return type

[**InterfaceGroup**](InterfaceGroup.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ipmi_user**
> IpmiTextResponse update_ipmi_user(body)

To update IPMI User Info for node

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Updates the ipmi user information for given node.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.ipmi_text_response import IpmiTextResponse
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.update_ipmi_user import UpdateIpmiUser
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = UpdateIpmiUser(
        node_id="node_id_example",
        node_ip="node_ip_example",
        password="password_example",
        username="username_example",
    ) # UpdateIpmiUser | Specifies the parameters to add an ipmi user to node.

# example passing only required values which don't have defaults set
try:
	# To update IPMI User Info for node
	api_response = client.platform.update_ipmi_user(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_ipmi_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateIpmiUser**](UpdateIpmiUser.md)| Specifies the parameters to add an ipmi user to node. |

### Return type

[**IpmiTextResponse**](IpmiTextResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update whether the cluster is a DMaaS cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_login_banner**
> LoginBanner update_login_banner(body)

Update login banner.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update contents of login banner. Setting the banner content to an empty string disables the banner.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.login_banner import LoginBanner
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = LoginBanner(
        content="content_example",
        is_enabled=True,
    ) # LoginBanner | Specifies text to update the login banner.

# example passing only required values which don't have defaults set
try:
	# Update login banner.
	api_response = client.platform.update_login_banner(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_login_banner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginBanner**](LoginBanner.md)| Specifies text to update the login banner. |

### Return type

[**LoginBanner**](LoginBanner.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ntp_servers**
> NtpServerList update_ntp_servers(body)

Update NTP servers.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update configuration of one or more NTP servers. Specified list of NTP servers will replace the currently configured NTP servers.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.ntp_server_list import NtpServerList
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = NtpServerList(
        ntp_authentication_enabled=True,
        ntp_server_auth_info=[
            NtpAuthKeyInfo(
                ntp_server_address="ntp_server_address_example",
                ntp_server_auth_key_encryption_algorithm="SHA1",
                ntp_server_auth_key_id=1,
                ntp_server_auth_key_value="ntp_server_auth_key_value_example",
            ),
        ],
        ntp_servers=[
            "ntp_servers_example",
        ],
    ) # NtpServerList | Specifies parameters to update NTP sever configuration.

# example passing only required values which don't have defaults set
try:
	# Update NTP servers.
	api_response = client.platform.update_ntp_servers(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_ntp_servers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NtpServerList**](NtpServerList.md)| Specifies parameters to update NTP sever configuration. |

### Return type

[**NtpServerList**](NtpServerList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_proxy_server**
> ProxyServer update_proxy_server(name, body)

Update specified proxy server.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update specified proxy server. If a proxy server with given name exists, it will be updated else error will be returned.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.proxy_server import ProxyServer
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


name = "name_example" # str | Specifies name of the proxy server.
body = ProxyServer(
        address="address_example",
        is_disabled=True,
        name="name_example",
        port=1,
        schemes=[
            "schemes_example",
        ],
        services=[
            "services_example",
        ],
        type="type_example",
        username="username_example",
    ) # ProxyServer | Specifies parameters to update the proxy server.

# example passing only required values which don't have defaults set
try:
	# Update specified proxy server.
	api_response = client.platform.update_proxy_server(name, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_proxy_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies name of the proxy server. |
 **body** | [**ProxyServer**](ProxyServer.md)| Specifies parameters to update the proxy server. |

### Return type

[**ProxyServer**](ProxyServer.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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



**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update selected properties of a rack given by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Updates list of racks with name, chassis list or/and location

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_restore_configuration**
> [RestoreConfig] update_restore_configuration(body)

Update Restore configuration.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update the restore config for one-helios cluster restore.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.restore_config_payload import RestoreConfigPayload
from cohesity_sdk.cluster.model.restore_config import RestoreConfig
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = RestoreConfigPayload(
        object_path=ObjectPath(
            data_store_path=DataStorePath(
                elastic="elastic_example",
                mongo="mongo_example",
                postgres="postgres_example",
            ),
            default_path="default_path_example",
        ),
        s3_config=S3RestoreConfig(
            access_key="access_key_example",
            bucket="bucket_example",
            host="host_example",
            region="region_example",
            secret_key="secret_key_example",
        ),
    ) # RestoreConfigPayload | 

# example passing only required values which don't have defaults set
try:
	# Update Restore configuration.
	api_response = client.platform.update_restore_configuration(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_restore_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestoreConfigPayload**](RestoreConfigPayload.md)|  |

### Return type

[**[RestoreConfig]**](RestoreConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specifies response of restore config during one-helios cluster create. |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_gflags**
> [ServiceGflags] update_service_gflags(body)

Update the gflags

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Updates the gflags for a service on the Cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.update_gflag_parameters import UpdateGflagParameters
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.service_gflags import ServiceGflags
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = UpdateGflagParameters(
        effective_now=True,
        reason="reason_example",
        service_flags=ServiceGflags(
            gflags=[
                Gflag(
                    clear=False,
                    name="name_example",
                    product_model="product_model_example",
                    reason="reason_example",
                    timestamp=1,
                    value="value_example",
                ),
            ],
            service_name="kInvalidService",
        ),
        skip_existence_check=True,
    ) # UpdateGflagParameters | 

# example passing only required values which don't have defaults set
try:
	# Update the gflags
	api_response = client.platform.update_service_gflags(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->update_service_gflags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateGflagParameters**](UpdateGflagParameters.md)|  |

### Return type

[**[ServiceGflags]**](ServiceGflags.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update SMTP configuration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update support channel configuration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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
        enable_extension=True,
        end_time_usecs=1,
        extension_duration_hours=1,
        force_enable_reverse_tunnel=True,
        is_enabled=True,
        node_ids=[
            1,
        ],
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get upgrade checks results. This API will be deprecated.  Use [GetClusterOperationStatusList](#tag/Platform/operation/GetClusterOperationStatusList) with `AssessSoftwareUpdate` operationType query. 

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY, CLUSTER_UPGRADE``` <br><br>Run upgrade checks on cluster. This API will be deprecated.  Use [UpdateClusterSoftware](#tag/Platform/operation/UpdateClusterSoftware) with `AssessSoftwareUpdate` operationType. 

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_nodes**
> NodeUpgradeResult upgrade_nodes(body)

Upgrade a free node.

**Privileges:** ```CLUSTER_CREATE``` <br><br>Upgrade a free Node.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.node_upgrade_parameters import NodeUpgradeParameters
from cohesity_sdk.cluster.model.node_upgrade_result import NodeUpgradeResult
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = NodeUpgradeParameters(
        node_ids=[
            1,
        ],
        target_sw_version="target_sw_version_example",
        upgrade_all_free_nodes=True,
        upgrade_self=True,
    ) # NodeUpgradeParameters | The parameters to upgrade free node(s).

# example passing only required values which don't have defaults set
try:
	# Upgrade a free node.
	api_response = client.platform.upgrade_nodes(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->upgrade_nodes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeUpgradeParameters**](NodeUpgradeParameters.md)| The parameters to upgrade free node(s). |

### Return type

[**NodeUpgradeResult**](NodeUpgradeResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

Upload package by files

**Privileges:** ```CLUSTER_UPGRADE, CLUSTER_MAINTENANCE``` <br><br>Upload upgrade/patch package.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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


package_file = open('/path/to/file', 'rb') # file_type | Binary content of the file.
package_type = "Upgrade" # str | Package Type. (optional) if omitted the server will use the default value of "Upgrade"

# example passing only required values which don't have defaults set
try:
	# Upload package by files
	client.platform.upload_file_package(package_file)
except ApiException as e:
	print("Exception when calling PlatformApi->upload_file_package: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Upload package by files
	client.platform.upload_file_package(package_file, package_type=package_type)
except ApiException as e:
	print("Exception when calling PlatformApi->upload_file_package: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_file** | **file_type**| Binary content of the file. |
 **package_type** | **str**| Package Type. | [optional] if omitted the server will use the default value of "Upgrade"

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_smtp_configuration**
> validate_smtp_configuration(body)

Validate SMTP configuration.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Validate SMTP configuration by sending a test email.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_ipmi_user**
> IpmiTextResponse verify_ipmi_user(body)

To verify IPMI User with Password for node

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Verifies the ipmi user with password information for given node.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.ipmi_text_response import IpmiTextResponse
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.verify_ipmi_user import VerifyIpmiUser
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = VerifyIpmiUser(
        node_id="node_id_example",
        node_ip="node_ip_example",
        password="password_example",
        username="username_example",
    ) # VerifyIpmiUser | Specifies the parameters to add an ipmi user to node.

# example passing only required values which don't have defaults set
try:
	# To verify IPMI User with Password for node
	api_response = client.platform.verify_ipmi_user(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PlatformApi->verify_ipmi_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyIpmiUser**](VerifyIpmiUser.md)| Specifies the parameters to add an ipmi user to node. |

### Return type

[**IpmiTextResponse**](IpmiTextResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

