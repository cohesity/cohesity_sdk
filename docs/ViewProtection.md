# ViewProtection

Specifies information about the Protection Groups that are protecting the View.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**magneto_entity_id** | **int, none_type** | Specifies the id of the Protection Source that is using this View. | [optional] 
**protection_groups** | [**[ProtectionGroupInfo], none_type**](ProtectionGroupInfo.md) | Array of Protection Group. Specifies the Protection Group that are protecting the View. | [optional] 
**inactive** | **bool, none_type** | Specifies if this View is an inactive View that was created on this Remote Cluster to store the Snapshots created by replication. This inactive View cannot be NFS or SMB mounted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


