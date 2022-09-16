# cohesity_sdk.ProtectionSourcesApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_protection_source_registration**](ProtectionSourcesApi.md#delete_protection_source_registration) | **DELETE** /data-protect/sources/registrations/{id} | Delete Protection Source Registration.
[**get_protection_source_registration**](ProtectionSourcesApi.md#get_protection_source_registration) | **GET** /data-protect/sources/registrations/{id} | Get a Protection Source registration.
[**get_protection_sources**](ProtectionSourcesApi.md#get_protection_sources) | **GET** /data-protect/sources | Get a List of Protection Sources.
[**get_source_attribute_filters**](ProtectionSourcesApi.md#get_source_attribute_filters) | **GET** /data-protect/sources/filters | List attribute filters for a source.
[**get_source_registrations**](ProtectionSourcesApi.md#get_source_registrations) | **GET** /data-protect/sources/registrations | Get the list of Protection Source registrations.
[**get_vdc_details**](ProtectionSourcesApi.md#get_vdc_details) | **GET** /data-protect/sources/virtual-datacenter/{id} | Get VDC Details.
[**protection_source_by_id**](ProtectionSourcesApi.md#protection_source_by_id) | **GET** /data-protect/sources/{id} | Get a Protection Sources.
[**refresh_protection_source_by_id**](ProtectionSourcesApi.md#refresh_protection_source_by_id) | **POST** /data-protect/sources/{id}/refresh | Refresh a Protection Source.
[**register_protection_source**](ProtectionSourcesApi.md#register_protection_source) | **POST** /data-protect/sources/registrations | Register a Protection Source.
[**test_connection_protection_source**](ProtectionSourcesApi.md#test_connection_protection_source) | **POST** /data-protect/sources/test-connection | Test connection to a source.
[**update_protection_source_registration**](ProtectionSourcesApi.md#update_protection_source_registration) | **PUT** /data-protect/sources/registrations/{id} | Update Protection Source registration.


# **delete_protection_source_registration**
> delete_protection_source_registration(id)

Delete Protection Source Registration.

Delete Protection Source Registration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the ID of the Protection Source Registration.

# example passing only required values which don't have defaults set
try:
	# Delete Protection Source Registration.
	client.protection_sources.delete_protection_source_registration(id)
except ApiException as e:
	print("Exception when calling ProtectionSourcesApi->delete_protection_source_registration: %s\n" % e)
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

# **get_protection_source_registration**
> CommonSourceRegistrationReponseParamsbb51eef19bdd4e3fB5257fcc70fe0a08 get_protection_source_registration(id)

Get a Protection Source registration.

Get a Protection Source registration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.common_source_registration_reponse_paramsbb51eef19bdd4e3f_b5257fcc70fe0a08 import CommonSourceRegistrationReponseParamsbb51eef19bdd4e3fB5257fcc70fe0a08
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the Protection Source registration.

# example passing only required values which don't have defaults set
try:
	# Get a Protection Source registration.
	api_response = client.protection_sources.get_protection_source_registration(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionSourcesApi->get_protection_source_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source registration. |

### Return type

[**CommonSourceRegistrationReponseParamsbb51eef19bdd4e3fB5257fcc70fe0a08**](CommonSourceRegistrationReponseParamsbb51eef19bdd4e3fB5257fcc70fe0a08.md)

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
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.sources import Sources
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
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
	api_response = client.[class Tag {
    name: ProtectionSources
    description: null
    externalDocs: null
}].get_protection_sources(tenant_ids=tenant_ids, include_tenants=include_tenants, include_source_credentials=include_source_credentials, encryption_key=encryption_key)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionSourcesApi->get_protection_sources: %s\n" % e)
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
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.source_attribute_filters_response_params import SourceAttributeFiltersResponseParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
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
	api_response = client.protection_sources.get_source_attribute_filters(source_uuid)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionSourcesApi->get_source_attribute_filters: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List attribute filters for a source.
	api_response = client.[class Tag {
    name: ProtectionSources
    description: null
    externalDocs: null
}].get_source_attribute_filters(source_uuid, environment=environment)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionSourcesApi->get_source_attribute_filters: %s\n" % e)
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
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.source_registrations import SourceRegistrations
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
        1,
    ] # [int] | Ids specifies the list of source registration ids to return. If left empty, every source registration will be returned by default. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
include_tenants = True # bool | If true, the response will include Registrations which were created by all tenants which the current user has permission to see. If false, then only Registrations created by the current user will be returned. (optional)
include_source_credentials = True # bool | If true, the encrypted crednetial for the registered sources will be included. Credential is first encrypted with internal key and then reencrypted with user supplied encryption key. (optional)
encryption_key = "encryptionKey_example" # str | Specifies the key to be used to encrypt the source credential. If includeSourceCredentials is set to true this key must be specified. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of Protection Source registrations.
	api_response = client.[class Tag {
    name: ProtectionSources
    description: null
    externalDocs: null
}].get_source_registrations(ids=ids, tenant_ids=tenant_ids, include_tenants=include_tenants, include_source_credentials=include_source_credentials, encryption_key=encryption_key)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionSourcesApi->get_source_registrations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**| Ids specifies the list of source registration ids to return. If left empty, every source registration will be returned by default. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which objects are to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include Registrations which were created by all tenants which the current user has permission to see. If false, then only Registrations created by the current user will be returned. | [optional]
 **include_source_credentials** | **bool**| If true, the encrypted crednetial for the registered sources will be included. Credential is first encrypted with internal key and then reencrypted with user supplied encryption key. | [optional]
 **encryption_key** | **str**| Specifies the key to be used to encrypt the source credential. If includeSourceCredentials is set to true this key must be specified. | [optional]

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
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.vdc_object import VdcObject
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the ID of the VMware virtual datacenter.

# example passing only required values which don't have defaults set
try:
	# Get VDC Details.
	api_response = client.protection_sources.get_vdc_details(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionSourcesApi->get_vdc_details: %s\n" % e)
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

# **protection_source_by_id**
> Source protection_source_by_id(id)

Get a Protection Sources.

Get a Protection Source.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.source import Source
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the Protection Source.

# example passing only required values which don't have defaults set
try:
	# Get a Protection Sources.
	api_response = client.protection_sources.protection_source_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionSourcesApi->protection_source_by_id: %s\n" % e)
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
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the Protection Source.

# example passing only required values which don't have defaults set
try:
	# Refresh a Protection Source.
	client.protection_sources.refresh_protection_source_by_id(id)
except ApiException as e:
	print("Exception when calling ProtectionSourcesApi->refresh_protection_source_by_id: %s\n" % e)
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
> CommonSourceRegistrationReponseParamsbb51eef19bdd4e3fB5257fcc70fe0a08 register_protection_source(body)

Register a Protection Source.

Register a Protection Source.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.common_source_registration_reponse_paramsbb51eef19bdd4e3f_b5257fcc70fe0a08 import CommonSourceRegistrationReponseParamsbb51eef19bdd4e3fB5257fcc70fe0a08
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.common_source_registration_request_paramsc0a85d8a0f7842869dff_b9a0cd9c1220 import CommonSourceRegistrationRequestParamsc0a85d8a0f7842869dffB9a0cd9c1220
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CommonSourceRegistrationRequestParamsc0a85d8a0f7842869dffB9a0cd9c1220(
        environment="kVMware",
        name="name_example",
        is_internal_encrypted=True,
        encryption_key="encryption_key_example",
        connection_id=1,
    ) # CommonSourceRegistrationRequestParamsc0a85d8a0f7842869dffB9a0cd9c1220 | Specifies the parameters to register a Protection Source.

# example passing only required values which don't have defaults set
try:
	# Register a Protection Source.
	api_response = client.protection_sources.register_protection_source(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionSourcesApi->register_protection_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommonSourceRegistrationRequestParamsc0a85d8a0f7842869dffB9a0cd9c1220**](CommonSourceRegistrationRequestParamsc0a85d8a0f7842869dffB9a0cd9c1220.md)| Specifies the parameters to register a Protection Source. |

### Return type

[**CommonSourceRegistrationReponseParamsbb51eef19bdd4e3fB5257fcc70fe0a08**](CommonSourceRegistrationReponseParamsbb51eef19bdd4e3fB5257fcc70fe0a08.md)

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
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.source_connection_response_params import SourceConnectionResponseParams
from cohesity_sdk.cluster.model.source_connection_request_params import SourceConnectionRequestParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = SourceConnectionRequestParams(
        environment="kCassandra",
        cassandra_connection_params=CassandraConnectionParams(
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
        ),
        hive_connection_params=HadoopConnectionParams(
            host="host_example",
            configuration_directory="configuration_directory_example",
            ssh_password_credentials=HadoopConnectionParamsSshPasswordCredentials(
                password="password_example",
                username="username_example",
            ),
            ssh_private_key_credentials=HadoopConnectionParamsSshPrivateKeyCredentials(
                passphrase="passphrase_example",
                private_key="private_key_example",
                user_id="user_id_example",
            ),
        ),
        hbase_connection_params=HadoopConnectionParams(
            host="host_example",
            configuration_directory="configuration_directory_example",
            ssh_password_credentials=HadoopConnectionParamsSshPasswordCredentials(
                password="password_example",
                username="username_example",
            ),
            ssh_private_key_credentials=HadoopConnectionParamsSshPrivateKeyCredentials(
                passphrase="passphrase_example",
                private_key="private_key_example",
                user_id="user_id_example",
            ),
        ),
        hdfs_connection_params=HadoopConnectionParams(
            host="host_example",
            configuration_directory="configuration_directory_example",
            ssh_password_credentials=HadoopConnectionParamsSshPasswordCredentials(
                password="password_example",
                username="username_example",
            ),
            ssh_private_key_credentials=HadoopConnectionParamsSshPrivateKeyCredentials(
                passphrase="passphrase_example",
                private_key="private_key_example",
                user_id="user_id_example",
            ),
        ),
        mssql_connection_params=MssqlConnectionParams(),
        vmware_connection_params=VmwareConnectionParams(
            type="kVCenter",
            vcd_params=VcdConnectionParams(),
        ),
    ) # SourceConnectionRequestParams | Specifies the parameters to test connectivity with a source.

# example passing only required values which don't have defaults set
try:
	# Test connection to a source.
	api_response = client.protection_sources.test_connection_protection_source(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionSourcesApi->test_connection_protection_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourceConnectionRequestParams**](SourceConnectionRequestParams.md)| Specifies the parameters to test connectivity with a source. |

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
> CommonSourceRegistrationReponseParamsbb51eef19bdd4e3fB5257fcc70fe0a08 update_protection_source_registration(id, body)

Update Protection Source registration.

Update Protection Source registration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.common_source_registration_reponse_paramsbb51eef19bdd4e3f_b5257fcc70fe0a08 import CommonSourceRegistrationReponseParamsbb51eef19bdd4e3fB5257fcc70fe0a08
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.common_source_registration_request_paramsc0a85d8a0f7842869dff_b9a0cd9c1220 import CommonSourceRegistrationRequestParamsc0a85d8a0f7842869dffB9a0cd9c1220
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the Protection Source registration.
body = CommonSourceRegistrationRequestParamsc0a85d8a0f7842869dffB9a0cd9c1220(
        environment="kVMware",
        name="name_example",
        is_internal_encrypted=True,
        encryption_key="encryption_key_example",
        connection_id=1,
    ) # CommonSourceRegistrationRequestParamsc0a85d8a0f7842869dffB9a0cd9c1220 | Specifies the parameters to update the registration.

# example passing only required values which don't have defaults set
try:
	# Update Protection Source registration.
	api_response = client.protection_sources.update_protection_source_registration(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectionSourcesApi->update_protection_source_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source registration. |
 **body** | [**CommonSourceRegistrationRequestParamsc0a85d8a0f7842869dffB9a0cd9c1220**](CommonSourceRegistrationRequestParamsc0a85d8a0f7842869dffB9a0cd9c1220.md)| Specifies the parameters to update the registration. |

### Return type

[**CommonSourceRegistrationReponseParamsbb51eef19bdd4e3fB5257fcc70fe0a08**](CommonSourceRegistrationReponseParamsbb51eef19bdd4e3fB5257fcc70fe0a08.md)

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

