# ConfigureSupportUserMfaParams

Specifies the request parameters for updating support user MFA configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str, none_type** | Specifies the current password of the support user, required for making updates to the configuration. | [optional] 
**email** | **str, none_type** | Specifies email address of the support user. Required when the support user email is being modified. | [optional] 
**mfa_type** | **str, none_type** | Specifies the mechanism to receive the OTP code. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


