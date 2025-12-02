# RecoverGmailParams

Specifies the parameters to recover Gmail.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[GmailParams], none_type**](GmailParams.md) | Specifies a list of Gmail params associated with the objects to recover. | 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other Gmail if one of Gmail failed to recover. Default value is false. | [optional] 
**download_as_zip** | **bool, none_type** | Specifies whether download the object as a ZIP file. If false and &#39;targetGmail&#39; is not specified, the objects will be recovered to original location. Default value is false. | [optional] 
**target_gmail** | [**TargetGmailParams**](TargetGmailParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


