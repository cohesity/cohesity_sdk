# VirtualDiskInformationResponseParams

specifies virtual disk information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disks** | [**List[VirtualDiskInformation]**](VirtualDiskInformation.md) | An array of objects, each providing information on the virtual disk object. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.virtual_disk_information_response_params import VirtualDiskInformationResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskInformationResponseParams from a JSON string
virtual_disk_information_response_params_instance = VirtualDiskInformationResponseParams.from_json(json)
# print the JSON string representation of the object
print(VirtualDiskInformationResponseParams.to_json())

# convert the object into a dict
virtual_disk_information_response_params_dict = virtual_disk_information_response_params_instance.to_dict()
# create an instance of VirtualDiskInformationResponseParams from a dict
virtual_disk_information_response_params_from_dict = VirtualDiskInformationResponseParams.from_dict(virtual_disk_information_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


