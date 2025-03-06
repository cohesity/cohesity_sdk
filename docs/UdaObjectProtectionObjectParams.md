# UdaObjectProtectionObjectParams

Specifies the object parameters to create an Universal Data Adapter Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_object_ids** | **List[int]** | Specifies the ids of the objects to be excluded in the Object Protection. This can be used to ignore specific objects under a parent object which has been included for protection. | [optional] 
**id** | **int** | Specifies the id of the object being protected. This can be a leaf level or non leaf level object. | 

## Example

```python
from cohesity_sdk.cluster.models.uda_object_protection_object_params import UdaObjectProtectionObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of UdaObjectProtectionObjectParams from a JSON string
uda_object_protection_object_params_instance = UdaObjectProtectionObjectParams.from_json(json)
# print the JSON string representation of the object
print(UdaObjectProtectionObjectParams.to_json())

# convert the object into a dict
uda_object_protection_object_params_dict = uda_object_protection_object_params_instance.to_dict()
# create an instance of UdaObjectProtectionObjectParams from a dict
uda_object_protection_object_params_from_dict = UdaObjectProtectionObjectParams.from_dict(uda_object_protection_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


