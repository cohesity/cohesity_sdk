# TargetTeamsChannelParam

Specifies the target Microsoft 365 Team channel to recover to in case of granular restore

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the id of the target channel. | [optional] 
**name** | **str, none_type** | Specifies the name of the target channel. | [optional] 
**create_new_channel** | **bool, none_type** | Specifies whether we should create a new channel. If this is true name must not be empty | [optional] 
**channel_type** | **str** | Specifies whether to create a public or private channel | [optional] 
**channel_owners** | [**[RecoveryObjectIdentifier], none_type**](RecoveryObjectIdentifier.md) | List of owners for the private channel. At least one owner is needed to create a private channel | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


