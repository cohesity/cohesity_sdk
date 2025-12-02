# CreateLSUParams

Specifies the parameter to create an LSU.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_domain_id** | **int** | ID of the Cloud Domain that the LSU will be associated with. Note: an LSU can only be associated with either a Storage Domain or a Cloud Domain. If both storageDomainId and cloudDomainId are specified, cloudDomainId will be used.  | [optional] 
**name** | **str** | Specifies the Storage Domain name. | 
**nbu_domain** | **str** | Specifies the NBU Domain this LSU is associated with. | 
**storage_domain_id** | **int** | ID of the Storage Domain (View Box) that the LSU will be associated with. - For non-tenant users, if no ID is provided, DefaultStorageDomain   will be used. - For tenant users, providing a valid Storage Domain ID is mandatory. Note: an LSU can only be associated with either a Storage Domain or a Cloud Domain. If both storageDomainId and cloudDomainId are specified, cloudDomainId will be used.  | [optional] 
**worm_config** | [**WormConfig**](WormConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.create_lsu_params import CreateLSUParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLSUParams from a JSON string
create_lsu_params_instance = CreateLSUParams.from_json(json)
# print the JSON string representation of the object
print(CreateLSUParams.to_json())

# convert the object into a dict
create_lsu_params_dict = create_lsu_params_instance.to_dict()
# create an instance of CreateLSUParams from a dict
create_lsu_params_from_dict = CreateLSUParams.from_dict(create_lsu_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


