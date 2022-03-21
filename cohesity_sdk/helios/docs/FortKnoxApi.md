# cohesity_sdk.FortKnoxApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fortknox_quiet_time_config**](FortKnoxApi.md#get_fortknox_quiet_time_config) | **GET** /mcm/fortknox/vaults/quiet-time-configs | Get quiet time configurations.
[**update_fortknox_quiet_time_config**](FortKnoxApi.md#update_fortknox_quiet_time_config) | **PUT** /mcm/fortknox/vaults/quiet-time-configs | Update quiet time configuration.


# **get_fortknox_quiet_time_config**
> QuietTimeConfigurations get_fortknox_quiet_time_config()

Get quiet time configurations.

Get quiet time configurations of FortKnox vaults.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.quiet_time_configurations import QuietTimeConfigurations
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
region_ids = [
        "regionIds_example",
    ] # [str], none_type | List of FortKnox region IDs. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get quiet time configurations.
	api_response = client.fort_knox.get_fortknox_quiet_time_config(region_id=region_id, region_ids=region_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling FortKnoxApi->get_fortknox_quiet_time_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **region_ids** | **[str], none_type**| List of FortKnox region IDs. | [optional]

### Return type

[**QuietTimeConfigurations**](QuietTimeConfigurations.md)

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

# **update_fortknox_quiet_time_config**
> QuietTimeConfiguration update_fortknox_quiet_time_config(body)

Update quiet time configuration.

Update quiet time configuration of a FortKnox vault. During the quiet times backup tasks to the FortKnox vaults are not started.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.quiet_time_configuration import QuietTimeConfiguration
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = QuietTimeConfiguration(
        region_id="region_id_example",
        quiet_time_config_params=QuietTimeConfigParams(
            timezone="America/Los_Angeles",
            quiet_times=[
                QuietTimeParams(
                    days=[
                        "Sunday",
                    ],
                    start_time=QuietTimeOfDay(
                        hour=0,
                        minute=0,
                    ),
                    end_time=QuietTimeOfDay(
                        hour=0,
                        minute=0,
                    ),
                ),
            ],
        ),
    ) # QuietTimeConfiguration | Parameters to update quiet time configuraion of a FortKnox vault.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update quiet time configuration.
	api_response = client.fort_knox.update_fortknox_quiet_time_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling FortKnoxApi->update_fortknox_quiet_time_config: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update quiet time configuration.
	api_response = client.fort_knox.update_fortknox_quiet_time_config(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling FortKnoxApi->update_fortknox_quiet_time_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuietTimeConfiguration**](QuietTimeConfiguration.md)| Parameters to update quiet time configuraion of a FortKnox vault. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**QuietTimeConfiguration**](QuietTimeConfiguration.md)

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

