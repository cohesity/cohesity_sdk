# SlaRule

Specifies an SLA rule for a specific Protection Group run type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_run_type** | **str** | Specifies the type of run this rule should apply to. | [optional] 
**sla_minutes** | **int** | Specifies the number of minutes allotted to a run of the specified type before SLA is considered violated. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.sla_rule import SlaRule

# TODO update the JSON string below
json = "{}"
# create an instance of SlaRule from a JSON string
sla_rule_instance = SlaRule.from_json(json)
# print the JSON string representation of the object
print(SlaRule.to_json())

# convert the object into a dict
sla_rule_dict = sla_rule_instance.to_dict()
# create an instance of SlaRule from a dict
sla_rule_from_dict = SlaRule.from_dict(sla_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


