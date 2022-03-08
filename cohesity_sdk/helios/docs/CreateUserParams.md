# CreateUserParams

Specifies the parameters to create a User.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str, none_type** | Specifies the username. | 
**domain** | **str, none_type** | Specifies the domain of the User. | 
**password** | **str, none_type** | Specifies the password of the User. | 
**description** | **str, none_type** | Specifies the description of the User. | [optional] 
**email** | **str, none_type** | Specifies the email address of the User. | [optional] 
**roles** | **[str], none_type** | Specifies the Roles of the User. | [optional] 
**primary_group** | **str, none_type** | Specifies the primary group of the User. Primary group is used for file access. | [optional] 
**other_groups** | **[str], none_type** | Specifies other groups of the User. | [optional] 
**restricted** | **bool, none_type** | Specifies whether the User is restricted. | [optional] 
**effective_time_msecs** | **int, none_type** | Specifies the epoch time in milliseconds when the user is effective. | [optional] 
**expired_time_msecs** | **int, none_type** | Specifies the epoch time in milliseconds when the user is expired. | [optional] 
**locked** | **bool, none_type** | Specifies whether the User is locked. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


