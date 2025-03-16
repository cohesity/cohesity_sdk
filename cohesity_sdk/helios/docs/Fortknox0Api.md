# cohesity_sdk.helios.FortknoxApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fort_knox_kms_key**](FortknoxApi.md#add_fort_knox_kms_key) | **POST** /mcm/fortknox/kms-keys | Add KMS key config for Fortknox.
[**add_fortknox_vaults**](FortknoxApi.md#add_fortknox_vaults) | **POST** /mcm/fortknox/vaults | Add Cohesity Fortknox vaults in a given list of regions for the given account.
[**get_fortknox_vaults**](FortknoxApi.md#get_fortknox_vaults) | **GET** /mcm/fortknox/vaults | Get Fortknox vaults.
[**get_vault_transfer_time_config**](FortknoxApi.md#get_vault_transfer_time_config) | **GET** /mcm/fortknox/vaults/transfer-time-config | Get transfer time configurations.
[**pair_fortknox_vaults_clusters**](FortknoxApi.md#pair_fortknox_vaults_clusters) | **POST** /mcm/fortknox/pairing | An endpoint to pair clusters with fortknox vaults.
[**perform_vault_actions**](FortknoxApi.md#perform_vault_actions) | **POST** /mcm/fortknox/vaults/{globalVaultId}/actions | Perform actions on a given FortKnox vault.
[**update_vault_transfer_time_config**](FortknoxApi.md#update_vault_transfer_time_config) | **PUT** /mcm/fortknox/vaults/{globalVaultId}/transfer-time-config | Update transfer time configuration.


# **add_fort_knox_kms_key**
> FortknoxKmsKeyInfo add_fort_knox_kms_key(body, region_id=region_id)

Add KMS key config for Fortknox.

Add KMS key config for Fortknox.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.add_fortknox_kms_key_req import AddFortknoxKmsKeyReq
from cohesity_sdk.helios.models.fortknox_kms_key_info import FortknoxKmsKeyInfo
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.FortknoxApi(api_client)
    body = cohesity_sdk.helios.AddFortknoxKmsKeyReq() # AddFortknoxKmsKeyReq | Specifies the parameters to add KMS key for FortKnox.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Add KMS key config for Fortknox.
        api_response = api_instance.add_fort_knox_kms_key(body, region_id=region_id)
        print("The response of FortknoxApi->add_fort_knox_kms_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FortknoxApi->add_fort_knox_kms_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddFortknoxKmsKeyReq**](AddFortknoxKmsKeyReq.md)| Specifies the parameters to add KMS key for FortKnox. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**FortknoxKmsKeyInfo**](FortknoxKmsKeyInfo.md)

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

# **add_fortknox_vaults**
> AddFortknoxVaultsResp add_fortknox_vaults(body, region_id=region_id)

Add Cohesity Fortknox vaults in a given list of regions for the given account.

Add Cohesity Fortknox vaults in a given set of regions for the helios account

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.add_fortknox_vaults_req import AddFortknoxVaultsReq
from cohesity_sdk.helios.models.add_fortknox_vaults_resp import AddFortknoxVaultsResp
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.FortknoxApi(api_client)
    body = cohesity_sdk.helios.AddFortknoxVaultsReq() # AddFortknoxVaultsReq | Specifies the parameters to add Fortknox vaults in a region.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Add Cohesity Fortknox vaults in a given list of regions for the given account.
        api_response = api_instance.add_fortknox_vaults(body, region_id=region_id)
        print("The response of FortknoxApi->add_fortknox_vaults:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FortknoxApi->add_fortknox_vaults: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddFortknoxVaultsReq**](AddFortknoxVaultsReq.md)| Specifies the parameters to add Fortknox vaults in a region. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**AddFortknoxVaultsResp**](AddFortknoxVaultsResp.md)

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

# **get_fortknox_vaults**
> GetFortknoxVaultsResp get_fortknox_vaults(region_id=region_id, region_ids=region_ids)

Get Fortknox vaults.

Get the list of FortKnox vaults for the logged in account.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.get_fortknox_vaults_resp import GetFortknoxVaultsResp
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.FortknoxApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    region_ids = ['region_ids_example'] # List[Optional[str]] | List of region IDs to filter the response. (optional)

    try:
        # Get Fortknox vaults.
        api_response = api_instance.get_fortknox_vaults(region_id=region_id, region_ids=region_ids)
        print("The response of FortknoxApi->get_fortknox_vaults:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FortknoxApi->get_fortknox_vaults: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **region_ids** | [**List[Optional[str]]**](str.md)| List of region IDs to filter the response. | [optional] 

### Return type

[**GetFortknoxVaultsResp**](GetFortknoxVaultsResp.md)

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

# **get_vault_transfer_time_config**
> VaultTransferTimeConfigs get_vault_transfer_time_config(region_id=region_id, global_vault_ids=global_vault_ids)

Get transfer time configurations.

Get data transfer time configurations of FortKnox vaults. These are backup data transfer configurations of FortKnox vaults.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.vault_transfer_time_configs import VaultTransferTimeConfigs
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.FortknoxApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    global_vault_ids = ['global_vault_ids_example'] # List[str] | List of FortKnox Global vault IDs. (optional)

    try:
        # Get transfer time configurations.
        api_response = api_instance.get_vault_transfer_time_config(region_id=region_id, global_vault_ids=global_vault_ids)
        print("The response of FortknoxApi->get_vault_transfer_time_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FortknoxApi->get_vault_transfer_time_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **global_vault_ids** | [**List[str]**](str.md)| List of FortKnox Global vault IDs. | [optional] 

### Return type

[**VaultTransferTimeConfigs**](VaultTransferTimeConfigs.md)

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

# **pair_fortknox_vaults_clusters**
> pair_fortknox_vaults_clusters(body, region_id=region_id)

An endpoint to pair clusters with fortknox vaults.

An endpoint to pair clusters with fortknox vaults.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.pair_fortknox_vaults_clusters_req import PairFortknoxVaultsClustersReq
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.FortknoxApi(api_client)
    body = cohesity_sdk.helios.PairFortknoxVaultsClustersReq() # PairFortknoxVaultsClustersReq | Specifies the parameters to pair claimed clusters with fortknox vaults.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # An endpoint to pair clusters with fortknox vaults.
        api_instance.pair_fortknox_vaults_clusters(body, region_id=region_id)
    except Exception as e:
        print("Exception when calling FortknoxApi->pair_fortknox_vaults_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PairFortknoxVaultsClustersReq**](PairFortknoxVaultsClustersReq.md)| Specifies the parameters to pair claimed clusters with fortknox vaults. | 
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

# **perform_vault_actions**
> perform_vault_actions(global_vault_id, body, region_id=region_id)

Perform actions on a given FortKnox vault.

Perform actions on a given FortKnox vault specified by global vault id.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.perform_vault_actions_req import PerformVaultActionsReq
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.FortknoxApi(api_client)
    global_vault_id = 'global_vault_id_example' # str | Specifies the global vault id of the vault on which the action needs to be performed.
    body = cohesity_sdk.helios.PerformVaultActionsReq() # PerformVaultActionsReq | Specifies the parameters to perform actions on a vault.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Perform actions on a given FortKnox vault.
        api_instance.perform_vault_actions(global_vault_id, body, region_id=region_id)
    except Exception as e:
        print("Exception when calling FortknoxApi->perform_vault_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_vault_id** | **str**| Specifies the global vault id of the vault on which the action needs to be performed. | 
 **body** | [**PerformVaultActionsReq**](PerformVaultActionsReq.md)| Specifies the parameters to perform actions on a vault. | 
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

# **update_vault_transfer_time_config**
> VaultTransferTimeConfig update_vault_transfer_time_config(global_vault_id, body, region_id=region_id)

Update transfer time configuration.

Update data transfer time configuration of a FortKnox vault. These configurations apply only for FortKnox vaulting.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.vault_transfer_time_config import VaultTransferTimeConfig
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.FortknoxApi(api_client)
    global_vault_id = 'global_vault_id_example' # str | Specifies the global vault id of the vault.
    body = cohesity_sdk.helios.VaultTransferTimeConfig() # VaultTransferTimeConfig | Parameters to update transfer time configuraion of a FortKnox vault.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update transfer time configuration.
        api_response = api_instance.update_vault_transfer_time_config(global_vault_id, body, region_id=region_id)
        print("The response of FortknoxApi->update_vault_transfer_time_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FortknoxApi->update_vault_transfer_time_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_vault_id** | **str**| Specifies the global vault id of the vault. | 
 **body** | [**VaultTransferTimeConfig**](VaultTransferTimeConfig.md)| Parameters to update transfer time configuraion of a FortKnox vault. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**VaultTransferTimeConfig**](VaultTransferTimeConfig.md)

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

