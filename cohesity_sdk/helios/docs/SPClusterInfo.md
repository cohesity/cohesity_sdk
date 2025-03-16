# SPClusterInfo

Specifies the details of a cluster claimed from IBM Storage Protect environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies cluster id. | [optional] 
**cluster_incarnation_id** | **int** | Specifies cluster incarnation id. | [optional] 
**cluster_name** | **str** | Specifies cluster&#39;s name. | [optional] 
**health** | **str** | Specifies the health of the cluster. | [optional] 
**is_connected_to_helios** | **bool** | Specifies if the cluster is connected to helios. | [optional] 
**provider_type** | **str** | Specifies the type of the cluster provider. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.sp_cluster_info import SPClusterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SPClusterInfo from a JSON string
sp_cluster_info_instance = SPClusterInfo.from_json(json)
# print the JSON string representation of the object
print(SPClusterInfo.to_json())

# convert the object into a dict
sp_cluster_info_dict = sp_cluster_info_instance.to_dict()
# create an instance of SPClusterInfo from a dict
sp_cluster_info_from_dict = SPClusterInfo.from_dict(sp_cluster_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


