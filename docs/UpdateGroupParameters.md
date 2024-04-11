# UpdateGroupParameters

Specifies group properties to update.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str, none_type** | Specifies the description of the group. | [optional] 
**local_group_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the LOCAL group properties. | [optional] 
**restricted** | **bool, none_type** | Specifies whether the Group is restricted. A restricted group can only view &amp; manage the objects it has permissions to. | [optional] 
**roles** | **[str]** | Specifies the Cohesity roles to associate with the group. The Cohesity roles determine privileges on the Cohesity Cluster for this group. | [optional] 
**tenant_ids** | **[str]** | Specifies a list of tenant ids who can access this group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


