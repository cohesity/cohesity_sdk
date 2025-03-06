# NetappProtectionGroupObjectParams

Specifies an object protected by a Netapp Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.netapp_protection_group_object_params import NetappProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of NetappProtectionGroupObjectParams from a JSON string
netapp_protection_group_object_params_instance = NetappProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(NetappProtectionGroupObjectParams.to_json())

# convert the object into a dict
netapp_protection_group_object_params_dict = netapp_protection_group_object_params_instance.to_dict()
# create an instance of NetappProtectionGroupObjectParams from a dict
netapp_protection_group_object_params_from_dict = NetappProtectionGroupObjectParams.from_dict(netapp_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


