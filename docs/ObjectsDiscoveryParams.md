# ObjectsDiscoveryParams

Specifies the parameters used for discovering the office 365 objects selectively during source registration or refresh.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discoverable_object_type_list** | **List[str]** | Specifies the list of object types that will be discovered as part of source registration or refresh. | [optional] 
**sites_discovery_params** | [**SitesDiscoveryParams**](SitesDiscoveryParams.md) |  | [optional] 
**teams_additional_params** | [**TeamsAdditionalParams**](TeamsAdditionalParams.md) |  | [optional] 
**users_discovery_params** | [**UsersDiscoveryParams**](UsersDiscoveryParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.objects_discovery_params import ObjectsDiscoveryParams

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectsDiscoveryParams from a JSON string
objects_discovery_params_instance = ObjectsDiscoveryParams.from_json(json)
# print the JSON string representation of the object
print(ObjectsDiscoveryParams.to_json())

# convert the object into a dict
objects_discovery_params_dict = objects_discovery_params_instance.to_dict()
# create an instance of ObjectsDiscoveryParams from a dict
objects_discovery_params_from_dict = ObjectsDiscoveryParams.from_dict(objects_discovery_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


