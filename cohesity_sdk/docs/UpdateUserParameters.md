# UpdateUserParameters

Specifies User properties to update.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str, none_type** | Specifies the description of the User. | [optional] 
**effective_time_msecs** | **int, none_type** | Specifies the epoch time in milliseconds since when the user can login. | [optional] 
**expiry_time_msecs** | **int, none_type** | Specifies the epoch time in milliseconds when the user expires. Post expiry the user cannot access Cohesity cluster. | [optional] 
**locked** | **bool, none_type** | Specifies whether the User is locked. | [optional] 
**restricted** | **bool, none_type** | Specifies whether the User is restricted. A restricted user can only view &amp; manage the objects it has permissions to. | [optional] 
**roles** | **[str], none_type** | Specifies the Cohesity roles to associate with the user. The Cohesity roles determine privileges on the Cohesity Cluster for this user. | [optional] 
**local_user_params** | [**LocalUserUpdateParams**](LocalUserUpdateParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


