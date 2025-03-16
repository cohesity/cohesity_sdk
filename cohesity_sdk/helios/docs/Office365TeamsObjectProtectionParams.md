# Office365TeamsObjectProtectionParams

Specifies the params to create a Teams Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[Office365ObjectProtectionObjectParams]**](Office365ObjectProtectionObjectParams.md) | Specifies the objects to be included in the Object Protection. | 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.office365_teams_object_protection_params import Office365TeamsObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of Office365TeamsObjectProtectionParams from a JSON string
office365_teams_object_protection_params_instance = Office365TeamsObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(Office365TeamsObjectProtectionParams.to_json())

# convert the object into a dict
office365_teams_object_protection_params_dict = office365_teams_object_protection_params_instance.to_dict()
# create an instance of Office365TeamsObjectProtectionParams from a dict
office365_teams_object_protection_params_from_dict = Office365TeamsObjectProtectionParams.from_dict(office365_teams_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


