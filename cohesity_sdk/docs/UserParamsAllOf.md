# UserParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time_msecs** | **int, none_type** | Specifies the epoch time in milliseconds when the user account was created. | [optional] [readonly] 
**domain** | **str** | Specifies the domain of the user. For active directories, this is the fully qualified domain name (FQDN). It is &#39;LOCAL&#39; for local users on the Cohesity Cluster. A user is uniquely identified by combination of the username and the domain. | [optional] [readonly] 
**force_password_change** | **bool, none_type** | Specifies if the user must change password. | [optional] [readonly] 
**last_login_time_msecs** | **int, none_type** | Specifies the epoch time in milliseconds when the user last logged in successfully. | [optional] [readonly] 
**last_updated_time_msecs** | **int, none_type** | Specifies the epoch time in milliseconds when the user account was last modified. | [optional] [readonly] 
**local_user_params** | [**LocalUserResponseParams**](LocalUserResponseParams.md) |  | [optional] 
**locked_reason** | **str, none_type** | Specifies the reason for locking the User. | [optional] [readonly] 
**other_groups** | **[str]** | Specifies additional groups the User may belong to. | [optional] [readonly] 
**primary_group** | **str, none_type** | Specifies the primary group of the User. Primary group is used for file access. | [optional] [readonly] 
**s3_account_params** | [**S3AccountParams**](S3AccountParams.md) |  | [optional] 
**sid** | **str, none_type** | Specifies the sid of the User. | [optional] [readonly] 
**tenant_id** | **str, none_type** | Specifies the tenant id of the User. | [optional] 
**username** | **str** | Specifies the username. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


