# AddedPrincipalResponseObject

Specifies the principals added for the user or group on the Cohesity Cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time_msecs** | **int, none_type** | Specifies the epoch time in milliseconds when the principal was added to the Cohesity Cluster. | [optional] 
**principal_type** | **str, none_type** | Specifies the category of the user or group being added to the Cohesity Cluster. | [optional]  if omitted the server will use the default value of "SSOUser"
**sid** | **str, none_type** | Specifies the unique Security ID (SID) of the principal associated with the group or user. | [optional] 
**sso_user_principal_details** | [**[SSOUserPrincipal], none_type**](SSOUserPrincipal.md) | Specifies the details of the SSO user added to the Cohesity Cluster. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


