# CSMParams

Specifies parameters of Microsoft 365 Backup Storage type snapshots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_fast_restore_point** | **bool** | Specifies if this snapshot is a fast restore point. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.csm_params import CSMParams

# TODO update the JSON string below
json = "{}"
# create an instance of CSMParams from a JSON string
csm_params_instance = CSMParams.from_json(json)
# print the JSON string representation of the object
print(CSMParams.to_json())

# convert the object into a dict
csm_params_dict = csm_params_instance.to_dict()
# create an instance of CSMParams from a dict
csm_params_from_dict = CSMParams.from_dict(csm_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


