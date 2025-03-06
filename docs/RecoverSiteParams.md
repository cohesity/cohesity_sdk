# RecoverSiteParams

Specifies the parameters to recover Microsoft Office 365 Sharepoint site.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering the doc libs of a site, if one or more of doc libs failed to recover. Default value is false. | [optional] 
**objects** | [**List[ObjectSiteParam]**](ObjectSiteParam.md) | Specifies a list of site params associated with the objects to recover. | 
**recover_preservation_hold_library** | **bool** | Specifies whether to recover Preservation Hold Library associated with the Sites selected for restore. Default value is false. | [optional] 
**target_domain_object_id** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**target_site** | [**TargetSiteParam**](TargetSiteParam.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_site_params import RecoverSiteParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverSiteParams from a JSON string
recover_site_params_instance = RecoverSiteParams.from_json(json)
# print the JSON string representation of the object
print(RecoverSiteParams.to_json())

# convert the object into a dict
recover_site_params_dict = recover_site_params_instance.to_dict()
# create an instance of RecoverSiteParams from a dict
recover_site_params_from_dict = RecoverSiteParams.from_dict(recover_site_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


