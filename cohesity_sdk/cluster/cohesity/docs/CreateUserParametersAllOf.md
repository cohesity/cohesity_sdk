# CreateUserParametersAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Specifies the domain of the user. For active directories, this is the fully qualified domain name (FQDN). It is &#39;LOCAL&#39; for local users on the Cohesity Cluster. A user is uniquely identified by combination of the username and the domain. | 
**username** | **str** | Specifies the username. | 
**s3_access_keys** | [**S3Keys**](S3Keys.md) |  | [optional] 
**allow_smb_access_token** | **bool, none_type** | Specifies whether the SMB access token is to be set for the user. | [optional] 
**local_user_params** | [**LocalUserParams**](LocalUserParams.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


