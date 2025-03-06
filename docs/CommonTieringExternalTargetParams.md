# CommonTieringExternalTargetParams

Specifies the common parameters which are specific to Tiering purpose type External Targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption_level** | **str** | Specifies the type of encryption for the Setting. | 
**storage_type** | **str** | Specifies the Storage type of the External Target. | 

## Example

```python
from cohesity_sdk.cluster.models.common_tiering_external_target_params import CommonTieringExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonTieringExternalTargetParams from a JSON string
common_tiering_external_target_params_instance = CommonTieringExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(CommonTieringExternalTargetParams.to_json())

# convert the object into a dict
common_tiering_external_target_params_dict = common_tiering_external_target_params_instance.to_dict()
# create an instance of CommonTieringExternalTargetParams from a dict
common_tiering_external_target_params_from_dict = CommonTieringExternalTargetParams.from_dict(common_tiering_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


