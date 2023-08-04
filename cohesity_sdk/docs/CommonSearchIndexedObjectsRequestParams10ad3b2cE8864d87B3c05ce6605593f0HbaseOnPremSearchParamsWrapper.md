# CommonSearchIndexedObjectsRequestParams10ad3b2cE8864d87B3c05ce6605593f0HbaseOnPremSearchParamsWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | Specifies the object type to be searched for. | 
**protection_group_ids** | **[str], none_type** | Specifies a list of Protection Group ids to filter the indexed objects. If specified, the objects indexed by specified Protection Group ids will be returned. | [optional] 
**storage_domain_ids** | **[int], none_type** | Specifies the Storage Domain ids to filter indexed objects for which Protection Groups are writing data to Cohesity Views on the specified Storage Domains. | [optional] 
**tenant_id** | **str, none_type** | TenantId contains id of the tenant for which objects are to be returned. | [optional] 
**include_tenants** | **bool, none_type** | If true, the response will include objects which belongs to all tenants which the current user has permission to see. Default value is false. | [optional]  if omitted the server will use the default value of False
**tags** | **[str], none_type** | \&quot;This field is deprecated. Please use mightHaveTagIds.\&quot; | [optional] 
**snapshot_tags** | **[str]** | \&quot;This field is deprecated. Please use mightHaveSnapshotTagIds.\&quot; | [optional] 
**must_have_tag_ids** | **[str], none_type** | Specifies tags which must be all present in the document. | [optional] 
**might_have_tag_ids** | **[str], none_type** | Specifies list of tags, one or more of which might be present in the document. These are OR&#39;ed together and the resulting criteria AND&#39;ed with the rest of the query. | [optional] 
**must_have_snapshot_tag_ids** | **[str], none_type** | Specifies snapshot tags which must be all present in the document. | [optional] 
**might_have_snapshot_tag_ids** | **[str], none_type** | Specifies list of snapshot tags, one or more of which might be present in the document. These are OR&#39;ed together and the resulting criteria AND&#39;ed with the rest of the query. | [optional] 
**pagination_cookie** | **str, none_type** | Specifies the pagination cookie with which subsequent parts of the response can be fetched. | [optional] 
**count** | **int, none_type** | Specifies the number of indexed objects to be fetched for the specified pagination cookie. | [optional] 
**use_cached_data** | **bool, none_type** | Specifies whether we can serve the GET request from the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. | [optional] 
**hbase_params** | [**HbaseOnPremSearchParams**](HbaseOnPremSearchParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


