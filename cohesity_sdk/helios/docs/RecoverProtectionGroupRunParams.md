# RecoverProtectionGroupRunParams

Specifies the Protection Group Run params to recover. All the VM's that are successfully backed up by specified Runs will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_target_id** | **int** | Specifies the archival target id. If specified and Protection Group run has an archival snapshot then VMs are recovered from the specified archival snapshot. If not specified (default), VMs are recovered from local snapshot. | [optional] 
**protection_group_id** | **str** | Specifies the local Protection Group id. In case of recovering a replication Run, this field should be provided with local Protection Group id. | [optional] 
**protection_group_instance_id** | **int** | Specifies the Protection Group Instance id. | 
**protection_group_run_id** | **str** | Specifies the Protection Group Run id from which to recover VMs. All the VM&#39;s that are successfully protected by this Run will be recovered. | 

## Example

```python
from cohesity_sdk.helios.models.recover_protection_group_run_params import RecoverProtectionGroupRunParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverProtectionGroupRunParams from a JSON string
recover_protection_group_run_params_instance = RecoverProtectionGroupRunParams.from_json(json)
# print the JSON string representation of the object
print(RecoverProtectionGroupRunParams.to_json())

# convert the object into a dict
recover_protection_group_run_params_dict = recover_protection_group_run_params_instance.to_dict()
# create an instance of RecoverProtectionGroupRunParams from a dict
recover_protection_group_run_params_from_dict = RecoverProtectionGroupRunParams.from_dict(recover_protection_group_run_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


