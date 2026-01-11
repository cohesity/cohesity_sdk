# cohesity_sdk.cluster.SourceApi

All URIs are relative to *http://localhost/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_azure_applications**](SourceApi.md#create_azure_applications) | **POST** /data-protect/sources/microsoft365/azure-applications | Create Microsoft 365 Azure Applications for a given domain.
[**create_or_update_azure_applications**](SourceApi.md#create_or_update_azure_applications) | **PUT** /data-protect/sources/microsoft365/azure-applications | Create/Update Microsoft 365 Azure Applications for a given domain.
[**delete_application_servers_registration**](SourceApi.md#delete_application_servers_registration) | **DELETE** /data-protect/sources/application-servers/{id} | Delete an application server registration.
[**delete_azure_applications**](SourceApi.md#delete_azure_applications) | **DELETE** /data-protect/sources/microsoft365/azure-applications | Deletes Azure Applications
[**delete_m365_self_service_config**](SourceApi.md#delete_m365_self_service_config) | **DELETE** /data-protect/sources/microsoft365/self-service-config/{uuid} | Deletes the Self-Service configuration for a Microsoft365 source.
[**delete_protection_source_registration**](SourceApi.md#delete_protection_source_registration) | **DELETE** /data-protect/sources/registrations/{id} | Delete Protection Source Registration.
[**enable_mbs_billing_profile**](SourceApi.md#enable_mbs_billing_profile) | **POST** /data-protect/sources/microsoft365/backup-controllers/billing | Enables billing profile for the MBS service for the tenant.
[**generate_m365_device_access_token**](SourceApi.md#generate_m365_device_access_token) | **POST** /data-protect/sources/microsoft365/auth/token | Generate access token for Microsoft365 Device Authorization Grant flow.
[**generate_m365_device_code**](SourceApi.md#generate_m365_device_code) | **POST** /data-protect/sources/microsoft365/auth/device-code | Generate device code for Microsoft365 Device Authorization Grant flow.
[**get_m365_backup_controller**](SourceApi.md#get_m365_backup_controller) | **GET** /data-protect/sources/microsoft365/backup-controllers | Fetches the Microsoft 365 registered Backup Controller by the Cohesity App for the owner tenant
[**get_microsoft365_self_service_config**](SourceApi.md#get_microsoft365_self_service_config) | **GET** /data-protect/sources/microsoft365/self-service-config | Get the list of Microsoft365 Self-Service configurations
[**get_network_entities**](SourceApi.md#get_network_entities) | **GET** /data-protect/sources/{vCenterId}/resource-pools/{id}/entities | Get Network Entities within a Resource pool
[**get_protection_source_registration**](SourceApi.md#get_protection_source_registration) | **GET** /data-protect/sources/registrations/{id} | Get a Protection Source registration.
[**get_protection_sources**](SourceApi.md#get_protection_sources) | **GET** /data-protect/sources | Get a List of Protection Sources.
[**get_source_attribute_filters**](SourceApi.md#get_source_attribute_filters) | **GET** /data-protect/sources/filters | List attribute filters for a source.
[**get_source_registrations**](SourceApi.md#get_source_registrations) | **GET** /data-protect/sources/registrations | Get the list of Protection Source registrations.
[**get_vdc_details**](SourceApi.md#get_vdc_details) | **GET** /data-protect/sources/virtual-datacenter/{id} | Get VDC Details.
[**list_application_servers**](SourceApi.md#list_application_servers) | **GET** /data-protect/sources/application-servers | The Application Servers in a Protection Source tree.
[**patch_protection_source_registration**](SourceApi.md#patch_protection_source_registration) | **PATCH** /data-protect/sources/registrations/{id} | Perform Partial Update on Protection Source registration. Currently this API is supported only for Cassandra
[**protection_source_by_id**](SourceApi.md#protection_source_by_id) | **GET** /data-protect/sources/{id} | Get a Protection Sources.
[**refresh_protection_source_by_id**](SourceApi.md#refresh_protection_source_by_id) | **POST** /data-protect/sources/{id}/refresh | Refresh a Protection Source.
[**register_m365_backup_controller**](SourceApi.md#register_m365_backup_controller) | **POST** /data-protect/sources/microsoft365/backup-controllers | Registers the Cohesity App to be the Microsoft 365 Backup Controller
[**register_protection_source**](SourceApi.md#register_protection_source) | **POST** /data-protect/sources/registrations | Register a Protection Source.
[**test_connection_protection_source**](SourceApi.md#test_connection_protection_source) | **POST** /data-protect/sources/test-connection | Test connection to a source.
[**unregister_m365_backup_controller**](SourceApi.md#unregister_m365_backup_controller) | **DELETE** /data-protect/sources/microsoft365/backup-controllers/{id} | Unregisters the Cohesity App as the Microsoft 365 Backup Controller
[**update_application_servers_registration**](SourceApi.md#update_application_servers_registration) | **PUT** /data-protect/sources/application-servers/{id} | Registers or update owner entity with applications.
[**update_m365_backup_controller**](SourceApi.md#update_m365_backup_controller) | **PATCH** /data-protect/sources/microsoft365/backup-controllers/{id} | Updates the status of the registered M365 Backup Controller
[**update_m365_self_service_config**](SourceApi.md#update_m365_self_service_config) | **PUT** /data-protect/sources/microsoft365/self-service-config/{uuid} | Create or Update the Self-Service configuration for a Microsoft365 source.
[**update_protection_source_registration**](SourceApi.md#update_protection_source_registration) | **PUT** /data-protect/sources/registrations/{id} | Update Protection Source registration.


# **create_azure_applications**
> CreateAzureApplicationResponseParams create_azure_applications(body)

Create Microsoft 365 Azure Applications for a given domain.

**Privileges:** ```PROTECTION_MODIFY``` <br><br>Creates Microsoft 365 Azure Applications

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.create_azure_application_request_params import CreateAzureApplicationRequestParams
from cohesity_sdk.cluster.cohesity.model.create_azure_application_response_params import CreateAzureApplicationResponseParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    body = CreateAzureApplicationRequestParams(
        access_token="access_token_example",
        app_count=1,
        azure_tenant_id="azure_tenant_id_example",
        certificate_thumbprints=[
            "certificate_thumbprints_example",
        ],
        existing_microsoft365_app_credentials_list=[
            Office365AppCredentials(
                client_certificate=CertificateObjectWithMetadata(
                    certificate=CertificateObject(
                        data='YQ==',
                        format="P12",
                        password="password_example",
                    ),
                    display_name="display_name_example",
                    environments=[
                        "microsoft365",
                    ],
                    expiry_time_usecs=1,
                    generated_by="External",
                    issued_time_usecs=1,
                    issuer=CertificateNameProperties(
                        common_name="common_name_example",
                        organization="organization_example",
                        organization_unit="organization_unit_example",
                    ),
                    subject=CertificateNameProperties(
                        common_name="common_name_example",
                        organization="organization_example",
                        organization_unit="organization_unit_example",
                    ),
                    thumbprint="thumbprint_example",
                ),
                client_id="client_id_example",
                client_secret="client_secret_example",
            ),
        ],
        microsoft365_region="Default",
        o365_app_credentials_list_for_cert_update=[
            Office365AppCredentials(
                client_certificate=CertificateObjectWithMetadata(
                    certificate=CertificateObject(
                        data='YQ==',
                        format="P12",
                        password="password_example",
                    ),
                    display_name="display_name_example",
                    environments=[
                        "microsoft365",
                    ],
                    expiry_time_usecs=1,
                    generated_by="External",
                    issued_time_usecs=1,
                    issuer=CertificateNameProperties(
                        common_name="common_name_example",
                        organization="organization_example",
                        organization_unit="organization_unit_example",
                    ),
                    subject=CertificateNameProperties(
                        common_name="common_name_example",
                        organization="organization_example",
                        organization_unit="organization_unit_example",
                    ),
                    thumbprint="thumbprint_example",
                ),
                client_id="client_id_example",
                client_secret="client_secret_example",
            ),
        ],
        update_app_key_only=False,
        use_cases=[
            "kVirtualMachine",
        ],
        username="username_example",
    ) # CreateAzureApplicationRequestParams | Specifies the parameters to create Azure applications within a given Microsoft365 source.

    # example passing only required values which don't have defaults set
    try:
        # Create Microsoft 365 Azure Applications for a given domain.
        api_response = api_instance.create_azure_applications(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->create_azure_applications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAzureApplicationRequestParams**](CreateAzureApplicationRequestParams.md)| Specifies the parameters to create Azure applications within a given Microsoft365 source. |

### Return type

[**CreateAzureApplicationResponseParams**](CreateAzureApplicationResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_azure_applications**
> CreateAzureApplicationResponseParams create_or_update_azure_applications(body)

Create/Update Microsoft 365 Azure Applications for a given domain.

**Privileges:** ```PROTECTION_MODIFY``` <br><br>Creates/Updates Microsoft 365 Azure Applications

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.create_azure_application_request_params import CreateAzureApplicationRequestParams
from cohesity_sdk.cluster.cohesity.model.create_azure_application_response_params import CreateAzureApplicationResponseParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    body = CreateAzureApplicationRequestParams(
        access_token="access_token_example",
        app_count=1,
        azure_tenant_id="azure_tenant_id_example",
        certificate_thumbprints=[
            "certificate_thumbprints_example",
        ],
        existing_microsoft365_app_credentials_list=[
            Office365AppCredentials(
                client_certificate=CertificateObjectWithMetadata(
                    certificate=CertificateObject(
                        data='YQ==',
                        format="P12",
                        password="password_example",
                    ),
                    display_name="display_name_example",
                    environments=[
                        "microsoft365",
                    ],
                    expiry_time_usecs=1,
                    generated_by="External",
                    issued_time_usecs=1,
                    issuer=CertificateNameProperties(
                        common_name="common_name_example",
                        organization="organization_example",
                        organization_unit="organization_unit_example",
                    ),
                    subject=CertificateNameProperties(
                        common_name="common_name_example",
                        organization="organization_example",
                        organization_unit="organization_unit_example",
                    ),
                    thumbprint="thumbprint_example",
                ),
                client_id="client_id_example",
                client_secret="client_secret_example",
            ),
        ],
        microsoft365_region="Default",
        o365_app_credentials_list_for_cert_update=[
            Office365AppCredentials(
                client_certificate=CertificateObjectWithMetadata(
                    certificate=CertificateObject(
                        data='YQ==',
                        format="P12",
                        password="password_example",
                    ),
                    display_name="display_name_example",
                    environments=[
                        "microsoft365",
                    ],
                    expiry_time_usecs=1,
                    generated_by="External",
                    issued_time_usecs=1,
                    issuer=CertificateNameProperties(
                        common_name="common_name_example",
                        organization="organization_example",
                        organization_unit="organization_unit_example",
                    ),
                    subject=CertificateNameProperties(
                        common_name="common_name_example",
                        organization="organization_example",
                        organization_unit="organization_unit_example",
                    ),
                    thumbprint="thumbprint_example",
                ),
                client_id="client_id_example",
                client_secret="client_secret_example",
            ),
        ],
        update_app_key_only=False,
        use_cases=[
            "kVirtualMachine",
        ],
        username="username_example",
    ) # CreateAzureApplicationRequestParams | Specifies the parameters to create/update Azure applications within a given Microsoft365 source.

    # example passing only required values which don't have defaults set
    try:
        # Create/Update Microsoft 365 Azure Applications for a given domain.
        api_response = api_instance.create_or_update_azure_applications(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->create_or_update_azure_applications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAzureApplicationRequestParams**](CreateAzureApplicationRequestParams.md)| Specifies the parameters to create/update Azure applications within a given Microsoft365 source. |

### Return type

[**CreateAzureApplicationResponseParams**](CreateAzureApplicationResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_servers_registration**
> delete_application_servers_registration(id, body)

Delete an application server registration.

**Privileges:** ```PROTECTION_SOURCE_MODIFY``` <br><br>Delete an application server registration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.un_register_application_servers_params import UnRegisterApplicationServersParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    id = 1 # int | Specifies the id of the Application Server.
    body = UnRegisterApplicationServersParams(
        application_environments=[
            "kVMware",
        ],
    ) # UnRegisterApplicationServersParams | Specifies the request to unregister a an application server.

    # example passing only required values which don't have defaults set
    try:
        # Delete an application server registration.
        api_instance.delete_application_servers_registration(id, body)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->delete_application_servers_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Application Server. |
 **body** | [**UnRegisterApplicationServersParams**](UnRegisterApplicationServersParams.md)| Specifies the request to unregister a an application server. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_azure_applications**
> delete_azure_applications(body)

Deletes Azure Applications

**Privileges:** ```PROTECTION_MODIFY``` <br><br>Deletes Azure Applications

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.delete_azure_application_request_params import DeleteAzureApplicationRequestParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    body = DeleteAzureApplicationRequestParams(
        access_token="access_token_example",
        azure_applications_list=[
            Office365AppCredentials(
                client_certificate=CertificateObjectWithMetadata(
                    certificate=CertificateObject(
                        data='YQ==',
                        format="P12",
                        password="password_example",
                    ),
                    display_name="display_name_example",
                    environments=[
                        "microsoft365",
                    ],
                    expiry_time_usecs=1,
                    generated_by="External",
                    issued_time_usecs=1,
                    issuer=CertificateNameProperties(
                        common_name="common_name_example",
                        organization="organization_example",
                        organization_unit="organization_unit_example",
                    ),
                    subject=CertificateNameProperties(
                        common_name="common_name_example",
                        organization="organization_example",
                        organization_unit="organization_unit_example",
                    ),
                    thumbprint="thumbprint_example",
                ),
                client_id="client_id_example",
                client_secret="client_secret_example",
            ),
        ],
        azure_tenant_id="azure_tenant_id_example",
        skip_client_id_verification=True,
    ) # DeleteAzureApplicationRequestParams | Specifies the parameters to delete Azure applications

    # example passing only required values which don't have defaults set
    try:
        # Deletes Azure Applications
        api_instance.delete_azure_applications(body)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->delete_azure_applications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteAzureApplicationRequestParams**](DeleteAzureApplicationRequestParams.md)| Specifies the parameters to delete Azure applications |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_m365_self_service_config**
> delete_m365_self_service_config(uuid)

Deletes the Self-Service configuration for a Microsoft365 source.

**Privileges:** ```PROTECTION_MODIFY``` <br><br>Delete the configuration for Self-Service for a Microsoft365 source. This includes deletion of both Mailbox & OneDrive workload configuration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    uuid = "uuid_example" # str | Specifies the UUID of the Microsoft365 Source.

    # example passing only required values which don't have defaults set
    try:
        # Deletes the Self-Service configuration for a Microsoft365 source.
        api_instance.delete_m365_self_service_config(uuid)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->delete_m365_self_service_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Specifies the UUID of the Microsoft365 Source. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_protection_source_registration**
> delete_protection_source_registration(id)

Delete Protection Source Registration.

**Privileges:** ```PROTECTION_SOURCE_MODIFY``` <br><br>Delete Protection Source Registration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.source_un_register_request_params import SourceUnRegisterRequestParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    id = 1 # int | Specifies the ID of the Protection Source Registration.
    body = SourceUnRegisterRequestParams(
        azure_params=AzureSourceUnRegisterParams(
            graph_access_token="graph_access_token_example",
            management_access_token="management_access_token_example",
        ),
    ) # SourceUnRegisterRequestParams | Specifies the request to unregister a source. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Protection Source Registration.
        api_instance.delete_protection_source_registration(id)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->delete_protection_source_registration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Protection Source Registration.
        api_instance.delete_protection_source_registration(id, body=body)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->delete_protection_source_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the ID of the Protection Source Registration. |
 **body** | [**SourceUnRegisterRequestParams**](SourceUnRegisterRequestParams.md)| Specifies the request to unregister a source. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_mbs_billing_profile**
> M365BackupControllerBillingResponseParams enable_mbs_billing_profile(azure_token)

Enables billing profile for the MBS service for the tenant.

**Privileges:** ```PROTECTION_MODIFY``` <br><br>Enables the M365 Backup Storage(MBS) service for the tenant.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.m365_backup_controller_billing_response_params import M365BackupControllerBillingResponseParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    azure_token = "azureToken_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Enables billing profile for the MBS service for the tenant.
        api_response = api_instance.enable_mbs_billing_profile(azure_token)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->enable_mbs_billing_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_token** | **str**|  |

### Return type

[**M365BackupControllerBillingResponseParams**](M365BackupControllerBillingResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_m365_device_access_token**
> GenerateM365DeviceAccessTokenResponseParams generate_m365_device_access_token(body)

Generate access token for Microsoft365 Device Authorization Grant flow.

**Privileges:** ```PROTECTION_MODIFY``` <br><br>Generates the access token if the device code has been granted authorization as part of device login flow.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.generate_m365_device_access_token_response_params import GenerateM365DeviceAccessTokenResponseParams
from cohesity_sdk.cluster.cohesity.model.generate_m365_device_access_token_request_params import GenerateM365DeviceAccessTokenRequestParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    body = GenerateM365DeviceAccessTokenRequestParams(
        device_code="device_code_example",
        domain="domain_example",
    ) # GenerateM365DeviceAccessTokenRequestParams | Specifies the parameters to validate and generate access token for authorizing the client within Microsoft365.

    # example passing only required values which don't have defaults set
    try:
        # Generate access token for Microsoft365 Device Authorization Grant flow.
        api_response = api_instance.generate_m365_device_access_token(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->generate_m365_device_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateM365DeviceAccessTokenRequestParams**](GenerateM365DeviceAccessTokenRequestParams.md)| Specifies the parameters to validate and generate access token for authorizing the client within Microsoft365. |

### Return type

[**GenerateM365DeviceAccessTokenResponseParams**](GenerateM365DeviceAccessTokenResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```PROTECTION_MODIFY``` <br><br>Generates User and Device code for Microsoft365 Device Authorization Grant for a given domain.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.generate_m365_device_code_response_params import GenerateM365DeviceCodeResponseParams
from cohesity_sdk.cluster.cohesity.model.generate_m365_device_code_request_params import GenerateM365DeviceCodeRequestParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    body = GenerateM365DeviceCodeRequestParams(
        domain="domain_example",
    ) # GenerateM365DeviceCodeRequestParams | Specifies the parameters to generate the user and device code to initiate authentication with Microsoft365.

    # example passing only required values which don't have defaults set
    try:
        # Generate device code for Microsoft365 Device Authorization Grant flow.
        api_response = api_instance.generate_m365_device_code(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->generate_m365_device_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateM365DeviceCodeRequestParams**](GenerateM365DeviceCodeRequestParams.md)| Specifies the parameters to generate the user and device code to initiate authentication with Microsoft365. |

### Return type

[**GenerateM365DeviceCodeResponseParams**](GenerateM365DeviceCodeResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_m365_backup_controller**
> get_m365_backup_controller()

Fetches the Microsoft 365 registered Backup Controller by the Cohesity App for the owner tenant

**Privileges:** ```PROTECTION_VIEW``` <br><br>Fetches the registered Backup Controller by the Cohesity App for the tenant id within the JWT specified within the header.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    azure_token = "azureToken_example" # str | Specifies the JWT obtained through user with the scope as BackupRestore-Control.ReadWrite.All (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetches the Microsoft 365 registered Backup Controller by the Cohesity App for the owner tenant
        api_instance.get_m365_backup_controller(azure_token=azure_token)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->get_m365_backup_controller: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_token** | **str**| Specifies the JWT obtained through user with the scope as BackupRestore-Control.ReadWrite.All | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**404** | (empty) |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_microsoft365_self_service_config**
> GetM365SelfServiceConfigResponse get_microsoft365_self_service_config()

Get the list of Microsoft365 Self-Service configurations

```No Privileges Required``` <br><br>Get the list of Self-Service configurations for all Microsoft365 sources for the given tenant ID.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.get_m365_self_service_config_response import GetM365SelfServiceConfigResponse
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    domain = "domain_example" # str, none_type | Specifies the domain name for the Microsoft365 source. (optional)
    tenant_id = "tenantId_example" # str, none_type | Specifies the Cohesity Tenant ID for the source owner. (optional)
    workload_type = "kO365Exchange" # str, none_type | Specifies the workload type as filter for fetching Self-Service configuration types. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of Microsoft365 Self-Service configurations
        api_response = api_instance.get_microsoft365_self_service_config(domain=domain, tenant_id=tenant_id, workload_type=workload_type)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->get_microsoft365_self_service_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str, none_type**| Specifies the domain name for the Microsoft365 source. | [optional]
 **tenant_id** | **str, none_type**| Specifies the Cohesity Tenant ID for the source owner. | [optional]
 **workload_type** | **str, none_type**| Specifies the workload type as filter for fetching Self-Service configuration types. | [optional]

### Return type

[**GetM365SelfServiceConfigResponse**](GetM365SelfServiceConfigResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_entities**
> Sources get_network_entities(id, v_center_id, ancestor_entity_type)

Get Network Entities within a Resource pool

**Privileges:** ```PROTECTION_VIEW``` <br><br>List network entities for a resource pool.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.sources import Sources
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    id = 1 # int | Specifies the entity Id of the resource pool
    v_center_id = 1 # int | Specifies the entity Id of the vCenter
    ancestor_entity_type = "kDatacenter" # str | Specifies the ancestor entity type i.e. the node in the entity hierarchy which lies at a higher level than the resource pool entity id.

    # example passing only required values which don't have defaults set
    try:
        # Get Network Entities within a Resource pool
        api_response = api_instance.get_network_entities(id, v_center_id, ancestor_entity_type)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->get_network_entities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the entity Id of the resource pool |
 **v_center_id** | **int**| Specifies the entity Id of the vCenter |
 **ancestor_entity_type** | **str**| Specifies the ancestor entity type i.e. the node in the entity hierarchy which lies at a higher level than the resource pool entity id. |

### Return type

[**Sources**](Sources.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
> SourceRegistration get_protection_source_registration(id)

Get a Protection Source registration.

**Privileges:** ```PROTECTION_VIEW``` <br><br>Get a Protection Source registration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.source_registration import SourceRegistration
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    id = 1 # int | Specifies the id of the Protection Source registration.
    request_initiator_type = "UIUser" # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a Protection Source registration.
        api_response = api_instance.get_protection_source_registration(id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->get_protection_source_registration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a Protection Source registration.
        api_response = api_instance.get_protection_source_registration(id, request_initiator_type=request_initiator_type)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->get_protection_source_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source registration. |
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional]

### Return type

[**SourceRegistration**](SourceRegistration.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

```Unknown Privileges``` <br><br>Get a List of Protection Sources.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.sources import Sources
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    request_initiator_type = "UIUser" # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
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
        api_response = api_instance.get_protection_sources(request_initiator_type=request_initiator_type, tenant_ids=tenant_ids, include_tenants=include_tenants, include_source_credentials=include_source_credentials, encryption_key=encryption_key)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->get_protection_sources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which Sources are to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include Sources which belong belong to all tenants which the current user has permission to see. If false, then only Sources for the current user will be returned. | [optional]
 **include_source_credentials** | **bool**| If true, the encrypted crednetial for the registered sources will be included. Credential is first encrypted with internal key and then reencrypted with user supplied encryption key. | [optional]
 **encryption_key** | **str**| Specifies the key to be used to encrypt the source credential. If includeSourceCredentials is set to true this key must be specified. | [optional]

### Return type

[**Sources**](Sources.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```PROTECTION_VIEW``` <br><br>Get a List of attribute filters for leaf entities within a a source

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.source_attribute_filters_response_params import SourceAttributeFiltersResponseParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    source_uuid = "sourceUuid_example" # str | Specifies the source UUID of the parent entity.
    environment = "kVMware" # str, none_type | Specifies the environment type of the Protection Source. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List attribute filters for a source.
        api_response = api_instance.get_source_attribute_filters(source_uuid)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->get_source_attribute_filters: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List attribute filters for a source.
        api_response = api_instance.get_source_attribute_filters(source_uuid, environment=environment)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```PROTECTION_VIEW``` <br><br>Get the list of Protection Source registrations.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.source_registrations import SourceRegistrations
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
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
    include_external_metadata = True # bool | If true, the external entity metadata like maintenance mode config for the registered sources will be included. (optional)
    ignore_tenant_migration_in_progress_check = True # bool | If true, tenant migration check will be ignored (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of Protection Source registrations.
        api_response = api_instance.get_source_registrations(ids=ids, tenant_ids=tenant_ids, include_tenants=include_tenants, include_source_credentials=include_source_credentials, encryption_key=encryption_key, use_cached_data=use_cached_data, include_external_metadata=include_external_metadata, ignore_tenant_migration_in_progress_check=ignore_tenant_migration_in_progress_check)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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
 **include_external_metadata** | **bool**| If true, the external entity metadata like maintenance mode config for the registered sources will be included. | [optional]
 **ignore_tenant_migration_in_progress_check** | **bool**| If true, tenant migration check will be ignored | [optional]

### Return type

[**SourceRegistrations**](SourceRegistrations.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```PROTECTION_VIEW``` <br><br>Get the details such as catelogs, Org networks associated with a VMware virtual datacenter (VDC).

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.vdc_object import VdcObject
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    id = 1 # int | Specifies the ID of the VMware virtual datacenter.

    # example passing only required values which don't have defaults set
    try:
        # Get VDC Details.
        api_response = api_instance.get_vdc_details(id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->get_vdc_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the ID of the VMware virtual datacenter. |

### Return type

[**VdcObject**](VdcObject.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_servers**
> ListAppServersResponse list_application_servers(root_node_id, application_environment)

The Application Servers in a Protection Source tree.

**Privileges:** ```PROTECTION_MODIFY``` <br><br>Returns the registered Application Servers and their Object subtrees. Given the root node id of a Protection Source tree, returns the list of Application Servers registered under that tree based on the filters.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.list_app_servers_response import ListAppServersResponse
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    root_node_id = 1 # int | Specifies the Protection Source Id of the root node of a Protection Sources tree. A root node represents a registered Source on the Cohesity Cluster, such as a vCenter Server.
    application_environment = "kSQL" # str | Specifies the types of applications such as 'kSQL', 'kExchange', 'kAD' etc. running on the Protection Source.
    environment = "kVMware" # str | Specifies the environment of the Protection Source tree. (optional)
    node_id = 1 # int | Specifies the Protection Source Id of the entity in the Protection Source tree hosting the applications. (optional)
    next_entity_id = 1 # int, none_type | Specifies the entity id for the Node at any level within the Source entity hierarchy whose children are to be paginated. (optional)
    page_size = 1 # int, none_type | Specifies the maximum number of entities to be returned within the page. (optional)
    after_cursor_entity_id = 1 # int, none_type | Specifies the entity id starting from which the items are to be returned (optional)
    before_cursor_entity_id = 1 # int, none_type | Specifies the entity id upto which the items are to be returned (optional)

    # example passing only required values which don't have defaults set
    try:
        # The Application Servers in a Protection Source tree.
        api_response = api_instance.list_application_servers(root_node_id, application_environment)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->list_application_servers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # The Application Servers in a Protection Source tree.
        api_response = api_instance.list_application_servers(root_node_id, application_environment, environment=environment, node_id=node_id, next_entity_id=next_entity_id, page_size=page_size, after_cursor_entity_id=after_cursor_entity_id, before_cursor_entity_id=before_cursor_entity_id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->list_application_servers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root_node_id** | **int**| Specifies the Protection Source Id of the root node of a Protection Sources tree. A root node represents a registered Source on the Cohesity Cluster, such as a vCenter Server. |
 **application_environment** | **str**| Specifies the types of applications such as &#39;kSQL&#39;, &#39;kExchange&#39;, &#39;kAD&#39; etc. running on the Protection Source. |
 **environment** | **str**| Specifies the environment of the Protection Source tree. | [optional]
 **node_id** | **int**| Specifies the Protection Source Id of the entity in the Protection Source tree hosting the applications. | [optional]
 **next_entity_id** | **int, none_type**| Specifies the entity id for the Node at any level within the Source entity hierarchy whose children are to be paginated. | [optional]
 **page_size** | **int, none_type**| Specifies the maximum number of entities to be returned within the page. | [optional]
 **after_cursor_entity_id** | **int, none_type**| Specifies the entity id starting from which the items are to be returned | [optional]
 **before_cursor_entity_id** | **int, none_type**| Specifies the entity id upto which the items are to be returned | [optional]

### Return type

[**ListAppServersResponse**](ListAppServersResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
> SourceRegistration patch_protection_source_registration(id, body)

Perform Partial Update on Protection Source registration. Currently this API is supported only for Cassandra

**Privileges:** ```PROTECTION_SOURCE_MODIFY``` <br><br>Patches a Protection Source.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.source_registration_patch_request_params import SourceRegistrationPatchRequestParams
from cohesity_sdk.cluster.cohesity.model.source_registration import SourceRegistration
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    id = 1 # int | Specifies the id of the Protection Source registration.
    body = SourceRegistrationPatchRequestParams(
        cassandra_params=CassandraSourceRegistrationPatchParams(
            cassandra_credentials=CassandraSourceRegistrationParamsAllOfCassandraCredentials(
                password="password_example",
                username="username_example",
            ),
            commit_log_backup_location="commit_log_backup_location_example",
            config_directory="config_directory_example",
            data_center_names=[
                "data_center_names_example",
            ],
            dse_configuration_directory="dse_configuration_directory_example",
            dse_solr_info=DSESolrInfo(
                solr_nodes=[
                    "solr_nodes_example",
                ],
                solr_port=1,
            ),
            is_dse_authenticator=True,
            is_dse_tiered_storage=True,
            jmx_credentials=CassandraSourceRegistrationParamsAllOfJmxCredentials(
                password="password_example",
                username="username_example",
            ),
            kerberos_principal="kerberos_principal_example",
            seed_node="seed_node_example",
            ssh_password_credentials=SshPasswordCredentials(
                password="password_example",
                username="username_example",
            ),
            ssh_private_key_credentials=SshPrivateKeyCredentials(
                passphrase="passphrase_example",
                private_key="private_key_example",
                user_id="user_id_example",
            ),
        ),
        environment="kVMware",
    ) # SourceRegistrationPatchRequestParams | Specifies the parameters to partially update the registration.

    # example passing only required values which don't have defaults set
    try:
        # Perform Partial Update on Protection Source registration. Currently this API is supported only for Cassandra
        api_response = api_instance.patch_protection_source_registration(id, body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->patch_protection_source_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source registration. |
 **body** | [**SourceRegistrationPatchRequestParams**](SourceRegistrationPatchRequestParams.md)| Specifies the parameters to partially update the registration. |

### Return type

[**SourceRegistration**](SourceRegistration.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

```Unknown Privileges``` <br><br>Get a Protection Source.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.source import Source
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    id = 1 # int | Specifies the id of the Protection Source.

    # example passing only required values which don't have defaults set
    try:
        # Get a Protection Sources.
        api_response = api_instance.protection_source_by_id(id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->protection_source_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source. |

### Return type

[**Source**](Source.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```PROTECTION_VIEW``` <br><br>Refresh a Protection Source.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    id = 1 # int | Specifies the id of the Protection Source.

    # example passing only required values which don't have defaults set
    try:
        # Refresh a Protection Source.
        api_instance.refresh_protection_source_by_id(id)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->refresh_protection_source_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_m365_backup_controller**
> GetM365BackupControllerResponseParams register_m365_backup_controller(azure_token)

Registers the Cohesity App to be the Microsoft 365 Backup Controller

**Privileges:** ```PROTECTION_MODIFY``` <br><br>Registers the Cohesity App to be the Microsoft365 Backup Controller

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.get_m365_backup_controller_response_params import GetM365BackupControllerResponseParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    azure_token = "azureToken_example" # str | Specifies the JWT obtained through user with the scope for BackupRestore-Control.ReadWrite.All

    # example passing only required values which don't have defaults set
    try:
        # Registers the Cohesity App to be the Microsoft 365 Backup Controller
        api_response = api_instance.register_m365_backup_controller(azure_token)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->register_m365_backup_controller: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_token** | **str**| Specifies the JWT obtained through user with the scope for BackupRestore-Control.ReadWrite.All |

### Return type

[**GetM365BackupControllerResponseParams**](GetM365BackupControllerResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_protection_source**
> SourceRegistration register_protection_source(body)

Register a Protection Source.

**Privileges:** ```PROTECTION_SOURCE_MODIFY``` <br><br>Register a Protection Source.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.source_registration import SourceRegistration
from cohesity_sdk.cluster.cohesity.model.source_registration_request_params import SourceRegistrationRequestParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    body = SourceRegistrationRequestParams() # SourceRegistrationRequestParams | Specifies the parameters to register a Protection Source.

    # example passing only required values which don't have defaults set
    try:
        # Register a Protection Source.
        api_response = api_instance.register_protection_source(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->register_protection_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourceRegistrationRequestParams**](SourceRegistrationRequestParams.md)| Specifies the parameters to register a Protection Source. |

### Return type

[**SourceRegistration**](SourceRegistration.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```PROTECTION_VIEW``` <br><br>Test connection to a source.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.source_connection_request_params import SourceConnectionRequestParams
from cohesity_sdk.cluster.cohesity.model.source_connection_response_params import SourceConnectionResponseParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    body = SourceConnectionRequestParams() # SourceConnectionRequestParams | Specifies the parameters to test connectivity with a source.

    # example passing only required values which don't have defaults set
    try:
        # Test connection to a source.
        api_response = api_instance.test_connection_protection_source(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->test_connection_protection_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourceConnectionRequestParams**](SourceConnectionRequestParams.md)| Specifies the parameters to test connectivity with a source. |

### Return type

[**SourceConnectionResponseParams**](SourceConnectionResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_m365_backup_controller**
> unregister_m365_backup_controller(id)

Unregisters the Cohesity App as the Microsoft 365 Backup Controller

**Privileges:** ```PROTECTION_MODIFY``` <br><br>Unregisters the Cohesity App as the Microsoft 365 Backup Controller

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    id = "id_example" # str, none_type | Specifies the Service App ID for the registered M365 Backup Controller when Cohesity App is the active Controller.
    azure_token = "azureToken_example" # str | Specifies the JWT obtained through user with the scope as BackupRestore-Control.ReadWrite.All (optional)

    # example passing only required values which don't have defaults set
    try:
        # Unregisters the Cohesity App as the Microsoft 365 Backup Controller
        api_instance.unregister_m365_backup_controller(id)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->unregister_m365_backup_controller: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unregisters the Cohesity App as the Microsoft 365 Backup Controller
        api_instance.unregister_m365_backup_controller(id, azure_token=azure_token)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->unregister_m365_backup_controller: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str, none_type**| Specifies the Service App ID for the registered M365 Backup Controller when Cohesity App is the active Controller. |
 **azure_token** | **str**| Specifies the JWT obtained through user with the scope as BackupRestore-Control.ReadWrite.All | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_servers_registration**
> CommonApplicationServersRegistrationParams update_application_servers_registration(id, body)

Registers or update owner entity with applications.

**Privileges:** ```PROTECTION_SOURCE_MODIFY``` <br><br>Register or update applications on an owner entity

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.application_servers_registration_request_params import ApplicationServersRegistrationRequestParams
from cohesity_sdk.cluster.cohesity.model.common_application_servers_registration_params import CommonApplicationServersRegistrationParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    id = 1 # int | Specifies the id of the source entity for application registration.
    body = ApplicationServersRegistrationRequestParams() # ApplicationServersRegistrationRequestParams | Specifies the parameters to register an application entity.

    # example passing only required values which don't have defaults set
    try:
        # Registers or update owner entity with applications.
        api_response = api_instance.update_application_servers_registration(id, body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->update_application_servers_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the source entity for application registration. |
 **body** | [**ApplicationServersRegistrationRequestParams**](ApplicationServersRegistrationRequestParams.md)| Specifies the parameters to register an application entity. |

### Return type

[**CommonApplicationServersRegistrationParams**](CommonApplicationServersRegistrationParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_m365_backup_controller**
> GetM365BackupControllerResponseParams update_m365_backup_controller(azure_token, id)

Updates the status of the registered M365 Backup Controller

**Privileges:** ```PROTECTION_MODIFY``` <br><br>Updates the Backup Controller status of the registered M365 Backup Controller

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.get_m365_backup_controller_response_params import GetM365BackupControllerResponseParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    azure_token = "azureToken_example" # str | Specifies the JWT obtained through user with the scope as BackupRestore-Control.ReadWrite.All
    id = "id_example" # str, none_type | Specifies the Service App ID for the registered M365 Backup Controller when Cohesity App is the active Controller.
    state = "Inactive" # str, none_type | Specifies the state of the Backup Controller. The state parameter can only be either set to Active/Inactive within the request. The other states like PendingInactive & PendingActive are not applicable. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates the status of the registered M365 Backup Controller
        api_response = api_instance.update_m365_backup_controller(azure_token, id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->update_m365_backup_controller: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates the status of the registered M365 Backup Controller
        api_response = api_instance.update_m365_backup_controller(azure_token, id, state=state)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->update_m365_backup_controller: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_token** | **str**| Specifies the JWT obtained through user with the scope as BackupRestore-Control.ReadWrite.All |
 **id** | **str, none_type**| Specifies the Service App ID for the registered M365 Backup Controller when Cohesity App is the active Controller. |
 **state** | **str, none_type**| Specifies the state of the Backup Controller. The state parameter can only be either set to Active/Inactive within the request. The other states like PendingInactive &amp; PendingActive are not applicable. | [optional]

### Return type

[**GetM365BackupControllerResponseParams**](GetM365BackupControllerResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_m365_self_service_config**
> CreateM365SelfServiceConfigRequestParams update_m365_self_service_config(uuid, body)

Create or Update the Self-Service configuration for a Microsoft365 source.

**Privileges:** ```PROTECTION_MODIFY``` <br><br>Create or Update the configuration for enabling Self-Service for a Microsoft365 source through Security Groups. The configuration can be done for Mailbox & OneDrive workload only.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.create_m365_self_service_config_request_params import CreateM365SelfServiceConfigRequestParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    uuid = "uuid_example" # str | Specifies the UUID of the Microsoft365 Source.
    body = CreateM365SelfServiceConfigRequestParams(
        domain="domain_example",
        mailbox_params=M365SelfServiceWorkloadParams(
            allowed_security_groups=[
                M365SelfServiceSecurityGroupInfo(
                    enable_download=True,
                    global_id="global_id_example",
                    name="name_example",
                ),
            ],
        ),
        oidc_config=OIDCStandardConfiguration(
            client_id="client_id_example",
            issuer="issuer_example",
        ),
        one_drive_params=M365SelfServiceWorkloadParams(
            allowed_security_groups=[
                M365SelfServiceSecurityGroupInfo(
                    enable_download=True,
                    global_id="global_id_example",
                    name="name_example",
                ),
            ],
        ),
        preferred_authentication_mode="AzureAD",
        tenant_id="tenant_id_example",
        uuid="uuid_example",
    ) # CreateM365SelfServiceConfigRequestParams | Specifies the parameters to enable Self-Service for a Microsoft365 source. This configuration will apply to all regions incase the same source is registered across regions.

    # example passing only required values which don't have defaults set
    try:
        # Create or Update the Self-Service configuration for a Microsoft365 source.
        api_response = api_instance.update_m365_self_service_config(uuid, body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->update_m365_self_service_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Specifies the UUID of the Microsoft365 Source. |
 **body** | [**CreateM365SelfServiceConfigRequestParams**](CreateM365SelfServiceConfigRequestParams.md)| Specifies the parameters to enable Self-Service for a Microsoft365 source. This configuration will apply to all regions incase the same source is registered across regions. |

### Return type

[**CreateM365SelfServiceConfigRequestParams**](CreateM365SelfServiceConfigRequestParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_protection_source_registration**
> SourceRegistration update_protection_source_registration(id, body)

Update Protection Source registration.

**Privileges:** ```PROTECTION_SOURCE_MODIFY``` <br><br>Update Protection Source registration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import source
from cohesity_sdk.cluster.cohesity.model.source_registration_update_request_params import SourceRegistrationUpdateRequestParams
from cohesity_sdk.cluster.cohesity.model.source_registration import SourceRegistration
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source.SourceApi(api_client)
    id = 1 # int | Specifies the id of the Protection Source registration.
    body = SourceRegistrationUpdateRequestParams() # SourceRegistrationUpdateRequestParams | Specifies the parameters to update the registration.

    # example passing only required values which don't have defaults set
    try:
        # Update Protection Source registration.
        api_response = api_instance.update_protection_source_registration(id, body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SourceApi->update_protection_source_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source registration. |
 **body** | [**SourceRegistrationUpdateRequestParams**](SourceRegistrationUpdateRequestParams.md)| Specifies the parameters to update the registration. |

### Return type

[**SourceRegistration**](SourceRegistration.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

