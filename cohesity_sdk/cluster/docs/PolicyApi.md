# cohesity_sdk.PolicyApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_protection_policy**](PolicyApi.md#create_protection_policy) | **POST** /data-protect/policies | Create a Protection Policy.
[**delete_protection_policy**](PolicyApi.md#delete_protection_policy) | **DELETE** /data-protect/policies/{id} | Delete a Protection Policy.
[**get_policy_template_by_id**](PolicyApi.md#get_policy_template_by_id) | **GET** /data-protect/policy-templates/{id} | List details about a single Policy Template.
[**get_policy_templates**](PolicyApi.md#get_policy_templates) | **GET** /data-protect/policy-templates | List Policy Templates filtered by query parameters.
[**get_protection_policies**](PolicyApi.md#get_protection_policies) | **GET** /data-protect/policies | List Protection Policies based on provided filtering parameters.
[**get_protection_policy_by_id**](PolicyApi.md#get_protection_policy_by_id) | **GET** /data-protect/policies/{id} | List details about a single Protection Policy.
[**update_protection_policy**](PolicyApi.md#update_protection_policy) | **PUT** /data-protect/policies/{id} | Update a Protection Policy.


# **create_protection_policy**
> ProtectionPolicyResponse create_protection_policy(body)

Create a Protection Policy.

Create the Protection Policy and returns the newly created policy object.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.protection_policy_response import ProtectionPolicyResponse
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.protection_policy_request import ProtectionPolicyRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ProtectionPolicyRequest() # ProtectionPolicyRequest | Request to create a Protection Policy.

# example passing only required values which don't have defaults set
try:
	# Create a Protection Policy.
	api_response = client.policy.create_protection_policy(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->create_protection_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtectionPolicyRequest**](ProtectionPolicyRequest.md)| Request to create a Protection Policy. |

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

# **delete_protection_policy**
> delete_protection_policy(id)

Delete a Protection Policy.

Deletes a Protection Policy based on given policy id.

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


id = "id_example" # str | Specifies a unique id of the Protection Policy to delete.

# example passing only required values which don't have defaults set
try:
	# Delete a Protection Policy.
	client.policy.delete_protection_policy(id)
except ApiException as e:
	print("Exception when calling PolicyApi->delete_protection_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Policy to delete. |

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

# **get_policy_template_by_id**
> PolicyTemplateResponse get_policy_template_by_id(id)

List details about a single Policy Template.

Returns the Policy Template corresponding to the specified Policy Id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.policy_template_response import PolicyTemplateResponse
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "id_example" # str | Specifies a unique id of the Policy Template to return.

# example passing only required values which don't have defaults set
try:
	# List details about a single Policy Template.
	api_response = client.policy.get_policy_template_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->get_policy_template_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Policy Template to return. |

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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.policy_templates_response_with_pagination import PolicyTemplatesResponseWithPagination
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


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
	api_response = client.policy.get_policy_templates(ids=ids, policy_names=policy_names, tenant_ids=tenant_ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->get_policy_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.protection_policy_response_with_pagination import ProtectionPolicyResponseWithPagination
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


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
	api_response = client.policy.get_protection_policies(ids=ids, policy_names=policy_names, tenant_ids=tenant_ids, include_tenants=include_tenants, types=types, exclude_linked_policies=exclude_linked_policies, include_replicated_policies=include_replicated_policies)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->get_protection_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.protection_policy_response import ProtectionPolicyResponse
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "id_example" # str | Specifies a unique id of the Protection Policy to return.

# example passing only required values which don't have defaults set
try:
	# List details about a single Protection Policy.
	api_response = client.policy.get_protection_policy_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->get_protection_policy_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Policy to return. |

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

# **update_protection_policy**
> ProtectionPolicyResponse update_protection_policy(id, body)

Update a Protection Policy.

Specifies the request to update the existing Protection Policy. On successful update, returns the updated policy object.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.protection_policy_response import ProtectionPolicyResponse
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.protection_policy_request import ProtectionPolicyRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "id_example" # str | Specifies a unique id of the Protection Policy to update.
body = ProtectionPolicyRequest() # ProtectionPolicyRequest | Request to update a Protection Policy.

# example passing only required values which don't have defaults set
try:
	# Update a Protection Policy.
	api_response = client.policy.update_protection_policy(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling PolicyApi->update_protection_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Policy to update. |
 **body** | [**ProtectionPolicyRequest**](ProtectionPolicyRequest.md)| Request to update a Protection Policy. |

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

