# AbortIncompleteMultipartUploadAction

Specifies the Lifecycle Abort Incomplete Multipart Upload Action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** | Specifies the number of days after which to abort an incomplete multipart upload. | [optional] 

## Example

```python
from cohesity_sdk.models.abort_incomplete_multipart_upload_action import AbortIncompleteMultipartUploadAction

# TODO update the JSON string below
json = "{}"
# create an instance of AbortIncompleteMultipartUploadAction from a JSON string
abort_incomplete_multipart_upload_action_instance = AbortIncompleteMultipartUploadAction.from_json(json)
# print the JSON string representation of the object
print(AbortIncompleteMultipartUploadAction.to_json())

# convert the object into a dict
abort_incomplete_multipart_upload_action_dict = abort_incomplete_multipart_upload_action_instance.to_dict()
# create an instance of AbortIncompleteMultipartUploadAction from a dict
abort_incomplete_multipart_upload_action_from_dict = AbortIncompleteMultipartUploadAction.from_dict(abort_incomplete_multipart_upload_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


