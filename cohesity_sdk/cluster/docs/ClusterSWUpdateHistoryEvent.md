# ClusterSWUpdateHistoryEvent

Represents an event of cluster upgrade/patch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_timestamp_secs** | **int** | Latest Unix epoch timestamp (in seconds) when the upgrade/patch was done - will contain the value from the node that got updated last.  | [optional] 
**node_history** | [**List[ClusterSWUpdateNodeHistoryEvent]**](ClusterSWUpdateNodeHistoryEvent.md) |  | [optional] 
**operation_type** | **str** | Type of operation.  | [optional] 
**package_sub_type** | **str** | Sub-type of package - Security Patch or Product Patch | [optional] 
**package_type** | **str** | Type of the package | [optional] 
**release_date** | **datetime** | Release date of the package. | [optional] 
**release_version** | **str** | Release version of the package. Examples: For upgrade package: &#39;6.6.0d_u6&#39;, &#39;7.0.&#39; For patch package - &#39;6.8.1-p1s1&#39;  | [optional] 
**version_name** | **str** | Name of the package version. Example: &#39;6.6.0d_u6_release-20210714_0fad884e&#39;,   &#39;7.0.1_release-20230623_ddbb8c79&#39; for upgrade packages, &#39;6.8.1-p1s1-2023Jun26-221b8a5c&#39; for patch packages  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_sw_update_history_event import ClusterSWUpdateHistoryEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterSWUpdateHistoryEvent from a JSON string
cluster_sw_update_history_event_instance = ClusterSWUpdateHistoryEvent.from_json(json)
# print the JSON string representation of the object
print(ClusterSWUpdateHistoryEvent.to_json())

# convert the object into a dict
cluster_sw_update_history_event_dict = cluster_sw_update_history_event_instance.to_dict()
# create an instance of ClusterSWUpdateHistoryEvent from a dict
cluster_sw_update_history_event_from_dict = ClusterSWUpdateHistoryEvent.from_dict(cluster_sw_update_history_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


