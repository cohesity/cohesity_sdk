# HeliosExtendedRetentionSchedule

Specifies a schedule frequency and schedule unit for Extended Retentions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | Specifies a factor to multiply the unit by, to determine the retention schedule. For example if set to 2 and the unit is hourly, then Snapshots from the first eligible Job Run for every 2 hour period is retained. | [optional] 
**unit** | **str** | Specifies the unit interval for retention of Snapshots. &lt;br&gt;&#39;Runs&#39; means that the Snapshot copy retained after the number of Protection Group Runs equals the number specified in the frequency. &lt;br&gt;&#39;Hours&#39; means that the Snapshot copy retained hourly at the frequency set in the frequency, for example if scheduleFrequency is 2, the copy occurs every 2 hours. &lt;br&gt;&#39;Days&#39; means that the Snapshot copy gets retained daily at the frequency set in the frequency. &lt;br&gt;&#39;Weeks&#39; means that the Snapshot copy is retained weekly at the frequency set in the frequency. &lt;br&gt;&#39;Months&#39; means that the Snapshot copy is retained monthly at the frequency set in the Frequency. &lt;br&gt;&#39;Years&#39; means that the Snapshot copy is retained yearly at the frequency set in the Frequency. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_extended_retention_schedule import HeliosExtendedRetentionSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosExtendedRetentionSchedule from a JSON string
helios_extended_retention_schedule_instance = HeliosExtendedRetentionSchedule.from_json(json)
# print the JSON string representation of the object
print(HeliosExtendedRetentionSchedule.to_json())

# convert the object into a dict
helios_extended_retention_schedule_dict = helios_extended_retention_schedule_instance.to_dict()
# create an instance of HeliosExtendedRetentionSchedule from a dict
helios_extended_retention_schedule_from_dict = HeliosExtendedRetentionSchedule.from_dict(helios_extended_retention_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


