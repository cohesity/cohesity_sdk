# AWSTier

Specifies the settings for a aws tier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_after** | **int** | Specifies the time period after which the backup will be moved from current tier to next tier. | [optional] 
**move_after_unit** | **str** | Specifies the unit for moving the data from current tier to next tier. This unit will be a base unit for the &#39;moveAfter&#39; field specified below. | [optional] 
**tier_type** | **str** | Specifies the AWS tier types. | 

## Example

```python
from cohesity_sdk.cluster.models.aws_tier import AWSTier

# TODO update the JSON string below
json = "{}"
# create an instance of AWSTier from a JSON string
aws_tier_instance = AWSTier.from_json(json)
# print the JSON string representation of the object
print(AWSTier.to_json())

# convert the object into a dict
aws_tier_dict = aws_tier_instance.to_dict()
# create an instance of AWSTier from a dict
aws_tier_from_dict = AWSTier.from_dict(aws_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


