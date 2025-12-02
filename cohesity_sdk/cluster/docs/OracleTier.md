# OracleTier

Specifies the settings for a Oracle tier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_after** | **int** | Specifies the time period after which the backup will be moved from current tier to next tier. | [optional] 
**move_after_unit** | **str** | Specifies the unit for moving the data from current tier to next tier. This unit will be a base unit for the &#39;moveAfter&#39; field specified below. | [optional] 
**tier_type** | **str** | Specifies the Oracle tier types. | 

## Example

```python
from cohesity_sdk.cluster.models.oracle_tier import OracleTier

# TODO update the JSON string below
json = "{}"
# create an instance of OracleTier from a JSON string
oracle_tier_instance = OracleTier.from_json(json)
# print the JSON string representation of the object
print(OracleTier.to_json())

# convert the object into a dict
oracle_tier_dict = oracle_tier_instance.to_dict()
# create an instance of OracleTier from a dict
oracle_tier_from_dict = OracleTier.from_dict(oracle_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


