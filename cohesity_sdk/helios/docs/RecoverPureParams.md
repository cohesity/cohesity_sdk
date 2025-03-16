# RecoverPureParams

Specifies the recovery options specific to Pure environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover object parameters. | 
**recover_san_group_params** | [**RecoverPureSanGroupParams**](RecoverPureSanGroupParams.md) | Specifies the parameters to recover SAN Pure Protection Group. | [optional] 
**recover_san_volume_params** | [**RecoverPureSanVolumeParams**](RecoverPureSanVolumeParams.md) | Specifies the parameters to recover SAN Volume. | [optional] 
**recovery_action** | **str** | Specifies the type of recovery action to be performed. The corresponding recovery action params must be filled out. | 

## Example

```python
from cohesity_sdk.helios.models.recover_pure_params import RecoverPureParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverPureParams from a JSON string
recover_pure_params_instance = RecoverPureParams.from_json(json)
# print the JSON string representation of the object
print(RecoverPureParams.to_json())

# convert the object into a dict
recover_pure_params_dict = recover_pure_params_instance.to_dict()
# create an instance of RecoverPureParams from a dict
recover_pure_params_from_dict = RecoverPureParams.from_dict(recover_pure_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


