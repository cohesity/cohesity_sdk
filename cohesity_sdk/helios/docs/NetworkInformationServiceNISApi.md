# cohesity_sdk.NetworkInformationServiceNISApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nis_netgroup**](NetworkInformationServiceNISApi.md#create_nis_netgroup) | **POST** /nis-netgroups | Create an NIS netgroup.
[**create_nis_provider**](NetworkInformationServiceNISApi.md#create_nis_provider) | **POST** /nis-providers | Create an NIS Provider.
[**delete_nis_netgroup_by_name**](NetworkInformationServiceNISApi.md#delete_nis_netgroup_by_name) | **DELETE** /nis-netgroups/{name} | Delete an NIS netgroup by name.
[**delete_nis_provider_by_domain_name**](NetworkInformationServiceNISApi.md#delete_nis_provider_by_domain_name) | **DELETE** /nis-providers/{domain} | Delete an NIS Provider by domain name.
[**get_nis_netgroup_by_name**](NetworkInformationServiceNISApi.md#get_nis_netgroup_by_name) | **GET** /nis-netgroups/{name} | Get an NIS netgroup by name.
[**get_nis_netgroups**](NetworkInformationServiceNISApi.md#get_nis_netgroups) | **GET** /nis-netgroups | Get a list of NIS netgroups.
[**get_nis_provider_by_domain_name**](NetworkInformationServiceNISApi.md#get_nis_provider_by_domain_name) | **GET** /nis-providers/{domain} | Get an NIS Provider by domain name.
[**get_nis_providers**](NetworkInformationServiceNISApi.md#get_nis_providers) | **GET** /nis-providers | Get a list of NIS Providers.
[**update_nis_netgroup_by_name**](NetworkInformationServiceNISApi.md#update_nis_netgroup_by_name) | **PUT** /nis-netgroups/{name} | Update an NIS netgroup by name.
[**update_nis_provider_by_domain_name**](NetworkInformationServiceNISApi.md#update_nis_provider_by_domain_name) | **PUT** /nis-providers/{domain} | Update an NIS Provider by domain name.


# **create_nis_netgroup**
> NisNetgroup create_nis_netgroup(body)

Create an NIS netgroup.

Create an NIS netgroup.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.nis_netgroup import NisNetgroup
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = NisNetgroup(
        name="name_example",
        domain="domain_example",
        nfs_access="kDisabled",
        nfs_squash="kNone",
    ) # NisNetgroup | Specifies the parameters to create an NIS netgroup.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create an NIS netgroup.
	api_response = client.network_information_service__nis.create_nis_netgroup(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->create_nis_netgroup: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create an NIS netgroup.
	api_response = client.network_information_service__nis.create_nis_netgroup(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->create_nis_netgroup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NisNetgroup**](NisNetgroup.md)| Specifies the parameters to create an NIS netgroup. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**NisNetgroup**](NisNetgroup.md)

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

# **create_nis_provider**
> NisProvider create_nis_provider(body)

Create an NIS Provider.

Create an NIS Provider.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.nis_provider import NisProvider
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = NisProvider(
        domain="domain_example",
        master_server_hostname="master_server_hostname_example",
        slave_servers=[
            "slave_servers_example",
        ],
        tenant_ids=[
            "tenant_ids_example",
        ],
    ) # NisProvider | Specifies the parameters to create an NIS provider entry.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create an NIS Provider.
	api_response = client.network_information_service__nis.create_nis_provider(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->create_nis_provider: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create an NIS Provider.
	api_response = client.network_information_service__nis.create_nis_provider(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->create_nis_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NisProvider**](NisProvider.md)| Specifies the parameters to create an NIS provider entry. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**NisProvider**](NisProvider.md)

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

# **delete_nis_netgroup_by_name**
> delete_nis_netgroup_by_name(name, body)

Delete an NIS netgroup by name.

Delete an NIS netgroup by name.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.nis_netgroup import NisNetgroup
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


name = "name_example" # str | Specifies name of the NIS netgroup.
body = NisNetgroup(
        name="name_example",
        domain="domain_example",
        nfs_access="kDisabled",
        nfs_squash="kNone",
    ) # NisNetgroup | Request to delete the NIS netgroup.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete an NIS netgroup by name.
	client.network_information_service__nis.delete_nis_netgroup_by_name(name, body)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->delete_nis_netgroup_by_name: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete an NIS netgroup by name.
	client.network_information_service__nis.delete_nis_netgroup_by_name(name, body, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->delete_nis_netgroup_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies name of the NIS netgroup. |
 **body** | [**NisNetgroup**](NisNetgroup.md)| Request to delete the NIS netgroup. |
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

# **delete_nis_provider_by_domain_name**
> delete_nis_provider_by_domain_name(domain)

Delete an NIS Provider by domain name.

Delete an NIS Provider by domain name.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


domain = "domain_example" # str | Specifies domain name of an NIS Provider.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete an NIS Provider by domain name.
	client.network_information_service__nis.delete_nis_provider_by_domain_name(domain)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->delete_nis_provider_by_domain_name: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete an NIS Provider by domain name.
	client.network_information_service__nis.delete_nis_provider_by_domain_name(domain, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->delete_nis_provider_by_domain_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Specifies domain name of an NIS Provider. |
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

# **get_nis_netgroup_by_name**
> NisNetgroup get_nis_netgroup_by_name(name)

Get an NIS netgroup by name.

Get an NIS netgroup by name.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.nis_netgroup import NisNetgroup
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


name = "name_example" # str | Specifies name of the NIS netgroup.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get an NIS netgroup by name.
	api_response = client.network_information_service__nis.get_nis_netgroup_by_name(name)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->get_nis_netgroup_by_name: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get an NIS netgroup by name.
	api_response = client.network_information_service__nis.get_nis_netgroup_by_name(name, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->get_nis_netgroup_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies name of the NIS netgroup. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**NisNetgroup**](NisNetgroup.md)

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

# **get_nis_netgroups**
> NisNetgroups get_nis_netgroups()

Get a list of NIS netgroups.

Get a list of NIS netgroups.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.nis_netgroups import NisNetgroups
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
netgroup_names = [
        "netgroupNames_example",
    ] # [str] | Filter by a list of NIS netgroup names. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a list of NIS netgroups.
	api_response = client.network_information_service__nis.get_nis_netgroups(access_cluster_id=access_cluster_id, region_id=region_id, netgroup_names=netgroup_names)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->get_nis_netgroups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **netgroup_names** | **[str]**| Filter by a list of NIS netgroup names. | [optional]

### Return type

[**NisNetgroups**](NisNetgroups.md)

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

# **get_nis_provider_by_domain_name**
> NisProvider get_nis_provider_by_domain_name(domain)

Get an NIS Provider by domain name.

Get an NIS Provider by domain name.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.nis_provider import NisProvider
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


domain = "domain_example" # str | Specifies domain of an NIS Provider.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get an NIS Provider by domain name.
	api_response = client.network_information_service__nis.get_nis_provider_by_domain_name(domain)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->get_nis_provider_by_domain_name: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get an NIS Provider by domain name.
	api_response = client.network_information_service__nis.get_nis_provider_by_domain_name(domain, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->get_nis_provider_by_domain_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Specifies domain of an NIS Provider. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**NisProvider**](NisProvider.md)

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

# **get_nis_providers**
> NisProviders get_nis_providers()

Get a list of NIS Providers.

Get a list of NIS Providers.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.nis_providers import NisProviders
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
domain_names = [
        "domainNames_example",
    ] # [str] | Filter by a list of NIS domain names. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a list of NIS Providers.
	api_response = client.network_information_service__nis.get_nis_providers(access_cluster_id=access_cluster_id, region_id=region_id, domain_names=domain_names)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->get_nis_providers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **domain_names** | **[str]**| Filter by a list of NIS domain names. | [optional]

### Return type

[**NisProviders**](NisProviders.md)

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

# **update_nis_netgroup_by_name**
> NisNetgroup update_nis_netgroup_by_name(name, body)

Update an NIS netgroup by name.

Update an NIS netgroup by name.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.nis_netgroup import NisNetgroup
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


name = "name_example" # str | Specifies name of the NIS netgroup.
body = NisNetgroup(
        name="name_example",
        domain="domain_example",
        nfs_access="kDisabled",
        nfs_squash="kNone",
    ) # NisNetgroup | Request to update the NIS netgroup.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update an NIS netgroup by name.
	api_response = client.network_information_service__nis.update_nis_netgroup_by_name(name, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->update_nis_netgroup_by_name: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update an NIS netgroup by name.
	api_response = client.network_information_service__nis.update_nis_netgroup_by_name(name, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->update_nis_netgroup_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies name of the NIS netgroup. |
 **body** | [**NisNetgroup**](NisNetgroup.md)| Request to update the NIS netgroup. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**NisNetgroup**](NisNetgroup.md)

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

# **update_nis_provider_by_domain_name**
> NisProvider update_nis_provider_by_domain_name(domain, body)

Update an NIS Provider by domain name.

Update an NIS Provider by domain name.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.nis_provider import NisProvider
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


domain = "domain_example" # str | Specifies domain name of an NIS Provider.
body = NisProvider(
        domain="domain_example",
        master_server_hostname="master_server_hostname_example",
        slave_servers=[
            "slave_servers_example",
        ],
        tenant_ids=[
            "tenant_ids_example",
        ],
    ) # NisProvider | Request to update an NIS Provider.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update an NIS Provider by domain name.
	api_response = client.network_information_service__nis.update_nis_provider_by_domain_name(domain, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->update_nis_provider_by_domain_name: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update an NIS Provider by domain name.
	api_response = client.network_information_service__nis.update_nis_provider_by_domain_name(domain, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NetworkInformationServiceNISApi->update_nis_provider_by_domain_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Specifies domain name of an NIS Provider. |
 **body** | [**NisProvider**](NisProvider.md)| Request to update an NIS Provider. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**NisProvider**](NisProvider.md)

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

