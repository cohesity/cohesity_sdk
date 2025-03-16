# UpgradeCancelResponse

Specifies a cluster scheduled upgrade cancel response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Specifies an error message if failed to cancel a scheduled upgrade. | [optional] 
**is_upgrade_cancel_successful** | **bool** | Specifies if scheduled upgrade cancelling was successful. | [optional] 
**cluster_id** | **int** | Specifies cluster id. | [optional] 
**cluster_incarnation_id** | **int** | Specifies cluster incarnation id. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.upgrade_cancel_response import UpgradeCancelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeCancelResponse from a JSON string
upgrade_cancel_response_instance = UpgradeCancelResponse.from_json(json)
# print the JSON string representation of the object
print(UpgradeCancelResponse.to_json())

# convert the object into a dict
upgrade_cancel_response_dict = upgrade_cancel_response_instance.to_dict()
# create an instance of UpgradeCancelResponse from a dict
upgrade_cancel_response_from_dict = UpgradeCancelResponse.from_dict(upgrade_cancel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


