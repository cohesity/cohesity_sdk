# RecoverPureParams

Specifies the recovery options specific to Pure environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[CommonRecoverObjectSnapshotParams], none_type**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover object parameters. | 
**recovery_action** | **str** | Specifies the type of recovery action to be performed. The corresponding recovery action params must be filled out. | defaults to "RecoverSanVolumes"
**recover_san_volume_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the parameters to recover SAN Volume. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


