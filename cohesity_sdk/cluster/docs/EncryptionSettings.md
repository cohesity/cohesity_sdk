# EncryptionSettings

Specifis the encryption setting of the External Target

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption_level** | **str, none_type** | Specifies the type of encryption for the Setting. | 
**enable_additional_security** | **bool, none_type** | Enable Additional security by managing key manually | [optional] 
**encryption_key_file_downloaded** | **bool, none_type** | Specifies if the encryption key file has been downloaded using the Cohesity Dashboard (Cohesity UI). If true, the encryption key has been downloaded using the Cohesity Dashboard. An encryption key can only be downloaded once using the Cohesity Dashboard. After setting it to true once, subsequent updates to this field will be ignored. | [optional] 
**key_file_download_time_usecs** | **int, none_type** | Specifies the time (in microseconds) when the encryption key file was downloaded from the Cohesity Dashboard (Cohesity UI). An encryption key can only be downloaded once using Cohesity Dashboard. Can be set only once when the key is downloaded. | [optional] [readonly] 
**key_file_download_user** | **str, none_type** | Specifies the user who downloaded the encryption key from the Cohesity Dashboard (Cohesity UI). This field is only populated if encryption is enabled for the Vault and customerManagingEncryptionKeys is true. Can be set only once when the key is downloaded. | [optional] [readonly] 
**kms_server_id** | **int, none_type** | Specifies the Key Management Service Server ID for the Encryption Setting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


