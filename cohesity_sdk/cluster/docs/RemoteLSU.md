# RemoteLSU

Specifies details about a Remote LSU.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_local_pairing** | **bool** | Indicates whether the paired LSUs belong to the same cluster and Storage Domain. | 
**remote_cluster_fqdn** | **str** | Specifies FQDN of the remote cluster. | 
**remote_cluster_id** | **int** | Specifies ID of the remote cluster this LSU belongs to. | 
**remote_lsuid** | **int** | ID of the remote LSU. | 
**remote_lsu_name** | **str** | Specifies the remote LSU name. | 
**remote_lsu_nbu_domain** | **str** | Specifies the NBU Domain this remote LSU is associated with. | 

## Example

```python
from cohesity_sdk.cluster.models.remote_lsu import RemoteLSU

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteLSU from a JSON string
remote_lsu_instance = RemoteLSU.from_json(json)
# print the JSON string representation of the object
print(RemoteLSU.to_json())

# convert the object into a dict
remote_lsu_dict = remote_lsu_instance.to_dict()
# create an instance of RemoteLSU from a dict
remote_lsu_from_dict = RemoteLSU.from_dict(remote_lsu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


