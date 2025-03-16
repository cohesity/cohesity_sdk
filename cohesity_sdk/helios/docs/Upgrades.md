# Upgrades

Specifies clusters upgrade request like clusterId, release upgrade URL, time stamp to upgrade at, intervals for rolling upgrade in hours.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[Upgrade]**](Upgrade.md) | Array for clusters to be upgraded. | [optional] 
**interval_for_rolling_upgrade_in_hours** | **int** | Specifies the difference of time between two cluster&#39;s upgrade. | [optional] 
**package_url** | **str** | Specifies URL from which package can be downloaded. Note: This option is only supported in Multi-Cluster Manager (MCM) | [optional] 
**target_version** | **str** | Specifies target version to which clusters are to be upgraded. | [optional] 
**time_stamp_to_upgrade_at_msecs** | **int** | Specifies the time in msecs at which the cluster has to be upgraded. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.upgrades import Upgrades

# TODO update the JSON string below
json = "{}"
# create an instance of Upgrades from a JSON string
upgrades_instance = Upgrades.from_json(json)
# print the JSON string representation of the object
print(Upgrades.to_json())

# convert the object into a dict
upgrades_dict = upgrades_instance.to_dict()
# create an instance of Upgrades from a dict
upgrades_from_dict = Upgrades.from_dict(upgrades_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


