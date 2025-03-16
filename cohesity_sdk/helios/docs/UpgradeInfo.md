# UpgradeInfo

Upgrade progress and upgrade status of cluster. It returns the percentage complete.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies cluster&#39;s id. | [optional] 
**cluster_incarnation_id** | **int** | Specifies cluster&#39;s incarnation id. | [optional] 
**software_version** | **str** | Upgrade software version against which these logs are generated. | [optional] 
**upgrade_logs** | [**List[NodeUpgradeLog]**](NodeUpgradeLog.md) | Upgrade logs per node. | [optional] 
**upgrade_percent_complete** | **float** | Upgrade percentage complete so far. | [optional] 
**upgrade_status** | **str** | Upgrade status. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.upgrade_info import UpgradeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeInfo from a JSON string
upgrade_info_instance = UpgradeInfo.from_json(json)
# print the JSON string representation of the object
print(UpgradeInfo.to_json())

# convert the object into a dict
upgrade_info_dict = upgrade_info_instance.to_dict()
# create an instance of UpgradeInfo from a dict
upgrade_info_from_dict = UpgradeInfo.from_dict(upgrade_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


