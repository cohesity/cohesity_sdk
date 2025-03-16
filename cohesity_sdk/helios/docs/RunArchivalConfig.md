# RunArchivalConfig

Specifies settings for copying Snapshots External Targets (such as AWS or Tape). This also specifies the retention policy that should be applied to Snapshots after they have been copied to the specified target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_target_type** | **str** | Specifies the snapshot&#39;s archival target type from which recovery has been performed. | 
**copy_only_fully_successful** | **bool** | Specifies if Snapshots are copied from a fully successful Protection Group Run or a partially successful Protection Group Run. If false, Snapshots are copied the Protection Group Run, even if the Run was not fully successful i.e. Snapshots were not captured for all Objects in the Protection Group. If true, Snapshots are copied only when the run is fully successful. | [optional] 
**id** | **int** | Specifies the Archival target to copy the Snapshots to. | 
**retention** | [**Retention**](Retention.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.run_archival_config import RunArchivalConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RunArchivalConfig from a JSON string
run_archival_config_instance = RunArchivalConfig.from_json(json)
# print the JSON string representation of the object
print(RunArchivalConfig.to_json())

# convert the object into a dict
run_archival_config_dict = run_archival_config_instance.to_dict()
# create an instance of RunArchivalConfig from a dict
run_archival_config_from_dict = RunArchivalConfig.from_dict(run_archival_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


