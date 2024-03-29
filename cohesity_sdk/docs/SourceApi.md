# cohesity_sdk.SourceApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_azure_applications**](SourceApi.md#create_azure_applications) | **POST** /data-protect/sources/microsoft365/azure-applications | Create Microsoft 365 Azure Applications for a given domain.
[**delete_protection_source_registration**](SourceApi.md#delete_protection_source_registration) | **DELETE** /data-protect/sources/registrations/{id} | Delete Protection Source Registration.
[**generate_m365_device_access_token**](SourceApi.md#generate_m365_device_access_token) | **POST** /data-protect/sources/microsoft365/auth/token | Generate access token for Microsoft365 Device Authorization Grant flow.
[**generate_m365_device_code**](SourceApi.md#generate_m365_device_code) | **POST** /data-protect/sources/microsoft365/auth/device-code | Generate device code for Microsoft365 Device Authorization Grant flow.
[**get_m365_source_region_endpoint**](SourceApi.md#get_m365_source_region_endpoint) | **GET** /data-protect/sources/microsoft365/region-info | Generates the region and endpoint for the Microsoft365 source.
[**get_protection_source_registration**](SourceApi.md#get_protection_source_registration) | **GET** /data-protect/sources/registrations/{id} | Get a Protection Source registration.
[**get_protection_sources**](SourceApi.md#get_protection_sources) | **GET** /data-protect/sources | Get a List of Protection Sources.
[**get_source_attribute_filters**](SourceApi.md#get_source_attribute_filters) | **GET** /data-protect/sources/filters | List attribute filters for a source.
[**get_source_registrations**](SourceApi.md#get_source_registrations) | **GET** /data-protect/sources/registrations | Get the list of Protection Source registrations.
[**get_vdc_details**](SourceApi.md#get_vdc_details) | **GET** /data-protect/sources/virtual-datacenter/{id} | Get VDC Details.
[**patch_protection_source_registration**](SourceApi.md#patch_protection_source_registration) | **PATCH** /data-protect/sources/registrations/{id} | Perform Partial Update on Protection Source registration. Currently this API is supported only for Cassandra
[**protection_source_by_id**](SourceApi.md#protection_source_by_id) | **GET** /data-protect/sources/{id} | Get a Protection Sources.
[**refresh_protection_source_by_id**](SourceApi.md#refresh_protection_source_by_id) | **POST** /data-protect/sources/{id}/refresh | Refresh a Protection Source.
[**register_protection_source**](SourceApi.md#register_protection_source) | **POST** /data-protect/sources/registrations | Register a Protection Source.
[**test_connection_protection_source**](SourceApi.md#test_connection_protection_source) | **POST** /data-protect/sources/test-connection | Test connection to a source.
[**update_protection_source_registration**](SourceApi.md#update_protection_source_registration) | **PUT** /data-protect/sources/registrations/{id} | Update Protection Source registration.


# **create_azure_applications**
> CreateAzureApplicationResponseParams create_azure_applications(body)

Create Microsoft 365 Azure Applications for a given domain.

Creates Microsoft 365 Azure Applications

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.create_azure_application_request_params import CreateAzureApplicationRequestParams
from cohesity_sdk.cluster.model.create_azure_application_response_params import CreateAzureApplicationResponseParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateAzureApplicationRequestParams(
        access_token="access_token_example",
        username="username_example",
        microsoft365_region="Default",
        app_count=1,
        existing_microsoft365_app_credentials_list=[
            Office365AppCredentials(
                client_id="client_id_example",
                client_secret="client_secret_example",
            ),
        ],
    ) # CreateAzureApplicationRequestParams | Specifies the parameters to create Azure applications within a given Microsoft365 source.

# example passing only required values which don't have defaults set
try:
	# Create Microsoft 365 Azure Applications for a given domain.
	api_response = client.source.create_azure_applications(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SourceApi->create_azure_applications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAzureApplicationRequestParams**](CreateAzureApplicationRequestParams.md)| Specifies the parameters to create Azure applications within a given Microsoft365 source. |

### Return type

[**CreateAzureApplicationResponseParams**](CreateAzureApplicationResponseParams.md)

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

# **delete_protection_source_registration**
> delete_protection_source_registration(id)

Delete Protection Source Registration.

Delete Protection Source Registration.

### Example

* Api Key Authentication (APIKeyHeader):
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


id = 1 # int | Specifies the ID of the Protection Source Registration.

# example passing only required values which don't have defaults set
try:
	# Delete Protection Source Registration.
	client.source.delete_protection_source_registration(id)
except ApiException as e:
	print("Exception when calling SourceApi->delete_protection_source_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the ID of the Protection Source Registration. |

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

# **generate_m365_device_access_token**
> GenerateM365DeviceAccessTokenResponseParams generate_m365_device_access_token(body)

Generate access token for Microsoft365 Device Authorization Grant flow.

Generates the access token if the device code has been granted authorization as part of device login flow.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.generate_m365_device_access_token_response_params import GenerateM365DeviceAccessTokenResponseParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.generate_m365_device_access_token_request_params import GenerateM365DeviceAccessTokenRequestParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = GenerateM365DeviceAccessTokenRequestParams(
        domain="domain_example",
        device_code="device_code_example",
    ) # GenerateM365DeviceAccessTokenRequestParams | Specifies the parameters to validate and generate access token for authorizing the client within Microsoft365.

# example passing only required values which don't have defaults set
try:
	# Generate access token for Microsoft365 Device Authorization Grant flow.
	api_response = client.source.generate_m365_device_access_token(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SourceApi->generate_m365_device_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateM365DeviceAccessTokenRequestParams**](GenerateM365DeviceAccessTokenRequestParams.md)| Specifies the parameters to validate and generate access token for authorizing the client within Microsoft365. |

### Return type

[**GenerateM365DeviceAccessTokenResponseParams**](GenerateM365DeviceAccessTokenResponseParams.md)

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

# **generate_m365_device_code**
> GenerateM365DeviceCodeResponseParams generate_m365_device_code(body)

Generate device code for Microsoft365 Device Authorization Grant flow.

Generates User and Device code for Microsoft365 Device Authorization Grant for a given domain.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.generate_m365_device_code_request_params import GenerateM365DeviceCodeRequestParams
from cohesity_sdk.cluster.model.generate_m365_device_code_response_params import GenerateM365DeviceCodeResponseParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = GenerateM365DeviceCodeRequestParams(
        domain="domain_example",
    ) # GenerateM365DeviceCodeRequestParams | Specifies the parameters to generate the user and device code to initiate authentication with Microsoft365.

# example passing only required values which don't have defaults set
try:
	# Generate device code for Microsoft365 Device Authorization Grant flow.
	api_response = client.source.generate_m365_device_code(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SourceApi->generate_m365_device_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateM365DeviceCodeRequestParams**](GenerateM365DeviceCodeRequestParams.md)| Specifies the parameters to generate the user and device code to initiate authentication with Microsoft365. |

### Return type

[**GenerateM365DeviceCodeResponseParams**](GenerateM365DeviceCodeResponseParams.md)

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

# **get_m365_source_region_endpoint**
> GetM365SourceRegionEndpointResponseParams get_m365_source_region_endpoint(domain)

Generates the region and endpoint for the Microsoft365 source.

Fetches the region and endpoint for the Microsoft365 source.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.get_m365_source_region_endpoint_response_params import GetM365SourceRegionEndpointResponseParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


domain = "domain_example" # str | Specifies the domain name of the source.

# example passing only required values which don't have defaults set
try:
	# Generates the region and endpoint for the Microsoft365 source.
	api_response = client.source.get_m365_source_region_endpoint(domain)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SourceApi->get_m365_source_region_endpoint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Specifies the domain name of the source. |

### Return type

[**GetM365SourceRegionEndpointResponseParams**](GetM365SourceRegionEndpointResponseParams.md)

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

# **get_protection_source_registration**
> CommonSourceRegistrationReponseParams0a86bd5cF7de4a5085d3Aa7003ecba89 get_protection_source_registration(id)

Get a Protection Source registration.

Get a Protection Source registration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.common_source_registration_reponse_params0a86bd5c_f7de4a5085d3_aa7003ecba89 import CommonSourceRegistrationReponseParams0a86bd5cF7de4a5085d3Aa7003ecba89
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the Protection Source registration.

# example passing only required values which don't have defaults set
try:
	# Get a Protection Source registration.
	api_response = client.source.get_protection_source_registration(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SourceApi->get_protection_source_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source registration. |

### Return type

[**CommonSourceRegistrationReponseParams0a86bd5cF7de4a5085d3Aa7003ecba89**](CommonSourceRegistrationReponseParams0a86bd5cF7de4a5085d3Aa7003ecba89.md)

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

# **get_protection_sources**
> Sources get_protection_sources()

Get a List of Protection Sources.

Get a List of Protection Sources.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.sources import Sources
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which Sources are to be returned. (optional)
include_tenants = True # bool | If true, the response will include Sources which belong belong to all tenants which the current user has permission to see. If false, then only Sources for the current user will be returned. (optional)
include_source_credentials = True # bool | If true, the encrypted crednetial for the registered sources will be included. Credential is first encrypted with internal key and then reencrypted with user supplied encryption key. (optional)
encryption_key = "encryptionKey_example" # str | Specifies the key to be used to encrypt the source credential. If includeSourceCredentials is set to true this key must be specified. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a List of Protection Sources.
	api_response = client.source.get_protection_sources(tenant_ids=tenant_ids, include_tenants=include_tenants, include_source_credentials=include_source_credentials, encryption_key=encryption_key)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SourceApi->get_protection_sources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which Sources are to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include Sources which belong belong to all tenants which the current user has permission to see. If false, then only Sources for the current user will be returned. | [optional]
 **include_source_credentials** | **bool**| If true, the encrypted crednetial for the registered sources will be included. Credential is first encrypted with internal key and then reencrypted with user supplied encryption key. | [optional]
 **encryption_key** | **str**| Specifies the key to be used to encrypt the source credential. If includeSourceCredentials is set to true this key must be specified. | [optional]

### Return type

[**Sources**](Sources.md)

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

# **get_source_attribute_filters**
> SourceAttributeFiltersResponseParams get_source_attribute_filters(source_uuid)

List attribute filters for a source.

Get a List of attribute filters for leaf entities within a a source

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.source_attribute_filters_response_params import SourceAttributeFiltersResponseParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


source_uuid = "sourceUuid_example" # str | Specifies the source UUID of the parent entity.
environment = "kVMware" # str, none_type | Specifies the environment type of the Protection Source. (optional)

# example passing only required values which don't have defaults set
try:
	# List attribute filters for a source.
	api_response = client.source.get_source_attribute_filters(source_uuid)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SourceApi->get_source_attribute_filters: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List attribute filters for a source.
	api_response = client.source.get_source_attribute_filters(source_uuid, environment=environment)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SourceApi->get_source_attribute_filters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_uuid** | **str**| Specifies the source UUID of the parent entity. |
 **environment** | **str, none_type**| Specifies the environment type of the Protection Source. | [optional]

### Return type

[**SourceAttributeFiltersResponseParams**](SourceAttributeFiltersResponseParams.md)

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

# **get_source_registrations**
> SourceRegistrations get_source_registrations()

Get the list of Protection Source registrations.

Get the list of Protection Source registrations.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.source_registrations import SourceRegistrations
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
    ] # [int] | Ids specifies the list of source registration ids to return. If left empty, every source registration will be returned by default. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
include_tenants = True # bool | If true, the response will include Registrations which were created by all tenants which the current user has permission to see. If false, then only Registrations created by the current user will be returned. (optional)
include_source_credentials = True # bool | If true, the encrypted crednetial for the registered sources will be included. Credential is first encrypted with internal key and then reencrypted with user supplied encryption key. (optional)
encryption_key = "encryptionKey_example" # str | Specifies the key to be used to encrypt the source credential. If includeSourceCredentials is set to true this key must be specified. (optional)
use_cached_data = True # bool | Specifies whether we can serve the GET request from the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of Protection Source registrations.
	api_response = client.source.get_source_registrations(ids=ids, tenant_ids=tenant_ids, include_tenants=include_tenants, include_source_credentials=include_source_credentials, encryption_key=encryption_key, use_cached_data=use_cached_data)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SourceApi->get_source_registrations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**| Ids specifies the list of source registration ids to return. If left empty, every source registration will be returned by default. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which objects are to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include Registrations which were created by all tenants which the current user has permission to see. If false, then only Registrations created by the current user will be returned. | [optional]
 **include_source_credentials** | **bool**| If true, the encrypted crednetial for the registered sources will be included. Credential is first encrypted with internal key and then reencrypted with user supplied encryption key. | [optional]
 **encryption_key** | **str**| Specifies the key to be used to encrypt the source credential. If includeSourceCredentials is set to true this key must be specified. | [optional]
 **use_cached_data** | **bool**| Specifies whether we can serve the GET request from the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. | [optional]

### Return type

[**SourceRegistrations**](SourceRegistrations.md)

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

# **get_vdc_details**
> VdcObject get_vdc_details(id)

Get VDC Details.

Get the details such as catelogs, Org networks associated with a VMware virtual datacenter (VDC).

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.vdc_object import VdcObject
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the ID of the VMware virtual datacenter.

# example passing only required values which don't have defaults set
try:
	# Get VDC Details.
	api_response = client.source.get_vdc_details(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SourceApi->get_vdc_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the ID of the VMware virtual datacenter. |

### Return type

[**VdcObject**](VdcObject.md)

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

# **patch_protection_source_registration**
> CommonSourceRegistrationReponseParams0a86bd5cF7de4a5085d3Aa7003ecba89 patch_protection_source_registration(id, body)

Perform Partial Update on Protection Source registration. Currently this API is supported only for Cassandra

Patches a Protection Source.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.source_registration_patch_request_params import SourceRegistrationPatchRequestParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.common_source_registration_reponse_params0a86bd5c_f7de4a5085d3_aa7003ecba89 import CommonSourceRegistrationReponseParams0a86bd5cF7de4a5085d3Aa7003ecba89
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the Protection Source registration.
body = SourceRegistrationPatchRequestParams(
        environment="kVMware",
        cassandra_params=CassandraSourceRegistrationPatchParams(
            seed_node="seed_node_example",
            config_directory="config_directory_example",
            dse_configuration_directory="dse_configuration_directory_example",
            is_dse_tiered_storage=True,
            is_dse_authenticator=True,
            ssh_password_credentials=SshPasswordCredentials(
                username="username_example",
                password="password_example",
            ),
            ssh_private_key_credentials=SshPrivateKeyCredentials(
                user_id="user_id_example",
                private_key="private_key_example",
                passphrase="passphrase_example",
            ),
            jmx_credentials=CassandraSourceRegistrationPatchParamsJmxCredentials(
                password="password_example",
                username="username_example",
            ),
            cassandra_credentials=CassandraSourceRegistrationPatchParamsCassandraCredentials(
                password="password_example",
                username="username_example",
            ),
            data_center_names=[
                "data_center_names_example",
            ],
            commit_log_backup_location="commit_log_backup_location_example",
            kerberos_principal="kerberos_principal_example",
            dse_solr_info=DSESolrInfo(
                solr_nodes=[
                    "solr_nodes_example",
                ],
                solr_port=1,
            ),
        ),
    ) # SourceRegistrationPatchRequestParams | Specifies the parameters to partially update the registration.

# example passing only required values which don't have defaults set
try:
	# Perform Partial Update on Protection Source registration. Currently this API is supported only for Cassandra
	api_response = client.source.patch_protection_source_registration(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SourceApi->patch_protection_source_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source registration. |
 **body** | [**SourceRegistrationPatchRequestParams**](SourceRegistrationPatchRequestParams.md)| Specifies the parameters to partially update the registration. |

### Return type

[**CommonSourceRegistrationReponseParams0a86bd5cF7de4a5085d3Aa7003ecba89**](CommonSourceRegistrationReponseParams0a86bd5cF7de4a5085d3Aa7003ecba89.md)

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

# **protection_source_by_id**
> Source protection_source_by_id(id)

Get a Protection Sources.

Get a Protection Source.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.source import Source
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the Protection Source.

# example passing only required values which don't have defaults set
try:
	# Get a Protection Sources.
	api_response = client.source.protection_source_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SourceApi->protection_source_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source. |

### Return type

[**Source**](Source.md)

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

# **refresh_protection_source_by_id**
> refresh_protection_source_by_id(id)

Refresh a Protection Source.

Refresh a Protection Source.

### Example

* Api Key Authentication (APIKeyHeader):
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


id = 1 # int | Specifies the id of the Protection Source.

# example passing only required values which don't have defaults set
try:
	# Refresh a Protection Source.
	client.source.refresh_protection_source_by_id(id)
except ApiException as e:
	print("Exception when calling SourceApi->refresh_protection_source_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source. |

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

# **register_protection_source**
> CommonSourceRegistrationReponseParams0a86bd5cF7de4a5085d3Aa7003ecba89 register_protection_source(body)

Register a Protection Source.

Register a Protection Source.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.common_source_registration_request_params55735f4993544f9e_a2ac_fca18c1c1a95 import CommonSourceRegistrationRequestParams55735f4993544f9eA2acFca18c1c1a95
from cohesity_sdk.cluster.model.common_source_registration_reponse_params0a86bd5c_f7de4a5085d3_aa7003ecba89 import CommonSourceRegistrationReponseParams0a86bd5cF7de4a5085d3Aa7003ecba89
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CommonSourceRegistrationRequestParams55735f4993544f9eA2acFca18c1c1a95(
        environment="kVMware",
        name="name_example",
        is_internal_encrypted=True,
        encryption_key="encryption_key_example",
        connection_id=1,
        connections=[
            ConnectionConfig(
                connection_id=1,
                entity_id=1,
                connector_group_id=1,
            ),
        ],
        connector_group_id=1,
    ) # CommonSourceRegistrationRequestParams55735f4993544f9eA2acFca18c1c1a95 | Specifies the parameters to register a Protection Source.

# example passing only required values which don't have defaults set
try:
	# Register a Protection Source.
	api_response = client.source.register_protection_source(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SourceApi->register_protection_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommonSourceRegistrationRequestParams55735f4993544f9eA2acFca18c1c1a95**](CommonSourceRegistrationRequestParams55735f4993544f9eA2acFca18c1c1a95.md)| Specifies the parameters to register a Protection Source. |

### Return type

[**CommonSourceRegistrationReponseParams0a86bd5cF7de4a5085d3Aa7003ecba89**](CommonSourceRegistrationReponseParams0a86bd5cF7de4a5085d3Aa7003ecba89.md)

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

# **test_connection_protection_source**
> SourceConnectionResponseParams test_connection_protection_source(body)

Test connection to a source.

Test connection to a source.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.source_connection_response_params import SourceConnectionResponseParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.common_source_connection_request_params208ba18711b94c2f_a7c12414ed0a71c0 import CommonSourceConnectionRequestParams208ba18711b94c2fA7c12414ed0a71c0
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CommonSourceConnectionRequestParams208ba18711b94c2fA7c12414ed0a71c0(
        environment="kCassandra",
        connection_id=1,
    ) # CommonSourceConnectionRequestParams208ba18711b94c2fA7c12414ed0a71c0 | Specifies the parameters to test connectivity with a source.

# example passing only required values which don't have defaults set
try:
	# Test connection to a source.
	api_response = client.source.test_connection_protection_source(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SourceApi->test_connection_protection_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommonSourceConnectionRequestParams208ba18711b94c2fA7c12414ed0a71c0**](CommonSourceConnectionRequestParams208ba18711b94c2fA7c12414ed0a71c0.md)| Specifies the parameters to test connectivity with a source. |

### Return type

[**SourceConnectionResponseParams**](SourceConnectionResponseParams.md)

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

# **update_protection_source_registration**
> CommonSourceRegistrationReponseParams0a86bd5cF7de4a5085d3Aa7003ecba89 update_protection_source_registration(id, body)

Update Protection Source registration.

Update Protection Source registration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.common_source_registration_request_params55735f4993544f9e_a2ac_fca18c1c1a95 import CommonSourceRegistrationRequestParams55735f4993544f9eA2acFca18c1c1a95
from cohesity_sdk.cluster.model.common_source_registration_reponse_params0a86bd5c_f7de4a5085d3_aa7003ecba89 import CommonSourceRegistrationReponseParams0a86bd5cF7de4a5085d3Aa7003ecba89
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the Protection Source registration.
body = CommonSourceRegistrationRequestParams55735f4993544f9eA2acFca18c1c1a95(
        environment="kVMware",
        name="name_example",
        is_internal_encrypted=True,
        encryption_key="encryption_key_example",
        connection_id=1,
        connections=[
            ConnectionConfig(
                connection_id=1,
                entity_id=1,
                connector_group_id=1,
            ),
        ],
        connector_group_id=1,
    ) # CommonSourceRegistrationRequestParams55735f4993544f9eA2acFca18c1c1a95 | Specifies the parameters to update the registration.

# example passing only required values which don't have defaults set
try:
	# Update Protection Source registration.
	api_response = client.source.update_protection_source_registration(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SourceApi->update_protection_source_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source registration. |
 **body** | [**CommonSourceRegistrationRequestParams55735f4993544f9eA2acFca18c1c1a95**](CommonSourceRegistrationRequestParams55735f4993544f9eA2acFca18c1c1a95.md)| Specifies the parameters to update the registration. |

### Return type

[**CommonSourceRegistrationReponseParams0a86bd5cF7de4a5085d3Aa7003ecba89**](CommonSourceRegistrationReponseParams0a86bd5cF7de4a5085d3Aa7003ecba89.md)

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

