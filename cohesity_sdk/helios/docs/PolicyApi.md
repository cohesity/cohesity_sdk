# cohesity_sdk.PolicyApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_helios_policy**](PolicyApi.md#create_helios_policy) | **POST** /mcm/data-protect/policies | Create a Policy.
[**create_internal_helios_policy_from_kepler**](PolicyApi.md#create_internal_helios_policy_from_kepler) | **POST** /mcm/kepler-internal/policies | Create a Internal Policy.
[**create_protection_policy**](PolicyApi.md#create_protection_policy) | **POST** /data-protect/policies | Create a Protection Policy.
[**delete_helios_policy**](PolicyApi.md#delete_helios_policy) | **DELETE** /mcm/data-protect/policies/{id} | Delete a Policy.
[**delete_protection_policy**](PolicyApi.md#delete_protection_policy) | **DELETE** /data-protect/policies/{id} | Delete a Protection Policy.
[**get_helios_policies**](PolicyApi.md#get_helios_policies) | **GET** /mcm/data-protect/policies | List Policies based on provided filtering parameters.
[**get_helios_policy_by_id**](PolicyApi.md#get_helios_policy_by_id) | **GET** /mcm/data-protect/policies/{id} | List details about a single Protection Policy.
[**get_policy_template_by_id**](PolicyApi.md#get_policy_template_by_id) | **GET** /data-protect/policy-templates/{id} | List details about a single Policy Template.
[**get_policy_templates**](PolicyApi.md#get_policy_templates) | **GET** /data-protect/policy-templates | List Policy Templates filtered by query parameters.
[**get_protection_policies**](PolicyApi.md#get_protection_policies) | **GET** /data-protect/policies | List Protection Policies based on provided filtering parameters.
[**get_protection_policy_by_id**](PolicyApi.md#get_protection_policy_by_id) | **GET** /data-protect/policies/{id} | List details about a single Protection Policy.
[**update_helios_policy**](PolicyApi.md#update_helios_policy) | **PUT** /mcm/data-protect/policies/{id} | Update a Protection Policy.
[**update_protection_policy**](PolicyApi.md#update_protection_policy) | **PUT** /data-protect/policies/{id} | Update a Protection Policy.


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
	api_response = client.policy.create_helios_policy(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->create_helios_policy: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a Policy.
	api_response = client.policy.create_helios_policy(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->create_helios_policy: %s\n" % e)
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
	api_response = client.policy.create_internal_helios_policy_from_kepler(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->create_internal_helios_policy_from_kepler: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a Internal Policy.
	api_response = client.policy.create_internal_helios_policy_from_kepler(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->create_internal_helios_policy_from_kepler: %s\n" % e)
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

# **create_protection_policy**
> ProtectionPolicyResponse create_protection_policy(body)

Create a Protection Policy.

Create the Protection Policy and returns the newly created policy object.

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


body = ProtectionPolicyRequest() # ProtectionPolicyRequest | Request to create a Protection Policy.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a Protection Policy.
	api_response = client.policy.create_protection_policy(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->create_protection_policy: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a Protection Policy.
	api_response = client.policy.create_protection_policy(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->create_protection_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtectionPolicyRequest**](ProtectionPolicyRequest.md)| Request to create a Protection Policy. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
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
	client.policy.delete_helios_policy(id)
except ApiException as e:
	print("Exception when calling PolicyApi->delete_helios_policy: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete a Policy.
	client.policy.delete_helios_policy(id, region_id=region_id)
except ApiException as e:
	print("Exception when calling PolicyApi->delete_helios_policy: %s\n" % e)
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

# **delete_protection_policy**
> delete_protection_policy(id)

Delete a Protection Policy.

Deletes a Protection Policy based on given policy id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies a unique id of the Protection Policy to delete.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete a Protection Policy.
	client.policy.delete_protection_policy(id)
except ApiException as e:
	print("Exception when calling PolicyApi->delete_protection_policy: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete a Protection Policy.
	client.policy.delete_protection_policy(id, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling PolicyApi->delete_protection_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Policy to delete. |
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
	api_response = client.policy.get_helios_policies(region_id=region_id, ids=ids, policy_names=policy_names, types=types, cluster_identifiers=cluster_identifiers, tenant_ids=tenant_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->get_helios_policies: %s\n" % e)
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
	api_response = client.policy.get_helios_policy_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->get_helios_policy_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List details about a single Protection Policy.
	api_response = client.policy.get_helios_policy_by_id(id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->get_helios_policy_by_id: %s\n" % e)
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

# **get_policy_template_by_id**
> PolicyTemplateResponse get_policy_template_by_id(id)

List details about a single Policy Template.

Returns the Policy Template corresponding to the specified Policy Id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.policy_template_response import PolicyTemplateResponse
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies a unique id of the Policy Template to return.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# List details about a single Policy Template.
	api_response = client.policy.get_policy_template_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->get_policy_template_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List details about a single Policy Template.
	api_response = client.policy.get_policy_template_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->get_policy_template_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Policy Template to return. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**PolicyTemplateResponse**](PolicyTemplateResponse.md)

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

# **get_policy_templates**
> PolicyTemplatesResponseWithPagination get_policy_templates()

List Policy Templates filtered by query parameters.

Returns the policy templates based on the filtering parameters. If no parameters are specified, then all the policy templates are returned.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.policy_templates_response_with_pagination import PolicyTemplatesResponseWithPagination
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
ids = [
        "ids_example",
    ] # [str] | Filter policies by a list of policy template ids. (optional)
policy_names = [
        "policyNames_example",
    ] # [str] | Filter policies by a list of policy names. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the organizations for which objects are to be returned. (optional)
include_tenants = True # bool | IncludeTenantPolicies specifies if objects of all the organizations under the hierarchy of the logged in user's organization should be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List Policy Templates filtered by query parameters.
	api_response = client.policy.get_policy_templates(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, policy_names=policy_names, tenant_ids=tenant_ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->get_policy_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **ids** | **[str]**| Filter policies by a list of policy template ids. | [optional]
 **policy_names** | **[str]**| Filter policies by a list of policy names. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the organizations for which objects are to be returned. | [optional]
 **include_tenants** | **bool**| IncludeTenantPolicies specifies if objects of all the organizations under the hierarchy of the logged in user&#39;s organization should be returned. | [optional]

### Return type

[**PolicyTemplatesResponseWithPagination**](PolicyTemplatesResponseWithPagination.md)

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

# **get_protection_policies**
> ProtectionPolicyResponseWithPagination get_protection_policies()

List Protection Policies based on provided filtering parameters.

Lists protection policies based on filtering query parameters.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.protection_policy_response_with_pagination import ProtectionPolicyResponseWithPagination
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
ids = [
        "ids_example",
    ] # [str] | Filter policies by a list of policy ids. (optional)
policy_names = [
        "policyNames_example",
    ] # [str] | Filter policies by a list of policy names. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the organizations for which objects are to be returned. (optional)
include_tenants = True # bool | IncludeTenantPolicies specifies if objects of all the organizations under the hierarchy of the logged in user's organization should be returned. (optional)
types = [
        "["Regular"]",
    ] # [str] | Types specifies the policy type of policies to be returned (optional) if omitted the server will use the default value of ["Regular"]
exclude_linked_policies = True # bool | If excludeLinkedPolicies is set to true then only local policies created on cluster will be returned. The result will exclude all linked policies created from policy templates. (optional)
include_replicated_policies = True # bool | If includeReplicatedPolicies is set to true, then response will also contain replicated policies. By default, replication policies are not included in the response. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List Protection Policies based on provided filtering parameters.
	api_response = client.policy.get_protection_policies(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, policy_names=policy_names, tenant_ids=tenant_ids, include_tenants=include_tenants, types=types, exclude_linked_policies=exclude_linked_policies, include_replicated_policies=include_replicated_policies)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->get_protection_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **ids** | **[str]**| Filter policies by a list of policy ids. | [optional]
 **policy_names** | **[str]**| Filter policies by a list of policy names. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the organizations for which objects are to be returned. | [optional]
 **include_tenants** | **bool**| IncludeTenantPolicies specifies if objects of all the organizations under the hierarchy of the logged in user&#39;s organization should be returned. | [optional]
 **types** | **[str]**| Types specifies the policy type of policies to be returned | [optional] if omitted the server will use the default value of ["Regular"]
 **exclude_linked_policies** | **bool**| If excludeLinkedPolicies is set to true then only local policies created on cluster will be returned. The result will exclude all linked policies created from policy templates. | [optional]
 **include_replicated_policies** | **bool**| If includeReplicatedPolicies is set to true, then response will also contain replicated policies. By default, replication policies are not included in the response. | [optional]

### Return type

[**ProtectionPolicyResponseWithPagination**](ProtectionPolicyResponseWithPagination.md)

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

# **get_protection_policy_by_id**
> ProtectionPolicyResponse get_protection_policy_by_id(id)

List details about a single Protection Policy.

Returns the Protection Policy details based on provided Policy Id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.protection_policy_response import ProtectionPolicyResponse
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies a unique id of the Protection Policy to return.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# List details about a single Protection Policy.
	api_response = client.policy.get_protection_policy_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->get_protection_policy_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List details about a single Protection Policy.
	api_response = client.policy.get_protection_policy_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->get_protection_policy_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Policy to return. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ProtectionPolicyResponse**](ProtectionPolicyResponse.md)

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
	api_response = client.policy.update_helios_policy(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->update_helios_policy: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update a Protection Policy.
	api_response = client.policy.update_helios_policy(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->update_helios_policy: %s\n" % e)
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

# **update_protection_policy**
> ProtectionPolicyResponse update_protection_policy(id, body)

Update a Protection Policy.

Specifies the request to update the existing Protection Policy. On successful update, returns the updated policy object.

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


id = "id_example" # str | Specifies a unique id of the Protection Policy to update.
body = ProtectionPolicyRequest() # ProtectionPolicyRequest | Request to update a Protection Policy.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update a Protection Policy.
	api_response = client.policy.update_protection_policy(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->update_protection_policy: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update a Protection Policy.
	api_response = client.policy.update_protection_policy(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->update_protection_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Policy to update. |
 **body** | [**ProtectionPolicyRequest**](ProtectionPolicyRequest.md)| Request to update a Protection Policy. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
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
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

