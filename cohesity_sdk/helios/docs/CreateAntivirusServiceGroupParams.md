# CreateAntivirusServiceGroupParams

Specifies the parameters to create an Antivirus Service group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**antivirus_services** | [**List[AntivirusService]**](AntivirusService.md) | Specifies a list of Antivirus Services for this group. | 
**description** | **str** | Specifies the description for the Antivirus Service group. | [optional] 
**enabled** | **bool** | This field is currently deprecated. Specifies whether the Antivirus Group is enabled. | [optional] 
**name** | **str** | Specifies the Antivirus Service group name. | 
**state** | **str** | Specifies the state[Enable, Disable] of the group. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.create_antivirus_service_group_params import CreateAntivirusServiceGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAntivirusServiceGroupParams from a JSON string
create_antivirus_service_group_params_instance = CreateAntivirusServiceGroupParams.from_json(json)
# print the JSON string representation of the object
print(CreateAntivirusServiceGroupParams.to_json())

# convert the object into a dict
create_antivirus_service_group_params_dict = create_antivirus_service_group_params_instance.to_dict()
# create an instance of CreateAntivirusServiceGroupParams from a dict
create_antivirus_service_group_params_from_dict = CreateAntivirusServiceGroupParams.from_dict(create_antivirus_service_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


