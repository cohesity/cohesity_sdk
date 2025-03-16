# CommonNasObjectParams

Specifies the common parameters for NAS objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_nas_mount_protocols** | **List[str]** | Specifies a list of NAS mount protocols supported by this object. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.common_nas_object_params import CommonNasObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonNasObjectParams from a JSON string
common_nas_object_params_instance = CommonNasObjectParams.from_json(json)
# print the JSON string representation of the object
print(CommonNasObjectParams.to_json())

# convert the object into a dict
common_nas_object_params_dict = common_nas_object_params_instance.to_dict()
# create an instance of CommonNasObjectParams from a dict
common_nas_object_params_from_dict = CommonNasObjectParams.from_dict(common_nas_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


