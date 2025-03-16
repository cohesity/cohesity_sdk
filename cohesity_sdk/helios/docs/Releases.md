# Releases

Specifies an array of release details and rules.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**releases** | [**List[Release]**](Release.md) | Specifies the release version. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.releases import Releases

# TODO update the JSON string below
json = "{}"
# create an instance of Releases from a JSON string
releases_instance = Releases.from_json(json)
# print the JSON string representation of the object
print(Releases.to_json())

# convert the object into a dict
releases_dict = releases_instance.to_dict()
# create an instance of Releases from a dict
releases_from_dict = Releases.from_dict(releases_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


