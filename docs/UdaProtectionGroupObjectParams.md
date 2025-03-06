# UdaProtectionGroupObjectParams

Specifies the Universal Data Adapter object details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | [optional] 
**name** | **str** | Specifies the fully qualified name of the object. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.uda_protection_group_object_params import UdaProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of UdaProtectionGroupObjectParams from a JSON string
uda_protection_group_object_params_instance = UdaProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(UdaProtectionGroupObjectParams.to_json())

# convert the object into a dict
uda_protection_group_object_params_dict = uda_protection_group_object_params_instance.to_dict()
# create an instance of UdaProtectionGroupObjectParams from a dict
uda_protection_group_object_params_from_dict = UdaProtectionGroupObjectParams.from_dict(uda_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


