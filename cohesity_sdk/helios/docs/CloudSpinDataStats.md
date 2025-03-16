# CloudSpinDataStats

Specifies statistics about Cloud Spin data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**physical_bytes_transferred** | **int** | Specifies the physical bytes transferred. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cloud_spin_data_stats import CloudSpinDataStats

# TODO update the JSON string below
json = "{}"
# create an instance of CloudSpinDataStats from a JSON string
cloud_spin_data_stats_instance = CloudSpinDataStats.from_json(json)
# print the JSON string representation of the object
print(CloudSpinDataStats.to_json())

# convert the object into a dict
cloud_spin_data_stats_dict = cloud_spin_data_stats_instance.to_dict()
# create an instance of CloudSpinDataStats from a dict
cloud_spin_data_stats_from_dict = CloudSpinDataStats.from_dict(cloud_spin_data_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


