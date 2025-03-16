# RestoreObjectCustomization

Specifies the customization for the VMware VMs being restored. Example: When recovering multiple VMs, users can customize network configuration for one or more VMs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_config** | [**RecoverVmwareVmNewSourceNetworkConfig**](RecoverVmwareVmNewSourceNetworkConfig.md) | Specifies the customized network configuration for the VM being recovered. | [optional] 
**object_id** | **int** | Specifies the object id of the VM. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.restore_object_customization import RestoreObjectCustomization

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreObjectCustomization from a JSON string
restore_object_customization_instance = RestoreObjectCustomization.from_json(json)
# print the JSON string representation of the object
print(RestoreObjectCustomization.to_json())

# convert the object into a dict
restore_object_customization_dict = restore_object_customization_instance.to_dict()
# create an instance of RestoreObjectCustomization from a dict
restore_object_customization_from_dict = RestoreObjectCustomization.from_dict(restore_object_customization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


