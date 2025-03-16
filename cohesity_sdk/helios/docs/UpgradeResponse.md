# UpgradeResponse

Specifies a cluster upgrade created or updated response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Specifies error message if failed to schedule upgrade. | [optional] 
**is_upgrade_scheduling_successful** | **bool** | Specifies if upgrade scheduling was successsful. | [optional] 
**cluster_id** | **int** | Specifies cluster id. | [optional] 
**cluster_incarnation_id** | **int** | Specifies cluster incarnation id. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.upgrade_response import UpgradeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeResponse from a JSON string
upgrade_response_instance = UpgradeResponse.from_json(json)
# print the JSON string representation of the object
print(UpgradeResponse.to_json())

# convert the object into a dict
upgrade_response_dict = upgrade_response_instance.to_dict()
# create an instance of UpgradeResponse from a dict
upgrade_response_from_dict = UpgradeResponse.from_dict(upgrade_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


