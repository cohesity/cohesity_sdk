# cohesity_sdk.McmProtectionGroupsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mcm_protection_group**](McmProtectionGroupsApi.md#create_mcm_protection_group) | **POST** /mcm/data-protect/protection-groups | Create a Protection Group.
[**update_mcm_protection_group**](McmProtectionGroupsApi.md#update_mcm_protection_group) | **PUT** /mcm/data-protect/protection-groups/{id} | Update a Protection Group.


# **create_mcm_protection_group**
> ProtectionGroup create_mcm_protection_group(body)

Create a Protection Group.

Create a Protection Group.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.create_or_update_protection_group_request import CreateOrUpdateProtectionGroupRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.protection_group import ProtectionGroup
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CreateOrUpdateProtectionGroupRequest() # CreateOrUpdateProtectionGroupRequest | Specifies the parameters to create a Protection Group.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a Protection Group.
	api_response = client.mcm_protection_groups.create_mcm_protection_group(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling McmProtectionGroupsApi->create_mcm_protection_group: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a Protection Group.
	api_response = client.mcm_protection_groups.create_mcm_protection_group(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling McmProtectionGroupsApi->create_mcm_protection_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateProtectionGroupRequest**](CreateOrUpdateProtectionGroupRequest.md)| Specifies the parameters to create a Protection Group. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ProtectionGroup**](ProtectionGroup.md)

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

# **update_mcm_protection_group**
> ProtectionGroup update_mcm_protection_group(id, body)

Update a Protection Group.

Update the specified Protection Group.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.create_or_update_protection_group_request import CreateOrUpdateProtectionGroupRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.protection_group import ProtectionGroup
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies the id of the Protection Group.
body = CreateOrUpdateProtectionGroupRequest() # CreateOrUpdateProtectionGroupRequest | Specifies the parameters to update a Protection Group.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update a Protection Group.
	api_response = client.mcm_protection_groups.update_mcm_protection_group(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling McmProtectionGroupsApi->update_mcm_protection_group: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update a Protection Group.
	api_response = client.mcm_protection_groups.update_mcm_protection_group(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling McmProtectionGroupsApi->update_mcm_protection_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the Protection Group. |
 **body** | [**CreateOrUpdateProtectionGroupRequest**](CreateOrUpdateProtectionGroupRequest.md)| Specifies the parameters to update a Protection Group. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ProtectionGroup**](ProtectionGroup.md)

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

