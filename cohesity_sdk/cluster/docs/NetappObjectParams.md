# NetappObjectParams

Specifies the common parameters for Netapp objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_nas_mount_protocols** | **List[str]** | Specifies a list of NAS mount protocols supported by this object. | [optional] 
**volume_extended_style** | **str** | Specifies the extended style of a NetApp volume. | [optional] 
**volume_type** | **str** | Specifies the Netapp volume type. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.netapp_object_params import NetappObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of NetappObjectParams from a JSON string
netapp_object_params_instance = NetappObjectParams.from_json(json)
# print the JSON string representation of the object
print(NetappObjectParams.to_json())

# convert the object into a dict
netapp_object_params_dict = netapp_object_params_instance.to_dict()
# create an instance of NetappObjectParams from a dict
netapp_object_params_from_dict = NetappObjectParams.from_dict(netapp_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


