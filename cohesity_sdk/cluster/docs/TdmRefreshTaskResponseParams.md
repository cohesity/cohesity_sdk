# TdmRefreshTaskResponseParams

Specifies the response parameters for a refresh task.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str, none_type** | Specifies the environment of the TDM refresh task. | defaults to "kOracle"
**parent** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the details of the parent object of the clone. | [optional] 
**snapshot** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the details of the snapshot used for refresh. | [optional] 
**target** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the details of the target, where the clone is created. | [optional] 
**view** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the details of the view, which is used for the clone. | [optional] 
**oracle_params** | [**OracleCloneRefreshTask**](OracleCloneRefreshTask.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


