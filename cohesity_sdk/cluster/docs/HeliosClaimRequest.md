# HeliosClaimRequest

Specifies the request to register to Helios.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_token** | **str** | Specifies the Helios registration token. | 
**rigel_guid** | **int** | Specifies the rigel guid to be used for registration. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.helios_claim_request import HeliosClaimRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosClaimRequest from a JSON string
helios_claim_request_instance = HeliosClaimRequest.from_json(json)
# print the JSON string representation of the object
print(HeliosClaimRequest.to_json())

# convert the object into a dict
helios_claim_request_dict = helios_claim_request_instance.to_dict()
# create an instance of HeliosClaimRequest from a dict
helios_claim_request_from_dict = HeliosClaimRequest.from_dict(helios_claim_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


