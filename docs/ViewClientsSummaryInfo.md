# ViewClientsSummaryInfo

Specifies the View Client summary info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nfs_client_count** | **int** | Specifies the number of NFS clients. | [optional] 
**node_ip** | **str** | Specifies the node ip the clients are connected to. | [optional] 
**server_ip** | **str** | Specifies the server ip the clients are connected to. | [optional] 
**smb_client_count** | **int** | Specifies the number of SMB clients. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.view_clients_summary_info import ViewClientsSummaryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ViewClientsSummaryInfo from a JSON string
view_clients_summary_info_instance = ViewClientsSummaryInfo.from_json(json)
# print the JSON string representation of the object
print(ViewClientsSummaryInfo.to_json())

# convert the object into a dict
view_clients_summary_info_dict = view_clients_summary_info_instance.to_dict()
# create an instance of ViewClientsSummaryInfo from a dict
view_clients_summary_info_from_dict = ViewClientsSummaryInfo.from_dict(view_clients_summary_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


