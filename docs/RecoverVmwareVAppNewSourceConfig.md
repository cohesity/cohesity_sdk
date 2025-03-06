# RecoverVmwareVAppNewSourceConfig

Specifies the new destination Source configuration where the vApps will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | **str** | Specifies the type of VMware source to which the VMs are being restored. | 
**v_cloud_director_params** | [**RecoverVmwareVAppVCDSourceConfig**](RecoverVmwareVAppVCDSourceConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_vmware_v_app_new_source_config import RecoverVmwareVAppNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVmwareVAppNewSourceConfig from a JSON string
recover_vmware_v_app_new_source_config_instance = RecoverVmwareVAppNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverVmwareVAppNewSourceConfig.to_json())

# convert the object into a dict
recover_vmware_v_app_new_source_config_dict = recover_vmware_v_app_new_source_config_instance.to_dict()
# create an instance of RecoverVmwareVAppNewSourceConfig from a dict
recover_vmware_v_app_new_source_config_from_dict = RecoverVmwareVAppNewSourceConfig.from_dict(recover_vmware_v_app_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


