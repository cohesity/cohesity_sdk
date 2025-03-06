# DataTransferInfo

Specifies the the details of network used in transferring the data from source account to Cohesity cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_private_network** | **bool** | Specifies whether to use private network or public network. | [optional] 
**private_network_info_list** | [**List[PrivateNetworkInfo]**](PrivateNetworkInfo.md) | Specifies Information required to create endpoints in private networks for all regions whose VMs are getting protected. | [optional] 
**use_protection_job_info** | **bool** | Specifies Whether to use private network info which was used in backup of VMs.This should be populated only for restore job. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_transfer_info import DataTransferInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataTransferInfo from a JSON string
data_transfer_info_instance = DataTransferInfo.from_json(json)
# print the JSON string representation of the object
print(DataTransferInfo.to_json())

# convert the object into a dict
data_transfer_info_dict = data_transfer_info_instance.to_dict()
# create an instance of DataTransferInfo from a dict
data_transfer_info_from_dict = DataTransferInfo.from_dict(data_transfer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


