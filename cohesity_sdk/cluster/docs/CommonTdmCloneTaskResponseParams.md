# CommonTdmCloneTaskResponseParams

Specifies the common response params for a TDM clone task.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str, none_type** | Specifies the environment of the TDM Clone task. | 
**policy_id** | **str, none_type** | Specifies the ID of the policy, which should be used to protect this clone. This is useful for automatic snapshots. This must be specified if either of protectionGroupId and protectionGroupName is specified. | [optional] 
**protection_group_id** | **str, none_type** | Specifies the ID of an existing protection group, which should start protecting this clone. Specifying this implies that the clone is eligible for automated snapshots based on the policy configuration. If this is specified, policyId should also be specified and protectionGroupName should not be specified. | [optional] 
**protection_group_name** | **str, none_type** | Specifies the name of a new protection group, which should be created to protect this clone. Specifying this implies that the clone is eligible for automated snapshots based on the policy configuration. If this is specified, policyId should also be specified and protectionGroupId should not be specified. | [optional] 
**parent** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the details of the parent object of the clone. | [optional] 
**snapshot** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the details of the snapshot used for cloning. | [optional] 
**target** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the details of the target, where the clone is created. | [optional] 
**view** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the details of the view, which is used for the clone. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


