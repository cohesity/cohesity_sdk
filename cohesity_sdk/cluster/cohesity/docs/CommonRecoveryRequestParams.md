# CommonRecoveryRequestParams

Specifies the common request parameters to create a Recovery.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the Recovery. | 
**snapshot_environment** | **str** | Specifies the type of environment of snapshots for which the Recovery has to be performed. | 
**filter_params** | [**CommonFilterExpression**](CommonFilterExpression.md) |  | [optional] 
**nfs_protocol** | **str, none_type** | Specifies NFS protocol version. This protocol will be employed if the recovery request mounts the Cohesity storage via NFS on the primary source. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


