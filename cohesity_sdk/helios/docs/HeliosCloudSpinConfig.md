# HeliosCloudSpinConfig

Specifies settings for copying Snapshots to on prem.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** | Specifies the unique identifier for the target getting added. This field need to be passed only when helios policies are updated. | [optional] 
**copy_on_run_success** | **bool** | Specifies if Snapshots are copied from the first completely successful Protection Group Run or the first partially successful Protection Group Run occurring at the start of the replication schedule. &lt;br&gt; If true, Snapshots are copied from the first Protection Group Run occurring at the start of the replication schedule that was completely successful i.e. Snapshots for all the Objects in the Protection Group were successfully captured. &lt;br&gt; If false, Snapshots are copied from the first Protection Group Run occurring at the start of the replication schedule, even if first Protection Group Run was not completely successful i.e. Snapshots were not captured for all Objects in the Protection Group. | [optional] 
**retention** | [**HeliosRetention**](HeliosRetention.md) |  | [optional] 
**schedule** | [**HeliosTargetSchedule**](HeliosTargetSchedule.md) |  | [optional] 
**target** | [**HeliosCloudSpinTarget**](HeliosCloudSpinTarget.md) |  | 

## Example

```python
from cohesity_sdk.helios.models.helios_cloud_spin_config import HeliosCloudSpinConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosCloudSpinConfig from a JSON string
helios_cloud_spin_config_instance = HeliosCloudSpinConfig.from_json(json)
# print the JSON string representation of the object
print(HeliosCloudSpinConfig.to_json())

# convert the object into a dict
helios_cloud_spin_config_dict = helios_cloud_spin_config_instance.to_dict()
# create an instance of HeliosCloudSpinConfig from a dict
helios_cloud_spin_config_from_dict = HeliosCloudSpinConfig.from_dict(helios_cloud_spin_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


