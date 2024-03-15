# TenantMigrationServiceAction

Describes a tenant migration action status.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str, none_type** | Specifies the action which will be performed on the tenant. | [optional] 
**action_incarnation_id** | **int, none_type** | Retry count for the action. If an action needs to be retried, then clients will increment action_incarnation_id and can send the same request again | [optional]  if omitted the server will use the default value of 1
**status** | **str, none_type** | Action status | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


