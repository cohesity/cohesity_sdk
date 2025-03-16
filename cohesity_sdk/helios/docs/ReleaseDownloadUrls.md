# ReleaseDownloadUrls

Different types of release urls.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deliverable_type** | **str** | Specifies url type. | [optional] 
**docs** | **str** | Specifies url doc link. | [optional] 
**fast_link** | **str** | Specifies url fast link. | [optional] 
**fixed_issues_link** | **str** | Specifies url doc link containing description for release. | [optional] 
**md5_check_sum** | **str** | Specifies url checksum. | [optional] 
**mirror_link** | **str** | Specifies url mirror link. | [optional] 
**what_is_new_link** | **str** | Specifies url doc link containing description for release. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.release_download_urls import ReleaseDownloadUrls

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseDownloadUrls from a JSON string
release_download_urls_instance = ReleaseDownloadUrls.from_json(json)
# print the JSON string representation of the object
print(ReleaseDownloadUrls.to_json())

# convert the object into a dict
release_download_urls_dict = release_download_urls_instance.to_dict()
# create an instance of ReleaseDownloadUrls from a dict
release_download_urls_from_dict = ReleaseDownloadUrls.from_dict(release_download_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


