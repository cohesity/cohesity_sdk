# VersionInfo

Id containing the unique identifer and version

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the string entity. This field is used to uniquely distinguish different entities within the system. | [optional] 
**version** | **int** | Version number associated with the string id. This can be used to track different versions of the entity id over time. The string ID assigned to the an entity may change (infrequently) across software versions. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.version_info import VersionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VersionInfo from a JSON string
version_info_instance = VersionInfo.from_json(json)
# print the JSON string representation of the object
print(VersionInfo.to_json())

# convert the object into a dict
version_info_dict = version_info_instance.to_dict()
# create an instance of VersionInfo from a dict
version_info_from_dict = VersionInfo.from_dict(version_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


