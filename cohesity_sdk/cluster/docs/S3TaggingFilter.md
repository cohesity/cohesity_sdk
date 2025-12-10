# S3TaggingFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | If set, it enables tagging filter for S3 views. | [optional] 
**mode** | **str** | Whitelist or blacklist the objects to be scanned. | [optional] 
**tag_set** | [**List[TagSet]**](TagSet.md) | List of key, value pair. If any of the tags on the object matches any tags defined in tagSet array, it&#39;s regarded as a match. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.s3_tagging_filter import S3TaggingFilter

# TODO update the JSON string below
json = "{}"
# create an instance of S3TaggingFilter from a JSON string
s3_tagging_filter_instance = S3TaggingFilter.from_json(json)
# print the JSON string representation of the object
print(S3TaggingFilter.to_json())

# convert the object into a dict
s3_tagging_filter_dict = s3_tagging_filter_instance.to_dict()
# create an instance of S3TaggingFilter from a dict
s3_tagging_filter_from_dict = S3TaggingFilter.from_dict(s3_tagging_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


