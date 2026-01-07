# LifecycleRule

Specifies the Lifecycle configuration rule.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the Unique identifier for the rule. The value cannot be longer than 255 characters. | 
**status** | **bool, none_type** | Specifies if the rule is currently being applied. | 
**abort_incomplete_multipart_upload_action** | [**AbortIncompleteMultipartUploadAction**](AbortIncompleteMultipartUploadAction.md) |  | [optional] 
**expiration** | [**ExpirationAction**](ExpirationAction.md) |  | [optional] 
**filter** | [**LifecycleRuleFilter**](LifecycleRuleFilter.md) |  | [optional] 
**non_current_version_expiration_action** | [**NonCurrentVersionExpirationAction**](NonCurrentVersionExpirationAction.md) |  | [optional] 
**prefix** | **str, none_type** | Specifies the prefix used to identify objects that a lifecycle rule applies to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


