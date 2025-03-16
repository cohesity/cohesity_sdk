# CommonHyperVObjectParams

Specifies the common object parameters required for HyperV protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backups_copy_only** | **bool** | Specifies whether the backups should be copy-only. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.common_hyper_v_object_params import CommonHyperVObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonHyperVObjectParams from a JSON string
common_hyper_v_object_params_instance = CommonHyperVObjectParams.from_json(json)
# print the JSON string representation of the object
print(CommonHyperVObjectParams.to_json())

# convert the object into a dict
common_hyper_v_object_params_dict = common_hyper_v_object_params_instance.to_dict()
# create an instance of CommonHyperVObjectParams from a dict
common_hyper_v_object_params_from_dict = CommonHyperVObjectParams.from_dict(common_hyper_v_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


