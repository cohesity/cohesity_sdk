# cohesity_sdk.HeliosProtectionPoliciesApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_helios_policy**](HeliosProtectionPoliciesApi.md#create_helios_policy) | **POST** /mcm/data-protect/policies | Create a Policy.
[**create_internal_helios_policy_from_kepler**](HeliosProtectionPoliciesApi.md#create_internal_helios_policy_from_kepler) | **POST** /mcm/kepler-internal/policies | Create a Internal Policy.
[**delete_helios_policy**](HeliosProtectionPoliciesApi.md#delete_helios_policy) | **DELETE** /mcm/data-protect/policies/{id} | Delete a Policy.
[**get_helios_policies**](HeliosProtectionPoliciesApi.md#get_helios_policies) | **GET** /mcm/data-protect/policies | List Policies based on provided filtering parameters.
[**get_helios_policy_by_id**](HeliosProtectionPoliciesApi.md#get_helios_policy_by_id) | **GET** /mcm/data-protect/policies/{id} | List details about a single Protection Policy.
[**update_helios_policy**](HeliosProtectionPoliciesApi.md#update_helios_policy) | **PUT** /mcm/data-protect/policies/{id} | Update a Protection Policy.


# **create_helios_policy**
> HeliosPolicyResponse create_helios_policy(body)

Create a Policy.

Create a Global policy or a DMaaS on Helios.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.helios_policy_request import HeliosPolicyRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.helios_policy_response import HeliosPolicyResponse
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = HeliosPolicyRequest() # HeliosPolicyRequest | Request to create a Helios Policy.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a Policy.
	api_response = client.helios_protection_policies.create_helios_policy(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionPoliciesApi->create_helios_policy: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a Policy.
	api_response = client.helios_protection_policies.create_helios_policy(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionPoliciesApi->create_helios_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HeliosPolicyRequest**](HeliosPolicyRequest.md)| Request to create a Helios Policy. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**HeliosPolicyResponse**](HeliosPolicyResponse.md)

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

# **create_internal_helios_policy_from_kepler**
> ProtectionPolicyResponse create_internal_helios_policy_from_kepler(body)

Create a Internal Policy.

Allows creating a ODP policy internally from Kepler micorservice.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.protection_policy_response import ProtectionPolicyResponse
from cohesity_sdk.helios.model.protection_policy_request import ProtectionPolicyRequest
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = ProtectionPolicyRequest() # ProtectionPolicyRequest | Request to create a Helios Policy.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a Internal Policy.
	api_response = client.helios_protection_policies.create_internal_helios_policy_from_kepler(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionPoliciesApi->create_internal_helios_policy_from_kepler: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a Internal Policy.
	api_response = client.helios_protection_policies.create_internal_helios_policy_from_kepler(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionPoliciesApi->create_internal_helios_policy_from_kepler: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtectionPolicyRequest**](ProtectionPolicyRequest.md)| Request to create a Helios Policy. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ProtectionPolicyResponse**](ProtectionPolicyResponse.md)

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

# **delete_helios_policy**
> delete_helios_policy(id)

Delete a Policy.

Deletes a Policy based on given policy id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies a unique id of the Policy to delete.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete a Policy.
	client.helios_protection_policies.delete_helios_policy(id)
except ApiException as e:
	print("Exception when calling HeliosProtectionPoliciesApi->delete_helios_policy: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete a Policy.
	client.helios_protection_policies.delete_helios_policy(id, region_id=region_id)
except ApiException as e:
	print("Exception when calling HeliosProtectionPoliciesApi->delete_helios_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Policy to delete. |
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

# **get_helios_policies**
> HeliosPoliciesResponseWithPagination get_helios_policies()

List Policies based on provided filtering parameters.

Lists policies based on filtering query parameters.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.helios_policies_response_with_pagination import HeliosPoliciesResponseWithPagination
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
ids = [
        "ids_example",
    ] # [str] | Filter policies by a list of policy ids. (optional)
policy_names = [
        "policyNames_example",
    ] # [str] | Filter policies by a list of policy names. (optional)
types = [
        "GlobalPolicy",
    ] # [str], none_type | Type specifies the policy type of policies to be returned. If not specified, all types of policies are fetched. (optional)
cluster_identifiers = [
        "4:072888001528021798096225500850762068629",
    ] # [str] | Specifies the list of cluster identifiers. This is applicable only for type OnPremPolicy. The format is clusterId:clusterIncarnationId. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str, none_type] | List of Tenant Ids to filter from. This is applicable only for type OnPremPolicy. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List Policies based on provided filtering parameters.
	api_response = client.helios_protection_policies.get_helios_policies(region_id=region_id, ids=ids, policy_names=policy_names, types=types, cluster_identifiers=cluster_identifiers, tenant_ids=tenant_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionPoliciesApi->get_helios_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **ids** | **[str]**| Filter policies by a list of policy ids. | [optional]
 **policy_names** | **[str]**| Filter policies by a list of policy names. | [optional]
 **types** | **[str], none_type**| Type specifies the policy type of policies to be returned. If not specified, all types of policies are fetched. | [optional]
 **cluster_identifiers** | **[str]**| Specifies the list of cluster identifiers. This is applicable only for type OnPremPolicy. The format is clusterId:clusterIncarnationId. | [optional]
 **tenant_ids** | [**[str, none_type]**](str, none_type.md)| List of Tenant Ids to filter from. This is applicable only for type OnPremPolicy. | [optional]

### Return type

[**HeliosPoliciesResponseWithPagination**](HeliosPoliciesResponseWithPagination.md)

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

# **get_helios_policy_by_id**
> HeliosPolicyResponse get_helios_policy_by_id(id)

List details about a single Protection Policy.

Returns the Protection Policy details based on provided Policy Id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.helios_policy_response import HeliosPolicyResponse
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies a unique id of the Protection Policy to return.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# List details about a single Protection Policy.
	api_response = client.helios_protection_policies.get_helios_policy_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionPoliciesApi->get_helios_policy_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List details about a single Protection Policy.
	api_response = client.helios_protection_policies.get_helios_policy_by_id(id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionPoliciesApi->get_helios_policy_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Policy to return. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**HeliosPolicyResponse**](HeliosPolicyResponse.md)

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

# **update_helios_policy**
> HeliosPolicyResponse update_helios_policy(id, body)

Update a Protection Policy.

Specifies the request to update the existing Protection Policy. On successful update, returns the updated policy object.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.helios_policy_request import HeliosPolicyRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.helios_policy_response import HeliosPolicyResponse
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies a unique id of the Protection Policy to update.
body = HeliosPolicyRequest() # HeliosPolicyRequest | Request to update a Protection Policy.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update a Protection Policy.
	api_response = client.helios_protection_policies.update_helios_policy(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionPoliciesApi->update_helios_policy: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update a Protection Policy.
	api_response = client.helios_protection_policies.update_helios_policy(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionPoliciesApi->update_helios_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Policy to update. |
 **body** | [**HeliosPolicyRequest**](HeliosPolicyRequest.md)| Request to update a Protection Policy. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**HeliosPolicyResponse**](HeliosPolicyResponse.md)

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

