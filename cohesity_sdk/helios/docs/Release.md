# Release

Specifies release details and rules.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_urls** | [**List[ReleaseDownloadUrls]**](ReleaseDownloadUrls.md) | Specifies the release download urls. | [optional] 
**from_versions** | **List[str]** | Specifies the list of version this release is compatible. | [optional] 
**release_notes** | **str** | Release&#39;s notes or description like what features this release has. | [optional] 
**release_series** | **str** | Release&#39;s version in series | [optional] 
**release_type** | **str** | Release&#39;s type e.g, GA, Feature. | [optional] [default to 'Feature']
**release_version** | **str** | Release&#39;s version | [optional] 
**stage** | **str** | Specifies the stage of a release. | [optional] 
**status** | **str** | Specifies the status of a release. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.release import Release

# TODO update the JSON string below
json = "{}"
# create an instance of Release from a JSON string
release_instance = Release.from_json(json)
# print the JSON string representation of the object
print(Release.to_json())

# convert the object into a dict
release_dict = release_instance.to_dict()
# create an instance of Release from a dict
release_from_dict = Release.from_dict(release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


