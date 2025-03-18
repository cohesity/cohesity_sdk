# RigelClaimInfo

Specifies the Rigel registration info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Specifies possible error message during registration. | [optional] 
**status** | **str** | Specifies the registration status. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.rigel_claim_info import RigelClaimInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RigelClaimInfo from a JSON string
rigel_claim_info_instance = RigelClaimInfo.from_json(json)
# print the JSON string representation of the object
print(RigelClaimInfo.to_json())

# convert the object into a dict
rigel_claim_info_dict = rigel_claim_info_instance.to_dict()
# create an instance of RigelClaimInfo from a dict
rigel_claim_info_from_dict = RigelClaimInfo.from_dict(rigel_claim_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


