# ExpirationAction

Specifies the Lifecycle current version ExpirationAction. Note: All the three fields are mutually exclusive to each other.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_in_usecs** | **int, none_type** | Specifies the Timestamp in Usecs for the date when the object is subject to the rule. | [optional] 
**days** | **int, none_type** | Specifies the Lifetime in days of the objects that are subject to the rule. | [optional] 
**expired_object_delete_marker** | **bool, none_type** | Specifies whether Amazon S3 will remove a delete marker with no non-current versions. If set, the delete marker will be expired. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


