# HeliosTier

Specifies the Helios Tier details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default_tier** | **bool** | Specifies whether the current tier will be the default tier for primary retention. | [optional] 
**move_after** | **int** | Specifies the duration after which the backup will be moved to next tier. | [optional] 
**type** | **str** | Specifies the tier type. | [optional] 
**unit** | **str** | Specificies the time unit after which backup will be moved to next tier. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_tier import HeliosTier

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosTier from a JSON string
helios_tier_instance = HeliosTier.from_json(json)
# print the JSON string representation of the object
print(HeliosTier.to_json())

# convert the object into a dict
helios_tier_dict = helios_tier_instance.to_dict()
# create an instance of HeliosTier from a dict
helios_tier_from_dict = HeliosTier.from_dict(helios_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


