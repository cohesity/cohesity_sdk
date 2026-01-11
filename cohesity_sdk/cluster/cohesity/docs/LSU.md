# LSU

Specifies an LSU.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the Storage Domain name. | 
**nbu_domain** | **str** | Specifies the NBU Domain this LSU is associated with. | 
**cloud_domain_id** | **int, none_type** | ID of the Cloud Domain that the LSU will be associated with. Note: an LSU can only be associated with either a Storage Domain or a Cloud Domain. If both storageDomainId and cloudDomainId are specified, cloudDomainId will be used.  | [optional] 
**storage_domain_id** | **int, none_type** | ID of the Storage Domain (View Box) that the LSU will be associated with. - For non-tenant users, if no ID is provided, DefaultStorageDomain   will be used. - For tenant users, providing a valid Storage Domain ID is mandatory. Note: an LSU can only be associated with either a Storage Domain or a Cloud Domain. If both storageDomainId and cloudDomainId are specified, cloudDomainId will be used.  | [optional] 
**worm_config** | [**WormConfig**](WormConfig.md) |  | [optional] 
**id** | **int** | Unique identifier of the LSU. | [optional] [readonly] 
**remote_lsu_source** | [**[RemoteLSU], none_type**](RemoteLSU.md) | Specifies list of remote LSUs that serve as data sources for transfer operations. This list is populated during remote LSU pairing process, and is applicable only when the LSU is associated with a View Box. The list will only contain one object for a given remote cluster Id &amp; remote LSU Id pair. | [optional] [readonly] 
**remote_lsu_target** | [**[RemoteLSU], none_type**](RemoteLSU.md) | Specifies list of remote LSUs that serve as data targets for transfer operations. This list is populated during remote LSU pairing process, and is applicable only when the LSU is associated with a View Box. The list will only contain one object for a given remote cluster Id &amp; remote LSU Id pair. | [optional] [readonly] 
**tenant_ids** | **[str], none_type** | Specifies a list of tenant ids that the LSU belongs to. This property is derived from the Storage Domain this LSU is associated with. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


