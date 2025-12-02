# ViewClientsClientsSummary

Specifies client summary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_active_connections** | **int** | Specifies total no. of clients with active connection (isIdle set to false). | [optional] 
**total_connections** | **int** | Specifies total no. of client connections | [optional] 
**total_inactive_connections** | **int** | Specifies total no. of clients with inactive connection (isIdle set to true). | [optional] 
**total_nfs_connections** | **int** | Specifies total no. of clients with NFS/NFS4 connection. | [optional] 
**total_smb_connections** | **int** | Specifies total no. of clients with SMB connection. | [optional] 
**unique_clients** | **int** | Specifies total no. of unique clients in client connections | [optional] 
**unique_nodes** | **int** | Specifies total no. of unique nodes in client connections | [optional] 
**unique_views** | **int** | Specifies total no. of unique views in client connections | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.view_clients_clients_summary import ViewClientsClientsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ViewClientsClientsSummary from a JSON string
view_clients_clients_summary_instance = ViewClientsClientsSummary.from_json(json)
# print the JSON string representation of the object
print(ViewClientsClientsSummary.to_json())

# convert the object into a dict
view_clients_clients_summary_dict = view_clients_clients_summary_instance.to_dict()
# create an instance of ViewClientsClientsSummary from a dict
view_clients_clients_summary_from_dict = ViewClientsClientsSummary.from_dict(view_clients_clients_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


