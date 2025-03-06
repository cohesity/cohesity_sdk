# ExternalTargets

List of External Target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_targets** | [**List[ExternalTarget]**](ExternalTarget.md) | Specifies the list of External Targets which were returned by the request. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.external_targets import ExternalTargets

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalTargets from a JSON string
external_targets_instance = ExternalTargets.from_json(json)
# print the JSON string representation of the object
print(ExternalTargets.to_json())

# convert the object into a dict
external_targets_dict = external_targets_instance.to_dict()
# create an instance of ExternalTargets from a dict
external_targets_from_dict = ExternalTargets.from_dict(external_targets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


