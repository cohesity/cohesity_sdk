# cohesity_sdk.PlatformApi

All URIs are relative to */v2*

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.host_entry import HostEntry
from cohesity_sdk.models.host_mappings import HostMappings
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = [cohesity_sdk.HostEntry()] # List[HostEntry] | Specifies the request to add entries to /etc/hosts

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.add_remote_disk_response_body import AddRemoteDiskResponseBody
from cohesity_sdk.models.remote_disks import RemoteDisks
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.RemoteDisks() # RemoteDisks | Specifies the remote disk configuration.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster import Cluster
from cohesity_sdk.models.create_cluster_params import CreateClusterParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.CreateClusterParams() # CreateClusterParams | Specifies the parameters to create cluster.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster_vlan_params import ClusterVlanParams
from cohesity_sdk.models.create_cluster_vlan_params import CreateClusterVlanParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.CreateClusterVlanParams() # CreateClusterVlanParams | Parameters to create a vlan.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.interface_group import InterfaceGroup
from cohesity_sdk.models.interface_group_params import InterfaceGroupParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.InterfaceGroupParams() # InterfaceGroupParams | Parameters to create an interface group.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.racks import Racks
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.Racks() # Racks | Specifies the parameters to create racks.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster_operation_response_params import ClusterOperationResponseParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    version_name = 'version_name_example' # str | Version name of the package. Example: 6.3.1h_release-20210714_0fad884e

    try:
        # Delete package
        api_response = api_instance.delete_cluster_package(version_name)
        print("The response of PlatformApi->delete_cluster_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->delete_cluster_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_name** | **str**| Version name of the package. Example: 6.3.1h_release-20210714_0fad884e | 

### Return type

[**ClusterOperationResponseParams**](ClusterOperationResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    interface_name = 'interface_name_example' # str | Vlan interface name, it should be in interface_group_name.vlan_id format.

    try:
        # Delete vlan
        api_instance.delete_cluster_vlan(interface_name)
    except Exception as e:
        print("Exception when calling PlatformApi->delete_cluster_vlan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_name** | **str**| Vlan interface name, it should be in interface_group_name.vlan_id format. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.delete_hosts_parameters import DeleteHostsParameters
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.DeleteHostsParameters() # DeleteHostsParameters | Specifies the params to delete host mappings

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    id = 56 # int | Id of the interface group.

    try:
        # Delete interface group
        api_instance.delete_interface_group(id)
    except Exception as e:
        print("Exception when calling PlatformApi->delete_interface_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the interface group. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.delete_ipmi_user import DeleteIpmiUser
from cohesity_sdk.models.ipmi_text_response import IpmiTextResponse
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.DeleteIpmiUser() # DeleteIpmiUser | Specifies the parameters to delete an ipmi user from given node.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the rack.

    try:
        # Delete a rack by id.
        api_instance.delete_rack_by_id(id)
    except Exception as e:
        print("Exception when calling PlatformApi->delete_rack_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the rack. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

    try:
        # Delete all the racks.
        api_instance.delete_racks()
    except Exception as e:
        print("Exception when calling PlatformApi->delete_racks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster_free_disks import ClusterFreeDisks
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.disk_identify import DiskIdentify
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.DiskIdentify() # DiskIdentify | Specifies the parameter to identify disk.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster_free_disks import ClusterFreeDisks
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.ClusterFreeDisks() # ClusterFreeDisks | Specifies the parameter to assimilate disks.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster_expand_params import ClusterExpandParams
from cohesity_sdk.models.cluster_operation_response_params import ClusterOperationResponseParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.ClusterExpandParams() # ClusterExpandParams | Specifies the parameters to expand the cluster.

    try:
        # Expand the cluster.
        api_response = api_instance.expand_cluster_nodes(body)
        print("The response of PlatformApi->expand_cluster_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->expand_cluster_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterExpandParams**](ClusterExpandParams.md)| Specifies the parameters to expand the cluster. | 

### Return type

[**ClusterOperationResponseParams**](ClusterOperationResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster_amqp_target_config import ClusterAMQPTargetConfig
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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

Get list of all chassis info that are part of cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.chassis_list import ChassisList
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.chassis import Chassis
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster import Cluster
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

    try:
        # Retrieve Cluster Configuration
        api_response = api_instance.get_cluster()
        print("The response of PlatformApi->get_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_cluster: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Cluster**](Cluster.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster_local_domain_sid import ClusterLocalDomainSID
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster_packages import ClusterPackages
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster_snapshot_policy import ClusterSnapshotPolicy
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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

Get the current state of the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster_state_params import ClusterStateParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
> ClusterVlans get_cluster_vlans(interface_names=interface_names, tenant_ids=tenant_ids, include_tenants=include_tenants, skip_primary_and_bond_iface=skip_primary_and_bond_iface, compress_ips_to_ranges=compress_ips_to_ranges)

Get vlans

Get vlans on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster_vlans import ClusterVlans
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    interface_names = ['interface_names_example'] # List[str] | Vlan interface names, it should be in interface_group_name.vlan_id format. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | Ids of the tenants, used to get vlans assigned to tenants. (optional)
    include_tenants = True # bool | If true, the response includes vlans which belongs to all the tenants the current user has permissions to see. (optional) (default to True)
    skip_primary_and_bond_iface = False # bool | If true, vlan primary and bond interfaces are not returned in the response. (optional) (default to False)
    compress_ips_to_ranges = False # bool | Compress vlan IPs to list of contigous IP ranges with startIp and endIp. (optional) (default to False)

    try:
        # Get vlans
        api_response = api_instance.get_cluster_vlans(interface_names=interface_names, tenant_ids=tenant_ids, include_tenants=include_tenants, skip_primary_and_bond_iface=skip_primary_and_bond_iface, compress_ips_to_ranges=compress_ips_to_ranges)
        print("The response of PlatformApi->get_cluster_vlans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_cluster_vlans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_names** | [**List[str]**](str.md)| Vlan interface names, it should be in interface_group_name.vlan_id format. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| Ids of the tenants, used to get vlans assigned to tenants. | [optional] 
 **include_tenants** | **bool**| If true, the response includes vlans which belongs to all the tenants the current user has permissions to see. | [optional] [default to True]
 **skip_primary_and_bond_iface** | **bool**| If true, vlan primary and bond interfaces are not returned in the response. | [optional] [default to False]
 **compress_ips_to_ranges** | **bool**| Compress vlan IPs to list of contigous IP ranges with startIp and endIp. | [optional] [default to False]

### Return type

[**ClusterVlans**](ClusterVlans.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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

Get a list of interface groups configured on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.interface_groups import InterfaceGroups
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
> NetworkInterfaceParams get_interfaces(node_id=node_id, chassis_serial=chassis_serial, slot=slot, cache=cache, bond_interfaces=bond_interfaces, interface_group=interface_group, uplink_switch=uplink_switch, bond_member=bond_member, stats=stats)

Get interfaces

Get interfaces on a cluster or free node.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.network_interface_params import NetworkInterfaceParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    node_id = 56 # int | Node id, used to get interfaces on a particular node. (optional)
    chassis_serial = 'chassis_serial_example' # str | Chassis serial number, used to get interfaces on a chassis. (optional)
    slot = 56 # int | Slot number, used to get interfaces on a slot. (optional)
    cache = True # bool | Get interfaces information from cache. (optional) (default to True)
    bond_interfaces = False # bool | Get bond interfaces only. (optional) (default to False)
    interface_group = False # bool | Get interfaces assigned to a interface group only. (optional) (default to False)
    uplink_switch = True # bool | Include uplink switch information. (optional) (default to True)
    bond_member = True # bool | Include bond member information for bond interfaces. (optional) (default to True)
    stats = True # bool | Include interface stats. (optional) (default to True)

    try:
        # Get interfaces
        api_response = api_instance.get_interfaces(node_id=node_id, chassis_serial=chassis_serial, slot=slot, cache=cache, bond_interfaces=bond_interfaces, interface_group=interface_group, uplink_switch=uplink_switch, bond_member=bond_member, stats=stats)
        print("The response of PlatformApi->get_interfaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_interfaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**| Node id, used to get interfaces on a particular node. | [optional] 
 **chassis_serial** | **str**| Chassis serial number, used to get interfaces on a chassis. | [optional] 
 **slot** | **int**| Slot number, used to get interfaces on a slot. | [optional] 
 **cache** | **bool**| Get interfaces information from cache. | [optional] [default to True]
 **bond_interfaces** | **bool**| Get bond interfaces only. | [optional] [default to False]
 **interface_group** | **bool**| Get interfaces assigned to a interface group only. | [optional] [default to False]
 **uplink_switch** | **bool**| Include uplink switch information. | [optional] [default to True]
 **bond_member** | **bool**| Include bond member information for bond interfaces. | [optional] [default to True]
 **stats** | **bool**| Include interface stats. | [optional] [default to True]

### Return type

[**NetworkInterfaceParams**](NetworkInterfaceParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.d_maa_s_info import DMaaSInfo
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster_interfaces import ClusterInterfaces
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

    try:
        # Get list of interfaces
        api_response = api_instance.get_network_interfaces()
        print("The response of PlatformApi->get_network_interfaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_network_interfaces: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterInterfaces**](ClusterInterfaces.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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

Gets the list of Nodes in a cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.node import Node
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.rack import Rack
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.racks import Racks
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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

Get remote disks.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.remote_disks import RemoteDisks
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.smtp_configuration import SMTPConfiguration
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.support_channel_config import SupportChannelConfig
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

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

[**SupportChannelConfig**](SupportChannelConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.node_identify_params import NodeIdentifyParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    id = 56 # int | Specifies id of node to identify.
    body = cohesity_sdk.NodeIdentifyParams() # NodeIdentifyParams | Specifies the parameter to identify node.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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

Get list of local disks.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.disks_list import DisksList
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
> List[FeatureFlag] list_feature_flag()

Get feature flag overrides list.

Get the list of feature flag overrides defined on cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.feature_flag import FeatureFlag
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

    try:
        # Get feature flag overrides list.
        api_response = api_instance.list_feature_flag()
        print("The response of PlatformApi->list_feature_flag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->list_feature_flag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FeatureFlag]**](FeatureFlag.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.free_nodes import FreeNodes
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

    try:
        # List the free Cohesity Nodes present on a network.
        api_response = api_instance.list_free_nodes()
        print("The response of PlatformApi->list_free_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->list_free_nodes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FreeNodes**](FreeNodes.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.host_mappings import HostMappings
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.mark_baseos_upgrade_info import MarkBaseosUpgradeInfo
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.MarkBaseosUpgradeInfo() # MarkBaseosUpgradeInfo | Param to whether set/clear BaseOS uprgade  operation.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.disk_removal_params import DiskRemovalParams
from cohesity_sdk.models.remove_disk import RemoveDisk
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    id = 56 # int | Specifies unique id of the disk to mark for removal.
    body = cohesity_sdk.DiskRemovalParams() # DiskRemovalParams | Specifies parameters to mark/cancel disk removal.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.node_removal_params import NodeRemovalParams
from cohesity_sdk.models.remove_node import RemoveNode
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    id = 56 # int | Specifies id of node to cancel removal.
    body = cohesity_sdk.NodeRemovalParams() # NodeRemovalParams | Specifies parameters to initiate/cancel node removal .

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
> NodeInfo node_information(show_services_version_info=show_services_version_info)

Fetch Node General Information

Fetch general information about the node to which the request is sent to.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.node_info import NodeInfo
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    show_services_version_info = True # bool | Specifies whether to show version info of the services running on the node. (optional)

    try:
        # Fetch Node General Information
        api_response = api_instance.node_information(show_services_version_info=show_services_version_info)
        print("The response of PlatformApi->node_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->node_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_services_version_info** | **bool**| Specifies whether to show version info of the services running on the node. | [optional] 

### Return type

[**NodeInfo**](NodeInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.public_key_request import PublicKeyRequest
from cohesity_sdk.models.public_key_response import PublicKeyResponse
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.PublicKeyRequest() # PublicKeyRequest | Specifies the parameters required to retrieve SSH public key

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.node_power_operation import NodePowerOperation
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.NodePowerOperation() # NodePowerOperation | Specifies the reboot or shutdown operation.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.airgap_config import AirgapConfig
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.AirgapConfig() # AirgapConfig | Specifies the parameters to update airgap config.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster_amqp_target_config import ClusterAMQPTargetConfig
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.ClusterAMQPTargetConfig() # ClusterAMQPTargetConfig | Specifies the parameters to update cluster AMQP target config.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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

Update selected properties of chassis info by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.chassis import Chassis
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    id = 56 # int | Specifies the id of chassis.
    body = cohesity_sdk.Chassis() # Chassis | Specifies the parameters to update chassis. (optional)

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster import Cluster
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.Cluster() # Cluster | Specifies the parameters to update cluster.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster_snapshot_policy import ClusterSnapshotPolicy
from cohesity_sdk.models.update_snapshot_policy_params import UpdateSnapshotPolicyParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.UpdateSnapshotPolicyParams() # UpdateSnapshotPolicyParams | Specifies the parameters to update cluster snapshot policy.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster_vlan_params import ClusterVlanParams
from cohesity_sdk.models.update_cluster_vlan_params import UpdateClusterVlanParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    interface_name = 'interface_name_example' # str | Vlan interface name, it should be in interface_group_name.vlan_id format.
    body = cohesity_sdk.UpdateClusterVlanParams() # UpdateClusterVlanParams | Parameters to update vlan on the cluster.

    try:
        # Update vlan
        api_response = api_instance.update_cluster_vlan(interface_name, body)
        print("The response of PlatformApi->update_cluster_vlan:\n")
        pprint(api_response)
    except Exception as e:
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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

Update a feature flag override status to cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.feature_flag import FeatureFlag
from cohesity_sdk.models.update_feature_flag_params import UpdateFeatureFlagParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.UpdateFeatureFlagParams() # UpdateFeatureFlagParams | Param for feature flag override request.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.host_entry import HostEntry
from cohesity_sdk.models.host_mappings import HostMappings
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = [cohesity_sdk.HostEntry()] # List[HostEntry] | 

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.interface_params import InterfaceParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    id = 56 # int | Id of the interface.
    body = cohesity_sdk.InterfaceParams() # InterfaceParams | Parameters to update an interface on a node or cluster.

    try:
        # Update interface
        api_response = api_instance.update_interface(id, body)
        print("The response of PlatformApi->update_interface:\n")
        pprint(api_response)
    except Exception as e:
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.interface_group import InterfaceGroup
from cohesity_sdk.models.interface_group_params import InterfaceGroupParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    id = 56 # int | Id of the interface group.
    body = cohesity_sdk.InterfaceGroupParams() # InterfaceGroupParams | Parameters to update an interface group on the cluster.

    try:
        # Update interface group
        api_response = api_instance.update_interface_group(id, body)
        print("The response of PlatformApi->update_interface_group:\n")
        pprint(api_response)
    except Exception as e:
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.d_maa_s_info import DMaaSInfo
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.DMaaSInfo() # DMaaSInfo | Param to update whether the cluster is a DMaaS cluster.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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

Update selected properties of a rack given by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.rack import Rack
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    id = 56 # int | Specifies the id of rack.
    body = cohesity_sdk.Rack() # Rack | Specifies the parameters to update rack. (optional)

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.racks import Racks
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.Racks() # Racks | Specifies the parameters to update racks.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.smtp_configuration import SMTPConfiguration
from cohesity_sdk.models.update_smtp_params import UpdateSMTPParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.UpdateSMTPParams() # UpdateSMTPParams | Specifies the parameters to update cluster SMTP configuration.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.support_channel_config import SupportChannelConfig
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.SupportChannelConfig() # SupportChannelConfig | Specifies the support channel configuration.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.upgrade_checks_results import UpgradeChecksResults
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.upgrade_check_run_tests_request import UpgradeCheckRunTestsRequest
from cohesity_sdk.models.upgrade_check_run_tests_result import UpgradeCheckRunTestsResult
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.UpgradeCheckRunTestsRequest() # UpgradeCheckRunTestsRequest | Run upgrade checks on cluster.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster_operation_response_params import ClusterOperationResponseParams
from cohesity_sdk.models.cluster_uprade_params import ClusterUpradeParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.ClusterUpradeParams() # ClusterUpradeParams | The parameters to upgrade the software on the cluster.

    try:
        # Upgrade cluster
        api_response = api_instance.upgrade_cluster_software(body)
        print("The response of PlatformApi->upgrade_cluster_software:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->upgrade_cluster_software: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterUpradeParams**](ClusterUpradeParams.md)| The parameters to upgrade the software on the cluster. | 

### Return type

[**ClusterOperationResponseParams**](ClusterOperationResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.cluster_operation_response_params import ClusterOperationResponseParams
from cohesity_sdk.models.upload_package_url_params import UploadPackageUrlParams
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.UploadPackageUrlParams() # UploadPackageUrlParams | Parameters to upload a package by URL.

    try:
        # Upload package by URL
        api_response = api_instance.upload_package_by_url(body)
        print("The response of PlatformApi->upload_package_by_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->upload_package_by_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UploadPackageUrlParams**](UploadPackageUrlParams.md)| Parameters to upload a package by URL. | 

### Return type

[**ClusterOperationResponseParams**](ClusterOperationResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.test_smtp_config import TestSMTPConfig
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.PlatformApi(api_client)
    body = cohesity_sdk.TestSMTPConfig() # TestSMTPConfig | Specifies the request parameters to validate SMTP configuration.

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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

