# AntivirusServiceGroup

Specifies an Antivirus Service group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**antivirus_services** | [**List[AntivirusService]**](AntivirusService.md) | Specifies a list of Antivirus Services for this group. | 
**description** | **str** | Specifies the description for the Antivirus Service group. | [optional] 
**enabled** | **bool** | This field is currently deprecated. Specifies whether the Antivirus Group is enabled. | [optional] 
**name** | **str** | Specifies the Antivirus Service group name. | 
**state** | **str** | Specifies the state[Enable, Disable] of the group. | [optional] 
**id** | **int** | Specifies the Antivirus Service group id. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.antivirus_service_group import AntivirusServiceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AntivirusServiceGroup from a JSON string
antivirus_service_group_instance = AntivirusServiceGroup.from_json(json)
# print the JSON string representation of the object
print(AntivirusServiceGroup.to_json())

# convert the object into a dict
antivirus_service_group_dict = antivirus_service_group_instance.to_dict()
# create an instance of AntivirusServiceGroup from a dict
antivirus_service_group_from_dict = AntivirusServiceGroup.from_dict(antivirus_service_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


