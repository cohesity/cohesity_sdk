# ObjectTypeVCenterParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_cloud_env** | **bool** | Specifies that registered vCenter source is a VMC (VMware Cloud) environment or not. | [optional] 

## Example

```python
from cohesity_sdk.models.object_type_v_center_params import ObjectTypeVCenterParams

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectTypeVCenterParams from a JSON string
object_type_v_center_params_instance = ObjectTypeVCenterParams.from_json(json)
# print the JSON string representation of the object
print(ObjectTypeVCenterParams.to_json())

# convert the object into a dict
object_type_v_center_params_dict = object_type_v_center_params_instance.to_dict()
# create an instance of ObjectTypeVCenterParams from a dict
object_type_v_center_params_from_dict = ObjectTypeVCenterParams.from_dict(object_type_v_center_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


