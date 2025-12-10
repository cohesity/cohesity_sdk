# ReplicationObjectDetails

Specifies the Replication Object Details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment of the object. | [optional] 
**name** | **str** | Specifies the name of the object. | [optional] 
**protection_group** | [**SimpleProtectionGroupInfo**](SimpleProtectionGroupInfo.md) |  | [optional] 
**replication_target_results** | [**List[ReplicationTargetInfo]**](ReplicationTargetInfo.md) | Replication result for a target. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.replication_object_details import ReplicationObjectDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationObjectDetails from a JSON string
replication_object_details_instance = ReplicationObjectDetails.from_json(json)
# print the JSON string representation of the object
print(ReplicationObjectDetails.to_json())

# convert the object into a dict
replication_object_details_dict = replication_object_details_instance.to_dict()
# create an instance of ReplicationObjectDetails from a dict
replication_object_details_from_dict = ReplicationObjectDetails.from_dict(replication_object_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


