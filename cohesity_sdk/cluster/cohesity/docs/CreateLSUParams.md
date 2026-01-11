# CreateLSUParams

Specifies the parameter to create an LSU.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the Storage Domain name. | 
**nbu_domain** | **str** | Specifies the NBU Domain this LSU is associated with. | 
**cloud_domain_id** | **int, none_type** | ID of the Cloud Domain that the LSU will be associated with. Note: an LSU can only be associated with either a Storage Domain or a Cloud Domain. If both storageDomainId and cloudDomainId are specified, cloudDomainId will be used.  | [optional] 
**storage_domain_id** | **int, none_type** | ID of the Storage Domain (View Box) that the LSU will be associated with. - For non-tenant users, if no ID is provided, DefaultStorageDomain   will be used. - For tenant users, providing a valid Storage Domain ID is mandatory. Note: an LSU can only be associated with either a Storage Domain or a Cloud Domain. If both storageDomainId and cloudDomainId are specified, cloudDomainId will be used.  | [optional] 
**worm_config** | [**WormConfig**](WormConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


