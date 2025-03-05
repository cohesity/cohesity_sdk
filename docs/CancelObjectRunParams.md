# CancelObjectRunParams

One object run to cancel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_target_ids** | **List[int]** | Specifies the archival target ids where the tasks run. If specified, the archival target ids must be present within the run specified by the runId above. | [optional] 
**cancel_local_run** | **bool** | Specifies whether to cancel the local backup run. Default is false. | [optional] 
**cloud_spin_target_ids** | **List[int]** | Specifies the cloud spin target ids where the tasks run. If specified, the archival target ids must be present within the run specified by the runId above. | [optional] 
**replication_targets** | [**List[ClusterIdentifier]**](ClusterIdentifier.md) | Specifies the cluster identifiers where the tasks run. If specified, the archival target ids must be present within the run specified by the runId above. | [optional] 
**run_id** | **str** | Specifies the id of the run to cancel. | 

## Example

```python
from cohesity_sdk.models.cancel_object_run_params import CancelObjectRunParams

# TODO update the JSON string below
json = "{}"
# create an instance of CancelObjectRunParams from a JSON string
cancel_object_run_params_instance = CancelObjectRunParams.from_json(json)
# print the JSON string representation of the object
print(CancelObjectRunParams.to_json())

# convert the object into a dict
cancel_object_run_params_dict = cancel_object_run_params_instance.to_dict()
# create an instance of CancelObjectRunParams from a dict
cancel_object_run_params_from_dict = CancelObjectRunParams.from_dict(cancel_object_run_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


