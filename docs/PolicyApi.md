# cohesity_sdk.PolicyApi

All URIs are relative to */v2*

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.protection_policy_request import ProtectionPolicyRequest
from cohesity_sdk.models.protection_policy_response import ProtectionPolicyResponse
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
    api_instance = cohesity_sdk.PolicyApi(api_client)
    body = cohesity_sdk.ProtectionPolicyRequest() # ProtectionPolicyRequest | Request to create a Protection Policy.

    try:
        # Create a Protection Policy.
        api_response = api_instance.create_protection_policy(body)
        print("The response of PolicyApi->create_protection_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->create_protection_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtectionPolicyRequest**](ProtectionPolicyRequest.md)| Request to create a Protection Policy. | 

### Return type

[**ProtectionPolicyResponse**](ProtectionPolicyResponse.md)

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

# **delete_protection_policy**
> delete_protection_policy(id)

Delete a Protection Policy.

Deletes a Protection Policy based on given policy id.

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
    api_instance = cohesity_sdk.PolicyApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the Protection Policy to delete.

    try:
        # Delete a Protection Policy.
        api_instance.delete_protection_policy(id)
    except Exception as e:
        print("Exception when calling PolicyApi->delete_protection_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Policy to delete. | 

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

# **get_policy_template_by_id**
> PolicyTemplateResponse get_policy_template_by_id(id)

List details about a single Policy Template.

Returns the Policy Template corresponding to the specified Policy Id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.policy_template_response import PolicyTemplateResponse
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
    api_instance = cohesity_sdk.PolicyApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the Policy Template to return.

    try:
        # List details about a single Policy Template.
        api_response = api_instance.get_policy_template_by_id(id)
        print("The response of PolicyApi->get_policy_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->get_policy_template_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Policy Template to return. | 

### Return type

[**PolicyTemplateResponse**](PolicyTemplateResponse.md)

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

# **get_policy_templates**
> PolicyTemplatesResponseWithPagination get_policy_templates(request_initiator_type=request_initiator_type, ids=ids, policy_names=policy_names, tenant_ids=tenant_ids, include_tenants=include_tenants)

List Policy Templates filtered by query parameters.

Returns the policy templates based on the filtering parameters. If no parameters are specified, then all the policy templates are returned.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.policy_templates_response_with_pagination import PolicyTemplatesResponseWithPagination
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
    api_instance = cohesity_sdk.PolicyApi(api_client)
    request_initiator_type = 'request_initiator_type_example' # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
    ids = ['ids_example'] # List[str] | Filter policies by a list of policy template ids. (optional)
    policy_names = ['policy_names_example'] # List[str] | Filter policies by a list of policy names. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the organizations for which objects are to be returned. (optional)
    include_tenants = True # bool | IncludeTenantPolicies specifies if objects of all the organizations under the hierarchy of the logged in user's organization should be returned. (optional)

    try:
        # List Policy Templates filtered by query parameters.
        api_response = api_instance.get_policy_templates(request_initiator_type=request_initiator_type, ids=ids, policy_names=policy_names, tenant_ids=tenant_ids, include_tenants=include_tenants)
        print("The response of PolicyApi->get_policy_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->get_policy_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional] 
 **ids** | [**List[str]**](str.md)| Filter policies by a list of policy template ids. | [optional] 
 **policy_names** | [**List[str]**](str.md)| Filter policies by a list of policy names. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the organizations for which objects are to be returned. | [optional] 
 **include_tenants** | **bool**| IncludeTenantPolicies specifies if objects of all the organizations under the hierarchy of the logged in user&#39;s organization should be returned. | [optional] 

### Return type

[**PolicyTemplatesResponseWithPagination**](PolicyTemplatesResponseWithPagination.md)

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

# **get_protection_policies**
> ProtectionPolicyResponseWithPagination get_protection_policies(request_initiator_type=request_initiator_type, ids=ids, policy_names=policy_names, tenant_ids=tenant_ids, include_tenants=include_tenants, types=types, exclude_linked_policies=exclude_linked_policies, include_replicated_policies=include_replicated_policies, include_stats=include_stats)

List Protection Policies based on provided filtering parameters.

Lists protection policies based on filtering query parameters.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.protection_policy_response_with_pagination import ProtectionPolicyResponseWithPagination
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
    api_instance = cohesity_sdk.PolicyApi(api_client)
    request_initiator_type = 'request_initiator_type_example' # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
    ids = ['ids_example'] # List[str] | Filter policies by a list of policy ids. (optional)
    policy_names = ['policy_names_example'] # List[str] | Filter policies by a list of policy names. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the organizations for which objects are to be returned. (optional)
    include_tenants = True # bool | IncludeTenantPolicies specifies if objects of all the organizations under the hierarchy of the logged in user's organization should be returned. (optional)
    types = ["Regular"] # List[str] | Types specifies the policy type of policies to be returned (optional) (default to ["Regular"])
    exclude_linked_policies = True # bool | If excludeLinkedPolicies is set to true then only local policies created on cluster will be returned. The result will exclude all linked policies created from policy templates. (optional)
    include_replicated_policies = True # bool | If includeReplicatedPolicies is set to true, then response will also contain replicated policies. By default, replication policies are not included in the response. (optional)
    include_stats = True # bool | If includeStats is set to true, then response will return number of protection groups and objects. By default, the protection stats are not included in the response. (optional)

    try:
        # List Protection Policies based on provided filtering parameters.
        api_response = api_instance.get_protection_policies(request_initiator_type=request_initiator_type, ids=ids, policy_names=policy_names, tenant_ids=tenant_ids, include_tenants=include_tenants, types=types, exclude_linked_policies=exclude_linked_policies, include_replicated_policies=include_replicated_policies, include_stats=include_stats)
        print("The response of PolicyApi->get_protection_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->get_protection_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional] 
 **ids** | [**List[str]**](str.md)| Filter policies by a list of policy ids. | [optional] 
 **policy_names** | [**List[str]**](str.md)| Filter policies by a list of policy names. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the organizations for which objects are to be returned. | [optional] 
 **include_tenants** | **bool**| IncludeTenantPolicies specifies if objects of all the organizations under the hierarchy of the logged in user&#39;s organization should be returned. | [optional] 
 **types** | [**List[str]**](str.md)| Types specifies the policy type of policies to be returned | [optional] [default to [&quot;Regular&quot;]]
 **exclude_linked_policies** | **bool**| If excludeLinkedPolicies is set to true then only local policies created on cluster will be returned. The result will exclude all linked policies created from policy templates. | [optional] 
 **include_replicated_policies** | **bool**| If includeReplicatedPolicies is set to true, then response will also contain replicated policies. By default, replication policies are not included in the response. | [optional] 
 **include_stats** | **bool**| If includeStats is set to true, then response will return number of protection groups and objects. By default, the protection stats are not included in the response. | [optional] 

### Return type

[**ProtectionPolicyResponseWithPagination**](ProtectionPolicyResponseWithPagination.md)

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

# **get_protection_policy_by_id**
> ProtectionPolicyResponse get_protection_policy_by_id(id, request_initiator_type=request_initiator_type)

List details about a single Protection Policy.

Returns the Protection Policy details based on provided Policy Id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.protection_policy_response import ProtectionPolicyResponse
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
    api_instance = cohesity_sdk.PolicyApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the Protection Policy to return.
    request_initiator_type = 'request_initiator_type_example' # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)

    try:
        # List details about a single Protection Policy.
        api_response = api_instance.get_protection_policy_by_id(id, request_initiator_type=request_initiator_type)
        print("The response of PolicyApi->get_protection_policy_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyApi->get_protection_policy_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Policy to return. | 
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional] 

### Return type

[**ProtectionPolicyResponse**](ProtectionPolicyResponse.md)

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

# **update_protection_policy**
> ProtectionPolicyResponse update_protection_policy(id, body)

Update a Protection Policy.

Specifies the request to update the existing Protection Policy. On successful update, returns the updated policy object.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.protection_policy_request import ProtectionPolicyRequest
from cohesity_sdk.models.protection_policy_response import ProtectionPolicyResponse
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
    api_instance = cohesity_sdk.PolicyApi(api_client)
    id = 'id_example' # str | Specifies a unique id of the Protection Policy to update.
    body = cohesity_sdk.ProtectionPolicyRequest() # ProtectionPolicyRequest | Request to update a Protection Policy.

    try:
        # Update a Protection Policy.
        api_response = api_instance.update_protection_policy(id, body)
        print("The response of PolicyApi->update_protection_policy:\n")
        pprint(api_response)
    except Exception as e:
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

