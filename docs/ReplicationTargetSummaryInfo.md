# ReplicationTargetSummaryInfo

Specifies replication target summary information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the id of the cluster. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the incarnation id of the cluster. | [optional] 
**cluster_name** | **str** | Specifies the name of the cluster. | [optional] [readonly] 
**aws_target_config** | [**AWSTargetConfig**](AWSTargetConfig.md) |  | [optional] 
**azure_target_config** | [**AzureTargetConfig**](AzureTargetConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.replication_target_summary_info import ReplicationTargetSummaryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationTargetSummaryInfo from a JSON string
replication_target_summary_info_instance = ReplicationTargetSummaryInfo.from_json(json)
# print the JSON string representation of the object
print(ReplicationTargetSummaryInfo.to_json())

# convert the object into a dict
replication_target_summary_info_dict = replication_target_summary_info_instance.to_dict()
# create an instance of ReplicationTargetSummaryInfo from a dict
replication_target_summary_info_from_dict = ReplicationTargetSummaryInfo.from_dict(replication_target_summary_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


