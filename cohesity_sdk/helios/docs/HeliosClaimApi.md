# cohesity_sdk.HeliosClaimApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mcm_claim**](HeliosClaimApi.md#create_mcm_claim) | **POST** /mcm/claim | Claim a Cohesity Entity.


# **create_mcm_claim**
> CreateMcmClaimResponseBody create_mcm_claim(body)

Claim a Cohesity Entity.

Claim a Cohesity entity to Helios. An entity could be Rigel or a Cohesity Cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.create_mcm_claim_request import CreateMcmClaimRequest
from cohesity_sdk.helios.model.create_mcm_claim_response_body import CreateMcmClaimResponseBody
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CreateMcmClaimRequest(
        entity_type="Rigel",
        rigel_params=McmRigelClaimRequestParams(
            rigel_guid=1,
            claim_token="claim_token_example",
            rigel_type="OnPrem",
            cluster_id=1,
            cluster_incarnation_id=1,
            rigel_name="rigel_name_example",
            rigel_ip="rigel_ip_example",
            software_version="software_version_example",
        ),
        cluster_params=McmClusterClaimRequestParams(
            cluster_id=1,
            cluster_incarnation_id=1,
            cluster_name="cluster_name_example",
            claim_token="claim_token_example",
        ),
    ) # CreateMcmClaimRequest | Request paramters to claim a Cohesity entity.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Claim a Cohesity Entity.
	api_response = client.helios_claim.create_mcm_claim(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosClaimApi->create_mcm_claim: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Claim a Cohesity Entity.
	api_response = client.helios_claim.create_mcm_claim(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosClaimApi->create_mcm_claim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMcmClaimRequest**](CreateMcmClaimRequest.md)| Request paramters to claim a Cohesity entity. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**CreateMcmClaimResponseBody**](CreateMcmClaimResponseBody.md)

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

