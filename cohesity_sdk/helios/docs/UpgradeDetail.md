# UpgradeDetail

Specifies the cluster upgrade details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | Specifies cluster&#39;s id. | [optional] 
**cluster_incarnation_id** | **str** | Specifies cluster&#39;s incarnation id. | [optional] 
**cluster_name** | **str** | Specifies cluster&#39;s name. | [optional] 
**current_version** | **str** | Specifies cluster&#39;s current version. | [optional] 
**pulse_task_id** | **str** | Specifies the upgrade&#39;s nexus task ID. | [optional] 
**release_version** | **str** | Specifies cluster&#39;s upgrade release version. | [optional] 
**scheduled_time** | **str** | Specifies the upgrade time for the cluster. | [optional] 
**status** | **str** | Specifies the upgrade status of the cluster. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.upgrade_detail import UpgradeDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeDetail from a JSON string
upgrade_detail_instance = UpgradeDetail.from_json(json)
# print the JSON string representation of the object
print(UpgradeDetail.to_json())

# convert the object into a dict
upgrade_detail_dict = upgrade_detail_instance.to_dict()
# create an instance of UpgradeDetail from a dict
upgrade_detail_from_dict = UpgradeDetail.from_dict(upgrade_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


