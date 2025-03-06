# DownloadBaseosPatchRequest

Specifies the url of baseos patch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_url** | **str** | Url of the hotfix with security patch | 

## Example

```python
from cohesity_sdk.cluster.models.download_baseos_patch_request import DownloadBaseosPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadBaseosPatchRequest from a JSON string
download_baseos_patch_request_instance = DownloadBaseosPatchRequest.from_json(json)
# print the JSON string representation of the object
print(DownloadBaseosPatchRequest.to_json())

# convert the object into a dict
download_baseos_patch_request_dict = download_baseos_patch_request_instance.to_dict()
# create an instance of DownloadBaseosPatchRequest from a dict
download_baseos_patch_request_from_dict = DownloadBaseosPatchRequest.from_dict(download_baseos_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


