# AzureTier

Specifies the settings for a Azure tier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_after** | **int** | Specifies the time period after which the backup will be moved from current tier to next tier. | [optional] 
**move_after_unit** | **str** | Specifies the unit for moving the data from current tier to next tier. This unit will be a base unit for the &#39;moveAfter&#39; field specified below. | [optional] 
**tier_type** | **str** | Specifies the Azure tier types. | 

## Example

```python
from cohesity_sdk.models.azure_tier import AzureTier

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTier from a JSON string
azure_tier_instance = AzureTier.from_json(json)
# print the JSON string representation of the object
print(AzureTier.to_json())

# convert the object into a dict
azure_tier_dict = azure_tier_instance.to_dict()
# create an instance of AzureTier from a dict
azure_tier_from_dict = AzureTier.from_dict(azure_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


