# ActiveAlertsStats

Specifies the active alert statistics details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_critical_alerts** | **int** | Specifies the count of active critical alerts. | [optional] 
**num_critical_alerts_categories** | **int** | Specifies the count of active critical alerts categories. | [optional] 
**num_data_service_alerts** | **int** | Specifies the count of active service alerts. | [optional] 
**num_data_service_critical_alerts** | **int** | Specifies the count of active service critical alerts. | [optional] 
**num_data_service_info_alerts** | **int** | Specifies the count of active service info alerts. | [optional] 
**num_data_service_warning_alerts** | **int** | Specifies the count of active service warning alerts. | [optional] 
**num_hardware_alerts** | **int** | Specifies the count of active hardware alerts. | [optional] 
**num_hardware_critical_alerts** | **int** | Specifies the count of active hardware critical alerts. | [optional] 
**num_hardware_info_alerts** | **int** | Specifies the count of active hardware info alerts. | [optional] 
**num_hardware_warning_alerts** | **int** | Specifies the count of active hardware warning alerts. | [optional] 
**num_info_alerts** | **int** | Specifies the count of active info alerts excluding alerts that belong to other bucket. | [optional] 
**num_info_alerts_categories** | **int** | Specifies the count of active info alerts categories. | [optional] 
**num_maintenance_alerts** | **int** | Specifies the count of active alerts of maintenance bucket | [optional] 
**num_maintenance_critical_alerts** | **int** | Specifies the count of active other critical alerts. | [optional] 
**num_maintenance_info_alerts** | **int** | Specifies the count of active other info alerts. | [optional] 
**num_maintenance_warning_alerts** | **int** | Specifies the count of active other warning alerts. | [optional] 
**num_software_alerts** | **int** | Specifies the count of active software alerts. | [optional] 
**num_software_critical_alerts** | **int** | Specifies the count of active software critical alerts. | [optional] 
**num_software_info_alerts** | **int** | Specifies the count of active software info alerts. | [optional] 
**num_software_warning_alerts** | **int** | Specifies the count of active software warning alerts. | [optional] 
**num_warning_alerts** | **int** | Specifies the count of active warning alerts excluding alerts that belong to other bucket. | [optional] 
**num_warning_alerts_categories** | **int** | Specifies the count of active warning alerts categories. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.active_alerts_stats import ActiveAlertsStats

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveAlertsStats from a JSON string
active_alerts_stats_instance = ActiveAlertsStats.from_json(json)
# print the JSON string representation of the object
print(ActiveAlertsStats.to_json())

# convert the object into a dict
active_alerts_stats_dict = active_alerts_stats_instance.to_dict()
# create an instance of ActiveAlertsStats from a dict
active_alerts_stats_from_dict = ActiveAlertsStats.from_dict(active_alerts_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


