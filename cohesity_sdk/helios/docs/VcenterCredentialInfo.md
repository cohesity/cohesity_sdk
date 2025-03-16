# VcenterCredentialInfo

Specifies the credential information for a specific vcenter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password to access target entity. | 
**username** | **str** | Specifies the username to access target entity. | 
**description** | **str** | Specifies the description of the source being registered. | [optional] 
**endpoint** | **str** | Specifies the endpoint IPaddress, URL or hostname of the host. | 
**name** | **str** | Specifies the name of the vCenter. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.vcenter_credential_info import VcenterCredentialInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VcenterCredentialInfo from a JSON string
vcenter_credential_info_instance = VcenterCredentialInfo.from_json(json)
# print the JSON string representation of the object
print(VcenterCredentialInfo.to_json())

# convert the object into a dict
vcenter_credential_info_dict = vcenter_credential_info_instance.to_dict()
# create an instance of VcenterCredentialInfo from a dict
vcenter_credential_info_from_dict = VcenterCredentialInfo.from_dict(vcenter_credential_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


