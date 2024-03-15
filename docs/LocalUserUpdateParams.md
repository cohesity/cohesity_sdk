# LocalUserUpdateParams

Specifies properties for LOCAL cohesity user which are updatable.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str, none_type** | Specifies the email address of the User. | [optional] 
**groups** | **[str]** | Specifies additional groups the User may belong to. | [optional] [readonly] 
**password** | **str, none_type** | Specifies the password of the User. | [optional] 
**primary_group** | **str, none_type** | Specifies the primary group of the User. Primary group is used for file access. | [optional] [readonly] 
**current_password** | **str, none_type** | Specifies the current password of the user. This is required when a session user tries to update his own password. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


