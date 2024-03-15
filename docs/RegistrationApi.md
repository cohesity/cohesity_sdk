# cohesity_sdk.RegistrationApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_helios_reg_config**](RegistrationApi.md#get_helios_reg_config) | **GET** /helios-registration-config | Lists the Helios Registration Config.
[**helios_claim**](RegistrationApi.md#helios_claim) | **POST** /helios-registration | Register to Helios.


# **get_helios_reg_config**
> HeliosRegConfig get_helios_reg_config()

Lists the Helios Registration Config.

Lists the Helios Registration Config.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.helios_reg_config import HeliosRegConfig
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint



client = ClusterClient(cluster_vip)


# example, this endpoint has no required or optional parameters
try:
	# Lists the Helios Registration Config.
	api_response = client.registration.get_helios_reg_config()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RegistrationApi->get_helios_reg_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**HeliosRegConfig**](HeliosRegConfig.md)

### Authorization

No authorization required

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

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.helios_claim_request import HeliosClaimRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint



client = ClusterClient(cluster_vip)

body = HeliosClaimRequest(
        registration_token="registration_token_example",
        rigel_guid=1,
    ) # HeliosClaimRequest | Specifies the parameters to claim to Helios.

# example passing only required values which don't have defaults set
try:
	# Register to Helios.
	client.registration.helios_claim(body)
except ApiException as e:
	print("Exception when calling RegistrationApi->helios_claim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HeliosClaimRequest**](HeliosClaimRequest.md)| Specifies the parameters to claim to Helios. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

