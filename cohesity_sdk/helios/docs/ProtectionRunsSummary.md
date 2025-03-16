# ProtectionRunsSummary

Specifies a list of summaries of protection runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_runs_summary** | [**List[ProtectionRunSummary]**](ProtectionRunSummary.md) | Specifies a list of summaries of protection runs. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.protection_runs_summary import ProtectionRunsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionRunsSummary from a JSON string
protection_runs_summary_instance = ProtectionRunsSummary.from_json(json)
# print the JSON string representation of the object
print(ProtectionRunsSummary.to_json())

# convert the object into a dict
protection_runs_summary_dict = protection_runs_summary_instance.to_dict()
# create an instance of ProtectionRunsSummary from a dict
protection_runs_summary_from_dict = ProtectionRunsSummary.from_dict(protection_runs_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


