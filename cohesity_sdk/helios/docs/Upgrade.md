# Upgrade

Specifies list of cluster upgrades.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies cluster id. | [optional] 
**cluster_incarnation_id** | **int** | Specifies cluster incarnation id. | [optional] 
**current_version** | **str** | Specifies current version of cluster. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.upgrade import Upgrade

# TODO update the JSON string below
json = "{}"
# create an instance of Upgrade from a JSON string
upgrade_instance = Upgrade.from_json(json)
# print the JSON string representation of the object
print(Upgrade.to_json())

# convert the object into a dict
upgrade_dict = upgrade_instance.to_dict()
# create an instance of Upgrade from a dict
upgrade_from_dict = Upgrade.from_dict(upgrade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


