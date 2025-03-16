# OrgVDCNetwork

Specifies a VDC Organization Network.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the catalog. | 
**v_center_uuid** | **str** | Specifies the UUID of network associated with the Vcenter. | [optional] [readonly] 
**vcd_uuid** | **str** | Specifies the UUID of network associated with the Virtual Cloud director. | 

## Example

```python
from cohesity_sdk.helios.models.org_vdc_network import OrgVDCNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of OrgVDCNetwork from a JSON string
org_vdc_network_instance = OrgVDCNetwork.from_json(json)
# print the JSON string representation of the object
print(OrgVDCNetwork.to_json())

# convert the object into a dict
org_vdc_network_dict = org_vdc_network_instance.to_dict()
# create an instance of OrgVDCNetwork from a dict
org_vdc_network_from_dict = OrgVDCNetwork.from_dict(org_vdc_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


