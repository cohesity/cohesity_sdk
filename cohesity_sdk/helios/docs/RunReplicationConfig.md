# RunReplicationConfig

Specifies settings for copying Snapshots to Remote Clusters. This also specifies the retention policy that should be applied to Snapshots after they have been copied to the specified target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies id of Remote Cluster to copy the Snapshots to. | 
**retention** | [**Retention**](Retention.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.run_replication_config import RunReplicationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RunReplicationConfig from a JSON string
run_replication_config_instance = RunReplicationConfig.from_json(json)
# print the JSON string representation of the object
print(RunReplicationConfig.to_json())

# convert the object into a dict
run_replication_config_dict = run_replication_config_instance.to_dict()
# create an instance of RunReplicationConfig from a dict
run_replication_config_from_dict = RunReplicationConfig.from_dict(run_replication_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


