# HeliosOracleTier

Specifies the settings for a Oracle tier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_after** | **int** | Specifies the time period after which the backup will be moved from current tier to next tier. | [optional] 
**move_after_unit** | **str** | Specifies the unit for moving the data from current tier to next tier. This unit will be a base unit for the &#39;moveAfter&#39; field specified below. | [optional] 
**tier_type** | **str** | Specifies the Oracle tier types. | 

## Example

```python
from cohesity_sdk.helios.models.helios_oracle_tier import HeliosOracleTier

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosOracleTier from a JSON string
helios_oracle_tier_instance = HeliosOracleTier.from_json(json)
# print the JSON string representation of the object
print(HeliosOracleTier.to_json())

# convert the object into a dict
helios_oracle_tier_dict = helios_oracle_tier_instance.to_dict()
# create an instance of HeliosOracleTier from a dict
helios_oracle_tier_from_dict = HeliosOracleTier.from_dict(helios_oracle_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


