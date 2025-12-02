# ApplicationServersRegistrationRequestParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_credentials_vec** | [**[ApplicationCredentials], none_type**](ApplicationCredentials.md) | Specifies application specific credentials vec. | [optional] 
**credentials** | [**Credentials**](Credentials.md) |  | [optional] 
**is_internal_encrypted** | **bool, none_type** | Set to true if credentials are encrypted by internal magneto key | [optional] 
**user_encryption_key** | **str, none_type** | If set the user has encrypted the credential with userEncryptionKey. If both isInternalEncrypted and userEncryptionKey is set, it is assumed that credentials are first encrypted using &#39;internalEncryptionKey&#39; and then encrypted using &#39;userEncryptionKey&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


