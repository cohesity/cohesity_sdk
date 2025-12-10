# M365Params

Specifies parameters of Microsoft 365 type snapshots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csm_params** | [**CSMParams**](CSMParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.m365_params import M365Params

# TODO update the JSON string below
json = "{}"
# create an instance of M365Params from a JSON string
m365_params_instance = M365Params.from_json(json)
# print the JSON string representation of the object
print(M365Params.to_json())

# convert the object into a dict
m365_params_dict = m365_params_instance.to_dict()
# create an instance of M365Params from a dict
m365_params_from_dict = M365Params.from_dict(m365_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


