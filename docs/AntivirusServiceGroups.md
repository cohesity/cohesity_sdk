# AntivirusServiceGroups

Specifies a list of Antivirus Service groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**antivirus_service_groups** | [**List[AntivirusServiceGroup]**](AntivirusServiceGroup.md) | Specifies the list of Antivirus Service groups. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.antivirus_service_groups import AntivirusServiceGroups

# TODO update the JSON string below
json = "{}"
# create an instance of AntivirusServiceGroups from a JSON string
antivirus_service_groups_instance = AntivirusServiceGroups.from_json(json)
# print the JSON string representation of the object
print(AntivirusServiceGroups.to_json())

# convert the object into a dict
antivirus_service_groups_dict = antivirus_service_groups_instance.to_dict()
# create an instance of AntivirusServiceGroups from a dict
antivirus_service_groups_from_dict = AntivirusServiceGroups.from_dict(antivirus_service_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


