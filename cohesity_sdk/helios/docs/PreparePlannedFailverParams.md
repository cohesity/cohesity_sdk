# PreparePlannedFailverParams

Specifies parameters of preparation of a planned failover.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reverse_replication** | **bool** | Specifies whether a reverse replication needs to be set for the view on target cluster after failover. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.prepare_planned_failver_params import PreparePlannedFailverParams

# TODO update the JSON string below
json = "{}"
# create an instance of PreparePlannedFailverParams from a JSON string
prepare_planned_failver_params_instance = PreparePlannedFailverParams.from_json(json)
# print the JSON string representation of the object
print(PreparePlannedFailverParams.to_json())

# convert the object into a dict
prepare_planned_failver_params_dict = prepare_planned_failver_params_instance.to_dict()
# create an instance of PreparePlannedFailverParams from a dict
prepare_planned_failver_params_from_dict = PreparePlannedFailverParams.from_dict(prepare_planned_failver_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


