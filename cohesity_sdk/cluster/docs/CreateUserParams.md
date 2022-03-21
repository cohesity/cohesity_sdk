# CreateUserParams

Specifies the parameters to create a new Cohesity User.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Specifies the username. | 
**domain** | **str** | Specifies the domain of the user. For active directories, this is the fully qualified domain name (FQDN). It is &#39;LOCAL&#39; for local users on the Cohesity Cluster. A user is uniquely identified by combination of the username and the domain. | 
**description** | **str, none_type** | Specifies the description of the User. | [optional] 
**local_user_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the LOCAL user properties. This field is required when adding a new LOCAL Cohesity User. | [optional] 
**roles** | **[str], none_type** | Specifies the Cohesity roles to associate with the user. The Cohesity roles determine privileges on the Cohesity Cluster for this user. | [optional] 
**restricted** | **bool, none_type** | Specifies whether the User is restricted. A restricted user can only view &amp; manage the objects it has permissions to. | [optional] 
**effective_time_msecs** | **int, none_type** | Specifies the epoch time in milliseconds since when the user can login. | [optional] 
**expiry_time_msecs** | **int, none_type** | Specifies the epoch time in milliseconds when the user expires. Post expiry the user cannot access Cohesity cluster. | [optional] 
**locked** | **bool, none_type** | Specifies whether the User is locked. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


