# LifecycleRule

Specifies the Lifecycle configuration rule.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the Unique identifier for the rule. The value cannot be longer than 255 characters. | 
**status** | **bool, none_type** | Specifies if the rule is currently being applied. | 
**prefix** | **str, none_type** | Specifies the prefix used to identify objects that a lifecycle rule applies to. | [optional] 
**filter** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the filter used to identify objects that a Lifecycle Rule applies to. | [optional] 
**expiration** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the expiration for the lifecycle of the object in the form of date, days and whether the object has a delete marker. | [optional] 
**non_current_version_expiration_action** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies when non-current object versions expire. Upon expiration, non-current object versions are permanently deleted. The action can be specified only in versioning enabled or suspended buckets. | [optional] 
**abort_incomplete_multipart_upload_action** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the days since the initiation of an incomplete multipart upload before permanently removing all parts of the upload. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


