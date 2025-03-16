# NodeRemovalParams

Specifies parameters to initiate/cancel node removal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel** | **bool** | If true, cancels node removal that is already in progress. | 
**is_offline** | **bool** | Specifies whether node being removed is offline. | [optional] [default to False]
**is_validate_only** | **bool** | Specifies whether request is for pre-check validations only | [optional] [default to False]

## Example

```python
from cohesity_sdk.helios.models.node_removal_params import NodeRemovalParams

# TODO update the JSON string below
json = "{}"
# create an instance of NodeRemovalParams from a JSON string
node_removal_params_instance = NodeRemovalParams.from_json(json)
# print the JSON string representation of the object
print(NodeRemovalParams.to_json())

# convert the object into a dict
node_removal_params_dict = node_removal_params_instance.to_dict()
# create an instance of NodeRemovalParams from a dict
node_removal_params_from_dict = NodeRemovalParams.from_dict(node_removal_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


