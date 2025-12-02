# NtpAuthKeyInfo

Specifies list of authentication keys corresponding to each NTP server.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ntp_server_address** | **str, none_type** | Specifies NTP server address. | [optional] 
**ntp_server_auth_key_encryption_algorithm** | **str, none_type** | Specifies the Symmetric Key algorithm used for the encryption key. | [optional] 
**ntp_server_auth_key_id** | **int, none_type** | Specifies the identifier of the authentication key used to verify the NTP server. | [optional] 
**ntp_server_auth_key_value** | **str, none_type** | Specifies the shared secret key corresponding to the authentication key identifier used to authenticate NTP messages. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


