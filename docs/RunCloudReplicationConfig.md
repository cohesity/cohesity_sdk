# RunCloudReplicationConfig

Specifies settings for copying Snapshots to cloud targets. This also specifies the retention policy that should be applied to Snapshots after they have been copied to the specified target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_target** | [**AWSTargetConfig**](AWSTargetConfig.md) |  | [optional] 
**azure_target** | [**AzureTargetConfig**](AzureTargetConfig.md) |  | [optional] 
**retention** | [**Retention**](Retention.md) |  | [optional] 
**target_type** | **str** | Specifies the type of target to which replication need to be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.run_cloud_replication_config import RunCloudReplicationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RunCloudReplicationConfig from a JSON string
run_cloud_replication_config_instance = RunCloudReplicationConfig.from_json(json)
# print the JSON string representation of the object
print(RunCloudReplicationConfig.to_json())

# convert the object into a dict
run_cloud_replication_config_dict = run_cloud_replication_config_instance.to_dict()
# create an instance of RunCloudReplicationConfig from a dict
run_cloud_replication_config_from_dict = RunCloudReplicationConfig.from_dict(run_cloud_replication_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


