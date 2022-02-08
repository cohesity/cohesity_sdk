# cohesity_sdk.HeliosRegistrationApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_helios_reg_config**](HeliosRegistrationApi.md#get_helios_reg_config) | **GET** /helios-registration-config | Lists the Helios Registration Config.
[**get_rigel_claim_logs**](HeliosRegistrationApi.md#get_rigel_claim_logs) | **GET** /rigel-claim-logs | Lists the claim logs for rigel.
[**helios_claim**](HeliosRegistrationApi.md#helios_claim) | **POST** /helios-registration | Register to Helios.


# **get_helios_reg_config**
> HeliosRegConfig get_helios_reg_config()

Lists the Helios Registration Config.

Lists the Helios Registration Config.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.helios_reg_config import HeliosRegConfig
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)



# example, this endpoint has no required or optional parameters
try:
	# Lists the Helios Registration Config.
	api_response = client.helios_registration.get_helios_reg_config()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosRegistrationApi->get_helios_reg_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**HeliosRegConfig**](HeliosRegConfig.md)

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

# **get_rigel_claim_logs**
> RigelClaimLogs get_rigel_claim_logs()

Lists the claim logs for rigel.

Lists the logs during rigel cluster creation and claim.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.rigel_claim_logs import RigelClaimLogs
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)



# example, this endpoint has no required or optional parameters
try:
	# Lists the claim logs for rigel.
	api_response = client.helios_registration.get_rigel_claim_logs()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosRegistrationApi->get_rigel_claim_logs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RigelClaimLogs**](RigelClaimLogs.md)

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

# **helios_claim**
> helios_claim(body)

Register to Helios.

Claim to Helios.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.helios_claim_request import HeliosClaimRequest
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = HeliosClaimRequest(
        registration_token="registration_token_example",
    ) # HeliosClaimRequest | Specifies the parameters to claim to Helios.

# example passing only required values which don't have defaults set
try:
	# Register to Helios.
	client.helios_registration.helios_claim(body)
except ApiException as e:
	print("Exception when calling HeliosRegistrationApi->helios_claim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HeliosClaimRequest**](HeliosClaimRequest.md)| Specifies the parameters to claim to Helios. |

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

