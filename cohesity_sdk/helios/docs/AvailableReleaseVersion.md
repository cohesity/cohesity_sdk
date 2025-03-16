# AvailableReleaseVersion

Specifies release information like release version, release notes and release upgrade URL

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | **str** | Specifies release&#39;s notes. | [optional] 
**release_stage** | **str** | Specifies the stage of a release. | [optional] 
**release_type** | **str** | Release&#39;s type e.g, LTS, Feature, Patch, MCM. | [optional] 
**version** | **str** | Specifies release&#39;s version. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.available_release_version import AvailableReleaseVersion

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableReleaseVersion from a JSON string
available_release_version_instance = AvailableReleaseVersion.from_json(json)
# print the JSON string representation of the object
print(AvailableReleaseVersion.to_json())

# convert the object into a dict
available_release_version_dict = available_release_version_instance.to_dict()
# create an instance of AvailableReleaseVersion from a dict
available_release_version_from_dict = AvailableReleaseVersion.from_dict(available_release_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


