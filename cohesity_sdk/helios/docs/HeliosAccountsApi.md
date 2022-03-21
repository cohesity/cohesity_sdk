# cohesity_sdk.HeliosAccountsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounts**](HeliosAccountsApi.md#get_accounts) | **GET** /mcm/accounts | Get Accounts
[**mcm_get_tenant_migration_status**](HeliosAccountsApi.md#mcm_get_tenant_migration_status) | **GET** /mcm/tenants/migrations | Get Tenant Migration Status
[**mcm_get_tenant_profiles**](HeliosAccountsApi.md#mcm_get_tenant_profiles) | **GET** /mcm/tenant-profiles | Get Tenant profiles
[**mcm_perform_tenant_action**](HeliosAccountsApi.md#mcm_perform_tenant_action) | **POST** /mcm/tenants/actions | Perform Mcm Tenant Action
[**perform_impersonation_action**](HeliosAccountsApi.md#perform_impersonation_action) | **POST** /mcm/accounts/impersonations/actions | Start or Stop Impersonation Session


# **get_accounts**
> HeliosAccounts get_accounts()

Get Accounts

Get Helios Accounts

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.helios_accounts import HeliosAccounts
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
search_string = "searchString_example" # str, none_type | Filter by accounts which partially match the string. (optional)
support_case_id = "supportCaseId_example" # str, none_type | Filter by Support Case ID. This must be specified if and only if the currently logged in user is a support user. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Accounts
	api_response = client.helios_accounts.get_accounts(region_id=region_id, search_string=search_string, support_case_id=support_case_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosAccountsApi->get_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **search_string** | **str, none_type**| Filter by accounts which partially match the string. | [optional]
 **support_case_id** | **str, none_type**| Filter by Support Case ID. This must be specified if and only if the currently logged in user is a support user. | [optional]

### Return type

[**HeliosAccounts**](HeliosAccounts.md)

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

# **mcm_get_tenant_migration_status**
> McmTenantMigrationStatus mcm_get_tenant_migration_status()

Get Tenant Migration Status

Get the migration status for the current tenant.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.mcm_tenant_migration_status import McmTenantMigrationStatus
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Tenant Migration Status
	api_response = client.helios_accounts.mcm_get_tenant_migration_status(region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosAccountsApi->mcm_get_tenant_migration_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**McmTenantMigrationStatus**](McmTenantMigrationStatus.md)

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

# **mcm_get_tenant_profiles**
> McmTenantProfiles mcm_get_tenant_profiles()

Get Tenant profiles

Get tenant profiles for currently logged in user.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.mcm_tenant_profiles import McmTenantProfiles
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Tenant profiles
	api_response = client.helios_accounts.mcm_get_tenant_profiles(region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosAccountsApi->mcm_get_tenant_profiles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**McmTenantProfiles**](McmTenantProfiles.md)

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

# **mcm_perform_tenant_action**
> McmTenantAction mcm_perform_tenant_action(body)

Perform Mcm Tenant Action

Perform an action on a DMaaS tenant.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.mcm_tenant_action import McmTenantAction
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = McmTenantAction(
        tenant_id="tenant_id_example",
        action="StartMigration",
    ) # McmTenantAction | Specifies the parameters to perform a tenant action.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Perform Mcm Tenant Action
	api_response = client.helios_accounts.mcm_perform_tenant_action(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosAccountsApi->mcm_perform_tenant_action: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Perform Mcm Tenant Action
	api_response = client.helios_accounts.mcm_perform_tenant_action(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosAccountsApi->mcm_perform_tenant_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**McmTenantAction**](McmTenantAction.md)| Specifies the parameters to perform a tenant action. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**McmTenantAction**](McmTenantAction.md)

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

# **perform_impersonation_action**
> ImpersonationAction perform_impersonation_action(body)

Start or Stop Impersonation Session

Starts or stops an impersonation session for Helios support and sales users.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.impersonation_action import ImpersonationAction
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = ImpersonationAction(
        sf_account_id="sf_account_id_example",
        action="StartImpersonation",
    ) # ImpersonationAction | Specifies the parameters to perform a tenant action.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Start or Stop Impersonation Session
	api_response = client.helios_accounts.perform_impersonation_action(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosAccountsApi->perform_impersonation_action: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Start or Stop Impersonation Session
	api_response = client.helios_accounts.perform_impersonation_action(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosAccountsApi->perform_impersonation_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImpersonationAction**](ImpersonationAction.md)| Specifies the parameters to perform a tenant action. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ImpersonationAction**](ImpersonationAction.md)

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

