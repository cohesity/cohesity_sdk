# ChassisList

Specifies the list of hardware chassis.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis** | [**List[Chassis]**](Chassis.md) | Specifies the list of chassis. | [optional] 

## Example

```python
from cohesity_sdk.models.chassis_list import ChassisList

# TODO update the JSON string below
json = "{}"
# create an instance of ChassisList from a JSON string
chassis_list_instance = ChassisList.from_json(json)
# print the JSON string representation of the object
print(ChassisList.to_json())

# convert the object into a dict
chassis_list_dict = chassis_list_instance.to_dict()
# create an instance of ChassisList from a dict
chassis_list_from_dict = ChassisList.from_dict(chassis_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


