# VdcObject

Specifies the details about VMware Virtual datacenter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalogs** | [**List[VdcCatalog]**](VdcCatalog.md) | Specifies a list of VDC Catalogs. | [optional] 
**org_networks** | [**List[OrgVDCNetwork]**](OrgVDCNetwork.md) | Specifies a list of Organization VDC Networks. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.vdc_object import VdcObject

# TODO update the JSON string below
json = "{}"
# create an instance of VdcObject from a JSON string
vdc_object_instance = VdcObject.from_json(json)
# print the JSON string representation of the object
print(VdcObject.to_json())

# convert the object into a dict
vdc_object_dict = vdc_object_instance.to_dict()
# create an instance of VdcObject from a dict
vdc_object_from_dict = VdcObject.from_dict(vdc_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


