# cohesity_sdk.cluster.PlatformApi

All URIs are relative to */v2*

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.host_entry import HostEntry
from cohesity_sdk.cluster.models.host_mappings import HostMappings
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = [cohesity_sdk.cluster.HostEntry()] # List[HostEntry] | Specifies the request to add entries to /etc/hosts

    try:
        # Create Cluster Host Mappings
        api_response = api_instance.add_hosts(body)
        print("The response of PlatformApi->add_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->add_hosts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**List[HostEntry]**](HostEntry.md)| Specifies the request to add entries to /etc/hosts | 

### Return type

[**HostMappings**](HostMappings.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.add_remote_disk_response_body import AddRemoteDiskResponseBody
from cohesity_sdk.cluster.models.remote_disks import RemoteDisks
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.RemoteDisks() # RemoteDisks | Specifies the remote disk configuration.

    try:
        # Add remote disk
        api_response = api_instance.add_remote_disk(body)
        print("The response of PlatformApi->add_remote_disk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->add_remote_disk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoteDisks**](RemoteDisks.md)| Specifies the remote disk configuration. | 

### Return type

[**AddRemoteDiskResponseBody**](AddRemoteDiskResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.change_services_states_params import ChangeServicesStatesParams
from cohesity_sdk.cluster.models.change_services_states_result import ChangeServicesStatesResult
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.ChangeServicesStatesParams() # ChangeServicesStatesParams | Specifies the parameters to change cluster services states.

    try:
        # Change cluster services states.
        api_response = api_instance.change_services_states(body)
        print("The response of PlatformApi->change_services_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->change_services_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangeServicesStatesParams**](ChangeServicesStatesParams.md)| Specifies the parameters to change cluster services states. | 

### Return type

[**ChangeServicesStatesResult**](ChangeServicesStatesResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Clear SMTP configuration.
        api_instance.clear_smtp_configuration()
    except Exception as e:
        print("Exception when calling PlatformApi->clear_smtp_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_delete_ipmi_users import ClusterDeleteIpmiUsers
from cohesity_sdk.cluster.models.ipmi_text_response import IpmiTextResponse
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.ClusterDeleteIpmiUsers() # ClusterDeleteIpmiUsers | Specifies the parameters to delete cluster ipmi users.

    try:
        # To delete IPMI Users for cluster
        api_response = api_instance.cluster_delete_ipmi_users(body)
        print("The response of PlatformApi->cluster_delete_ipmi_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->cluster_delete_ipmi_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterDeleteIpmiUsers**](ClusterDeleteIpmiUsers.md)| Specifies the parameters to delete cluster ipmi users. | 

### Return type

[**IpmiTextResponse**](IpmiTextResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_update_ipmi_users import ClusterUpdateIpmiUsers
from cohesity_sdk.cluster.models.ipmi_text_response import IpmiTextResponse
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.ClusterUpdateIpmiUsers() # ClusterUpdateIpmiUsers | Specifies the parameters to update cluster ipmi users.

    try:
        # To update IPMI Users for cluster
        api_response = api_instance.cluster_update_ipmi_users(body)
        print("The response of PlatformApi->cluster_update_ipmi_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->cluster_update_ipmi_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterUpdateIpmiUsers**](ClusterUpdateIpmiUsers.md)| Specifies the parameters to update cluster ipmi users. | 

### Return type

[**IpmiTextResponse**](IpmiTextResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.create_bond_params import CreateBondParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.CreateBondParams() # CreateBondParams | Parameters to create bond.

    try:
        # Create a new network bond.
        api_response = api_instance.create_bond(body)
        print("The response of PlatformApi->create_bond:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->create_bond: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBondParams**](CreateBondParams.md)| Parameters to create bond. | 

### Return type

[**CreateBondParams**](CreateBondParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster import Cluster
from cohesity_sdk.cluster.models.create_cluster_params import CreateClusterParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.CreateClusterParams() # CreateClusterParams | Specifies the parameters to create cluster.

    try:
        # Create a cluster.
        api_response = api_instance.create_cluster(body)
        print("The response of PlatformApi->create_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->create_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateClusterParams**](CreateClusterParams.md)| Specifies the parameters to create cluster. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_vlan_params import ClusterVlanParams
from cohesity_sdk.cluster.models.create_cluster_vlan_params import CreateClusterVlanParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.CreateClusterVlanParams() # CreateClusterVlanParams | Parameters to create a vlan.

    try:
        # Create vlan
        api_response = api_instance.create_cluster_vlan(body)
        print("The response of PlatformApi->create_cluster_vlan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->create_cluster_vlan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateClusterVlanParams**](CreateClusterVlanParams.md)| Parameters to create a vlan. | 

### Return type

[**ClusterVlanParams**](ClusterVlanParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.interface_group import InterfaceGroup
from cohesity_sdk.cluster.models.interface_group_params import InterfaceGroupParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.InterfaceGroupParams() # InterfaceGroupParams | Parameters to create an interface group.

    try:
        # Create interface group
        api_response = api_instance.create_interface_group(body)
        print("The response of PlatformApi->create_interface_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->create_interface_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InterfaceGroupParams**](InterfaceGroupParams.md)| Parameters to create an interface group. | 

### Return type

[**InterfaceGroup**](InterfaceGroup.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.proxy_server import ProxyServer
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.ProxyServer() # ProxyServer | Specifies parameters to create the proxy server.

    try:
        # Creare a proxy server.
        api_response = api_instance.create_proxy_server(body)
        print("The response of PlatformApi->create_proxy_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->create_proxy_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **ProxyServer**| Specifies parameters to create the proxy server. | 

### Return type

[**ProxyServer**](ProxyServer.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.racks import Racks
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.Racks() # Racks | Specifies the parameters to create racks.

    try:
        # Create racks
        api_response = api_instance.create_racks(body)
        print("The response of PlatformApi->create_racks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->create_racks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Racks**](Racks.md)| Specifies the parameters to create racks. | 

### Return type

[**Racks**](Racks.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Delete AMQP Target Config
        api_instance.delete_amqp_target_config()
    except Exception as e:
        print("Exception when calling PlatformApi->delete_amqp_target_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Delete cluster snapshot policy.
        api_instance.delete_cluster_snapshot_policy()
    except Exception as e:
        print("Exception when calling PlatformApi->delete_cluster_snapshot_policy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    vlan_interface_group_name = 'vlan_interface_group_name_example' # str | Vlan interface group name, it should be in interface_group_name.vlan_id format.

    try:
        # Delete vlan
        api_instance.delete_cluster_vlan(vlan_interface_group_name)
    except Exception as e:
        print("Exception when calling PlatformApi->delete_cluster_vlan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vlan_interface_group_name** | **str**| Vlan interface group name, it should be in interface_group_name.vlan_id format. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.delete_hosts_parameters import DeleteHostsParameters
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.DeleteHostsParameters() # DeleteHostsParameters | Specifies the params to delete host mappings

    try:
        # Deletes multiple Host Mappings within the cluster
        api_instance.delete_hosts(body)
    except Exception as e:
        print("Exception when calling PlatformApi->delete_hosts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteHostsParameters**](DeleteHostsParameters.md)| Specifies the params to delete host mappings | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    name = 'name_example' # str | Name of the interface group.

    try:
        # Delete interface group
        api_instance.delete_interface_group(name)
    except Exception as e:
        print("Exception when calling PlatformApi->delete_interface_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the interface group. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.delete_ipmi_user import DeleteIpmiUser
from cohesity_sdk.cluster.models.ipmi_text_response import IpmiTextResponse
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.DeleteIpmiUser() # DeleteIpmiUser | Specifies the parameters to delete an ipmi user from given node.

    try:
        # To delete IPMI User for node
        api_response = api_instance.delete_ipmi_user(body)
        print("The response of PlatformApi->delete_ipmi_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->delete_ipmi_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteIpmiUser**](DeleteIpmiUser.md)| Specifies the parameters to delete an ipmi user from given node. | 

### Return type

[**IpmiTextResponse**](IpmiTextResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_free_disks import ClusterFreeDisks
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Discover new disks
        api_response = api_instance.discover_disks()
        print("The response of PlatformApi->discover_disks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->discover_disks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterFreeDisks**](ClusterFreeDisks.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.disk_identify import DiskIdentify
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.DiskIdentify() # DiskIdentify | Specifies the parameter to identify disk.

    try:
        # Identify a disk
        api_response = api_instance.disk_identify(body)
        print("The response of PlatformApi->disk_identify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->disk_identify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DiskIdentify**](DiskIdentify.md)| Specifies the parameter to identify disk. | 

### Return type

[**DiskIdentify**](DiskIdentify.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_free_disks import ClusterFreeDisks
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.ClusterFreeDisks() # ClusterFreeDisks | Specifies the parameter to assimilate disks.

    try:
        # Assimilate disks.
        api_response = api_instance.disks_assimilate(body)
        print("The response of PlatformApi->disks_assimilate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->disks_assimilate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterFreeDisks**](ClusterFreeDisks.md)| Specifies the parameter to assimilate disks. | 

### Return type

[**ClusterFreeDisks**](ClusterFreeDisks.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_amqp_target_config import ClusterAMQPTargetConfig
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Get AMQP Target Config
        api_response = api_instance.get_amqp_target_config()
        print("The response of PlatformApi->get_amqp_target_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_amqp_target_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterAMQPTargetConfig**](ClusterAMQPTargetConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> ChassisList get_chassis(no_rack_assigned=no_rack_assigned)

Get list of chassis

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get list of all chassis info that are part of cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.chassis_list import ChassisList
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    no_rack_assigned = True # bool | Filters chassis that have no rack assigned. (optional)

    try:
        # Get list of chassis
        api_response = api_instance.get_chassis(no_rack_assigned=no_rack_assigned)
        print("The response of PlatformApi->get_chassis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_chassis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **no_rack_assigned** | **bool**| Filters chassis that have no rack assigned. | [optional] 

### Return type

[**ChassisList**](ChassisList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.chassis import Chassis
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    id = 56 # int | Specifies the id of chassis.

    try:
        # Get a chassis by chassis id.
        api_response = api_instance.get_chassis_by_id(id)
        print("The response of PlatformApi->get_chassis_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_chassis_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of chassis. | 

### Return type

[**Chassis**](Chassis.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> Cluster get_cluster(fetch_stats=fetch_stats, fetch_time_series_schema=fetch_time_series_schema, include_minimum_nodes_info=include_minimum_nodes_info, fetch_patch_info=fetch_patch_info, fetch_license_info=fetch_license_info, fetch_encryption_info=fetch_encryption_info, fetch_metadata_info=fetch_metadata_info, fetch_upgrade_info=fetch_upgrade_info)

Retrieve Cluster Configuration

**Privileges:** ```CLUSTER_VIEW, TENANT_VIEW``` <br><br>Retrieve some summary information about the Cluster Configuration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster import Cluster
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    fetch_stats = True # bool | If 'true', also get statistics about the Cohesity Cluster. (optional)
    fetch_time_series_schema = True # bool | Specifies whether to get time series schema info of the cluster (optional)
    include_minimum_nodes_info = True # bool | Specifies whether to include info about minimum failure domains (optional)
    fetch_patch_info = True # bool | If 'true', return patch information about the Cohesity Cluster. (optional)
    fetch_license_info = True # bool | If 'true', return licensing information about the Cohesity Cluster. (optional)
    fetch_encryption_info = True # bool | If 'true', return encryption information about the Cohesity Cluster. (optional)
    fetch_metadata_info = True # bool | If 'true', return metadata information about the Cohesity Cluster. (optional)
    fetch_upgrade_info = True # bool | If 'true', return upgrade information about the Cohesity Cluster. (optional)

    try:
        # Retrieve Cluster Configuration
        api_response = api_instance.get_cluster(fetch_stats=fetch_stats, fetch_time_series_schema=fetch_time_series_schema, include_minimum_nodes_info=include_minimum_nodes_info, fetch_patch_info=fetch_patch_info, fetch_license_info=fetch_license_info, fetch_encryption_info=fetch_encryption_info, fetch_metadata_info=fetch_metadata_info, fetch_upgrade_info=fetch_upgrade_info)
        print("The response of PlatformApi->get_cluster:\n")
        pprint(api_response)
    except Exception as e:
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

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_ipmi_lan_info import ClusterIpmiLanInfo
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # To get IPMI LAN info for the cluster
        api_response = api_instance.get_cluster_ipmi_lan_info()
        print("The response of PlatformApi->get_cluster_ipmi_lan_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_cluster_ipmi_lan_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterIpmiLanInfo**](ClusterIpmiLanInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_ipmi_users import ClusterIpmiUsers
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # To get IPMI users info for the cluster
        api_response = api_instance.get_cluster_ipmi_users()
        print("The response of PlatformApi->get_cluster_ipmi_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_cluster_ipmi_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterIpmiUsers**](ClusterIpmiUsers.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_local_domain_sid import ClusterLocalDomainSID
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Get Cluster Local Domain SID
        api_response = api_instance.get_cluster_local_domain_sid()
        print("The response of PlatformApi->get_cluster_local_domain_sid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_cluster_local_domain_sid: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterLocalDomainSID**](ClusterLocalDomainSID.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_metadata_request import ClusterMetadataRequest
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Get Cluster Metadata
        api_response = api_instance.get_cluster_metadata()
        print("The response of PlatformApi->get_cluster_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_cluster_metadata: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterMetadataRequest**](ClusterMetadataRequest.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> List[ClusterOperationStatus] get_cluster_operation_status_list(operation_types=operation_types, operation_ids=operation_ids, include_finished_operations=include_finished_operations, include_event_logs=include_event_logs, start_time=start_time, end_time=end_time)

Get cluster operations status.

```No Privileges Required``` <br><br>Get list of cluster operations status information.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_operation_status import ClusterOperationStatus
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    operation_types = ['operation_types_example'] # List[str] | One or more operation types to query for. (optional)
    operation_ids = ['operation_ids_example'] # List[str] | One or more operation ids to query for. (optional)
    include_finished_operations = True # bool | Controls whether finished operations should be included in the query results. The default value is false. Applicable only for patch apply, revert, and upgrade operations (optional)
    include_event_logs = True # bool | Controls whether event logs should be included in the query results. If set to true, 'operationIds' becomes mandatory. The default value is false. Applicable only for patch apply, revert, and upgrade operations (optional)
    start_time = 56 # int | Filters operations that started after the specified time. Applicable only for patch apply, revert, and upgrade operations (optional)
    end_time = 56 # int | Filters operations that ended before the specified time. Applicable only for patch apply, revert, and upgrade operations (optional)

    try:
        # Get cluster operations status.
        api_response = api_instance.get_cluster_operation_status_list(operation_types=operation_types, operation_ids=operation_ids, include_finished_operations=include_finished_operations, include_event_logs=include_event_logs, start_time=start_time, end_time=end_time)
        print("The response of PlatformApi->get_cluster_operation_status_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_cluster_operation_status_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_types** | [**List[str]**](str.md)| One or more operation types to query for. | [optional] 
 **operation_ids** | [**List[str]**](str.md)| One or more operation ids to query for. | [optional] 
 **include_finished_operations** | **bool**| Controls whether finished operations should be included in the query results. The default value is false. Applicable only for patch apply, revert, and upgrade operations | [optional] 
 **include_event_logs** | **bool**| Controls whether event logs should be included in the query results. If set to true, &#39;operationIds&#39; becomes mandatory. The default value is false. Applicable only for patch apply, revert, and upgrade operations | [optional] 
 **start_time** | **int**| Filters operations that started after the specified time. Applicable only for patch apply, revert, and upgrade operations | [optional] 
 **end_time** | **int**| Filters operations that ended before the specified time. Applicable only for patch apply, revert, and upgrade operations | [optional] 

### Return type

[**List[ClusterOperationStatus]**](ClusterOperationStatus.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_packages import ClusterPackages
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Get packages
        api_response = api_instance.get_cluster_packages()
        print("The response of PlatformApi->get_cluster_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_cluster_packages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterPackages**](ClusterPackages.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_snapshot_policy import ClusterSnapshotPolicy
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Get cluster snapshot policy.
        api_response = api_instance.get_cluster_snapshot_policy()
        print("The response of PlatformApi->get_cluster_snapshot_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_cluster_snapshot_policy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterSnapshotPolicy**](ClusterSnapshotPolicy.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> ClusterStateParams get_cluster_state(system_apps=system_apps)

Get cluster state

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get the current state of the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_state_params import ClusterStateParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    system_apps = True # bool | The filter whether or not to get the system apps state details. (optional)

    try:
        # Get cluster state
        api_response = api_instance.get_cluster_state(system_apps=system_apps)
        print("The response of PlatformApi->get_cluster_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_cluster_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_apps** | **bool**| The filter whether or not to get the system apps state details. | [optional] 

### Return type

[**ClusterStateParams**](ClusterStateParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_status import ClusterStatus
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Get cluster status.
        api_response = api_instance.get_cluster_status()
        print("The response of PlatformApi->get_cluster_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_cluster_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterStatus**](ClusterStatus.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> List[Subnet] get_cluster_subnets_info()

Get cluster subnets info.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get cluster subnet info.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.subnet import Subnet
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Get cluster subnets info.
        api_response = api_instance.get_cluster_subnets_info()
        print("The response of PlatformApi->get_cluster_subnets_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_cluster_subnets_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Subnet]**](Subnet.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_vlan_params import ClusterVlanParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    vlan_interface_group_name = 'vlan_interface_group_name_example' # str | Vlan interface group name, it should be in interface_group_name.vlan_id format.

    try:
        # Get vlan
        api_response = api_instance.get_cluster_vlan(vlan_interface_group_name)
        print("The response of PlatformApi->get_cluster_vlan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_cluster_vlan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vlan_interface_group_name** | **str**| Vlan interface group name, it should be in interface_group_name.vlan_id format. | 

### Return type

[**ClusterVlanParams**](ClusterVlanParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> ClusterVlans get_cluster_vlans(vlan_interface_group_names=vlan_interface_group_names, tenant_ids=tenant_ids, include_tenants=include_tenants, skip_primary_and_bond_iface=skip_primary_and_bond_iface, compress_ips_to_ranges=compress_ips_to_ranges)

Get vlans

**Privileges:** ```VLAN_VIEW, CLUSTER_CREATE``` <br><br>Get vlans on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_vlans import ClusterVlans
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    vlan_interface_group_names = ['vlan_interface_group_names_example'] # List[str] | Vlan interface group names, it should be in interface_group_name.vlan_id format. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | Ids of the tenants, used to get vlans assigned to tenants. (optional)
    include_tenants = True # bool | If true, the response includes vlans which belongs to all the tenants the current user has permissions to see. (optional) (default to True)
    skip_primary_and_bond_iface = False # bool | If true, vlan primary and bond interfaces are not returned in the response. (optional) (default to False)
    compress_ips_to_ranges = False # bool | Compress vlan IPs to list of contigous IP ranges with startIp and endIp. (optional) (default to False)

    try:
        # Get vlans
        api_response = api_instance.get_cluster_vlans(vlan_interface_group_names=vlan_interface_group_names, tenant_ids=tenant_ids, include_tenants=include_tenants, skip_primary_and_bond_iface=skip_primary_and_bond_iface, compress_ips_to_ranges=compress_ips_to_ranges)
        print("The response of PlatformApi->get_cluster_vlans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_cluster_vlans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vlan_interface_group_names** | [**List[str]**](str.md)| Vlan interface group names, it should be in interface_group_name.vlan_id format. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| Ids of the tenants, used to get vlans assigned to tenants. | [optional] 
 **include_tenants** | **bool**| If true, the response includes vlans which belongs to all the tenants the current user has permissions to see. | [optional] [default to True]
 **skip_primary_and_bond_iface** | **bool**| If true, vlan primary and bond interfaces are not returned in the response. | [optional] [default to False]
 **compress_ips_to_ranges** | **bool**| Compress vlan IPs to list of contigous IP ranges with startIp and endIp. | [optional] [default to False]

### Return type

[**ClusterVlans**](ClusterVlans.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.hardware_info import HardwareInfo
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Fetch Node Hardware Information
        api_response = api_instance.get_hardware_info()
        print("The response of PlatformApi->get_hardware_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_hardware_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HardwareInfo**](HardwareInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> InterfaceGroups get_interface_groups(ids=ids)

Get interface groups

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get a list of interface groups configured on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.interface_groups import InterfaceGroups
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    ids = [56] # List[int] | Ids of the interface groups. (optional)

    try:
        # Get interface groups
        api_response = api_instance.get_interface_groups(ids=ids)
        print("The response of PlatformApi->get_interface_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_interface_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| Ids of the interface groups. | [optional] 

### Return type

[**InterfaceGroups**](InterfaceGroups.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> IpmiFruInfo get_ipmi_fru_info(node_id=node_id, node_ip=node_ip)

To get IPMI FRU info

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetches the information about FRU for given IPMI

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.ipmi_fru_info import IpmiFruInfo
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    node_id = 'node_id_example' # str | Specifies the node id of the node for which fru info is requested. This parameter is incompatible with 'nodeIp'. (optional)
    node_ip = 'node_ip_example' # str | Specifies the IP Address of the node for which fru info is requested. This parameter is incompatible with 'nodeId'. (optional)

    try:
        # To get IPMI FRU info
        api_response = api_instance.get_ipmi_fru_info(node_id=node_id, node_ip=node_ip)
        print("The response of PlatformApi->get_ipmi_fru_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_ipmi_fru_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Specifies the node id of the node for which fru info is requested. This parameter is incompatible with &#39;nodeIp&#39;. | [optional] 
 **node_ip** | **str**| Specifies the IP Address of the node for which fru info is requested. This parameter is incompatible with &#39;nodeId&#39;. | [optional] 

### Return type

[**IpmiFruInfo**](IpmiFruInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> IpmiLanInfo get_ipmi_lan_info(node_id=node_id, node_ip=node_ip)

To get IPMI LAN info

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetches the information about LAN for given IPMI

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.ipmi_lan_info import IpmiLanInfo
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    node_id = 'node_id_example' # str | Specifies the node id of the node for which lan info is requested. This parameter is incompatible with 'nodeIp'. (optional)
    node_ip = 'node_ip_example' # str | Specifies the IP Address of the node for which lan info is requested. This parameter is incompatible with 'nodeId'. (optional)

    try:
        # To get IPMI LAN info
        api_response = api_instance.get_ipmi_lan_info(node_id=node_id, node_ip=node_ip)
        print("The response of PlatformApi->get_ipmi_lan_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_ipmi_lan_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Specifies the node id of the node for which lan info is requested. This parameter is incompatible with &#39;nodeIp&#39;. | [optional] 
 **node_ip** | **str**| Specifies the IP Address of the node for which lan info is requested. This parameter is incompatible with &#39;nodeId&#39;. | [optional] 

### Return type

[**IpmiLanInfo**](IpmiLanInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> IpmiSdrInfo get_ipmi_sdr_info(node_id=node_id, node_ip=node_ip)

To get IPMI SDR Info

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetches the information about SDR info for given IPMI

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.ipmi_sdr_info import IpmiSdrInfo
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    node_id = 'node_id_example' # str | Specifies the node id of the node for which sdr is requested. This parameter is incompatible with 'nodeIp'. (optional)
    node_ip = 'node_ip_example' # str | Specifies the IP Address of the node for which sdr is requested. This parameter is incompatible with 'nodeId'. (optional)

    try:
        # To get IPMI SDR Info
        api_response = api_instance.get_ipmi_sdr_info(node_id=node_id, node_ip=node_ip)
        print("The response of PlatformApi->get_ipmi_sdr_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_ipmi_sdr_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Specifies the node id of the node for which sdr is requested. This parameter is incompatible with &#39;nodeIp&#39;. | [optional] 
 **node_ip** | **str**| Specifies the IP Address of the node for which sdr is requested. This parameter is incompatible with &#39;nodeId&#39;. | [optional] 

### Return type

[**IpmiSdrInfo**](IpmiSdrInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> IpmiSel get_ipmi_sel(node_id=node_id, node_ip=node_ip, verbose=verbose)

To get IPMI SEL

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetches the information about SEL for given IPMI

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.ipmi_sel import IpmiSel
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    node_id = 'node_id_example' # str | Specifies the node id of the node for which sel is requested. This parameter is incompatible with 'nodeIp'. (optional)
    node_ip = 'node_ip_example' # str | Specifies the IP Address of the node for which sel is requested. This parameter is incompatible with 'nodeId'. (optional)
    verbose = True # bool | Specifies the Verbosity of log produced by sel request. (optional)

    try:
        # To get IPMI SEL
        api_response = api_instance.get_ipmi_sel(node_id=node_id, node_ip=node_ip, verbose=verbose)
        print("The response of PlatformApi->get_ipmi_sel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_ipmi_sel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Specifies the node id of the node for which sel is requested. This parameter is incompatible with &#39;nodeIp&#39;. | [optional] 
 **node_ip** | **str**| Specifies the IP Address of the node for which sel is requested. This parameter is incompatible with &#39;nodeId&#39;. | [optional] 
 **verbose** | **bool**| Specifies the Verbosity of log produced by sel request. | [optional] 

### Return type

[**IpmiSel**](IpmiSel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> IpmiSelInfo get_ipmi_sel_info(node_id=node_id, node_ip=node_ip)

To get IPMI SEL Info

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetches the information about SEL info for given IPMI

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.ipmi_sel_info import IpmiSelInfo
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    node_id = 'node_id_example' # str | Specifies the node id of the node for which sel is requested. This parameter is incompatible with 'nodeIp'. (optional)
    node_ip = 'node_ip_example' # str | Specifies the IP Address of the node for which sel is requested. This parameter is incompatible with 'nodeId'. (optional)

    try:
        # To get IPMI SEL Info
        api_response = api_instance.get_ipmi_sel_info(node_id=node_id, node_ip=node_ip)
        print("The response of PlatformApi->get_ipmi_sel_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_ipmi_sel_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Specifies the node id of the node for which sel is requested. This parameter is incompatible with &#39;nodeIp&#39;. | [optional] 
 **node_ip** | **str**| Specifies the IP Address of the node for which sel is requested. This parameter is incompatible with &#39;nodeId&#39;. | [optional] 

### Return type

[**IpmiSelInfo**](IpmiSelInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> IpmiUsers get_ipmi_users(node_id=node_id, node_ip=node_ip)

To get IPMI User Info for node

**Privileges:** ```CLUSTER_VIEW``` <br><br>Fetches the ipmi user information for given node.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.ipmi_users import IpmiUsers
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    node_id = 'node_id_example' # str | Specifies the node id of the node for which ipmi users info is requested. This parameter is incompatible with 'nodeIp'. (optional)
    node_ip = 'node_ip_example' # str | Specifies the IP address of the node for which ipmi users info is requested. This parameter is incompatible with 'nodeId'. (optional)

    try:
        # To get IPMI User Info for node
        api_response = api_instance.get_ipmi_users(node_id=node_id, node_ip=node_ip)
        print("The response of PlatformApi->get_ipmi_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_ipmi_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Specifies the node id of the node for which ipmi users info is requested. This parameter is incompatible with &#39;nodeIp&#39;. | [optional] 
 **node_ip** | **str**| Specifies the IP address of the node for which ipmi users info is requested. This parameter is incompatible with &#39;nodeId&#39;. | [optional] 

### Return type

[**IpmiUsers**](IpmiUsers.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.d_maa_s_info import DMaaSInfo
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Get whether the cluster is a DMaaS cluster.
        api_response = api_instance.get_is_d_maa_s_cluster()
        print("The response of PlatformApi->get_is_d_maa_s_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_is_d_maa_s_cluster: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DMaaSInfo**](DMaaSInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.get_kubernetes_status_response import GetKubernetesStatusResponse
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Get Kubernetes Infra Health Status
        api_response = api_instance.get_kubernetes_infra_health_status()
        print("The response of PlatformApi->get_kubernetes_infra_health_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_kubernetes_infra_health_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetKubernetesStatusResponse**](GetKubernetesStatusResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.login_banner import LoginBanner
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Get login banner.
        api_response = api_instance.get_login_banner()
        print("The response of PlatformApi->get_login_banner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_login_banner: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LoginBanner**](LoginBanner.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> ClusterInterfaces get_network_interfaces(node_id=node_id, cache=cache, bond_interface_only=bond_interface_only, iface_group_assigned_only=iface_group_assigned_only, include_uplink_switch_info=include_uplink_switch_info, include_bond_slave_details=include_bond_slave_details, include_stats=include_stats)

Get list of interfaces

**Privileges:** ```CLUSTER_VIEW, CLUSTER_CREATE``` <br><br>Get a list of interfaces present on the node or cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_interfaces import ClusterInterfaces
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    node_id = 56 # int | Node id, used to get interfaces on a particular node. (optional)
    cache = False # bool | Get interfaces information from cache. (optional) (default to False)
    bond_interface_only = False # bool | Specifies if only show bond interface info. (optional) (default to False)
    iface_group_assigned_only = False # bool | Specifies if only show interface group assigned interface info. (optional) (default to False)
    include_uplink_switch_info = False # bool | Specifies if include uplink switch info. (optional) (default to False)
    include_bond_slave_details = False # bool | Specifies if include bond secondary detailed info. (optional) (default to False)
    include_stats = False # bool | Specifies if include stats. (optional) (default to False)

    try:
        # Get list of interfaces
        api_response = api_instance.get_network_interfaces(node_id=node_id, cache=cache, bond_interface_only=bond_interface_only, iface_group_assigned_only=iface_group_assigned_only, include_uplink_switch_info=include_uplink_switch_info, include_bond_slave_details=include_bond_slave_details, include_stats=include_stats)
        print("The response of PlatformApi->get_network_interfaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_network_interfaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**| Node id, used to get interfaces on a particular node. | [optional] 
 **cache** | **bool**| Get interfaces information from cache. | [optional] [default to False]
 **bond_interface_only** | **bool**| Specifies if only show bond interface info. | [optional] [default to False]
 **iface_group_assigned_only** | **bool**| Specifies if only show interface group assigned interface info. | [optional] [default to False]
 **include_uplink_switch_info** | **bool**| Specifies if include uplink switch info. | [optional] [default to False]
 **include_bond_slave_details** | **bool**| Specifies if include bond secondary detailed info. | [optional] [default to False]
 **include_stats** | **bool**| Specifies if include stats. | [optional] [default to False]

### Return type

[**ClusterInterfaces**](ClusterInterfaces.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> List[Node] get_nodes(ids=ids, include_marked_for_removal=include_marked_for_removal, include_only_unassigned_nodes=include_only_unassigned_nodes, cluster_partition_ids=cluster_partition_ids, fetch_stats=fetch_stats, show_system_disks=show_system_disks)

List Nodes of the cluster.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Gets the list of Nodes in a cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.node import Node
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    ids = [56] # List[int] | \"List of IDs to be returned. If empty, all nodes are returned.\" (optional)
    include_marked_for_removal = True # bool | IncludeMarkedForRemoval is used to specify whether to include nodes marked for removal. (optional)
    include_only_unassigned_nodes = True # bool | IncludeOnlyUnassignedNodes will return nodes that are not yet assigned to any cluster partition. If this parameter is specified as true and ClusterPartitionIdList is also non-empty, then no nodes will be returned. (optional)
    cluster_partition_ids = [56] # List[int] | ClusterPartitionIdList specifies the list of Ids used to filter the nodes by specified cluster partition. (optional)
    fetch_stats = True # bool | FetchStats is used to specify whether to call Stats service to fetch the stats for the nodes. Stats not displayed by default (optional)
    show_system_disks = True # bool | ShowSystemdisks is used to specify whether to display system disks for the nodes. Not populated by default. (optional)

    try:
        # List Nodes of the cluster.
        api_response = api_instance.get_nodes(ids=ids, include_marked_for_removal=include_marked_for_removal, include_only_unassigned_nodes=include_only_unassigned_nodes, cluster_partition_ids=cluster_partition_ids, fetch_stats=fetch_stats, show_system_disks=show_system_disks)
        print("The response of PlatformApi->get_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| \&quot;List of IDs to be returned. If empty, all nodes are returned.\&quot; | [optional] 
 **include_marked_for_removal** | **bool**| IncludeMarkedForRemoval is used to specify whether to include nodes marked for removal. | [optional] 
 **include_only_unassigned_nodes** | **bool**| IncludeOnlyUnassignedNodes will return nodes that are not yet assigned to any cluster partition. If this parameter is specified as true and ClusterPartitionIdList is also non-empty, then no nodes will be returned. | [optional] 
 **cluster_partition_ids** | [**List[int]**](int.md)| ClusterPartitionIdList specifies the list of Ids used to filter the nodes by specified cluster partition. | [optional] 
 **fetch_stats** | **bool**| FetchStats is used to specify whether to call Stats service to fetch the stats for the nodes. Stats not displayed by default | [optional] 
 **show_system_disks** | **bool**| ShowSystemdisks is used to specify whether to display system disks for the nodes. Not populated by default. | [optional] 

### Return type

[**List[Node]**](Node.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.ntp_server_list import NtpServerList
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Get list of NTP servers.
        api_response = api_instance.get_ntp_servers()
        print("The response of PlatformApi->get_ntp_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_ntp_servers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NtpServerList**](NtpServerList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.proxy_server_list import ProxyServerList
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Get list of proxy servers
        api_response = api_instance.get_proxy_servers()
        print("The response of PlatformApi->get_proxy_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_proxy_servers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProxyServerList**](ProxyServerList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.rack import Rack
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    id = 56 # int | Specifies the id of rack.

    try:
        # Get a rack by rack id.
        api_response = api_instance.get_rack_by_id(id)
        print("The response of PlatformApi->get_rack_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_rack_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of rack. | 

### Return type

[**Rack**](Rack.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.racks import Racks
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Get list of racks
        api_response = api_instance.get_racks()
        print("The response of PlatformApi->get_racks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_racks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Racks**](Racks.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> RemoteDisks get_remote_disks(disk_ids=disk_ids, node_ids=node_ids, tiers=tiers, mount_path=mount_path, file_system=file_system)

Get remote disks

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get remote disks.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.remote_disks import RemoteDisks
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    disk_ids = [56] # List[int] | Specifies a list of disk ids, only disks having these ids will be returned. (optional)
    node_ids = [56] # List[int] | Specifies a list of node ids, only disks in these nodes will be returned. (optional)
    tiers = ['tiers_example'] # List[str] | Specifies a list of disk tiers, only disks with given tiers will be returned. (optional)
    mount_path = 'mount_path_example' # str | This field is deprecated. Providing this queryparam will not have any impact. Please use fileSystem query param to filter instead. (optional)
    file_system = 'file_system_example' # str | Specified file system name to search. only disks with file system name that partially matches the specified name will be returned. (optional)

    try:
        # Get remote disks
        api_response = api_instance.get_remote_disks(disk_ids=disk_ids, node_ids=node_ids, tiers=tiers, mount_path=mount_path, file_system=file_system)
        print("The response of PlatformApi->get_remote_disks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_remote_disks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disk_ids** | [**List[int]**](int.md)| Specifies a list of disk ids, only disks having these ids will be returned. | [optional] 
 **node_ids** | [**List[int]**](int.md)| Specifies a list of node ids, only disks in these nodes will be returned. | [optional] 
 **tiers** | [**List[str]**](str.md)| Specifies a list of disk tiers, only disks with given tiers will be returned. | [optional] 
 **mount_path** | **str**| This field is deprecated. Providing this queryparam will not have any impact. Please use fileSystem query param to filter instead. | [optional] 
 **file_system** | **str**| Specified file system name to search. only disks with file system name that partially matches the specified name will be returned. | [optional] 

### Return type

[**RemoteDisks**](RemoteDisks.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> List[ServiceGflags] get_service_gflags(gflags=gflags, service_name=service_name)

Gets cluster gflags for a service.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Gets the cluster gflags for a service.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.service_gflags import ServiceGflags
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    gflags = ['gflags_example'] # List[str] | \"Specifies a list of gflag names. If specified, only gflags matching the gflag name list will be returned.\" (optional)
    service_name = 'service_name_example' # str | Specifies the service name. If specified, only gflags matching the service name will be returned. (optional)

    try:
        # Gets cluster gflags for a service.
        api_response = api_instance.get_service_gflags(gflags=gflags, service_name=service_name)
        print("The response of PlatformApi->get_service_gflags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_service_gflags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gflags** | [**List[str]**](str.md)| \&quot;Specifies a list of gflag names. If specified, only gflags matching the gflag name list will be returned.\&quot; | [optional] 
 **service_name** | **str**| Specifies the service name. If specified, only gflags matching the service name will be returned. | [optional] 

### Return type

[**List[ServiceGflags]**](ServiceGflags.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.smtp_configuration import SMTPConfiguration
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Get SMTP configuration.
        api_response = api_instance.get_smtp_configuration()
        print("The response of PlatformApi->get_smtp_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_smtp_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SMTPConfiguration**](SMTPConfiguration.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.software_components import SoftwareComponents
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Get Software Components
        api_response = api_instance.get_software_components()
        print("The response of PlatformApi->get_software_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_software_components: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SoftwareComponents**](SoftwareComponents.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.support_channel import SupportChannel
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Get support channel configuration.
        api_response = api_instance.get_support_channel_config()
        print("The response of PlatformApi->get_support_channel_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_support_channel_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SupportChannel**](SupportChannel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> List[ClusterSWUpdateHistoryEvent] get_sw_update_history(include_node_history)

Get cluster software history

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get upgrade and patch history of the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_sw_update_history_event import ClusterSWUpdateHistoryEvent
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    include_node_history = True # bool | Flag to specify whether to fetch data from current node or all the nodes. 

    try:
        # Get cluster software history
        api_response = api_instance.get_sw_update_history(include_node_history)
        print("The response of PlatformApi->get_sw_update_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_sw_update_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_node_history** | **bool**| Flag to specify whether to fetch data from current node or all the nodes.  | 

### Return type

[**List[ClusterSWUpdateHistoryEvent]**](ClusterSWUpdateHistoryEvent.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.node_identify_params import NodeIdentifyParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    id = 56 # int | Specifies id of node to identify.
    body = cohesity_sdk.cluster.NodeIdentifyParams() # NodeIdentifyParams | Specifies the parameter to identify node.

    try:
        # Identify node
        api_response = api_instance.identify_node(id, body)
        print("The response of PlatformApi->identify_node:\n")
        pprint(api_response)
    except Exception as e:
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

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    file_name = 'file_name_example' # str | 
    crlfile = None # bytearray | 

    try:
        # Import Crl File
        api_instance.import_crl_file(file_name, crlfile)
    except Exception as e:
        print("Exception when calling PlatformApi->import_crl_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 
 **crlfile** | **bytearray**|  | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> DisksList list_disks(node_id=node_id)

Get list of disks

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get list of local disks.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.disks_list import DisksList
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    node_id = 56 # int | Specifies node id of the node to get list of disks (optional)

    try:
        # Get list of disks
        api_response = api_instance.list_disks(node_id=node_id)
        print("The response of PlatformApi->list_disks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->list_disks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**| Specifies node id of the node to get list of disks | [optional] 

### Return type

[**DisksList**](DisksList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> FreeNodes list_free_nodes(ips=ips)

List the free Cohesity Nodes present on a network.

**Privileges:** ```CLUSTER_VIEW, CLUSTER_CREATE``` <br><br>Sends a request to any Node to list all of the free Nodes that are present on the network.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.free_nodes import FreeNodes
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    ips = ['ips_example'] # List[str] | \"Specifies a list of ips of nodes among which free and compatible nodes to be returned\" (optional)

    try:
        # List the free Cohesity Nodes present on a network.
        api_response = api_instance.list_free_nodes(ips=ips)
        print("The response of PlatformApi->list_free_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->list_free_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ips** | [**List[str]**](str.md)| \&quot;Specifies a list of ips of nodes among which free and compatible nodes to be returned\&quot; | [optional] 

### Return type

[**FreeNodes**](FreeNodes.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.host_mappings import HostMappings
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # List Host Mappings
        api_response = api_instance.list_hosts()
        print("The response of PlatformApi->list_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->list_hosts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HostMappings**](HostMappings.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> ClusterServicesStates list_services_states(body=body)

List services states

**Privileges:** ```CLUSTER_VIEW``` <br><br>List the states of the services on the Cluster

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_services_states import ClusterServicesStates
from cohesity_sdk.cluster.models.cluster_services_states_params import ClusterServicesStatesParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.ClusterServicesStatesParams() # ClusterServicesStatesParams | Specifies the parameters to get cluster services states. (optional)

    try:
        # List services states
        api_response = api_instance.list_services_states(body=body)
        print("The response of PlatformApi->list_services_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->list_services_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterServicesStatesParams**](ClusterServicesStatesParams.md)| Specifies the parameters to get cluster services states. | [optional] 

### Return type

[**ClusterServicesStates**](ClusterServicesStates.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.mark_baseos_upgrade_info import MarkBaseosUpgradeInfo
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.MarkBaseosUpgradeInfo() # MarkBaseosUpgradeInfo | Param to whether set/clear BaseOS uprgade  operation.

    try:
        # Sets/clears the BaseOS upgrade cluster operation.
        api_response = api_instance.mark_baseos_upgrade(body)
        print("The response of PlatformApi->mark_baseos_upgrade:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->mark_baseos_upgrade: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MarkBaseosUpgradeInfo**](MarkBaseosUpgradeInfo.md)| Param to whether set/clear BaseOS uprgade  operation. | 

### Return type

[**MarkBaseosUpgradeInfo**](MarkBaseosUpgradeInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.disk_removal_params import DiskRemovalParams
from cohesity_sdk.cluster.models.remove_disk import RemoveDisk
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    id = 56 # int | Specifies unique id of the disk to mark for removal.
    body = cohesity_sdk.cluster.DiskRemovalParams() # DiskRemovalParams | Specifies parameters to mark/cancel disk removal.

    try:
        # Mark Disk for removal
        api_response = api_instance.mark_disk_removal(id, body)
        print("The response of PlatformApi->mark_disk_removal:\n")
        pprint(api_response)
    except Exception as e:
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

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.node_removal_params import NodeRemovalParams
from cohesity_sdk.cluster.models.remove_node import RemoveNode
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    id = 56 # int | Specifies id of node to cancel removal.
    body = cohesity_sdk.cluster.NodeRemovalParams() # NodeRemovalParams | Specifies parameters to initiate/cancel node removal .

    try:
        # Mark Node for removal
        api_response = api_instance.mark_node_removal(id, body)
        print("The response of PlatformApi->mark_node_removal:\n")
        pprint(api_response)
    except Exception as e:
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

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.node_cert_request import NodeCertRequest
from cohesity_sdk.cluster.models.node_cert_result import NodeCertResult
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.NodeCertRequest() # NodeCertRequest | The parameters to import the signed cert.

    try:
        # Import a signed certificate used for n2n communication
        api_response = api_instance.node_import_signed_cert(body)
        print("The response of PlatformApi->node_import_signed_cert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->node_import_signed_cert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeCertRequest**](NodeCertRequest.md)| The parameters to import the signed cert. | 

### Return type

[**NodeCertResult**](NodeCertResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> NodeInfo node_information(show_services_version_info=show_services_version_info, only_check_node_reachability=only_check_node_reachability)

Fetch Node General Information

**Privileges:** ```CLUSTER_VIEW, NODE_VIEW``` <br><br>Fetch general information about the node to which the request is sent to.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.node_info import NodeInfo
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    show_services_version_info = True # bool | Specifies whether to show version info of the services running on the node. (optional)
    only_check_node_reachability = False # bool | Specifies to show only node reachability details (optional) (default to False)

    try:
        # Fetch Node General Information
        api_response = api_instance.node_information(show_services_version_info=show_services_version_info, only_check_node_reachability=only_check_node_reachability)
        print("The response of PlatformApi->node_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->node_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_services_version_info** | **bool**| Specifies whether to show version info of the services running on the node. | [optional] 
 **only_check_node_reachability** | **bool**| Specifies to show only node reachability details | [optional] [default to False]

### Return type

[**NodeInfo**](NodeInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.node_status_result import NodeStatusResult
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Fetch Node status Information
        api_response = api_instance.node_status()
        print("The response of PlatformApi->node_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->node_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NodeStatusResult**](NodeStatusResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.public_key_request import PublicKeyRequest
from cohesity_sdk.cluster.models.public_key_response import PublicKeyResponse
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.PublicKeyRequest() # PublicKeyRequest | Specifies the parameters required to retrieve SSH public key

    try:
        # Get the SSH public key.
        api_response = api_instance.public_key_request(body)
        print("The response of PlatformApi->public_key_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->public_key_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublicKeyRequest**](PublicKeyRequest.md)| Specifies the parameters required to retrieve SSH public key | 

### Return type

[**PublicKeyResponse**](PublicKeyResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    name = 'name_example' # str | Specifies name of the proxy server.

    try:
        # Remove specified proxy server.
        api_instance.remove_proxy_server(name)
    except Exception as e:
        print("Exception when calling PlatformApi->remove_proxy_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies name of the proxy server. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    id = 56 # int | Specifies the id of the remote disk to remove.

    try:
        # Remove remote disk
        api_instance.remove_remote_disk(id)
    except Exception as e:
        print("Exception when calling PlatformApi->remove_remote_disk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the remote disk to remove. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.ipmi_text_response import IpmiTextResponse
from cohesity_sdk.cluster.models.reset_ipmi_bmc_params import ResetIpmiBmcParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.ResetIpmiBmcParams() # ResetIpmiBmcParams | Specifies the parameters to reset ipmi bmc for given node.

    try:
        # To reset IPMI BMC for given node
        api_response = api_instance.reset_ipmi_bmc(body)
        print("The response of PlatformApi->reset_ipmi_bmc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->reset_ipmi_bmc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetIpmiBmcParams**](ResetIpmiBmcParams.md)| Specifies the parameters to reset ipmi bmc for given node. | 

### Return type

[**IpmiTextResponse**](IpmiTextResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> List[RestoreConfig] restore_configuration()

Restore configuration.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Config to be restored during one-helios cluster creation.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.restore_config import RestoreConfig
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)

    try:
        # Restore configuration.
        api_response = api_instance.restore_configuration()
        print("The response of PlatformApi->restore_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->restore_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RestoreConfig]**](RestoreConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.node_power_operation import NodePowerOperation
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.NodePowerOperation() # NodePowerOperation | Specifies the reboot or shutdown operation.

    try:
        # Reboot or shutdown nodes in cluster.
        api_instance.set_node_power(body)
    except Exception as e:
        print("Exception when calling PlatformApi->set_node_power: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodePowerOperation**](NodePowerOperation.md)| Specifies the reboot or shutdown operation. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.airgap_config import AirgapConfig
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.AirgapConfig() # AirgapConfig | Specifies the parameters to update airgap config.

    try:
        # Update Airgap config
        api_response = api_instance.update_airgap_config(body)
        print("The response of PlatformApi->update_airgap_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_airgap_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AirgapConfig**](AirgapConfig.md)| Specifies the parameters to update airgap config. | 

### Return type

[**AirgapConfig**](AirgapConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_amqp_target_config import ClusterAMQPTargetConfig
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.ClusterAMQPTargetConfig() # ClusterAMQPTargetConfig | Specifies the parameters to update cluster AMQP target config.

    try:
        # Update AMQP Target Config
        api_response = api_instance.update_amqp_target_config(body)
        print("The response of PlatformApi->update_amqp_target_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_amqp_target_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterAMQPTargetConfig**](ClusterAMQPTargetConfig.md)| Specifies the parameters to update cluster AMQP target config. | 

### Return type

[**ClusterAMQPTargetConfig**](ClusterAMQPTargetConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> Chassis update_chassis_by_id(id, body=body)

Update a chassis by chassis id.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update selected properties of chassis info by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.chassis import Chassis
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    id = 56 # int | Specifies the id of chassis.
    body = cohesity_sdk.cluster.Chassis() # Chassis | Specifies the parameters to update chassis. (optional)

    try:
        # Update a chassis by chassis id.
        api_response = api_instance.update_chassis_by_id(id, body=body)
        print("The response of PlatformApi->update_chassis_by_id:\n")
        pprint(api_response)
    except Exception as e:
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

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster import Cluster
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.Cluster() # Cluster | Specifies the parameters to update cluster.

    try:
        # Update a cluster.
        api_response = api_instance.update_cluster(body)
        print("The response of PlatformApi->update_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Cluster**](Cluster.md)| Specifies the parameters to update cluster. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_ipmi_lan_info import ClusterIpmiLanInfo
from cohesity_sdk.cluster.models.ipmi_text_response import IpmiTextResponse
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.ClusterIpmiLanInfo() # ClusterIpmiLanInfo | Specifies the parameters to update the information about LAN for the cluster in which current node is present.

    try:
        # To update IPMI LAN info for the cluster
        api_response = api_instance.update_cluster_ipmi_lan_info(body)
        print("The response of PlatformApi->update_cluster_ipmi_lan_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_cluster_ipmi_lan_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterIpmiLanInfo**](ClusterIpmiLanInfo.md)| Specifies the parameters to update the information about LAN for the cluster in which current node is present. | 

### Return type

[**IpmiTextResponse**](IpmiTextResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_snapshot_policy import ClusterSnapshotPolicy
from cohesity_sdk.cluster.models.update_snapshot_policy_params import UpdateSnapshotPolicyParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.UpdateSnapshotPolicyParams() # UpdateSnapshotPolicyParams | Specifies the parameters to update cluster snapshot policy.

    try:
        # Update cluster snapshot policy.
        api_response = api_instance.update_cluster_snapshot_policy(body)
        print("The response of PlatformApi->update_cluster_snapshot_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_cluster_snapshot_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSnapshotPolicyParams**](UpdateSnapshotPolicyParams.md)| Specifies the parameters to update cluster snapshot policy. | 

### Return type

[**ClusterSnapshotPolicy**](ClusterSnapshotPolicy.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> List[ClusterOperationTypeAndId] update_cluster_software(body)

Update cluster software

**Privileges:** ```CLUSTER_UPGRADE, CLUSTER_MAINTENANCE``` <br><br>Update the software on the cluster through upgrade and/or patch.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_operation_type_and_id import ClusterOperationTypeAndId
from cohesity_sdk.cluster.models.cluster_sw_update_params import ClusterSWUpdateParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.ClusterSWUpdateParams() # ClusterSWUpdateParams | The parameters to update the software on the cluster.

    try:
        # Update cluster software
        api_response = api_instance.update_cluster_software(body)
        print("The response of PlatformApi->update_cluster_software:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_cluster_software: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterSWUpdateParams**](ClusterSWUpdateParams.md)| The parameters to update the software on the cluster. | 

### Return type

[**List[ClusterOperationTypeAndId]**](ClusterOperationTypeAndId.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> List[Subnet] update_cluster_subnets(body)

Update the Cluster Subnets

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update the cluster subnet Info

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.subnet import Subnet
from cohesity_sdk.cluster.models.update_cluster_subnets_params import UpdateClusterSubnetsParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.UpdateClusterSubnetsParams() # UpdateClusterSubnetsParams | 

    try:
        # Update the Cluster Subnets
        api_response = api_instance.update_cluster_subnets(body)
        print("The response of PlatformApi->update_cluster_subnets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_cluster_subnets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateClusterSubnetsParams**](UpdateClusterSubnetsParams.md)|  | 

### Return type

[**List[Subnet]**](Subnet.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.cluster_vlan_params import ClusterVlanParams
from cohesity_sdk.cluster.models.update_cluster_vlan_params import UpdateClusterVlanParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    vlan_interface_group_name = 'vlan_interface_group_name_example' # str | Vlan interface group name, it should be in interface_group_name.vlan_id format.
    body = cohesity_sdk.cluster.UpdateClusterVlanParams() # UpdateClusterVlanParams | Parameters to update vlan on the cluster.

    try:
        # Update vlan
        api_response = api_instance.update_cluster_vlan(vlan_interface_group_name, body)
        print("The response of PlatformApi->update_cluster_vlan:\n")
        pprint(api_response)
    except Exception as e:
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

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> List[FeatureFlag] update_feature_flag(body)

Update feature flag override status.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update a feature flag override status to cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.feature_flag import FeatureFlag
from cohesity_sdk.cluster.models.update_feature_flag_params import UpdateFeatureFlagParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.UpdateFeatureFlagParams() # UpdateFeatureFlagParams | Param for feature flag override request.

    try:
        # Update feature flag override status.
        api_response = api_instance.update_feature_flag(body)
        print("The response of PlatformApi->update_feature_flag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_feature_flag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateFeatureFlagParams**](UpdateFeatureFlagParams.md)| Param for feature flag override request. | 

### Return type

[**List[FeatureFlag]**](FeatureFlag.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.host_entry import HostEntry
from cohesity_sdk.cluster.models.host_mappings import HostMappings
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = [cohesity_sdk.cluster.HostEntry()] # List[HostEntry] | 

    try:
        # Update Host Mappings
        api_response = api_instance.update_hosts(body)
        print("The response of PlatformApi->update_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_hosts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**List[HostEntry]**](HostEntry.md)|  | 

### Return type

[**HostMappings**](HostMappings.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.interface_group import InterfaceGroup
from cohesity_sdk.cluster.models.interface_group_params import InterfaceGroupParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    name = 'name_example' # str | Name of the interface group.
    body = cohesity_sdk.cluster.InterfaceGroupParams() # InterfaceGroupParams | Parameters to update an interface group on the cluster.

    try:
        # Update interface group
        api_response = api_instance.update_interface_group(name, body)
        print("The response of PlatformApi->update_interface_group:\n")
        pprint(api_response)
    except Exception as e:
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

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.ipmi_text_response import IpmiTextResponse
from cohesity_sdk.cluster.models.update_ipmi_user import UpdateIpmiUser
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.UpdateIpmiUser() # UpdateIpmiUser | Specifies the parameters to add an ipmi user to node.

    try:
        # To update IPMI User Info for node
        api_response = api_instance.update_ipmi_user(body)
        print("The response of PlatformApi->update_ipmi_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_ipmi_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateIpmiUser**](UpdateIpmiUser.md)| Specifies the parameters to add an ipmi user to node. | 

### Return type

[**IpmiTextResponse**](IpmiTextResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.d_maa_s_info import DMaaSInfo
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.DMaaSInfo() # DMaaSInfo | Param to update whether the cluster is a DMaaS cluster.

    try:
        # Update whether the cluster is a DMaaS cluster.
        api_response = api_instance.update_is_d_maa_s_cluster(body)
        print("The response of PlatformApi->update_is_d_maa_s_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_is_d_maa_s_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DMaaSInfo**](DMaaSInfo.md)| Param to update whether the cluster is a DMaaS cluster. | 

### Return type

[**DMaaSInfo**](DMaaSInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.login_banner import LoginBanner
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.LoginBanner() # LoginBanner | Specifies text to update the login banner.

    try:
        # Update login banner.
        api_response = api_instance.update_login_banner(body)
        print("The response of PlatformApi->update_login_banner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_login_banner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginBanner**](LoginBanner.md)| Specifies text to update the login banner. | 

### Return type

[**LoginBanner**](LoginBanner.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.ntp_server_list import NtpServerList
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.NtpServerList() # NtpServerList | Specifies parameters to update NTP sever configuration.

    try:
        # Update NTP servers.
        api_response = api_instance.update_ntp_servers(body)
        print("The response of PlatformApi->update_ntp_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_ntp_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NtpServerList**](NtpServerList.md)| Specifies parameters to update NTP sever configuration. | 

### Return type

[**NtpServerList**](NtpServerList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.proxy_server import ProxyServer
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    name = 'name_example' # str | Specifies name of the proxy server.
    body = cohesity_sdk.cluster.ProxyServer() # ProxyServer | Specifies parameters to update the proxy server.

    try:
        # Update specified proxy server.
        api_response = api_instance.update_proxy_server(name, body)
        print("The response of PlatformApi->update_proxy_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_proxy_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies name of the proxy server. | 
 **body** | **ProxyServer**| Specifies parameters to update the proxy server. | 

### Return type

[**ProxyServer**](ProxyServer.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> Rack update_rack_by_id(id, body=body)



**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update selected properties of a rack given by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.rack import Rack
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    id = 56 # int | Specifies the id of rack.
    body = cohesity_sdk.cluster.Rack() # Rack | Specifies the parameters to update rack. (optional)

    try:
        api_response = api_instance.update_rack_by_id(id, body=body)
        print("The response of PlatformApi->update_rack_by_id:\n")
        pprint(api_response)
    except Exception as e:
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

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.racks import Racks
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.Racks() # Racks | Specifies the parameters to update racks.

    try:
        # Update racks
        api_response = api_instance.update_racks(body)
        print("The response of PlatformApi->update_racks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_racks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Racks**](Racks.md)| Specifies the parameters to update racks. | 

### Return type

[**Racks**](Racks.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> List[RestoreConfig] update_restore_configuration(body)

Update Restore configuration.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update the restore config for one-helios cluster restore.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.restore_config import RestoreConfig
from cohesity_sdk.cluster.models.restore_config_payload import RestoreConfigPayload
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.RestoreConfigPayload() # RestoreConfigPayload | 

    try:
        # Update Restore configuration.
        api_response = api_instance.update_restore_configuration(body)
        print("The response of PlatformApi->update_restore_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_restore_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **RestoreConfigPayload**|  | 

### Return type

[**List[RestoreConfig]**](RestoreConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> List[ServiceGflags] update_service_gflags(body)

Update the gflags

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Updates the gflags for a service on the Cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.service_gflags import ServiceGflags
from cohesity_sdk.cluster.models.update_gflag_parameters import UpdateGflagParameters
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.UpdateGflagParameters() # UpdateGflagParameters | 

    try:
        # Update the gflags
        api_response = api_instance.update_service_gflags(body)
        print("The response of PlatformApi->update_service_gflags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_service_gflags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateGflagParameters**](UpdateGflagParameters.md)|  | 

### Return type

[**List[ServiceGflags]**](ServiceGflags.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.smtp_configuration import SMTPConfiguration
from cohesity_sdk.cluster.models.update_smtp_params import UpdateSMTPParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.UpdateSMTPParams() # UpdateSMTPParams | Specifies the parameters to update cluster SMTP configuration.

    try:
        # Update SMTP configuration.
        api_response = api_instance.update_smtp_configuration(body)
        print("The response of PlatformApi->update_smtp_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_smtp_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSMTPParams**](UpdateSMTPParams.md)| Specifies the parameters to update cluster SMTP configuration. | 

### Return type

[**SMTPConfiguration**](SMTPConfiguration.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.support_channel_config import SupportChannelConfig
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.SupportChannelConfig() # SupportChannelConfig | Specifies the support channel configuration.

    try:
        # Update support channel configuration.
        api_response = api_instance.update_support_channel_config(body)
        print("The response of PlatformApi->update_support_channel_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_support_channel_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupportChannelConfig**](SupportChannelConfig.md)| Specifies the support channel configuration. | 

### Return type

[**SupportChannelConfig**](SupportChannelConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.upgrade_checks_results import UpgradeChecksResults
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    test_run_instance_id = 56 # int | Specifies test run instance for which to fetch results

    try:
        # Get upgrade checks results.
        api_response = api_instance.upgrade_check_get_results(test_run_instance_id)
        print("The response of PlatformApi->upgrade_check_get_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->upgrade_check_get_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_instance_id** | **int**| Specifies test run instance for which to fetch results | 

### Return type

[**UpgradeChecksResults**](UpgradeChecksResults.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.upgrade_check_run_tests_request import UpgradeCheckRunTestsRequest
from cohesity_sdk.cluster.models.upgrade_check_run_tests_result import UpgradeCheckRunTestsResult
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.UpgradeCheckRunTestsRequest() # UpgradeCheckRunTestsRequest | Run upgrade checks on cluster.

    try:
        # Run upgrade checks on cluster.
        api_response = api_instance.upgrade_check_run_tests(body)
        print("The response of PlatformApi->upgrade_check_run_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->upgrade_check_run_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpgradeCheckRunTestsRequest**](UpgradeCheckRunTestsRequest.md)| Run upgrade checks on cluster. | 

### Return type

[**UpgradeCheckRunTestsResult**](UpgradeCheckRunTestsResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.node_upgrade_parameters import NodeUpgradeParameters
from cohesity_sdk.cluster.models.node_upgrade_result import NodeUpgradeResult
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.NodeUpgradeParameters() # NodeUpgradeParameters | The parameters to upgrade free node(s).

    try:
        # Upgrade a free node.
        api_response = api_instance.upgrade_nodes(body)
        print("The response of PlatformApi->upgrade_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->upgrade_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeUpgradeParameters**](NodeUpgradeParameters.md)| The parameters to upgrade free node(s). | 

### Return type

[**NodeUpgradeResult**](NodeUpgradeResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> upload_file_package(package_file, package_type=package_type)

Upload package by files

**Privileges:** ```CLUSTER_UPGRADE, CLUSTER_MAINTENANCE``` <br><br>Upload upgrade/patch package.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    package_file = None # bytearray | Binary content of the file.
    package_type = Upgrade # str | Package Type. (optional) (default to Upgrade)

    try:
        # Upload package by files
        api_instance.upload_file_package(package_file, package_type=package_type)
    except Exception as e:
        print("Exception when calling PlatformApi->upload_file_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_file** | **bytearray**| Binary content of the file. | 
 **package_type** | **str**| Package Type. | [optional] [default to Upgrade]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.test_smtp_config import TestSMTPConfig
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.TestSMTPConfig() # TestSMTPConfig | Specifies the request parameters to validate SMTP configuration.

    try:
        # Validate SMTP configuration.
        api_instance.validate_smtp_configuration(body)
    except Exception as e:
        print("Exception when calling PlatformApi->validate_smtp_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TestSMTPConfig**](TestSMTPConfig.md)| Specifies the request parameters to validate SMTP configuration. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.ipmi_text_response import IpmiTextResponse
from cohesity_sdk.cluster.models.verify_ipmi_user import VerifyIpmiUser
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.PlatformApi(api_client)
    body = cohesity_sdk.cluster.VerifyIpmiUser() # VerifyIpmiUser | Specifies the parameters to add an ipmi user to node.

    try:
        # To verify IPMI User with Password for node
        api_response = api_instance.verify_ipmi_user(body)
        print("The response of PlatformApi->verify_ipmi_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->verify_ipmi_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyIpmiUser**](VerifyIpmiUser.md)| Specifies the parameters to add an ipmi user to node. | 

### Return type

[**IpmiTextResponse**](IpmiTextResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

