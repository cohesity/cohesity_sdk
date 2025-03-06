# ExtendedRetentionSchedule

Specifies a schedule frequency and schedule unit for Extended Retentions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | Specifies a factor to multiply the unit by, to determine the retention schedule. For example if set to 2 and the unit is hourly, then Snapshots from the first eligible Job Run for every 2 hour period is retained. | [optional] 
**unit** | **str** | Specifies the unit interval for retention of Snapshots. &lt;br&gt;&#39;Runs&#39; means that the Snapshot copy retained after the number of Protection Group Runs equals the number specified in the frequency. &lt;br&gt;&#39;Hours&#39; means that the Snapshot copy retained hourly at the frequency set in the frequency, for example if scheduleFrequency is 2, the copy occurs every 2 hours. &lt;br&gt;&#39;Days&#39; means that the Snapshot copy gets retained daily at the frequency set in the frequency. &lt;br&gt;&#39;Weeks&#39; means that the Snapshot copy is retained weekly at the frequency set in the frequency. &lt;br&gt;&#39;Months&#39; means that the Snapshot copy is retained monthly at the frequency set in the Frequency. &lt;br&gt;&#39;Years&#39; means that the Snapshot copy is retained yearly at the frequency set in the Frequency. | 

## Example

```python
from cohesity_sdk.cluster.models.extended_retention_schedule import ExtendedRetentionSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedRetentionSchedule from a JSON string
extended_retention_schedule_instance = ExtendedRetentionSchedule.from_json(json)
# print the JSON string representation of the object
print(ExtendedRetentionSchedule.to_json())

# convert the object into a dict
extended_retention_schedule_dict = extended_retention_schedule_instance.to_dict()
# create an instance of ExtendedRetentionSchedule from a dict
extended_retention_schedule_from_dict = ExtendedRetentionSchedule.from_dict(extended_retention_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


