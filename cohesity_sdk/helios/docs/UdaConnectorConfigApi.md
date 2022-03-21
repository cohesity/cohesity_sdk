# cohesity_sdk.UdaConnectorConfigApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_uda_connector_config**](UdaConnectorConfigApi.md#create_uda_connector_config) | **POST** /uda/connector-configs | Create a new UDA connector config
[**delete_uda_connector_config**](UdaConnectorConfigApi.md#delete_uda_connector_config) | **DELETE** /uda/connector-configs/{id} | Delete a UDA connector config
[**get_connector_configs**](UdaConnectorConfigApi.md#get_connector_configs) | **GET** /uda/connector-configs | Get the workflow Parameters for all the sources
[**get_connector_configs_by_id**](UdaConnectorConfigApi.md#get_connector_configs_by_id) | **GET** /uda/connector-configs/{id} | Get the Parameters of a source based on id
[**get_uda_connector_config_raw**](UdaConnectorConfigApi.md#get_uda_connector_config_raw) | **GET** /uda/connector-configs/raw | Get UDA connector config
[**update_uda_connector_config**](UdaConnectorConfigApi.md#update_uda_connector_config) | **PUT** /uda/connector-configs | Update a UDA connector config


# **create_uda_connector_config**
> create_uda_connector_config(body)

Create a new UDA connector config

Stores the new config in gandalf via iris proxy.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.uda_connector_config_params import UdaConnectorConfigParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = UdaConnectorConfigParams(
        index_config="index_config_example",
        ui_translation_config=[
            UdaLocaleSpecificTranslations(
                locale_name="locale_name_example",
                translations="translations_example",
            ),
        ],
        os_specific_config=[
            UdaOSSpecificConfigParams(
                os_type="os_type_example",
                index_config="index_config_example",
                registration_config="registration_config_example",
                protection_config="protection_config_example",
                recovery_config="recovery_config_example",
            ),
        ],
        replace=True,
    ) # UdaConnectorConfigParams | Specifies the parameters to create a new UDA config.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a new UDA connector config
	client.uda_connector_config.create_uda_connector_config(body)
except ApiException as e:
	print("Exception when calling UdaConnectorConfigApi->create_uda_connector_config: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a new UDA connector config
	client.uda_connector_config.create_uda_connector_config(body, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling UdaConnectorConfigApi->create_uda_connector_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UdaConnectorConfigParams**](UdaConnectorConfigParams.md)| Specifies the parameters to create a new UDA config. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
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

# **delete_uda_connector_config**
> delete_uda_connector_config(id)

Delete a UDA connector config

Delete the config in gandalf via iris proxy.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of the UDA 
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete a UDA connector config
	client.uda_connector_config.delete_uda_connector_config(id)
except ApiException as e:
	print("Exception when calling UdaConnectorConfigApi->delete_uda_connector_config: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete a UDA connector config
	client.uda_connector_config.delete_uda_connector_config(id, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling UdaConnectorConfigApi->delete_uda_connector_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the UDA  |
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

# **get_connector_configs**
> [UdaConfigParams] get_connector_configs()

Get the workflow Parameters for all the sources

Get the workflow Parameters for all the sources.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.uda_config_params import UdaConfigParams
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the workflow Parameters for all the sources
	api_response = client.uda_connector_config.get_connector_configs(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UdaConnectorConfigApi->get_connector_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**[UdaConfigParams]**](UdaConfigParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of objects with source info and parameters to customize registration, protection and recovery workflows for all the uda sources. |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector_configs_by_id**
> UdaConfigParams get_connector_configs_by_id(id)

Get the Parameters of a source based on id

Get the Parameters of a source based on id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.uda_config_params import UdaConfigParams
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of the Uda Source.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get the Parameters of a source based on id
	api_response = client.uda_connector_config.get_connector_configs_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UdaConnectorConfigApi->get_connector_configs_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the Parameters of a source based on id
	api_response = client.uda_connector_config.get_connector_configs_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UdaConnectorConfigApi->get_connector_configs_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Uda Source. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**UdaConfigParams**](UdaConfigParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object with source info and parameters to customize registration, protection and recovery workflows for the given source id. |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_uda_connector_config_raw**
> UdaConfigsList get_uda_connector_config_raw()

Get UDA connector config

Get the UDA config from gandalf via iris proxy.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.uda_configs_list import UdaConfigsList
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
id = 1 # int | Specifies the id of the UDA config. (optional)
filter_index_config = True # bool | If true, returns index config only as response. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get UDA connector config
	api_response = client.uda_connector_config.get_uda_connector_config_raw(access_cluster_id=access_cluster_id, region_id=region_id, id=id, filter_index_config=filter_index_config)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UdaConnectorConfigApi->get_uda_connector_config_raw: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **id** | **int**| Specifies the id of the UDA config. | [optional]
 **filter_index_config** | **bool**| If true, returns index config only as response. | [optional]

### Return type

[**UdaConfigsList**](UdaConfigsList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success. |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_uda_connector_config**
> update_uda_connector_config(body)

Update a UDA connector config

Updates the config in gandalf via iris proxy.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.uda_connector_config_params import UdaConnectorConfigParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = UdaConnectorConfigParams(
        index_config="index_config_example",
        ui_translation_config=[
            UdaLocaleSpecificTranslations(
                locale_name="locale_name_example",
                translations="translations_example",
            ),
        ],
        os_specific_config=[
            UdaOSSpecificConfigParams(
                os_type="os_type_example",
                index_config="index_config_example",
                registration_config="registration_config_example",
                protection_config="protection_config_example",
                recovery_config="recovery_config_example",
            ),
        ],
        replace=True,
    ) # UdaConnectorConfigParams | Specifies the parameters to update the UDA config.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update a UDA connector config
	client.uda_connector_config.update_uda_connector_config(body)
except ApiException as e:
	print("Exception when calling UdaConnectorConfigApi->update_uda_connector_config: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update a UDA connector config
	client.uda_connector_config.update_uda_connector_config(body, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling UdaConnectorConfigApi->update_uda_connector_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UdaConnectorConfigParams**](UdaConnectorConfigParams.md)| Specifies the parameters to update the UDA config. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
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

