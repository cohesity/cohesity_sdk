# S3TaggingFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool, none_type** | If set, it enables tagging filter for S3 views. | [optional] 
**mode** | **str, none_type** | Whitelist or blacklist the objects to be scanned. | [optional] 
**tag_set** | [**[TagSet], none_type**](TagSet.md) | List of key, value pair. If any of the tags on the object matches any tags defined in tagSet array, it&#39;s regarded as a match. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


