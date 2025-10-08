# ChannelParam

Specifies the parameters to recover a Microsoft 365 Teams Channel.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the Channel id. | 
**recover_entire_channel** | **bool, none_type** | Specifies whether to recover the whole Microsoft 365 Channel. | 
**document_library_params** | [**[OneDriveParam], none_type**](OneDriveParam.md) | Specifies the list of doclibs of the Channel to recover. It is populated iff recoverEntireChannel is false. | [optional] 
**name** | **str, none_type** | Specifies the Channel name. | [optional] 
**type** | **str** | Specifies the type of channel public or private | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


