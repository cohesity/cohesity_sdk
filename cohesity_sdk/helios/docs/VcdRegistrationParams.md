# VcdRegistrationParams

Specifies parameters to register VMware vCloud director.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password to access target entity. | 
**username** | **str** | Specifies the username to access target entity. | 
**description** | **str** | Specifies the description of the source being registered. | [optional] 
**endpoint** | **str** | Specifies the endpoint IPaddress, URL or hostname of the host. | 
**vcenter_credential_info_list** | [**List[VcenterCredentialInfo]**](VcenterCredentialInfo.md) | Specifies the credentials information for all the vcenters in vcloud director. | 

## Example

```python
from cohesity_sdk.helios.models.vcd_registration_params import VcdRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of VcdRegistrationParams from a JSON string
vcd_registration_params_instance = VcdRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(VcdRegistrationParams.to_json())

# convert the object into a dict
vcd_registration_params_dict = vcd_registration_params_instance.to_dict()
# create an instance of VcdRegistrationParams from a dict
vcd_registration_params_from_dict = VcdRegistrationParams.from_dict(vcd_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


